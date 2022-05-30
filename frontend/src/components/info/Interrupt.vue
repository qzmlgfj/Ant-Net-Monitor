<template>
    <div>
        <n-h1>Interrupt</n-h1>
        <n-p>当前系统范围内每秒钟的中断数.</n-p>

        <n-ul>
            <n-li><n-text code> interrupt </n-text> 系统中断数</n-li>
            <n-li><n-text code> soft_interrupt </n-text> 系统软中断数</n-li>
        </n-ul>
    </div>

    
</template>

<script>
import { NP, NH1, NText, NUl, NLi } from "naive-ui";

export default {
    components: {
        NP,
        NH1,
        NText,
        NUl,
        NLi,
    },
};
</script>
