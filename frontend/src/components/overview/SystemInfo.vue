<template>
    <n-grid :x-gap="12" :y-gap="8" :cols="3">
        <n-gi>
            <n-statistic label="处理器内核数" tabular-nums>
                <n-number-animation :from="0" :to="cpuCount" />
                <template #suffix> Core(s) </template>
            </n-statistic>
        </n-gi>
        <n-gi>
            <n-statistic label="内存容量" tabular-nums>
                <n-number-animation :from="0" :to="totalRAM" :precision="2" />
                <template #suffix> GiB </template>
            </n-statistic>
        </n-gi>
        <n-gi>
            <n-statistic label="交换内存容量" tabular-nums>
                <n-number-animation :from="0" :to="totalSwap" :precision="2" />
                <template #suffix> GiB </template>
            </n-statistic>
        </n-gi>
        <n-gi>
            <n-statistic label="磁盘容量" tabular-nums>
                <n-number-animation :from="0" :to="totalDisk" :precision="2" />
                <template #suffix> GiB </template>
            </n-statistic>
        </n-gi>
        <n-gi>
            <n-statistic label="磁盘占用率" tabular-nums>
                <n-number-animation :from="0" :to="diskPercent" :precision="2" />
                <template #suffix> % </template>
            </n-statistic>
        </n-gi>
    </n-grid>
</template>

<script>
import { NGrid, NGi, NStatistic, NNumberAnimation } from "naive-ui";

import { getSystemInfo } from "@/utils/request";

export default {
    components: {
        NGrid,
        NGi,
        NStatistic,
        NNumberAnimation,
    },
    data() {
        return {
            cpuCount: 0,
            totalRAM: 0,
            totalSwap: 0,
            totalDisk: 0,
            diskPercent: 0,
        };
    },
    methods: {
        async getSystemInfo() {
            const res = await getSystemInfo();
            this.cpuCount = res.data.cpu_count;
            this.totalRAM = res.data.ram_total;
            this.totalSwap = res.data.swap_total;
            this.totalDisk = res.data.disk_total;
            this.diskPercent = res.data.disk_percent;
        },
    },
    mounted() {
        this.getSystemInfo();
    },
};
</script>
