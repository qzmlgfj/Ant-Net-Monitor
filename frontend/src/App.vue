<template>
    <div>
        <n-config-provider :theme="naiveTheme">
            <n-layout id="container">
                <n-layout-header id="head-bar" bordered>
                    <head-bar @changeTheme="changeTheme" @alarm="switchAlarm" />
                </n-layout-header>
                <n-layout has-sider>
                    <n-layout-sider id="side-bar">
                        <side-bar />
                    </n-layout-sider>
                    <n-layout-content id="main-content">
                        <n-space vertical>
                            <n-message-provider>
                                <n-notification-provider placement="bottom-right">
                                    <dash-board />
                                </n-notification-provider>
                            </n-message-provider>
                            <router-view />
                        </n-space>
                    </n-layout-content>
                </n-layout>
                <n-layout-footer id="foot-bar" bordered>
                    <foot-bar />
                </n-layout-footer>
            </n-layout>

            <n-message-provider>
                <n-modal v-model:show="alarmSettingVisible">
                    <alarm-card @switchAlarm="switchAlarm" />
                </n-modal>
            </n-message-provider>
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
    NLayoutFooter,
    NConfigProvider,
    NSpace,
    NModal,
    NNotificationProvider,
    NMessageProvider,
    darkTheme,
} from "naive-ui";
import { THEME_KEY } from "vue-echarts";
import { registerTheme } from "echarts/core";
import DarkModeJson from "./assets/DarkMode.json";

import HeadBar from "./components/HeadBar.vue";
import SideBar from "./components/SideBar.vue";
import FootBar from "./components/FootBar.vue";
import DashBoard from "./components/DashBoard.vue";
import AlarmCard from "./components/AlarmCard.vue";

registerTheme("dark-mode", DarkModeJson);

export default {
    name: "App",
    components: {
        NConfigProvider,
        NLayout,
        NLayoutHeader,
        NLayoutSider,
        NLayoutContent,
        NLayoutFooter,
        NSpace,
        NModal,
        NNotificationProvider,
        NMessageProvider,
        HeadBar,
        SideBar,
        FootBar,
        DashBoard,
        AlarmCard,
    },
    setup() {
        const alarmSettingVisible = ref(false);
        const switchAlarm = function () {
            alarmSettingVisible.value = !alarmSettingVisible.value;
        };

        return {
            darkTheme,
            naiveTheme: ref(null),
            chartTheme: ref("white"),
            alarmSettingVisible,
            switchAlarm,
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
}

#side-bar {
    width: 12vw;
}

#main-content {
    width: 82vw;
    height: 90vh;
    padding-right: 10px;
}

#foot-bar {
    height: 3vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>