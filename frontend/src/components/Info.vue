<template>
    <div id="info">
        <n-space>
            <n-card id="info-sider" hoverable>
                <router-view />
            </n-card>
            <n-card hoverable>
                <line-chart :argv="series" :enableZoom="enableZoom"/>
            </n-card>
        </n-space>
    </div>
</template>

<script>
import { NCard, NSpace } from "naive-ui";
import LineChart from "@/components/charts/LineChart.vue";
import { initLineChart, updateLineChart } from "@/utils/request";
import { setCPUSeries, updateCPUSeries } from "@/utils/series/cpu-series";
import { setRAMSeries, updateRAMSeries } from "@/utils/series/ram-series";

//TODO 需要继续封装，最好复用折线图组件
export default {
    name: "Info",
    components: {
        NCard,
        NSpace,
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