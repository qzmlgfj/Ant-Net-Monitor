<template>
    <chart />
</template>

<script>
import chart from "./components/EChartsDemo.vue";

export default {
    components: {
        chart,
    },
};
</script>

<style scoped>
.chart {
    height: 400px;
}
</style>