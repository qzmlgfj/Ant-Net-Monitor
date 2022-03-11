import service from "./service";

function getBasicStatus() {
    return service({
        method: "get",
        url: "/status/basic_status",
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

export { getBasicStatus, initLineChart };
