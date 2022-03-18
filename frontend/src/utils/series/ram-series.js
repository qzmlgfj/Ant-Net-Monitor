import { ref } from "vue"

const available = {
    name: "available",
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
    available,
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
    data.forEach(item => {
        available.data.value.push([new Date(item.time_stamp), item.available])
        used.data.value.push([new Date(item.time_stamp), item.used])
        cached.data.value.push([new Date(item.time_stamp), item.cached])
        buffers.data.value.push([new Date(item.time_stamp), item.buffers])
    })
    return RAMSeries
}

const updateRAMSeries = (data) => {
    available.data.value.shift()
    available.data.value.push([new Date(data.time_stamp), data.available])

    used.data.value.shift()
    used.data.value.push([new Date(data.time_stamp), data.used])

    cached.data.value.shift()
    cached.data.value.push([new Date(data.time_stamp), data.cached])

    buffers.data.value.shift()
    buffers.data.value.push([new Date(data.time_stamp), data.buffers])
}

export { setRAMSeries, updateRAMSeries }
