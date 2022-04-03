import { ref } from "vue";

const send = {
    name: 'send',
    type: 'line',
    smooth: false,
    symbol: 'none',
    areaStyle: {},
    data: ref([]),
}

const receive = {
    name: 'receive',
    type: 'line',
    smooth: false,
    symbol: 'none',
    areaStyle: {},
    data: ref([]),
}

const networkSeries = [
    send,
    receive,
];

const clearNetnetworkSeries = () => {
    networkSeries.forEach(item => {
        item.data.value = [];
    });
}

const setNetworkSeries = (data) => {
    clearNetnetworkSeries();
    data.forEach(item => {
        send.data.value.push([new Date((item.time_stamp)), item.send_speed]);
        receive.data.value.push([new Date((item.time_stamp)), item.recv_speed]);
    });
    return networkSeries;
}

const updateNetworkSeries = (data) => {
    send.data.value.shift();
    send.data.value.push([new Date((data.time_stamp)), data.send_speed]);

    receive.data.value.shift();
    receive.data.value.push([new Date((data.time_stamp)), data.recv_speed]);
}

export { setNetworkSeries, updateNetworkSeries };
