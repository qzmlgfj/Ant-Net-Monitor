<script>
import { NTimeline, NTimelineItem, NText, NTime, NEmpty } from "naive-ui";
import { h } from "vue";

import { getAlarmLog } from "@/utils/request";

export default {
    render() {
        if (this.alarmLog.length === 0) {
            return h(NEmpty, {
                description: "无警报记录",
            });
        } else {
            return h(
                NTimeline,
                {
                    size: "large",
                },
                this.alarmLog.map((item) => {
                    return h(NTimelineItem, {
                        title: h(
                            NText,
                            { code: true },
                            {
                                default: () => item.name,
                            }
                        ),
                        type: item.status === "warning" ? "warning" : "success",
                        time: h(NTime, {
                            type: "datetime",
                            time: new Date(item.time_stamp),
                        }),
                    });
                })
            );
        }
    },
    data() {
        return {
            alarmLog: [],
        };
    },
    methods: {
        //! 好刺激的异步处理
        async getAlarmLog() {
            const res = await getAlarmLog();
            this.alarmLog = res.data;
        },
    },
    mounted() {
        this.getAlarmLog();
    },
};
</script>
