<template>
    <div id="root">
        <div id="sidebar">
            <side-bar />
        </div>
        <div id="main">
            <dash-board />
            <router-view />
        </div>
    </div>
</template>

<script>
import DashBoard from "./components/DashBoard.vue";
import SideBar from "./components/SideBar.vue";

export default {
    components: {
        DashBoard,
        SideBar,
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
    display: flex;
}

#sidebar {
    width: 12%;
    height: 100%;
}

#main {
    width: 88%;
    height: 100%;
}
</style>