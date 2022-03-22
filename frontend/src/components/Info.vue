<template>
    <div id="info">
        <n-space>
            <n-card id="info-sider" hoverable>
                <router-view />
            </n-card>
            <n-card hoverable>
                <n-button-group>
                    <n-button type="default" round @click="switchToHistory">
                        <template #icon>
                            <n-icon><history /></n-icon>
                        </template>
                        24小时历史
                    </n-button>
                    <n-button type="default" @click="switchToRealTime">
                        <template #icon>
                            <n-icon><chart-line /></n-icon>
                        </template>
                        实时状态
                    </n-button>
                    <n-button type="default" round @click="switchAlarmSetting">
                        <template #icon>
                            <n-icon><thermometer-half /></n-icon>
                        </template>
                        异常警报
                    </n-button>
                </n-button-group>
                <line-chart :argv="series" :enableZoom="enableZoom" />
            </n-card>
        </n-space>
        <n-modal v-model:show="alarmSettingVisible">
            <n-card
                style="width: 600px"
                title="警报设置"
                :bordered="false"
                size="huge"
                role="dialog"
                aria-modal="true"
                footer-style="display:flex;justify-content:flex-end;"
                closable
                @close="switchAlarmSetting"
            >
                设置点什么玩意儿
                <template #footer>
                    <n-button type="primary">保存</n-button>
                    <n-button type="default">取消</n-button>
                </template>
            </n-card>
        </n-modal>
    </div>
</template>

<script>
import { NCard, NSpace, NButtonGroup, NButton, NIcon, NModal } from "naive-ui";
import { History, ChartLine, ThermometerHalf } from "@vicons/fa";

import LineChart from "@/components/charts/LineChart.vue";
import {
    initLineChart,
    updateLineChart,
    getHistoryLineChart,
} from "@/utils/request";
import { setCPUSeries, updateCPUSeries } from "@/utils/series/cpu-series";
import { setRAMSeries, updateRAMSeries } from "@/utils/series/ram-series";

export default {
    name: "Info",
    components: {
        NCard,
        NSpace,
        NButtonGroup,
        NButton,
        NIcon,
        NModal,
        History,
        ChartLine,
        ThermometerHalf,
        LineChart,
    },
    data() {
        return {
            series: {},
            interval: null,
            enableZoom: false,
            alarmSettingVisible: false,
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
                        }
                    }
                );
            }
        },
        switchToRealTime() {
            // FIXME 有点脏，想个办法重构一下
            if (this.enableZoom) {
                this.enableZoom = false;
                this.initSeries(this.$route.meta.apiUrl);
                this.interval = setInterval(() => {
                    this.updateSeries(this.$route.meta.apiUrl);
                }, 1000);
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
        }, 1000);
    },
    beforeRouteUpdate(to) {
        clearInterval(this.interval);
        this.initSeries(to.meta.apiUrl);
        this.interval = setInterval(() => {
            this.updateSeries(to.meta.apiUrl);
        }, 1000);
        this.enableZoom = false;
    },
};
</script>

<style scoped>
#info {
    height: 44vh;
    width: 88vw;
}

#info-sider {
    height: 42vh;
    width: 35vw;
}

.n-button {
    margin: 10px;
}
</style>