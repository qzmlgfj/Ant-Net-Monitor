import service from "./service";

function getStatus() {
    service({
        method: "get",
        url: "status",
    }).then(response => {
        console.log(response.data);
        return response.data;
    })
}

export {getStatus};
