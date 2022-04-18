<template>
    <div>
        <n-h1>Load</n-h1>
        <n-p>当前系统在过去1、5、15分钟内的平均负载（%）</n-p>

        <n-ul>
            <n-li><n-text code> load_1 </n-text> 1分钟内的系统平均负载</n-li>
            <n-li><n-text code> load_5 </n-text> 5分钟内的系统平均负载</n-li>
            <n-li><n-text code> load_15 </n-text> 15分钟内的系统平均负载</n-li>
        </n-ul>
    </div>
</template>

<script>
import { NP, NH1, NText, NUl, NLi} from "naive-ui";

export default {
    components: {
        NP,
        NH1,
        NText,
        NUl,
        NLi,
    },
    setup() {
        return {};
    },
};
</script>
