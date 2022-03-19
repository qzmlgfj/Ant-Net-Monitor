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
        ]
    },

]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export { routes };

export default router;