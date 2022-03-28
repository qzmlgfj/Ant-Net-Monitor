<template>
    <div>
        <n-config-provider :theme="naiveTheme">
            <n-layout id="container">
                <n-layout-header bordered>
                    <head-bar @changeTheme="changeTheme" />
                </n-layout-header>
                <n-layout has-sider>
                    <n-layout-sider>
                        <side-bar />
                    </n-layout-sider>
                    <n-layout-content>
                        <n-space vertical>
                            <n-notification-provider>
                                <dash-board />
                            </n-notification-provider>
                            <router-view />
                        </n-space>
                    </n-layout-content>
                </n-layout>
            </n-layout>
        </n-config-provider>
    </div>
</template>

<script>
import { ref, computed } from "vue";
import {
    NLayout,
    NLayoutHeader,
    NLayoutSider,
    NLayoutContent,
    NConfigProvider,
    NSpace,
    NNotificationProvider,
    darkTheme,
} from "naive-ui";
import { THEME_KEY } from "vue-echarts";
import { registerTheme } from "echarts/core";
import DarkModeJson from "./assets/DarkMode.json";

import HeadBar from "./components/HeadBar.vue";
import SideBar from "./components/SideBar.vue";
import DashBoard from "./components/DashBoard.vue";

registerTheme("dark-mode", DarkModeJson);

export default {
    name: "App",
    components: {
        NConfigProvider,
        NLayout,
        NLayoutHeader,
        NLayoutSider,
        NLayoutContent,
        NSpace,
        NNotificationProvider,
        HeadBar,
        SideBar,
        DashBoard,
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
        //! Echarts 主题与naive-ui 主题切换速度不同步，因此将Echarts背景设为透明
        changeTheme() {
            if (!this.$store.state.darkMode) {
                this.naiveTheme = darkTheme;
                this.chartTheme = "dark-mode";
            } else {
                this.naiveTheme = null;
                this.chartTheme = "white";
            }

            this.$store.commit("changeTheme");
        },
    },
};
</script>

<style>
body {
    max-height: 100vh;
    margin: 0;
    font-family: v-sans, system-ui, -apple-system, BlinkMacSystemFont,
        "Segoe UI", sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
        "Segoe UI Symbol";
}

#container {
    height: 100vh;
    padding: 10px;
}
</style>