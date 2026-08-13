<template>
  <div class="project-card">
    <h2>{{ title }}</h2>
    <p class="subtitle">{{ subtitle }}</p>
    <p class="description">{{ description }}</p>
    
    <div class="tech-stack">
      <span v-for="tech in technologies" :key="tech" class="tech-badge">
        {{ tech }}
      </span>
    </div>

    <div class="card-actions">
      <button @click="isExpanded = !isExpanded" class="toggle-btn">
        {{ isExpanded ? 'Hide Quick Preview' : 'Preview Recent Posts' }}
      </button>

      <router-link :to="`/project/${slug}`" class="full-page-link">
        Full Page Feed & History &rarr;
      </router-link>
    </div>

    <!-- Inline Drawer -->
    <div v-if="isExpanded" class="posts-drawer">
      <h3>Recent Bot Outputs (Preview)</h3>
      <div v-if="posts && posts.length" class="posts-list">
        <div v-for="post in posts.slice(0, 3)" :key="post.id" class="post-item">
          <p class="post-date">{{ post.date }}</p>
          <p class="post-text">{{ post.content }}</p>

          <!-- Render Bot Image if Available -->
          <div v-if="post.image" class="post-image-container">
            <img :src="post.image" alt="Bot Output Image" class="post-image" />
          </div>
        </div>
      </div>
      <p v-else class="no-posts">No recent posts loaded.</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  slug: String,
  title: String,
  subtitle: String,
  description: String,
  technologies: Array,
  posts: Array
})

const isExpanded = ref(false)
</script>

<style scoped>
.project-card {
  border: 1px solid #333;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  background-color: #1a1a1a;
  color: #ffffff;
  text-align: left;
}

.subtitle {
  font-style: italic;
  color: #a8a8a8;
  margin-top: -0.5rem;
  margin-bottom: 1rem;
}

.description {
  line-height: 1.5;
  color: #d1d5db;
}

.tech-stack {
  display: flex;
  gap: 0.5rem;
  margin-top: 1rem;
  margin-bottom: 1.25rem;
  flex-wrap: wrap;
}

.tech-badge {
  background-color: #2563eb;
  color: #ffffff;
  padding: 0.25rem 0.6rem;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.02em;
}

.card-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
  margin-top: 1rem;
}

.toggle-btn {
  background-color: transparent;
  border: 1px solid #3b82f6;
  color: #3b82f6;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s ease-in-out;
}

.toggle-btn:hover {
  background-color: #3b82f6;
  color: #ffffff;
}

.full-page-link {
  color: #3b82f6;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 600;
}

.full-page-link:hover {
  text-decoration: underline;
}

.posts-drawer {
  margin-top: 1.5rem;
  padding-top: 1rem;
  border-top: 1px solid #333;
}

.posts-drawer h3 {
  font-size: 1rem;
  margin-bottom: 0.75rem;
  color: #9ca3af;
}

.posts-list {
  display: grid;
  /* Automatically creates columns that fit at least 240px width */
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
}

.post-item {
  background-color: #262626;
  padding: 1rem;
  border-radius: 6px;
  border: 1px solid #333;
  display: flex;
  flex-direction: column;
  justify-content: space-between; /* Pushes images neatly to the bottom */
}

.post-content-wrapper {
  margin-bottom: 0.75rem;
}

.post-date {
  font-size: 0.75rem;
  color: #9ca3af;
  margin: 0 0 0.5rem 0;
}

.post-text {
  margin: 0;
  font-size: 0.85rem;
  color: #e5e7eb;
  line-height: 1.4;
  white-space: pre-wrap;
}

.post-image-container {
  margin-top: auto; /* Keeps image aligned at bottom across different card heights */
}

.post-image {
  width: 100%;
  height: 380px; /* Uniform height for grid cards */
  object-fit: cover; /* Ensures images crop neatly without stretching */
  border-radius: 4px;
  border: 1px solid #444;
  display: block;
}

.no-posts {
  color: #6b7280;
  font-style: italic;
  font-size: 0.9rem;
}
</style>