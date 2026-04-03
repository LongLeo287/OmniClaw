<template>
  <v-app>
    <AuthLayout v-if="route.meta.layout === 'auth'">
      <router-view />
    </AuthLayout>
    <DefaultLayout v-else>
      <router-view :key="(route.params.tenantId as string) || 'home'" />
    </DefaultLayout>
  </v-app>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'
import DefaultLayout from './layouts/DefaultLayout.vue'
import AuthLayout from './layouts/AuthLayout.vue'
import { useAuthStore } from './stores/auth'

const route = useRoute()
const authStore = useAuthStore()

onMounted(async () => {
  if (authStore.accessToken && !authStore.user) {
    try {
      await authStore.fetchProfile()
    } catch {
      // Token expired — will redirect via router guard
    }
  }
})
</script>
