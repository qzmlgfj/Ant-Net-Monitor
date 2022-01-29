<template>
    <gauge-chart :argv="argv[0]" />
</template>

<script>
import GaugeChart from "./charts/GaugeChart.vue";

export default {
    components: {
        GaugeChart,
    },
    data() {
        return {
            argv: [],
        };
    },
    methods: {
        addArgv(name, type, value) {
            this.argv.push({ name, type, value });
        },
    },
    beforeMount() {
        this.addArgv("CPU", "Main", 50);
        setInterval(() => {
            this.argv[0].value = Math.floor(Math.random() * 100);
        }, 1000);
    },
};
</script>
