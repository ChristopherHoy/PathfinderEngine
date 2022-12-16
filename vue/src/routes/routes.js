import Base from "../pages/Base.vue";
import Login from "../pages/Login.vue";
import Logout from "../pages/Logout.vue";
import Home from "../pages/Home.vue";
import NotFound from "../pages/NotFound.vue";


export default [
    {
        path: '/',
        name: 'Base',
        component: Base,
        redirect: "/home",
        children: [
            {
                path: 'home',
                component: Home,
            },
        ]
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    {
        path: '/logout',
        name: 'Logout',
        component: Logout,
    },
    {
        path: "/:pathMatch(.*)*",
        name: "NotFound",
        component: NotFound,
    }
]