import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import(/* webpackChunkName: "home" */ "../views/Home.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import(/* webpackChunkName: "login" */ "../views/Login.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import(/* webpackChunkName: "register" */ "../views/Register.vue"),
  },
  {
    path: "/empleados",
    name: "empleados",
    props: true,
    component: () => import(/* webpackChunkName: "empleados" */ "../views/Empleados.vue"),
  },

  {
    path: "/tareas",
    name: "tareas",
    component: () => import(/* webpackChunkName: "tareas" */ "../views/Tareas.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
