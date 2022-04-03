<template>
    <div id="info">
        <n-space wrap="false" size="large" justify="space-between">
            <n-card id="info-sider" hoverable>
                <router-view />
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
import { NCard, NSpace, NSwitch } from "naive-ui";

import LineChart from "@/components/charts/LineChart.vue";
import {
    initLineChart,
    updateLineChart,
    getHistoryLineChart,
} from "@/utils/request";
import { setCPUSeries, updateCPUSeries } from "@/utils/series/cpu-series";
import { setRAMSeries, updateRAMSeries } from "@/utils/series/ram-series";
import { setDiskSeries, updateDiskSeries } from "@/utils/series/disk-series";

export default {
    name: "Info",
    components: {
        NCard,
        NSpace,
        NSwitch,
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
        updateSeries(url) {
            updateLineChart(url).then((response) => {
                switch (this.$route.name) {
                    case "CPU-Info":
                        updateCPUSeries(response.data);
                        break;
                    case "RAM-Info":
                        updateRAMSeries(response.data);
                        break;
                    case "Disk-Info":
                        updateDiskSeries(response.data);
                        break;
                }
            });
        },
        initSeries(url) {
            initLineChart(url).then((response) => {
                switch (this.$route.name) {
                    case "CPU-Info":
                        this.series = setCPUSeries(response.data);
                        break;
                    case "RAM-Info":
                        this.series = setRAMSeries(response.data);
                        break;
                    case "Disk-Info":
                        this.series = setDiskSeries(response.data);
                        break;
                }
            });
        },
        switchToHistory() {
            if (!this.enableZoom) {
                this.enableZoom = true;
                clearInterval(this.interval);
                getHistoryLineChart(this.$route.meta.apiUrl).then(
                    (response) => {
                        switch (this.$route.name) {
                            case "CPU-Info":
                                this.series = setCPUSeries(response.data);
                                break;
                            case "RAM-Info":
                                this.series = setRAMSeries(response.data);
                                break;
                            case "Disk-Info":
                                this.series = setDiskSeries(response.data);
                                break;
                        }
                    }
                );
            }
        },
        switchToRealTime() {
            if (this.enableZoom) {
                this.enableZoom = false;
                this.initSeries(this.$route.meta.apiUrl);
                this.interval = setInterval(() => {
                    this.updateSeries(this.$route.meta.apiUrl);
                }, this.intervalTime);
            }
        },
        switchAlarmSetting() {
            this.alarmSettingVisible = !this.alarmSettingVisible;
        },
    },
    created() {
        this.initSeries(this.$route.meta.apiUrl);
        this.interval = setInterval(() => {
            this.updateSeries(this.$route.meta.apiUrl);
        }, this.intervalTime);
    },
    beforeRouteUpdate(to) {
        clearInterval(this.interval);
        this.initSeries(to.meta.apiUrl);
        this.interval = setInterval(() => {
            this.updateSeries(to.meta.apiUrl);
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