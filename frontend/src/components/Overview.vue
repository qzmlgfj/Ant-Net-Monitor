<template>
    <div id="overview">
        <n-space wrap="false" size="large" justify="space-between">
            <n-card id="alarm-timeline" title="警报历史" hoverable>
                <n-scrollbar style="height: 30vh">
                    <alarm-time-line />
                </n-scrollbar>
            </n-card>
            <n-card id="system-info" title="系统详情" hoverable>
                <n-scrollbar style="height: 30vh">
                    <system-info />
                </n-scrollbar>
            </n-card>
        </n-space>
    </div>
</template>

<script>
import { NSpace, NCard, NScrollbar } from "naive-ui";

import AlarmTimeLine from "@/components/overview/AlarmTimeLine.vue";
import SystemInfo from "@/components/overview/SystemInfo.vue";

export default {
    components: {
        NSpace,
        NCard,
        NScrollbar,
        AlarmTimeLine,
        SystemInfo,
    },
};
</script>

<style scoped>
#overview {
    height: 45%;
}

#alarm-timeline {
    height: 38vh;
    width: 37vw;
}

#system-info {
    height: 38vh;
    width: 47vw;
}
</style>
