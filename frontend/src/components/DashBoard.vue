<template>
    <div id="dashboard">
        <gauge-chart :argv="CPUStatus" />
        <gauge-chart :argv="MemStatus" />
    </div>
</template>

<script>
import GaugeChart from "./charts/GaugeChart.vue";
import { getStatus } from "../utils/request";

//TODO 建立完整仪表盘

export default {
    components: {
        GaugeChart,
    },
    data() {
        return {
            status: {},
            CPUStatus: {
                name: "CPU",
                value: 0,
                height: "90%",
            },
            MemStatus: {
                name: "Used RAM",
                value: 0,
                height: "75%",
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
                    this.CPUStatus.value = this.status.cpu;
                    this.MemStatus.value = this.status.memory;
                });
            }
        }, 1000);
    },
};
</script>

<style>
#dashboard {
    width: 88vw;
    height: 45vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
