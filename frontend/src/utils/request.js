import service from "./service";

function getStatus() {
    return service({
        method: "get",
        url: "status",
    })
}

export { getStatus };
