<template>
  <section class="article-view" v-if="article">
    <h1>{{ article.title }}</h1>
    <div class="markdown-body" v-html="markdownHtml"></div>
    <RouterLink class="ai-entry" to="/aichat">进入 AI Chat</RouterLink>
  </section>
  <section v-else class="empty-state">文章加载中或不存在</section>
</template>

<script setup>
import DOMPurify from "dompurify"
import { marked } from "marked"
import { computed, onMounted, ref } from "vue"
import { useRoute } from "vue-router"
import { getArticleApi } from "../api"

const route = useRoute()
const article = ref(null)

const markdownHtml = computed(() => {
  if (!article.value) {
    return ""
  }
  const raw = marked.parse(article.value.content || "")
  return DOMPurify.sanitize(raw)
})

onMounted(async () => {
  const id = route.params.id
  try {
    const { data } = await getArticleApi(id)
    article.value = data.data
  } catch {
    article.value = null
  }
})
</script>
