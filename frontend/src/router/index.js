import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: "/status",
        name: "status",
        component: () => import("@/components/Info.vue"),
        children: [
            {
                path: "CPU",
                name: "CPU-Info",
                meta: {
                    title: "CPU-Info"
                },
                component: () => import("@/components/info/CPU.vue")
            },
            {
                path: "RAM",
                name: "RAM-Info",
                meta: {
                    title: "RAM-Info"
                },
                component: () => import("@/components/info/RAM.vue")
            },
        ]
    },

]

const router = createRouter({
    history: createWebHistory(),
    routes
});

//* 用于测试的导出路由表
export { routes };

export default router;