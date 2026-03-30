<template>
  <section class="chat-wrap">
    <h2 class="page-title">AI Chat</h2>
    <div class="chat-box">
      <div v-for="(item, index) in messages" :key="index" :class="item.role">
        {{ item.content }}
      </div>
    </div>
    <form class="chat-input" @submit.prevent="sendMessage">
      <input v-model="prompt" placeholder="输入你的问题..." />
      <button type="submit">发送</button>
    </form>
  </section>
</template>

<script setup>
import { ref } from "vue"
import { chatApi } from "../api"

const prompt = ref("")
const messages = ref([])

const sendMessage = async () => {
  if (!prompt.value.trim()) {
    return
  }
  messages.value.push({ role: "user", content: prompt.value })
  const currentPrompt = prompt.value
  prompt.value = ""
  try {
    const { data } = await chatApi({ prompt: currentPrompt })
    messages.value.push({ role: "assistant", content: data.data.answer })
  } catch {
    messages.value.push({ role: "assistant", content: "服务暂不可用，请稍后再试" })
  }
}
</script>
