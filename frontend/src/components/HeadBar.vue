<template>
    <n-space>
        <n-h1>Ant Net Monitor</n-h1>
        <n-button @click="changeTheme">Change</n-button>
    </n-space>
</template>

<script>
import { NSpace, NH1, NButton } from "naive-ui";
export default {
    components: {
        NSpace,
        NH1,
        NButton,
    },
    methods: {
        changeTheme() {
            this.$emit("changeTheme");
        },
    },
};
</script>