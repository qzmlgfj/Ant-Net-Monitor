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
} from "echarts/components";
import { LineChart } from "echarts/charts";
import { UniversalTransition } from "echarts/features";
import { CanvasRenderer } from "echarts/renderers";
import VChart from "vue-echarts";

use([
    TitleComponent,
    ToolboxComponent,
    TooltipComponent,
    GridComponent,
    LineChart,
    CanvasRenderer,
    UniversalTransition
]);

//TODO 暂时删去了DataZoomComponent

export default {
    name: "LineChart",
    components: {
        VChart,
    },
    props: ["argv"],
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
    },
};
</script>

<style scoped>
.chart {
    height: 37vh;
    width: 48vw;
}
</style>
