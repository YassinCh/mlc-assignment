import { createRouter, createWebHistory } from "vue-router";
import Datasets from "@/views/Datasets.vue";
import Details from "@/views/Details.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'datasets',
            component: Datasets,
        },
        {
            path: '/details/:datasetId',
            name: 'details',
            component: Details,
        },
    ]
})

export default router;