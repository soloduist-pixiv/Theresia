import axios from "axios"

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000"

const client = axios.create({
  baseURL: apiBaseUrl,
  timeout: 15000
})

export const registerApi = (payload) => client.post("/register", payload)
export const loginApi = (payload) => client.post("/login", payload)
export const listArticlesApi = () => client.get("/article")
export const getArticleApi = (id) => client.get(`/article/${id}`)
export const chatApi = (payload) => client.post("/chat", payload)
