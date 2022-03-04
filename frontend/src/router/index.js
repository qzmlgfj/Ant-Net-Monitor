import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: "/A",
        name: "Test-A",
        meta: {
            title: "Test-A"
        },
        component: () => import("../components/TestA.vue")
    },
    {
        path: "/B",
        name: "Test-B",
        meta: {
            title: "Test-B"
        },
        component: () => import("../components/TestB.vue")
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;