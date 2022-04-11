import { ref } from 'vue'

const read = {
    name: 'read',
    type: 'line',
    smooth: false,
    symbol: 'none',
    areaStyle: {},
    data: ref([]),
}

const write = {
    name: 'write',
    type: 'line',
    smooth: false,
    symbol: 'none',
    areaStyle: {},
    data: ref([]),
}

const diskSeries = [
    read,
    write,
];

const clearDiskSeries = () => {
    diskSeries.forEach(item => {
        item.data.value = [];
    });
}

const setDiskSeries = (data) => {
    clearDiskSeries();
    data.forEach(item => {
        read.data.value.push([new Date((item.time_stamp)), item.read_speed]);
        write.data.value.push([new Date((item.time_stamp)), item.write_speed]);
    });
    return diskSeries;
}

const updateDiskSeries = (data) => {
    read.data.value.shift();
    read.data.value.push([new Date((data.time_stamp)), data.read_speed]);

    write.data.value.shift();
    write.data.value.push([new Date((data.time_stamp)), data.write_speed]);
}

export { setDiskSeries, updateDiskSeries };

