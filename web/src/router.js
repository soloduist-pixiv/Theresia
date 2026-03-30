import { createRouter, createWebHistory } from "vue-router"
import LoginView from "./views/LoginView.vue"
import RegisterView from "./views/RegisterView.vue"
import MainView from "./views/MainView.vue"
import ArticleView from "./views/ArticleView.vue"
import AiChatView from "./views/AiChatView.vue"

const routes = [
  { path: "/", redirect: "/login" },
  { path: "/login", component: LoginView },
  { path: "/register", component: RegisterView },
  { path: "/main", component: MainView, meta: { requiresAuth: true } },
  { path: "/article/:id", component: ArticleView, props: true, meta: { requiresAuth: true } },
  { path: "/aichat", component: AiChatView, meta: { requiresAuth: true } }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to) => {
  const currentUser = localStorage.getItem("current_user")
  const isAuthed = Boolean(currentUser)
  if (to.meta.requiresAuth && !isAuthed) {
    return "/login"
  }
  if ((to.path === "/login" || to.path === "/register") && isAuthed) {
    return "/main"
  }
  return true
})

export default router
