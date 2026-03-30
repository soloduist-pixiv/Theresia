<template>
  <div class="app-shell">
    <header class="top-bar">
      <div>
        <div class="top-title">个人技术博客</div>
        <div class="top-subtitle">FastAPI + Vue3 全栈实战</div>
      </div>
      <nav class="top-nav">
        <template v-if="isAuthed">
          <RouterLink to="/main">首页</RouterLink>
          <RouterLink to="/aichat">AI Chat</RouterLink>
          <button type="button" class="top-action" @click="logout">退出</button>
        </template>
        <template v-else>
          <RouterLink to="/login">登录</RouterLink>
          <RouterLink to="/register">注册</RouterLink>
        </template>
      </nav>
    </header>
    <main class="page-content">
      <RouterView />
    </main>
    <footer class="bottom-bar">备案号：ICP备XXXXXXXX号 · 版权所有 © 2026</footer>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from "vue"
import { useRoute, useRouter } from "vue-router"

const route = useRoute()
const router = useRouter()
const isAuthed = ref(false)

const syncAuth = () => {
  isAuthed.value = Boolean(localStorage.getItem("current_user"))
}

const logout = () => {
  localStorage.removeItem("current_user")
  syncAuth()
  router.push("/login")
}

watch(() => route.fullPath, syncAuth)
onMounted(syncAuth)
</script>
