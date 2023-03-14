<template>
    <n-card id="dashboard" hoverable>
        <div id="dashboard-container">
            <gauge-chart id="swap-status" :argv="SwapStatus" />
            <gauge-chart id="cpu-status" :argv="CPUStatus" />
            <gauge-chart id="ram-status" :argv="RAMStatus" />
        </div>
    </n-card>
</template>

<script>
import GaugeChart from "./charts/GaugeChart.vue";
import { getBasicStatus, getAlarmFlag } from "../utils/request";
import { NCard, useNotification, NTime, useMessage } from "naive-ui";
import { h } from "vue";

//TODO 建立完整仪表盘

export default {
    components: {
        NCard,
        GaugeChart,
    },
    setup() {
        const notification = useNotification();
        const message = useMessage();
        return {
            notify(type, info) {
                notification[type](info);
            },
            message,
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
            alarmFlag: [],
        };
    },
    methods: {
        initAlarmFlag(data) {
            data.forEach((item) => {
                this.alarmFlag.push({
                    name: item.name,
                    flag: item.flag,
                    activated: item.activated,
                    //TODO 考虑在接口区分激活的Alarm和所有Alarm
                    intervalTime: item.interval_time,
                    visible: false,
                    lastTime: 0,
                });
            });
        },
        updateAlarmFlag(data) {
            let count = 0;
            for (let i = 0; i < data.length; i++) {
                this.alarmFlag[i].flag = data[i].flag;
                this.alarmFlag[i].activated = data[i].activated;
                this.alarmFlag[i].intervalTime = data[i].interval_time;
                if (this.alarmFlag[i].flag) {
                    count++;
                }
            }
            this.$store.commit("updateAlarmCount", count);
        },
        checkAlarm() {
            this.alarmFlag.forEach((item) => {
                if (item.flag && !item.visible) {
                    if (
                        item.lastTime === 0 ||
                        item.lastTime + item.intervalTime * 1000 < Date.now()
                    ) {
                        this.notify("warning", {
                            title: item.name,
                            content: `${item.name}超出警告阈值`,
                            meta: () =>
                                h(NTime, {
                                    time: Date.now(),
                                }),
                            onClose: () => {
                                this.handleNotificationClose(item.name);
                            },
                        });
                        item.visible = true;
                        item.lastTime = Date.now();
                    }
                }
            });
        },
        handleNotificationClose(name) {
            this.alarmFlag.forEach((item) => {
                if (item.name === name) {
                    item.visible = false;
                    item.lastTime = Date.now();
                    this.message.success(`${item.intervalTime}秒内不再提示`);
                }
            });
        },
    },
    beforeMount() {
        setInterval(() => {
            getBasicStatus(process.env.NODE_ENV).then((response) => {
                this.status = response.data;
                this.CPUStatus.value = this.status.cpu_percent;
                this.RAMStatus.value = this.status.ram_percent;
                this.SwapStatus.value = this.status.swap_percent;
            });
        }, 1000);

        setInterval(() => {
            getAlarmFlag().then((response) => {
                if (this.alarmFlag.length == 0) {
                    this.initAlarmFlag(response.data);
                } else {
                    this.updateAlarmFlag(response.data);
                }
                this.checkAlarm();
            });
        }, 5000);
    },
};
</script>

<style>
/*
#dashboard {
    width: 79vw;
    height: 40vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
*/

#dashboard {
    height: 47vh;
}

#dashboard-container {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
