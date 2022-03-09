<template>
        <n-card hoverable>
            <div id="dashboard">
                <gauge-chart :argv="CPUStatus" />
                <gauge-chart :argv="MemStatus" />
            </div>
        </n-card>
</template>

<script>
import GaugeChart from "./charts/GaugeChart.vue";
import { getStatus } from "../utils/request";
import { NCard } from "naive-ui";

//TODO 建立完整仪表盘

export default {
    components: {
        NCard,
        GaugeChart,
    },
    data() {
        return {
            status: {},
            CPUStatus: {
                name: "CPU",
                value: 0,
                height: "40vh",
            },
            MemStatus: {
                name: "Used RAM",
                value: 0,
                height: "35vh",
            },
        };
    },
    methods: {},
    beforeMount() {
        setInterval(() => {
            if (process.env.NODE_ENV === "development") {
                this.CPUStatus.value = (Math.random() * 100).toFixed(1);
                this.MemStatus.value = (Math.random() * 100).toFixed(1);
            } else {
                getStatus().then((response) => {
                    this.status = response.data;
                    this.CPUStatus.value = this.status.cpu_percent;
                    this.MemStatus.value = this.status.ram_percent;
                });
            }
        }, 1000);
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
