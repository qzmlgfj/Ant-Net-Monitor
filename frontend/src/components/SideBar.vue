<template>
    <n-menu :options="menuOptions" />
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
                        name: "Test-A",
                    },
                },
                {
                    default: () => "Change to A",
                }
            ),
        key: "Test-A",
    },
    {
        label: () =>
            h(
                RouterLink,
                {
                    to: {
                        name: "Test-B",
                    },
                },
                {
                    default: () => "Change to B",
                }
            ),
        key: "Test-B",
    },
];

export default {
    components: {
        NMenu,
    },
    setup() {
        return {
            menuOptions,
        };
    },
};
</script>