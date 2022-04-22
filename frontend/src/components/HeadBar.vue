<template>
    <div id="header">
        <n-h1>Ant Net Monitor</n-h1>
        <div id="header-end">
            <n-space>
                <n-button @click="changeTheme" id="change-theme" quaternary>
                    <template #icon>
                        <n-icon>
                            <switch-horizontal />
                        </n-icon>
                    </template>
                    切换主题
                </n-button>
                <n-button @click="switchAlarm" quaternary>
                    <template #icon>
                        <n-icon><thermometer-half /></n-icon>
                    </template>
                    异常警报
                </n-button>
            </n-space>
        </div>
    </div>
</template>

<script>
import { NH1, NButton, NIcon, NSpace } from "naive-ui";
import { SwitchHorizontal } from "@vicons/tabler";
import { ThermometerHalf } from "@vicons/fa";
export default {
    components: {
        NH1,
        NButton,
        NIcon,
        NSpace,
        SwitchHorizontal,
        ThermometerHalf,
    },
    methods: {
        changeTheme() {
            this.$emit("changeTheme");
        },
        switchAlarm() {
            this.$emit("alarm");
        },
    },
};
</script>

<style scoped>
#header {
    display: flex;
    align-items: center;
    padding: 5px;
    padding-left: 20px;
}

.n-h1 {
    margin: 0;
}

#header-end {
    display: flex;
    width: 85%;
    justify-content: flex-end;
}
</style>
