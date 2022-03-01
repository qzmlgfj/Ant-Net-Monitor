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

<style lang='scss'>

body {
    min-height: 100vh;
    min-width: 100vw;
    margin: 0;
}

#root {
    width: 100%;
    height: 100%;
}

#dashboard {
    width: 100%;
    height: 40%;
    display: flex;
}
</style>