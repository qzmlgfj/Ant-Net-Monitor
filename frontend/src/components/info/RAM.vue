<template>
    <div>
        <n-h1>RAM</n-h1>
        <n-p>当前系统范围内的内存占用量,以<n-text coded>GB</n-text>为单位</n-p>

        <n-ul>
            <n-li><n-text code> availiable </n-text> 可用内存量</n-li>
            <n-li><n-text code> used </n-text> 已使用内存量</n-li>
            <n-li><n-text code> cached </n-text> 缓存数据占用的内存量</n-li>
            <n-li><n-text code> buffers </n-text> 缓存文件系统元数据等内容占有的内存量</n-li>
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
