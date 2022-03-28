<template>
    <div id="header">
        <n-h1>Ant Net Monitor</n-h1>
        <n-space id="header-end">
            <n-button @click="changeTheme" id="change-theme" quaternary>
                <template #icon>
                    <n-icon>
                        <switch-horizontal />
                    </n-icon>
                </template>
                切换主题
            </n-button>
        </n-space>
    </div>
</template>

<script>
import { NH1, NButton, NIcon, NSpace } from "naive-ui";
import { SwitchHorizontal } from "@vicons/tabler";
export default {
    components: {
        NH1,
        NButton,
        NIcon,
        NSpace,
        SwitchHorizontal,
    },
    methods: {
        changeTheme() {
            this.$emit("changeTheme");
        },
    },
};
</script>

<style scoped>
#header {
    display: flex;
    align-items: center;
}

.n-h1 {
    margin: 0;
}

#header-end {
    position: relative;
    left: 80vw;
}
</style>
