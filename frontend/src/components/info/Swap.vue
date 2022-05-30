<template>
    <div>
        <n-h1>Swap</n-h1>
        <n-p>当前系统范围内的交换内存占用量，以<n-text code>GiB</n-text>为单位.</n-p>

        <n-p><n-text code>free</n-text>命令也提供了交换内存信息的查看.</n-p>
    </div>
</template>

<script>
import { NP, NH1, NText } from "naive-ui";

export default {
    components: {
        NP,
        NH1,
        NText,
    },
    setup() {
        return {};
    },
};
</script>
