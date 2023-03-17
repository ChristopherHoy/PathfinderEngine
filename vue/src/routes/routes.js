import Base from "../pages/Base.vue";
import Login from "../pages/Login.vue";
import Logout from "../pages/Logout.vue";
import Home from "../pages/Home.vue";
import NotFound from "../pages/NotFound.vue";
import SelectClass from "../components/CharacterCreation/SelectClass.vue"
import CreateCharacter from "../pages/CreateCharacter.vue"


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
            },{
                path: 'create-character',
                component: CreateCharacter,
                redirect: "/create-character/select-class",
                name: "create-character",
                children: [
                    {
                        path: "select-class",
                        component: SelectClass,
                        name: "select-class"
                    }
                ]
            }
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