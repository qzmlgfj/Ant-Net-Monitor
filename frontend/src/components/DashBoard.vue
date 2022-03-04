<template>
    <div id='dashboard'>
        <gauge-chart :argv="CPUStatus" />
        <gauge-chart :argv="MemStatus" />
    </div>
</template>

<script>
import GaugeChart from "./charts/GaugeChart.vue";
import { getStatus } from "../utils/request";

//TODO 建立完整仪表盘，以及前端部分标记测试的环境变量

export default {
    components: {
        GaugeChart,
    },
    data() {
        return {
            status: {},
            CPUStatus:{
                name: "CPU",
                value: 0,
                height: "90%",
            },
            MemStatus:{
                name: "Used RAM",
                value: 0,
                height: "75%",
            },
        };
    },
    methods: {},
    beforeMount() {
        setInterval(() => {
            getStatus().then((response) => {
                this.status = response.data;
                this.CPUStatus.value = this.status.cpu;
                this.MemStatus.value = this.status.memory;
            });
        }, 1000);
    },
};
</script>

<style>
#dashboard {
    height: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
