<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const isLoading = ref(false)

const handleSubmit = async () => {
  if (password.value !== confirmPassword.value) {
    alert("Passwords don't match!")
    return
  }

  isLoading.value = true

  try {
    await authStore.signup(email.value, password.value)
    console.log('Signup successful')
    router.push('/login')
    // router.push('/dashboard')
  } catch (error: any) {
    console.error('Signup failed:', error)
    alert(error.response?.data?.detail?.[0] || 'Signup failed. Please try again.')
  } finally {
    isLoading.value = false
  }
};
</script>
<template>
    <div class="container mt-5">
      <b-row class="justify-content-center">
        <b-col cols="auto">
        <h2 class="head">Register</h2>
          <b-card>
            <b-form @submit.prevent="handleSubmit">
              <b-form-group
                id="email-group"
                label="User Name:"
                label-for="email"
              >
                <b-form-input
                  id="email"
                  v-model="email"
                  type="email"
                  required
                  placeholder="Enter email"
                  class="mb-2"
                ></b-form-input>
              </b-form-group>
  
              <b-form-group
                id="password-group"
                label="Password:"
                label-for="password"
                class="mb-2"
              >
                <b-form-input
                  id="password"
                  v-model="password"
                  type="password"
                  required
                  placeholder="Enter password"
                ></b-form-input>
              </b-form-group>
  
              <b-form-group
                id="confirm-password-group"
                label-for="confirm-password"
                class="mb-2"
              >
                <b-form-input
                  id="confirm-password"
                  v-model="confirmPassword"
                  type="password"
                  required
                  placeholder="Confirm password"
                ></b-form-input>
              </b-form-group>
  
              <b-button type="submit" variant="success" class="mt-2" :disabled="isLoading">
                {{ isLoading ? 'Signing up...' : 'Sign Up' }}
              </b-button>
            </b-form>
          </b-card>
          <p>You already have an account? <a href="#" @click.prevent="$router.push('/login')">Signin</a></p>
        </b-col>
      </b-row>
    </div>
  </template>
  
  
  <style scoped>
  /* Add any component-specific styles here */
  </style>