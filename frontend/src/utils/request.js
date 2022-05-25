import { service } from "./service";

function getVersion() {
    return service({
        method: "get",
        url: "/api/version",
    })
}

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

function getSystemInfo() {
    return service({
        method: "get",
        url: "/api/status/system_info"
    })
}

function getAlarmFlag() {
    return service({
        method: "get",
        url: "/api/alarm/alarm_item",
    })
}

function updateAlarmFlag(data) {
    return service({
        method: "post",
        url: "/api/alarm/alarm_item",
        data: data
    })
}

function getAlarmLog() {
    return service({
        method: "get",
        url: "/api/alarm/alarm_log"
    })
}

export { getVersion, getBasicStatus, initLineChart, updateLineChart, getHistoryLineChart, getAlarmFlag, updateAlarmFlag, getAlarmLog, getSystemInfo };
