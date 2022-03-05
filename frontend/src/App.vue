<template>
    <div>
        <n-config-provider :theme="theme">
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
import {ref} from "vue";
import { NLayout, NConfigProvider, darkTheme } from "naive-ui";
import HeadBar from "./components/HeadBar.vue";
import SideBar from "./components/SideBar.vue";
import DashBoard from "./components/DashBoard.vue";
import Info from "./components/Info.vue";

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
            theme: ref(null),
        };
    },
    methods: {
        changeTheme() {
            this.theme = this.theme === null ? darkTheme : null;
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