<template>
    <n-text depth="3">Ant Net Monitor {{version}} · Made by Ant</n-text>
</template>

<script>
import { NText } from "naive-ui";

import { getVersion } from "@/utils/request";

export default {
    components: {
        NText,
    },
    data() {
        return {
            version: "",
        };
    },
    mounted() {
        getVersion().then((res) => {
            this.version = res.data;
        });
    },
};
</script>
