<template>
  <v-card class="pa-6" elevation="2">
    <v-card-title class="text-h6 text-center pb-2">Chat Quality Agent</v-card-title>
    <p class="text-body-2 text-center text-grey mb-4">Tạo tài khoản quản trị viên đầu tiên</p>
    <v-form @submit.prevent="handleSetup">
      <v-text-field
        v-model="email"
        label="Email"
        type="email"
        prepend-inner-icon="mdi-email"
        :error-messages="errorMsg"
        required
        class="mb-2"
      />
      <v-text-field
        v-model="name"
        label="Tên hiển thị"
        prepend-inner-icon="mdi-account"
        class="mb-2"
      />
      <v-text-field
        v-model="password"
        label="Mật khẩu"
        :type="showPass ? 'text' : 'password'"
        prepend-inner-icon="mdi-lock"
        :append-inner-icon="showPass ? 'mdi-eye-off' : 'mdi-eye'"
        @click:append-inner="showPass = !showPass"
        required
        class="mb-2"
        hint="Tối thiểu 8 ký tự, có chữ hoa và số"
      />
      <v-text-field
        v-model="confirmPassword"
        label="Nhập lại mật khẩu"
        :type="showPass ? 'text' : 'password'"
        prepend-inner-icon="mdi-lock-check"
        :error-messages="confirmError"
        required
        class="mb-4"
      />
      <v-btn type="submit" color="primary" block size="large" :loading="loading">
        Tạo tài khoản
      </v-btn>
    </v-form>
  </v-card>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api'
import { markSetupComplete } from '../router'

const router = useRouter()

const email = ref('')
const name = ref('')
const password = ref('')
const confirmPassword = ref('')
const showPass = ref(false)
const loading = ref(false)
const errorMsg = ref('')
const confirmError = ref('')

async function handleSetup() {
  confirmError.value = ''
  errorMsg.value = ''

  if (password.value !== confirmPassword.value) {
    confirmError.value = 'Mật khẩu không khớp'
    return
  }

  loading.value = true
  try {
    const { data } = await api.post('/setup', {
      email: email.value,
      password: password.value,
      name: name.value || undefined,
    })
    localStorage.setItem('cqa_access_token', data.access_token)
    markSetupComplete()
    router.push('/')
  } catch (err: any) {
    const msg = err.response?.data?.message || err.response?.data?.error || 'Có lỗi xảy ra'
    errorMsg.value = msg
  } finally {
    loading.value = false
  }
}
</script>
