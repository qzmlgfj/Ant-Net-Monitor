<template>
    <div id="root">
        <dash-board id="dashboard" />
    </div>
</template>

<script>
import DashBoard from "./components/DashBoard.vue";

export default {
    components: {
        DashBoard,
    },
};
</script>

<style>
body {
    height: 100vh;
    margin: 0;
}

#app {
    height: 100%;
    width: 100%;
}

#root {
    width: 100%;
    height: 100%;
}
</style>