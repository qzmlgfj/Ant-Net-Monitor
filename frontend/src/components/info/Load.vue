<template>
    <div>
        <n-h1>Load</n-h1>
        <n-p>当前系统在过去1、5、15分钟内的平均负载（%），在终端可以使用<n-text code>uptime</n-text>命令查看具体情况.</n-p>
        <n-ul>
            <n-li><n-text code> load_1 </n-text> 1分钟内的系统平均负载</n-li>
            <n-li><n-text code> load_5 </n-text> 5分钟内的系统平均负载</n-li>
            <n-li><n-text code> load_15 </n-text> 15分钟内的系统平均负载</n-li>
        </n-ul>
        <n-p>
            在单核系统上，<n-text code> 1.0 </n-text>的负载意味着CPU满载，
            峰值短暂超出<n-text code> 1.0 </n-text>的情况可以接受，
            在实践中，许多管理员遵循以下的规则：
        </n-p>
        <n-ul>
            <n-li>需要注意：<n-text code> 0.7 </n-text> 系统可能存在异常情况</n-li>
            <n-li>立即修复：<n-text code> 1.0 </n-text> 系统已经满载，置之不顾可能会导致严重问题</n-li>
            <n-li>大事不妙：<n-text code> 5.0 </n-text> 此时系统严重卡顿，不要让事情走到这一步</n-li>
        </n-ul>
        <n-p>
            在多核系统上，CPU的满载和CPU内核数挂钩，满载在双核系统上表现为<n-text code> 2.0 </n-text>，
            四核系统上表现为<n-text code> 4.0 </n-text>，依此类推.
        </n-p>
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
