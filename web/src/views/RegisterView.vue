<template>
  <section class="auth-wrap">
    <form class="auth-card" @submit.prevent="submitRegister">
      <div class="auth-head">
        <h2>创建账号</h2>
        <p>注册后即可登录并体验完整功能</p>
      </div>
      <input v-model="form.username" placeholder="用户名" />
      <input v-model="form.password" type="password" placeholder="密码" />
      <input v-model="form.confirmPassword" type="password" placeholder="验证密码" />
      <button type="submit">注册</button>
      <p class="hint">{{ message }}</p>
      <RouterLink class="auth-link" to="/login">已有账号？去登录</RouterLink>
    </form>
  </section>
</template>

<script setup>
import { reactive, ref } from "vue"
import { registerApi } from "../api"

const message = ref("")
const form = reactive({
  username: "",
  password: "",
  confirmPassword: ""
})

const submitRegister = async () => {
  if (form.password !== form.confirmPassword) {
    message.value = "两次密码输入不一致"
    return
  }
  try {
    const { data } = await registerApi({
      username: form.username,
      password: form.password
    })
    message.value = data.message
  } catch {
    message.value = "注册失败，请检查网络或服务状态"
  }
}
</script>
