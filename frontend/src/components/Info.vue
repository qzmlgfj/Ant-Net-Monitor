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
import {initLineChart} from "@/utils/request";
import {setCPUSeries} from "@/utils/cpu-series";

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
        const data = ref([]);
        let Series = ref({});

        // TODO 重构一下，太难看了
        const updateData = function () {
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
            console.log(router.currentRoute._value.path);
        };

        const initData = function (url) {
            /*
            if (process.env.NODE_ENV === "development") {
                updateData();
            } else {
                initLineChart(url).then((response) => {
                    console.log(response);
                });
            }
            */
            initLineChart(url).then((response) => {
                initSeries(response.data);
            });
        };

        const initSeries = function(data){
            switch (router.currentRoute._value.name){
                case "CPU-Info":
                    Series.value = setCPUSeries(data);
            }
        }

        initData(router.currentRoute._value.path);

        return {
            updateData,
            initData,
            Series,
        };
    },
    beforeRouteUpdate(to) {
        this.initData(to);
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