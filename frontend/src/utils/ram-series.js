import { ref } from "vue"

const free = {
    name: "user",
    type: "line",
    smooth: true,
    symbol: "none",
    areaStyle: {},
    data: ref([]),
}

const used = {
    name: "used",
    type: "line",
    smooth: true,
    symbol: "none",
    areaStyle: {},
    data: ref([]),
}

const cached = {
    name: "cached",
    type: "line",
    smooth: true,
    symbol: "none",
    areaStyle: {},
    data: ref([]),
}

const buffers = {
    name: "buffers",
    type: "line",
    smooth: true,
    symbol: "none",
    areaStyle: {},
    data: ref([]),
}

const RAMSeries = [
    free,
    used,
    cached,
    buffers,
]

const clearRAMSeries = () => {
    RAMSeries.forEach(series => {
        series.data.value = [];
    })
}

const setRAMSeries = (data) => {
    clearRAMSeries()
    data.reverse().forEach(item => {
        free.data.value.push([new Date(item.time_stamp), item.free])
        used.data.value.push([new Date(item.time_stamp), item.used])
        cached.data.value.push([new Date(item.time_stamp), item.cached])
        buffers.data.value.push([new Date(item.time_stamp), item.buffers])
    })
    return RAMSeries
}

const updateRAMSeries = (data) => {
    free.data.value.shift()
    free.data.value.push([new Date(data.time_stamp), data.free])

    used.data.value.shift()
    used.data.value.push([new Date(data.time_stamp), data.used])

    cached.data.value.shift()
    cached.data.value.push([new Date(data.time_stamp), data.cached])

    buffers.data.value.shift()
    buffers.data.value.push([new Date(data.time_stamp), data.buffers])
}

export { setRAMSeries, updateRAMSeries }
