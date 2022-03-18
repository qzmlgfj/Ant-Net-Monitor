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
                    <n-button type="default" round @click="switchToRealTime">
                        <template #icon>
                            <n-icon><chart-line /></n-icon>
                        </template>
                        实时状态
                    </n-button>
                </n-button-group>
                <line-chart :argv="series" :enableZoom="enableZoom" />
            </n-card>
        </n-space>
    </div>
</template>

<script>
import { NCard, NSpace, NButtonGroup, NButton, NIcon } from "naive-ui";
import { History,ChartLine } from "@vicons/fa";

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
        History,
        ChartLine,
        LineChart,
    },
    data() {
        return {
            series: {},
            interval: null,
            enableZoom: false,
        };
    },
    methods: {
        updateSeries(url) {
            /*
            let base = +new Date(1988, 9, 3);
            const oneDay = 24 * 3600 * 1000;
            data.value = [[base, Math.random() * 300]];
            for (let i = 1; i < 100; i++) {
                const now = new Date((base += oneDay));
                data.value.push([
                    +now,
                    Math.round(
                        (Math.random() - 0.5) * 20 + data.value[i - 1][1]
                    ),
                ]);
            }
            */
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
                getHistoryLineChart(this.$route.path).then((response) => {
                    switch (this.$route.name) {
                        case "CPU-Info":
                            this.series = setCPUSeries(response.data);
                            break;
                        case "RAM-Info":
                            this.series = setRAMSeries(response.data);
                            break;
                    }
                });
            }
        },
        switchToRealTime() {
            // TODO 有点脏，想个办法重构一下
            if (this.enableZoom) {
                this.enableZoom = false;
                this.interval = setInterval(() => {
                    this.updateSeries(this.$route.path);
                }, 1000);
                this.initSeries(this.$route.path);
            }
        },
    },
    created() {
        this.initSeries(this.$route.path);
        this.interval = setInterval(() => {
            this.updateSeries(this.$route.path);
        }, 1000);
    },
    beforeRouteUpdate(to) {
        clearInterval(this.interval);
        this.initSeries(to.path);
        this.interval = setInterval(() => {
            this.updateSeries(to.path);
        }, 1000);
        this.enableZoom = false;
    },
};
</script>

<style>
#info {
    height: 44vh;
    width: 88vw;
}

#info-sider {
    height: 42vh;
    width: 35vw;
}
</style>