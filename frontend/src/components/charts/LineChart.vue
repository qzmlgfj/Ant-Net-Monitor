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
import VChart from "vue-echarts";

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
    //props: ["argv"],
    setup() {
        let base = +new Date(1988, 9, 3);
        const oneDay = 24 * 3600 * 1000;
        const fakedata = [[base, Math.random() * 300]];
        const fakedata1 = [[base, Math.random() * 300]];
        for (let i = 1; i < 100; i++) {
            const now = new Date((base += oneDay));
            fakedata.push([
                +now,
                Math.round((Math.random() - 0.5) * 20 + fakedata[i - 1][1]),
            ]);
            fakedata1.push([
                +now,
                Math.round((Math.random() - 0.5) * 20 + fakedata1[i - 1][1]),
            ]);
        }
        return {
            fakedata,
            fakedata1
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
                    text: "Large Ara Chart",
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
                dataZoom: [
                    {
                        type: "inside",
                        start: 0,
                        end: 20,
                    },
                    {
                        start: 0,
                        end: 20,
                    },
                ],
                series: [
                    {
                        name: "Fake Data",
                        type: "line",
                        smooth: true,
                        symbol: "none",
                        areaStyle: {},
                        data: this.fakedata,
                    },
                    {
                        name: "Fake Data1",
                        type: "line",
                        smooth: true,
                        symbol: "none",
                        areaStyle: {},
                        data: this.fakedata1,
                    },
                ],
            },
        };
    },
};
</script>

<style scoped>
.chart {
    height: 37vh;
    width: 48vw;
}
</style>
