<template>
    <v-chart class="chart" :option="option" autoresize />
</template>

<script>
import { use } from "echarts/core";
import {
    TitleComponent,
    ToolboxComponent,
    TooltipComponent,
    GridComponent,
    DataZoomComponent,
} from "echarts/components";
import { LineChart } from "echarts/charts";
import { UniversalTransition } from "echarts/features";
import { CanvasRenderer } from "echarts/renderers";
import VChart, { UPDATE_OPTIONS_KEY } from "vue-echarts";

use([
    TitleComponent,
    ToolboxComponent,
    TooltipComponent,
    GridComponent,
    LineChart,
    CanvasRenderer,
    UniversalTransition,
    DataZoomComponent,
]);

export default {
    name: "LineChart",
    components: {
        VChart,
    },
    props: ["argv", "enableZoom"],
    provide() {
        return {
            [UPDATE_OPTIONS_KEY]: {
                notMerge: true,
            },
        };
    },
    data() {
        return {
            option: {
                tooltip: {
                    trigger: "axis",
                    position: function (pt) {
                        return [pt[0], "10%"];
                    },
                },
                title: {
                    left: "center",
                    text: "Historical Situation",
                },
                toolbox: {
                    feature: {
                        dataZoom: {
                            yAxisIndex: "none",
                        },
                        restore: {},
                        saveAsImage: {},
                    },
                },
                xAxis: {
                    type: "time",
                    boundaryGap: false,
                },
                yAxis: {
                    type: "value",
                    boundaryGap: [0, "100%"],
                },
                series: this.argv,
            },
        };
    },
    watch: {
        //! I hate syntactic sugar
        argv: {
            handler: function (argv) {
                this.option.series = argv;
            },
            deep: true,
            immediate: true,
        },
        enableZoom: {
            handler: function (enableZoom) {
                if (enableZoom) {
                    this.option.dataZoom = [
                        {
                            type: "inside",
                            start: 0,
                            end: 20,
                        },
                        {
                            start: 0,
                            end: 20,
                        },
                    ];
                } else {
                    this.option.dataZoom = null;
                }
            },
        },
    },
};
</script>

<style scoped>
.chart {
    height: 32vh;
    width: 48vw;
}
</style>
