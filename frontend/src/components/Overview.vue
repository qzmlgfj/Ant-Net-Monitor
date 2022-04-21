<template>
    <div id="overview">
        <n-space wrap="false" size="large" justify="space-between">
            <n-card hoverable>
                <n-scrollbar
                    style="height: 35vh"
                >
                    <alarm-time-line />
                </n-scrollbar>
            </n-card>
        </n-space>
    </div>
</template>

<script>
import { NCard, NScrollbar } from "naive-ui";
import AlarmTimeLine from "@/components/overview/AlarmTimeLine.vue";

export default {
    components: {
        NCard,
        NScrollbar,
        AlarmTimeLine,
    },
};
</script>

<style scoped>
#overview {
    height: 45%;
}
</style>
