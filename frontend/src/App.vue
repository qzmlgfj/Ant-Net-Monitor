<template>
    <div>
        <dash-board />
    </div>
</template>

<script>
import DashBoard from "./components/DashBoard.vue";

export default {
    components: {
        DashBoard
    }
};
</script>

<style scoped>
.chart {
    height: 400px;
}
</style>