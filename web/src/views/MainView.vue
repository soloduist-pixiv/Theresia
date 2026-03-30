<template>
  <section>
    <div class="main-hero">
      <h2 class="page-title">推荐文章</h2>
      <p>精选技术内容，帮助你快速进入开发状态</p>
    </div>
    <div class="article-grid">
      <article v-for="item in articles" :key="item.id" class="article-card">
        <h3>{{ item.title }}</h3>
        <p>{{ item.content.slice(0, 120) }}...</p>
        <RouterLink class="article-link" :to="`/article/${item.id}`">阅读全文</RouterLink>
      </article>
    </div>
  </section>
</template>

<script setup>
import { onMounted, ref } from "vue"
import { listArticlesApi } from "../api"

const articles = ref([])

onMounted(async () => {
  try {
    const { data } = await listArticlesApi()
    articles.value = data.data || []
  } catch {
    articles.value = []
  }
})
</script>
