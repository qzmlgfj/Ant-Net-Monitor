<template>
    <div>
        <n-h1>RAM</n-h1>
        <n-p>当前系统范围内的内存占用量，以<n-text code>GiB</n-text>为单位，在终端可以使用<n-text code>free -m</n-text>命令查看.</n-p>
        <n-ul>
            <n-li><n-text code> free </n-text> 未使用内存量</n-li>
            <n-li><n-text code> used </n-text> 已使用内存量</n-li>
            <n-li><n-text code> cached </n-text> 页面缓存占用的内存量</n-li>
            <n-li><n-text code> buffers </n-text> 内核缓冲区占用的内存量</n-li>
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
