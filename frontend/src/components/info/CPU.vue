<template>
    <div>
        <n-h1>CPU</n-h1>
        <n-p>
            当前系统范围的CPU占用率（%），在终端可以使用<n-text code>top</n-text>命令查看.
        </n-p>
        <n-ul>
            <n-li><n-text code> user </n-text> 用户级进程的CPU占用率</n-li>
            <n-li><n-text code> nice </n-text> 低优先级用户进程的CPU占用率</n-li>
            <n-li><n-text code> system </n-text> 系统级进程的CPU占用率</n-li>
            <n-li><n-text code> iowait </n-text> 等待I/O时的CPU占用率</n-li>
            <n-li><n-text code> steal </n-text> 被其它虚拟机挪用的CPU占用率</n-li>
        </n-ul>
        <n-p>
            请留意其中的<n-text code>iowait</n-text>指标，如果它持续处在较高的范围，意味着磁盘会拖慢系统性能，此外较高的<n-text code>steal</n-text>也会影响系统正常运行.
        </n-p>
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
    setup() {
        return {};
    },
};
</script>
