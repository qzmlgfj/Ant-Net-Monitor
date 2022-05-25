<template>
    <div>
        <n-h1>Network</n-h1>
        <n-p>当前网络接收/发送数据量情况，以<n-text code>MiB/s</n-text>为单位.</n-p>
        <n-ul>
            <n-li><n-text code> send </n-text> 接收数据量</n-li>
            <n-li><n-text code> receive </n-text> 发送数据量</n-li>
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
