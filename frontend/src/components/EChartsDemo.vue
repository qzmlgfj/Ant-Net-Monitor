<template>
    <v-chart class="chart" :option="option" />
</template>

<script>
import { use } from "echarts/core";
import {
    TitleComponent,
    TooltipComponent,
    GridComponent,
} from "echarts/components";
import { LineChart } from "echarts/charts";
import { UniversalTransition } from "echarts/features";
import { CanvasRenderer } from "echarts/renderers";
import VChart, { THEME_KEY } from "vue-echarts";
import {ref} from "vue";

use([
    TitleComponent,
    TooltipComponent,
    GridComponent,
    LineChart,
    CanvasRenderer,
    UniversalTransition,
]);

export default {
    name: "HelloWorld",
    components: {
        VChart,
    },
    provide: {
        [THEME_KEY]: "white",
    },
    setup() {
        const randomData = () => {
            now = new Date(+now + oneDay);
            value = value + Math.random() * 21 - 10;
            return {
                name: now.toString(),
                value: [
                    [now.getFullYear(), now.getMonth() + 1, now.getDate()].join(
                        "/"
                    ),
                    Math.round(value),
                ],
            };
        };
        const data = ref([]);
        let now = new Date(1997, 9, 3);
        let oneDay = 24 * 3600 * 1000;
        let value = Math.random() * 1000;
        for (var i = 0; i < 1000; i++) {
            data.value.push(randomData());
        }

        const updateData = () => {
            data.value.shift();
            data.value.push(randomData());
        };
        const option = {
            title: {
                text: "Dynamic Data & Time Axis",
            },
            tooltip: {
                trigger: "axis",
                formatter: function (params) {
                    params = params[0];
                    let date = new Date(params.name);
                    return (
                        date.getDate() +
                        "/" +
                        (date.getMonth() + 1) +
                        "/" +
                        date.getFullYear() +
                        " : " +
                        params.value[1]
                    );
                },
                axisPointer: {
                    animation: false,
                },
            },
            xAxis: {
                type: "time",
                splitLine: {
                    show: false,
                },
            },
            yAxis: {
                type: "value",
                boundaryGap: [0, "100%"],
                splitLine: {
                    show: false,
                },
            },
            series: [
                {
                    name: "Fake Data",
                    type: "line",
                    showSymbol: false,
                    data: data.value,
                },
            ],
        };
        return {
            option,
            data,
            randomData,
            updateData,
        };
    },
    methods: {
        hello: function () {
            console.log("hello");
        },
    },
    mounted: function () {
        /*setInterval 中的function this会指向Window*/
        setInterval(() => {
            this.updateData();
            this.hello();
        }, 1000);
    },
};
</script>

<style scoped>
.chart {
    height: 400px;
}
</style>