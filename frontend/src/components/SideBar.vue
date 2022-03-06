<template>
    <n-menu id="sidebar" :options="menuOptions" />
</template>

<script>
import { h } from "vue";
import { NMenu } from "naive-ui";
import { RouterLink } from "vue-router";

const menuOptions = [
    {
        label: () =>
            h(
                RouterLink,
                {
                    to: {
                        name: "CPU-Info",
                    },
                },
                {
                    default: () => "CPU",
                }
            ),
        key: "CPU",
    },
    {
        label: () =>
            h(
                RouterLink,
                {
                    to: {
                        name: "RAM-Info",
                    },
                },
                {
                    default: () => "RAM",
                }
            ),
        key: "RAM",
    },
];

export default {
    components: {
        NMenu,
    },
    data(){
        return {
            menuOptions,
        };
    },
};
</script>

<style>
#sidebar {
    width: 12vw;
}
</style>
