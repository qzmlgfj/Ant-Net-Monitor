<template>
    <n-card
        style="width: 600px"
        title="警报相关"
        :bordered="false"
        size="huge"
        role="dialog"
        aria-modal="true"
        footer-style="display:flex;justify-content:flex-end;"
        closable
        @close="switchAlarm"
    >
        <n-data-table
            remote
            striped 
            ref="table"
            :columns="columns"
            :data="data"
            :loading="loadingFlag"
            :row-key="rowKey"
        />

        <!--
        <template #footer>
            <n-button type="primary">保存</n-button>
            <n-button type="default">取消</n-button>
        </template>
        -->
    </n-card>
</template>

<script>
import { ref, h } from "vue";
import { NCard, NDataTable, NText, NTag } from "naive-ui";
import { getAlarmFlag } from "../utils/request";

const createColumns = () => {
    return [
        {
            title: "指标",
            key: "name",
            render(row) {
                return h(
                    NText,
                    {
                        code: true,
                    },
                    {
                        default: () => row.name,
                    }
                );
            },
        },
        {
            title: "警告阈值",
            key: "alarm_value",
        },
        {
            title: "状态",
            key: "flag",
            render(row) {
                return h(
                    NTag,
                    {
                        type: row.flag ? "error" : "success",
                    },
                    {
                        default: () => (row.flag ? "警报" : "正常"),
                    }
                );
            },
        },
    ];
};

export default {
    components: {
        NCard,
        NDataTable,
    },
    setup() {
        const columns = createColumns();
        const data = ref([]);
        const loadingFlag = ref(true);

        const initData = function () {
            getAlarmFlag().then((response) => {
                data.value = response.data;
                loadingFlag.value = false;
            });
        };

        const rowKey = (rowData) => rowData.name;

        initData();

        return {
            columns,
            data,
            loadingFlag,
            initData,
            rowKey,
        };
    },
    methods: {
        switchAlarm() {
            this.$emit("switchAlarm");
        },
    },
};
</script>
