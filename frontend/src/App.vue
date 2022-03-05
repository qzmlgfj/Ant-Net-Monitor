<template>
    <div>
        <n-config-provider :theme="naiveTheme">
            <n-layout id="container">
                <n-layout-header id="header">
                    <head-bar @changeTheme="changeTheme" />
                </n-layout-header>
                <n-layout has-sider>
                    <n-layout-sider>
                        <side-bar />
                    </n-layout-sider>
                    <n-layout-content>
                        <dash-board />
                        <info />
                    </n-layout-content>
                </n-layout>
            </n-layout>
        </n-config-provider>
    </div>
</template>

<script>
import { ref, computed } from "vue";
import { NLayout, NConfigProvider, darkTheme } from "naive-ui";
import { THEME_KEY } from "vue-echarts";
import { registerTheme } from "echarts/core";
import DarkModeJson from "./assets/DarkMode.json";

import HeadBar from "./components/HeadBar.vue";
import SideBar from "./components/SideBar.vue";
import DashBoard from "./components/DashBoard.vue";
import Info from "./components/Info.vue";

registerTheme("dark-mode", DarkModeJson);

export default {
    name: "App",
    components: {
        NConfigProvider,
        NLayout,
        HeadBar,
        SideBar,
        DashBoard,
        Info,
    },
    setup() {
        return {
            darkTheme,
            naiveTheme: ref(null),
            chartTheme: ref("white"),
        };
    },
    provide() {
        return {
            [THEME_KEY]: computed(() => this.chartTheme),
        };
    },
    methods: {
        //! Echarts 主题与naive-ui 主题切换速度不同步，建议将Echarts背景设为透明
        //TODO 调整仪表盘在深色模式下颜色过浅的问题
        changeTheme() {
            this.$store.commit("changeTheme");
            this.naiveTheme = this.naiveTheme === null ? darkTheme : null;
            this.chartTheme =
                this.chartTheme === "white" ? "dark-mode" : "white";
        },
    },
};
</script>

<style>
body {
    height: 100vh;
    margin: 0;
    font-family: v-sans, system-ui, -apple-system, BlinkMacSystemFont,
        "Segoe UI", sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
        "Segoe UI Symbol";
}

#container {
    height: 100vh;
}

#header > * {
    display: inline-block;
}
</style>