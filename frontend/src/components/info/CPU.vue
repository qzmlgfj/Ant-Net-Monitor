<template>
    <n-space>
        <n-card class="info-sider" hoverable>
            <n-h1>CPU</n-h1>
            <n-p>CPU实时负荷</n-p>
        </n-card>
        <n-card hoverable>
            <line-chart />
        </n-card>
    </n-space>
</template>

<script>
import { NP, NH1, NCard, NSpace } from "naive-ui";
import LineChart from "@/components/charts/LineChart.vue";

export default {
    components: {
        NP,
        NH1,
        NCard,
        NSpace,
        LineChart,
    },
    setup() {
        return {};
    },
};
</script>

<style scoped>
.info-sider {
    height: 42vh;
    width: 35vw;
}
</style>
