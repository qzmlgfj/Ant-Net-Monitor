<template>
    <div>
        <gauge-chart id="CPU" :argv="CPU" />
        <gauge-chart :argv="CPU" />
    </div>
</template>

<script>
import GaugeChart from "./charts/GaugeChart.vue";
import { getStatus } from "../utils/request";

export default {
    components: {
        GaugeChart,
    },
    data() {
        return {
            status: {},
            CPU: 0,
        };
    },
    methods: {},
    beforeMount() {
        setInterval(() => {
            getStatus().then((response) => {
                this.status = response.data;
                this.CPU = this.status.cpu;
            });
        }, 1000);
    },
};
</script>
