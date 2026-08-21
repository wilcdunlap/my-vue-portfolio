<template>
  <div class="home-view">
    <header class="hero-section">
      <h1>William Dunlap</h1>
      <p>Software Engineer | AI & Automation</p>
    </header>

    <!-- Backend Connection Indicator -->
    <section class="api-status-banner">
      <h3>Backend Connection Status</h3>
      <div v-if="projectStatus.length > 0" class="status-online">
        <p v-for="item in projectStatus" :key="item.id">
          🟢 Connected to .NET API — <strong>{{ item.title }}</strong>: {{ item.status }} (Health: {{ item.systemHealth }})
        </p>
      </div>
      <p v-else class="status-offline">🔴 Waiting for .NET Backend...</p>
    </section>

    <section class="projects-section">
      <h2>Featured AI Projects</h2>
      
      <!-- Waifu Bot Card -->
      <ProjectCard 
        slug="waifu"
        title="This Waifu Does Not Exist"
        subtitle="Multi-Stage AI Content Generator"
        description="A fully autonomous content-production system. It utilizes a more simplified architecture to generate the synopsis of an anime with a charming protagonist, then reviews said anime."
        :technologies="['Python', 'Multi-Stage LLM Pipelines', 'SD.Next', 'Facebook Graph API']"
        :posts="botPosts['waifu'] || []"
      >
        <template #details>
          <h3>Waifu Bot: For Myself</h3>
          <p>
            This was the first bot I created, shortly after college. It was inspired by https://www.thiswaifudoesnotexist.net/ and originally just scraped and manipulated content from that site. This was long before LLMs and current generation generative AI was available.
            <br><br>
            When I revamped my bots, I decided to modify this one to generate content from a local LLM instance and generate the images locally as well.
            <br>
            I wanted to create a more autonomous system that could generate its own content, and I wanted to see how far I could push the capabilities of LLMs and image generation models.
            <br><br>
            The text is processed through an Ollama instance running llama3.2:3b, and the images are generated through a local instance of Stable Diffusion, SD.Next. I use a few Lora including heavy weighting for a possummachine anime Lora and a very slight weight of a disgaea Lora. 
            <br><br>
            I tried to strike a balance between creating images that were aesthetically pleasing, while also maintaining the odd, sometimes uncanny qualities of the images that originally featured on the website that inspired the bot. I think I did a pretty good job!
          </p>
        </template>
      </ProjectCard>

      <!-- Cat Bot Card -->
      <ProjectCard 
        slug="cat"
        title="This Cat Does Not Exist"
        subtitle="Multi-Stage AI Content Generator"
        description="A fully autonomous content-production system. It utilizes multiple LLM calls to generate details about a fictional cat, such as name, likes/dislikes, and a sound it makes. Then it combines these details into a short adoption-style description."
        :technologies="['Python', 'Multi-Stage LLM Pipelines', 'SD.Next', 'Facebook Graph API']"
        :posts="botPosts['cat'] || []"
      >
        <template #details>
          <h3>Cat Bot: For My Friends</h3>
          <p>
            This was among the first bots I created, shortly after college. It was inspired by https://thesecatsdonotexist.com/ 
          </p>
        </template>
      </ProjectCard>

      <!-- Alien Romance Bot Card -->
      <ProjectCard 
        slug="alien-romance"
        title="This Alien Romance Does Not Exist"
        subtitle="Multi-Stage AI Content Generator"
        description="A fully autonomous content-production system using micro-prompt decoding for deterministic field extraction."
        :technologies="['Python', 'Multi-Stage LLM Pipelines', 'SD.Next', 'Facebook Graph API']"
        :posts="botPosts['alien-romance'] || []"
      >
        <template #details>
          <h3>Alien Romance Bot: For My Wife</h3>
          <p>
            I designed this bot at the request of my wife, who is a fan of alien romance stories.
            Specifically, she mentioned how disappointing it was to see alien romance stories with love interests that were barely different from regular humans.
            I wanted to create unique, very otherworldly qualities to give to the love interest, and I knew it would lead to interesting image generation as well.
            <br><br>
            This is what inspired my "Alien Romance Book Number" or "ARBN" system. Inspired by the ISBN system, the first step is generating all the details for the story, encoded in the ARBN code. Several details can (theoretically) be gleaned or verified comparing the ARBN code to the synopsis, though the LLMs rarely stick to it perfectly. 
            <br><br>
            First, we generate the ARBN with letters or numbers. Then, several lightweight LLM calls "decode" the ARBN letters in certain index positions into concrete info to build out the synopsis. An image is generated with the character details for the alien love interest, and then a more heavyweight LLM call puts it all together in a synopsis.
          </p>
        </template>
      </ProjectCard>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ProjectCard from '../components/ProjectCard.vue'

const botPosts = ref({})
const projectStatus = ref([])

// ... existing imports and refs ...

onMounted(async () => {
  // 1. Fetch Bot Posts from the PostgreSQL Database via .NET!
  try {
    const postsResponse = await fetch('http://localhost:5151/api/projects/posts')
    if (postsResponse.ok) {
      botPosts.value = await postsResponse.json()
    }
  } catch (error) {
    console.error('Could not load dynamic posts:', error)
  }

  // 2. Fetch .NET API Health Status
  try {
    const apiResponse = await fetch('http://localhost:5151/api/projects')
    if (apiResponse.ok) {
      projectStatus.value = await apiResponse.json()
    }
  } catch (err) {
    console.error('Error connecting to .NET API:', err)
  }
})
</script>

<style scoped>
.hero-section {
  text-align: center;
  margin-bottom: 2.5rem;
  border-bottom: 1px solid #333;
  padding-bottom: 1.5rem;
}

.hero-section h1 {
  margin: 0;
  font-size: 2.2rem;
  color: #3b82f6;
}

.api-status-banner {
  background-color: #1a1a1a;
  border: 1px solid #333;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 2rem;
}

.status-online { color: #4ade80; }
.status-offline { color: #f87171; }

.projects-section h2 {
  margin-bottom: 1.5rem;
}
</style>