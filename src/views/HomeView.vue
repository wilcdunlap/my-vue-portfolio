<template>
  <div class="home-view">
    <header>
      <h1>William Dunlap</h1>
      <p>Software Engineer | AI & Automation</p>
    </header>

      <section class="projects-section">
        <h2>Featured AI Projects</h2>
        
        <!-- We use the component here and pass the data into the props we defined -->
        <ProjectCard 
            slug="alien-romance"
            title="This Alien Romance Does Not Exist"
            subtitle="Multi-Stage AI Content Generator"
            description="A fully autonomous content-production system using micro-prompt decoding for deterministic field extraction."
            :technologies="['Python', 'Multi-Stage LLM Pipelines', 'SD.Next', 'Facebook Graph API']"
            :posts="botPosts['alien-romance'] || []"
            />
        <ProjectCard 
        slug="waifu"
          title="This Waifu Does Not Exist"
          subtitle="Multi-Stage AI Content Generator"
          description="A fully autonomous content-production system. It utilizes a more simplified architecture to generate the synopsis of an anime with a charming protagonist, then reviews said anime."
          :technologies="['Python', 'Multi-Stage LLM Pipelines', 'SD.Next', 'Facebook Graph API']"
          :posts="botPosts['waifu'] || []"
        />
        <ProjectCard 
        slug="cat"
          title="This Cat Does Not Exist"
          subtitle="Multi-Stage AI Content Generator"
          description="A fully autonomous content-production system. It utilizes multiple LLM calls to generate details about a fictional cat, such as name, likes/dislikes, and a sound it makes. Then it combines these details into a short adoption-style description."
          :technologies="['Python', 'Multi-Stage LLM Pipelines', 'SD.Next', 'Facebook Graph API']"
          :posts="botPosts['cat'] || []"
        />
      </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ProjectCard from '../components/ProjectCard.vue'

// Reactive state to hold post data fetched from JSON
const botPosts = ref({})

// Fetch the posts dynamically when the view mounts
onMounted(async () => {
  try {
    const response = await fetch('/posts.json')
    if (response.ok) {
      botPosts.value = await response.json()
    }
  } catch (error) {
    console.error('Could not load dynamic posts:', error)
  }
})
</script>

<style scoped>
.hero-section {
  text-align: center;
  margin-bottom: 2.5rem;
  border-bottom: 1px solid #333;
  padding-bottom: 1.5rem;
  white-space: pre-wrap;
}

.hero-section h1 {
  margin: 0;
  font-size: 2.2rem;
  color: #3b82f6;
  white-space: pre-wrap;
}

.projects-section h2 {
  margin-bottom: 1.5rem;
  white-space: pre-wrap;
}
</style>