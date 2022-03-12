<template>
    <n-menu id="sidebar" :options="menuOptions" />
</template>

<script>
import { h } from "vue";
import { NMenu, NIcon } from "naive-ui";
import { RouterLink } from "vue-router";
import {Cpu} from "@vicons/tabler";
import {Memory} from "@vicons/fa"

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
        icon: renderIcon(Cpu),
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
        icon: renderIcon(Memory),
    },
];

function renderIcon(icon) {
  return () => h(NIcon, null, { default: () => h(icon) });
}

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
