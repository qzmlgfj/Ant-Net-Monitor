<template>
    <v-chart class="chart" :option="option" />
</template>

<script>
import { use } from "echarts/core";
import {
    TitleComponent,
    ToolboxComponent,
    TooltipComponent,
    GridComponent,
    LegendComponent,
} from "echarts/components";
import { LineChart } from "echarts/charts";
import { UniversalTransition } from "echarts/features";
import { CanvasRenderer } from "echarts/renderers";
import VChart, { THEME_KEY } from "vue-echarts";

use([
    TitleComponent,
    ToolboxComponent,
    TooltipComponent,
    GridComponent,
    LegendComponent,
    LineChart,
    CanvasRenderer,
    UniversalTransition,
]);

export default {
    name: "Demo",
    components: {
        VChart,
    },
    props:['option'],
    provide: {
        [THEME_KEY]: "white",
    },
    beforeMount: function(){
        setInterval(()=>{
            console.log(this.option.url);
        },1000)
    }
};
/*setInterval 中的function this会指向Window*/
</script>

<style scoped>
.chart {
    height: 400px;
}
</style>