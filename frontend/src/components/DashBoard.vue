<template>
    <n-card hoverable>
        <div id="dashboard">
            <gauge-chart id="swap-status" :argv="SwapStatus" />
            <gauge-chart id="cpu-status" :argv="CPUStatus" />
            <gauge-chart id="ram-status" :argv="RAMStatus" />
        </div>
    </n-card>
</template>

<script>
import GaugeChart from "./charts/GaugeChart.vue";
import { getBasicStatus, getAlarmFlag } from "../utils/request";
import { NCard, useNotification } from "naive-ui";

//TODO 建立完整仪表盘

export default {
    components: {
        NCard,
        GaugeChart,
    },
    setup() {
        const notification = useNotification();
        return {
            notify(type, info) {
                notification[type](info);
            },
        };
    },
    data() {
        return {
            status: {},
            CPUStatus: {
                name: "CPU",
                value: 0,
                height: "45vh",
            },
            RAMStatus: {
                name: "Used RAM",
                value: 0,
                height: "35vh",
            },
            SwapStatus: {
                name: "Used Swap",
                value: 0,
                height: "35vh",
            },
            alarmFlag: {},
        };
    },
    methods: {},
    beforeMount() {
        setInterval(() => {
            if (process.env.NODE_ENV === "development") {
                this.CPUStatus.value = (Math.random() * 100).toFixed(1);
                this.RAMStatus.value = (Math.random() * 100).toFixed(1);
                this.SwapStatus.value = (Math.random() * 100).toFixed(1);
            } else {
                getBasicStatus(process.env.NODE_ENV).then((response) => {
                    this.status = response.data;
                    this.CPUStatus.value = this.status.cpu_percent;
                    this.RAMStatus.value = this.status.ram_percent;
                    this.SwapStatus.value = this.status.swap_percent;
                });
            }
        }, 1000);

        setInterval(() => {
            getAlarmFlag().then((response) => {
                this.alarmFlag = response.data;
            });
        }, 5000);
    },
    watch: {
        alarmFlag: {
            // FIXME 改改逻辑，重复弹窗
            handler: function (alarmFlag) {
                if (alarmFlag.cpu_usage) {
                    console.log("cpu_usage");
                    this.notify("warning", {
                        content: "CPU usage is too high",
                        meta: Date.now(),
                    });
                }
                if (alarmFlag.cpu_steal) {
                    console.log("cpu_steal");
                    this.notify("warning", {
                        content: "CPU steal time is too high",
                        meta: Date.now(),
                    });
                }
                if (alarmFlag.cpu_iowait) {
                    console.log("cpu_iowait");
                    this.notify("warning", {
                        content: "CPU iowait time is too high",
                        meta: Date.now(),
                    });
                }
            },
            deep: true,
            immediate: true,
        },
    },
};
</script>

<style>
#dashboard {
    width: 79vw;
    height: 40vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
