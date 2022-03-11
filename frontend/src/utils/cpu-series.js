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

const setCPUSeries = (data) => {
    data.forEach(item => {
        user.data.value.push([Date.parse(item.time_stamp), item.user_percent]);
        nice.data.value.push([Date.parse(item.time_stamp), item.nice_percent]);
        system.data.value.push([Date.parse(item.time_stamp), item.system_percent]);
        idle.data.value.push([Date.parse(item.time_stamp), item.idle_percent]);
        iowait.data.value.push([Date.parse(item.time_stamp), item.iowait_percent]);
        steal.data.value.push([Date.parse(item.time_stamp), item.steal_percent]);
    });
    return CPUSeries;
}

export {setCPUSeries};
