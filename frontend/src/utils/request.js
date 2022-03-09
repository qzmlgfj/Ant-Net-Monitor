import service from "./service";

function getStatus() {
    return service({
        method: "get",
        url: "/status/basic_status",
    })
}

export { getStatus };
