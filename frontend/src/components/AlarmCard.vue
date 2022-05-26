<template>
    <n-card
        style="width: 800px"
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
            :row-props="rowProps"
        />

        <n-modal v-model:show="alarmItemVisiable">
            <n-card
                style="width: 300px"
                :title="formValue.alarmItem.name"
                :bordered="false"
                size="huge"
                role="dialog"
                aria-modal="true"
                footer-style="display:flex;justify-content:space-evenly;"
                closable
                @close="switchAlarmItemVisiable"
            >
                <n-form
                    ref="formRef"
                    inline
                    :label-width="80"
                    :model="formValue"
                    :rules="rules"
                    size="medium"
                >
                    <n-space vertical>
                        <n-form-item
                            label="警告阈值"
                            path="alarmItem.alarmValue"
                        >
                            <n-input-number
                                v-model:value="formValue.alarmItem.alarmValue"
                                :show-button="false"
                            />
                        </n-form-item>
                        <n-form-item
                            label="警告间隔"
                            path="alarmItem.intervalTime"
                        >
                            <n-input-number
                                v-model:value="formValue.alarmItem.intervalTime"
                                :show-button="false"
                            >
                                <template #suffix> 秒 </template>
                            </n-input-number>
                        </n-form-item>
                        <n-form-item
                            label="触发时长"
                            path="alarmItem.durationTime"
                        >
                            <n-input-number
                                v-model:value="formValue.alarmItem.durationTime"
                                :show-button="false"
                            >
                                <template #suffix> 秒 </template>
                            </n-input-number>
                        </n-form-item>
                        <n-form-item
                            label="是否启用"
                            path="alarmItem.activated"
                        >
                            <n-switch
                                v-model:value="formValue.alarmItem.activated"
                            />
                        </n-form-item>
                    </n-space>
                </n-form>

                <template #footer>
                    <n-button type="primary" @click="handleAlarmItemUpdate"
                        >更新</n-button
                    >
                    <n-button type="default" @click="switchAlarmItemVisiable"
                        >取消</n-button
                    >
                </template>
            </n-card>
        </n-modal>
    </n-card>
</template>

<script>
import { ref, h } from "vue";
import {
    NCard,
    NDataTable,
    NText,
    NTag,
    useMessage,
    NModal,
    NButton,
    NForm,
    NSpace,
    NFormItem,
    NSwitch,
    NInputNumber,
} from "naive-ui";

import { getAlarmFlag, updateAlarmFlag } from "../utils/request";

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
            title: "警告间隔",
            key: "interval_time",
        },
        {
            title: "触发时长",
            key: "duration_time",
        },
        {
            title: "状态",
            key: "flag",
            render(row) {
                return h(
                    NTag,
                    {
                        // ! 慎用三元运算符，但好像也只能这样
                        type: row.activated
                            ? row.flag
                                ? "error"
                                : "success"
                            : "default",
                    },
                    {
                        default: () =>
                            row.activated
                                ? row.flag
                                    ? "警报"
                                    : "正常"
                                : "停用",
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
        NModal,
        NButton,
        NForm,
        NSpace,
        NFormItem,
        NSwitch,
        NInputNumber,
    },
    setup() {
        const columns = createColumns();
        const data = ref([]);
        const loadingFlag = ref(true);

        const message = useMessage();
        const formValue = ref({
            alarmItem: {
                alarmValue: 0,
                intervalTime: 0,
                durationTime: 0,
                activated: true,
            },
        });
        const alarmItemVisiable = ref(false);
        const formRef = ref(null);
        const rules = {
            alarmItem: {
                alarmValue: {
                    type: "number",
                    required: true,
                    message: "请输入警告阈值",
                    trigger: ["input", "blur"],
                },
                intervalTime: {
                    type: "number",
                    required: true,
                    message: "请输入警告间隔",
                    trigger: ["input", "blur"],
                },
                durationTime: {
                    type: "number",
                    required: true,
                    message: "请输入触发时长",
                    trigger: ["input", "blur"],
                },
            },
        };

        // TODO 解决一下响应性问题
        const initData = function () {
            getAlarmFlag().then((response) => {
                data.value = response.data;
                loadingFlag.value = false;
            });
        };

        const rowKey = (rowData) => rowData.name;

        const rowProps = (row) => {
            return {
                style: "cursor: pointer;",
                onClick: () => {
                    formValue.value.alarmItem.name = row.name;
                    formValue.value.alarmItem.alarmValue = row.alarm_value;
                    formValue.value.alarmItem.activated = row.activated;
                    formValue.value.alarmItem.intervalTime = row.interval_time;
                    formValue.value.alarmItem.durationTime = row.duration_time;
                    alarmItemVisiable.value = true;
                },
            };
        };

        const switchAlarmItemVisiable = () => {
            alarmItemVisiable.value = !alarmItemVisiable.value;
        };

        const handleAlarmItemUpdate = (e) => {
            e.preventDefault();
            formRef.value?.validate((errors) => {
                if (!errors) {
                    updateAlarmFlag(formValue.value.alarmItem).then(
                        (response) => {
                            if (response.data.status === "success") {
                                initData();
                                switchAlarmItemVisiable();
                                message.success("更新成功");
                            } else {
                                message.error("更新失败");
                            }
                        }
                    );
                } else {
                    message.error("请检查参数填写");
                }
            });
        };

        initData();

        return {
            columns,
            data,
            loadingFlag,
            message,
            initData,
            rowKey,
            rowProps,
            alarmItemVisiable,
            formValue,
            formRef,
            rules,
            switchAlarmItemVisiable,
            handleAlarmItemUpdate,
        };
    },
    methods: {
        switchAlarm() {
            this.$emit("switchAlarm");
        },
    },
};
</script>
