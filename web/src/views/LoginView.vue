<template>
  <section class="auth-wrap auth-wrap-login">
    <form class="auth-card" @submit.prevent="submitLogin">
      <div class="auth-head">
        <h2>欢迎回来</h2>
        <p>登录后查看文章与 AI 助手</p>
      </div>
      <input v-model="form.username" placeholder="用户名" />
      <input v-model="form.password" type="password" placeholder="密码" />
      <button type="submit">登录</button>
      <p class="hint">{{ message }}</p>
      <RouterLink class="auth-link" to="/register">没有账号？去注册</RouterLink>
    </form>
  </section>
</template>

<script setup>
import { reactive, ref } from "vue"
import { useRouter } from "vue-router"
import { loginApi } from "../api"

const router = useRouter()
const message = ref("")
const form = reactive({
  username: "",
  password: ""
})

const submitLogin = async () => {
  try {
    const { data } = await loginApi(form)
    message.value = data.message
    if (data.status_code === 200) {
      localStorage.setItem("current_user", JSON.stringify(data.data))
      router.push("/main")
    }
  } catch {
    message.value = "登录失败，请检查网络或服务状态"
  }
}
</script>
