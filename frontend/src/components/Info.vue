<template>
    <div id="info">
        <n-space wrap="false" size="large" justify="space-between">
            <n-card id="info-sider" hoverable>
                <n-scrollbar style="height: 30vh">
                    <router-view />
                </n-scrollbar>
            </n-card>
            <n-card hoverable id="info-chart">
                <n-switch v-model:value="historyMode">
                    <template #checked> 24小时历史 </template>
                    <template #unchecked> 实时状态 </template>
                </n-switch>
                <line-chart :argv="series" :enableZoom="enableZoom" />
            </n-card>
        </n-space>
    </div>
</template>

<script>
import { NCard, NSpace, NSwitch, NScrollbar } from "naive-ui";

import LineChart from "@/components/charts/LineChart.vue";
import {
    initLineChart,
    updateLineChart,
    getHistoryLineChart,
} from "@/utils/request";
import { initSeries, setSeries, updateSeries } from "@/utils/series";

export default {
    name: "Info",
    components: {
        NCard,
        NSpace,
        NSwitch,
        NScrollbar,
        LineChart,
    },
    data() {
        return {
            series: {},
            interval: null,
            enableZoom: false,
            alarmSettingVisible: false,
            intervalTime: 1500,
            historyMode: false,
        };
    },
    methods: {
        updateChart(url) {
            updateLineChart(url).then((response) => {
                updateSeries(response.data);
            });
        },
        initChart(url) {
            initLineChart(url).then((response) => {
                initSeries(response.data[0]);
                this.series = setSeries(response.data);
            });
        },
        switchToHistory() {
            if (!this.enableZoom) {
                this.enableZoom = true;
                clearInterval(this.interval);
                getHistoryLineChart(this.$route.meta.apiUrl).then(
                    (response) => {
                        this.series = setSeries(response.data);
                    }
                );
            }
        },
        switchToRealTime() {
            if (this.enableZoom) {
                this.enableZoom = false;
                this.initChart(this.$route.meta.apiUrl);
                this.interval = setInterval(() => {
                    this.updateChart(this.$route.meta.apiUrl);
                }, this.intervalTime);
            }
        },
        switchAlarmSetting() {
            this.alarmSettingVisible = !this.alarmSettingVisible;
        },
    },
    created() {
        this.initChart(this.$route.meta.apiUrl);
        this.interval = setInterval(() => {
            this.updateChart(this.$route.meta.apiUrl);
        }, this.intervalTime);
    },
    beforeRouteUpdate(to) {
        clearInterval(this.interval);
        this.initChart(to.meta.apiUrl);
        this.interval = setInterval(() => {
            this.updateChart(to.meta.apiUrl);
        }, this.intervalTime);
        this.enableZoom = false;
        this.historyMode = false;
    },
    watch: {
        historyMode: {
            handler: function (historyMode) {
                if (historyMode) {
                    this.switchToHistory();
                } else {
                    this.switchToRealTime();
                }
            },
        },
    },
};
</script>

<style scoped>
#info {
    height: 45%;
}

#info-sider {
    height: 39vh;
    width: 30vw;
}

#info-chart {
    height: 39vh;
    width: 52.5vw;
}

.n-button {
    margin: 10px;
}
</style>