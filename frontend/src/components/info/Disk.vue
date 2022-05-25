<template>
    <div>
        <n-h1>Disk</n-h1>
        <n-p>当前磁盘的读写量，以<n-text code>MiB/s</n-text>为单位.</n-p>

        <n-ul>
            <n-li><n-text code> read </n-text> 磁盘读取量</n-li>
            <n-li><n-text code> write </n-text> 磁盘写入量</n-li>
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
