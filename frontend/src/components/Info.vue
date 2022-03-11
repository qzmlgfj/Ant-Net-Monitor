<template>
    <div id="info">
        <n-space>
            <n-card id="info-sider" hoverable>
                <router-view />
            </n-card>
            <n-card hoverable>
                <line-chart :argv="Series" />
            </n-card>
        </n-space>
    </div>
</template>

<script>
import { ref } from "vue";
import { NCard, NSpace } from "naive-ui";
import LineChart from "@/components/charts/LineChart.vue";
import { useRouter } from "vue-router";
import { initLineChart, updateLineChart } from "@/utils/request";
import { setCPUSeries, updateCPUSeries } from "@/utils/cpu-series";

//TODO 需要继续封装，最好复用折线图组件
export default {
    name: "Info",
    components: {
        NCard,
        NSpace,
        LineChart,
    },
    setup() {
        const router = useRouter();
        let Series = ref({});

        // TODO 重构一下，太难看了
        const updateSeries = function (url) {
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
                switch (router.currentRoute._value.name) {
                    case "CPU-Info":
                        updateCPUSeries(response.data);
                }
            });
        };

        const initSeries = function (url) {
            initLineChart(url).then((response) => {
                switch (router.currentRoute._value.name) {
                    case "CPU-Info":
                        Series.value = setCPUSeries(response.data);
                }
            });
        };

        initSeries(router.currentRoute._value.path);
        
        let interval = setInterval(() => {
            updateSeries(router.currentRoute._value.path);
        }, 1000);

        return {
            Series,
            interval,
            initSeries,
            updateSeries,
        };
    },
    beforeRouteUpdate(to) {
        this.initSeries(to.path);
        clearInterval(this.interval);
        this.interval = setInterval(() => {
            this.updateData(to.path);
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