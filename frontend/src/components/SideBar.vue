<template>
    <n-menu :options="menuOptions" />
</template>

<script>
import { h } from "vue";
import { NMenu, NIcon } from "naive-ui";
import { RouterLink } from "vue-router";
import {Cpu} from "@vicons/tabler";
import {Memory} from "@vicons/fa";
import {VmdkDisk} from "@vicons/carbon";

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
    {
        label: () =>
            h(
                RouterLink,
                {
                    to: {
                        name: "Disk-Info",
                    },
                },
                {
                    default: () => "Disk",
                }
            ),
        key: "Disk",
        icon: renderIcon(VmdkDisk),
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
