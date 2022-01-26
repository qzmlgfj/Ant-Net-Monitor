<template>
    <v-chart class="chart" :option="option" />
</template>

<script>
import { use } from "echarts/core";
import { GaugeChart } from "echarts/charts";
import { CanvasRenderer } from "echarts/renderers";
import VChart, { THEME_KEY } from "vue-echarts";
use([GaugeChart, CanvasRenderer]);

export default {
    name: "DashBoard",
    components: {
        VChart
    },
    provide: {
        [THEME_KEY]: "white",
    },
    data: function () {
        return {
            option: {
                series: [
                    {
                        type: "gauge",
                        axisLine: {
                            lineStyle: {
                                width: 30,
                                color: [
                                    [0.3, "#67e0e3"],
                                    [0.7, "#37a2da"],
                                    [1, "#fd666d"],
                                ],
                            },
                        },
                        pointer: {
                            itemStyle: {
                                color: "auto",
                            },
                        },
                        axisTick: {
                            distance: -30,
                            length: 8,
                            lineStyle: {
                                color: "#fff",
                                width: 2,
                            },
                        },
                        splitLine: {
                            distance: -30,
                            length: 30,
                            lineStyle: {
                                color: "#fff",
                                width: 4,
                            },
                        },
                        axisLabel: {
                            color: "auto",
                            distance: 40,
                            fontSize: 20,
                        },
                        detail: {
                            valueAnimation: true,
                            formatter: "{value} %",
                            color: "auto",
                        },
                        data: [
                            {
                                value: 70,
                            },
                        ],
                    },
                ],
            },
        };
    },
    beforeMount: function () {
        setInterval(() => {
            this.option.series[0].data[0].value = (Math.random() * 100).toFixed(2)
        }, 1000);
    },
};
</script>
