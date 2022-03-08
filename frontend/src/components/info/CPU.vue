<template>
    <div style="display:flex">
        <div class="info-sider">
            <n-h1>CPU</n-h1>
            <n-p>CPU实时负荷</n-p>
        </div>
        <line-chart />
    </div>
</template>

<script>
import { NP, NH1 } from "naive-ui";
import LineChart from "@/components/charts/LineChart.vue";

export default {
    components: {
        NP,
        NH1,
        LineChart,
    },
    setup() {
        return {};
    },
};
</script>

<style scoped>
.info-sider {
    height: 45vh;
    width: 40%;
    display: inline-block;
}
</style>
