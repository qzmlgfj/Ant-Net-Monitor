import { service } from "./service";

function getBasicStatus() {
    return service({
        method: "get",
        url: "/api/status/basic_status",
    })
}

function initLineChart(url) {
    return service({
        method: "get",
        url: url,
        params: {
            type: "init"
        }
    })
}

function updateLineChart(url) {
    return service({
        method: "get",
        url: url,
        params: {
            type: "update"
        }
    })
}

function getHistoryLineChart(url) {
    return service({
        method: "get",
        url: url,
        params: {
            type: "day"
        }
    })
}

export { getBasicStatus, initLineChart, updateLineChart, getHistoryLineChart };
