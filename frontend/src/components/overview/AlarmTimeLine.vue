<script>
import { NTimeline, NTimelineItem, NText } from "naive-ui";
import { h } from "vue";

const AlarmLog = [
    {
        name: "cpu_status",
        status: "warning",
        time: "2020-05-01 12:00:00",
    },
    {
        name: "cpu_status",
        status: "recover",
        time: "2020-05-01 12:05:00",
    },
    {
        name: "ram_status",
        status: "warning",
        time: "2020-05-01 12:15:00",
    },
    {
        name: "ram_status",
        status: "warning",
        time: "2020-05-01 12:15:00",
    },
    {
        name: "ram_status",
        status: "warning",
        time: "2020-05-01 12:15:00",
    },
    {
        name: "ram_status",
        status: "warning",
        time: "2020-05-01 12:15:00",
    },
    {
        name: "ram_status",
        status: "warning",
        time: "2020-05-01 12:15:00",
    },
];

export default {
    render() {
        return h(
            NTimeline,
            {
                size: "large",
            },
            AlarmLog.map((item) => {
                return h(NTimelineItem, {
                    title: h(
                        NText,
                        { code: true },
                        {
                            default: () => item.name,
                        }
                    ),
                    type: item.status === "warning" ? "warning" : "success",
                    time: item.time,
                });
            })
        );
    },
};
</script>
