import axios from "axios";

axios.defaults.retry = 4;

const serviceProd = axios.create({
    timeout: 3000,
});

const serviceDev = axios.create({
    baseURL: "http://localhost:5000/",
    timeout: 3000,
});

export {serviceProd, serviceDev};
