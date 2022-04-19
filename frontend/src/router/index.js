import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: "/status",
        name: "status",
        component: () => import("@/components/Info.vue"),
        children: [
            {
                path: "cpu_status",
                name: "CPU-Info",
                meta: {
                    title: "CPU-Info",
                    apiUrl: "/api/status/cpu_status"
                },
                component: () => import("@/components/info/CPU.vue"),
            },
            {
                path: "ram_status",
                name: "RAM-Info",
                meta: {
                    title: "RAM-Info",
                    apiUrl: "/api/status/ram_status"
                },
                component: () => import("@/components/info/RAM.vue"),
            },
            {
                path: "disk_status",
                name: "Disk-Info",
                meta: {
                    title: "Disk-Info",
                    apiUrl: "/api/status/disk_status"
                },
                component: () => import("@/components/info/Disk.vue"),
            },
            {
                path: "network_status",
                name: "Network-Info",
                meta: {
                    title: "Network-Info",
                    apiUrl: "/api/status/network_status"
                },
                component: () => import("@/components/info/Network.vue"),
            },
            {
                path: "load_status",
                name: "Load-Info",
                meta: {
                    title: "Load-Info",
                    apiUrl: "/api/status/load_status"
                },
                component: () => import("@/components/info/Load.vue"),
            },
            {
                path: "swap_status",
                name: "Swap-Info",
                meta: {
                    title: "Swap-Info",
                    apiUrl: "/api/status/swap_status"
                },
                component: () => import("@/components/info/Swap.vue"),
            },
        ]
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export { routes };

export default router;