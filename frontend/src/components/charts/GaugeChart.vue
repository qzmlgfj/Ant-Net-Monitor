<template>
    <v-chart class="chart" :option="option" autoresize />
</template>

<script>
import { use } from "echarts/core";
import { GaugeChart } from "echarts/charts";
import { CanvasRenderer } from "echarts/renderers";
import VChart, { THEME_KEY } from "vue-echarts";
use([GaugeChart, CanvasRenderer]);

export default {
    name: "GaugeChart",
    components: {
        VChart,
    },
    props: ["argv"],
    provide: {
        [THEME_KEY]: "white",
    },
    data: function () {
        return {
            option: {
                tooltip: {
                    formatter: "{a} <br/>{b} : {c}%",
                },
                series: [
                    {
                        name: this.argv.name,
                        type: "gauge",
                        progress: {
                            show: true,
                        },
                        detail: {
                            valueAnimation: true,
                            formatter: "{value} %",
                        },
                        data: [
                            {
                                value: this.argv.value,
                                name: this.argv.name,
                            },
                        ],
                    },
                ],
            },
            height: this.argv.height,
        };
    },
    watch: {
        //! I hate syntactic sugar
        argv: {
            handler: function (argv) {
                this.option.series[0].data[0].value = argv.value;
            },
            deep: true,
            immediate: true,
        }
    },
};
</script>

<style>
.chart {
    width: 25%;
    height: v-bind(height);
    display: inline-block;
}
</style>
