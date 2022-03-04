<template>
    <div>
        <n-h1>RAM</n-h1>
        <n-p>RAM占用率</n-p>
    </div>
</template>

<script>
import { NP, NH1 } from "naive-ui";

export default {
    components: {
        NP,
        NH1,
    },
    setup() {
        return {};
    },
};
</script>

<style scoped>
div {
    height: 40%;
}
</style>
