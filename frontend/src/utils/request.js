import { serviceDev, serviceProd } from "./service";

function getBasicStatus(env) {
    if (env === "development") {
        return serviceDev({
            method: "get",
            url: "/status/basic_status",
        })
    }
    else {
        return serviceProd({
            method: "get",
            url: "/status/basic_status",
        })
    }
}

function initLineChart(env, url) {
    if (env === "development") {
        return serviceDev({
            method: "get",
            url: url,
            params: {
                type: "init"
            }
        })
    }
    else {
        return serviceProd({
            method: "get",
            url: url,
            params: {
                type: "init"
            }
        })
    }
}

function updateLineChart(env, url) {
    if (env === "development") {
        return serviceDev({
            method: "get",
            url: url,
            params: {
                type: "update"
            }
        })
    }
    else {
        return serviceProd({
            method: "get",
            url: url,
            params: {
                type: "update"
            }
        })
    }
}

export { getBasicStatus, initLineChart, updateLineChart };
