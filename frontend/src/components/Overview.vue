<template>
    <div id="overview">
        <n-space wrap="false" size="large" justify="space-between">
            <n-card hoverable>
                <n-layout
                    :native-scrollbar="false"
                    style="height: 35vh"
                >
                    <alarm-time-line />
                </n-layout>
            </n-card>
        </n-space>
    </div>
</template>

<script>
import { NCard, NLayout } from "naive-ui";
import AlarmTimeLine from "@/components/overview/AlarmTimeLine.vue";

export default {
    components: {
        NCard,
        NLayout,
        AlarmTimeLine,
    },
};
</script>

<style scoped>
#overview {
    height: 45%;
}
</style>
