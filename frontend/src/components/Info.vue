<template>
    <div id="info">
        <n-space>
            <n-card id="info-sider" hoverable>
                <router-view />
            </n-card>
            <n-card hoverable>
                <line-chart :argv="CPUSeries" />
            </n-card>
        </n-space>
    </div>
</template>

<script>
import { ref } from "vue";
import { NCard, NSpace } from "naive-ui";
import LineChart from "@/components/charts/LineChart.vue";

//TODO 需要继续封装，最好复用折线图组件
export default {
    name: "Info",
    components: {
        NCard,
        NSpace,
        LineChart,
    },
    setup() {
        let data = ref([]);
        const CPUSeries = [
            {
                name: "user",
                type: "line",
                smooth: true,
                symbol: "none",
                areaStyle: {},
                data: data,
            },
        ];

        // TODO 重构一下，太难看了
        const updateData = function () {
            let base = +new Date(1988, 9, 3);
            const oneDay = 24 * 3600 * 1000;
            data.value = [[base, Math.random() * 300]];
            for (let i = 1; i < 100; i++) {
                const now = new Date((base += oneDay));
                data.value.push([
                    +now,
                    Math.round((Math.random() - 0.5) * 20 + data.value[i - 1][1]),
                ]);
            }
        };

        updateData();

        return {
            CPUSeries,
            updateData,
        };
    },
    beforeRouteUpdate() {
        this.updateData();
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