import axios from "axios";

axios.defaults.retry = 4;

const service = axios.create({
    baseURL: 'http://localhost:5000/',
    timeout: 3000,
});

export default service;
