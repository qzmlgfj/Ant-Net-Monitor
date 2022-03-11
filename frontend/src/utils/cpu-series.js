import { ref } from "vue";

const user = {
    name: "user",
    type: "line",
    smooth: true,
    symbol: "none",
    areaStyle: {},
    data: ref([]),
}

const nice = {
    name: "nice",
    type: "line",
    smooth: true,
    symbol: "none",
    areaStyle: {},
    data: ref([]),
}

const system = {
    name: "system",
    type: "line",
    smooth: true,
    symbol: "none",
    areaStyle: {},
    data: ref([]),
}

const idle = {
    name: "idle",
    type: "line",
    smooth: true,
    symbol: "none",
    areaStyle: {},
    data: ref([]),
}

const iowait = {
    name: "iowait",
    type: "line",
    smooth: true,
    symbol: "none",
    areaStyle: {},
    data: ref([]),
}

const steal = {
    name: "steal",
    type: "line",
    smooth: true,
    symbol: "none",
    areaStyle: {},
    data: ref([]),
}

const CPUSeries = [
    user,
    nice,
    system,
    idle,
    iowait,
    steal,
];

const clearCPUSeries = () => {
    CPUSeries.forEach(item => {
        item.data.value = [];
    });
}

const setCPUSeries = (data) => {
    clearCPUSeries();
    data.reverse().forEach(item => {
        user.data.value.push([new Date((item.time_stamp)), item.user_percent]);
        nice.data.value.push([new Date(item.time_stamp), item.nice_percent]);
        system.data.value.push([new Date(item.time_stamp), item.system_percent]);
        idle.data.value.push([new Date(item.time_stamp), item.idle_percent]);
        iowait.data.value.push([new Date(item.time_stamp), item.iowait_percent]);
        steal.data.value.push([new Date(item.time_stamp), item.steal_percent]);
    });
    return CPUSeries;
}

const updateCPUSeries = (data) => {
    user.data.value.shift();
    user.data.value.push([new Date((data.time_stamp)), data.user_percent]);

    nice.data.value.shift();
    nice.data.value.push([new Date(data.time_stamp), data.nice_percent]);

    system.data.value.shift();
    system.data.value.push([new Date(data.time_stamp), data.system_percent]);

    idle.data.value.shift();
    idle.data.value.push([new Date(data.time_stamp), data.idle_percent]);

    iowait.data.value.shift();
    iowait.data.value.push([new Date(data.time_stamp), data.iowait_percent]);

    steal.data.value.shift();
    steal.data.value.push([new Date(data.time_stamp), data.steal_percent]);
}

export { setCPUSeries, updateCPUSeries };
