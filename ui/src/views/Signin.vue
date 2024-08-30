<script setup lang="ts">
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { useAuthStore } from '@/stores/auth'
//   import { useNotification } from '../composables/useNotification'

  const router = useRouter()
  const authStore = useAuthStore()
//   const { addNotification } = useNotification()

  const username = ref('')
  const password = ref('')
  const errorLogin = ref('')
  
  const handleLogin = async () => {
    try {
      await authStore.login(username.value, password.value)
    //   addNotification('Login successful', 'success')
      router.push('/')
      // router.push('/dashboard')
    } catch (error: any) {
      if (error['response']){
        errorLogin.value = error['response']['data']['detail'] || 'Please check your credentials.'
      } else {
        errorLogin.value = 'Error server. Please check your connexion.'
        console.error(`Login failed: ${error['response']}`)
      }
      
    //   addNotification(`Login failed. ${errorLogin.value}.`, 'error')
    }
  }
  </script>
  
  <template>
    <b-row class="login my-4">
        <b-col cols="auto">
          <b-icon name="lock-fill" />
          <h2 class="head">Login</h2>

        <b-form @submit.prevent="handleLogin">
          <b-form-group label="Username" label-for="username">
            <b-form-input id="username" v-model="username" required autofocus></b-form-input>
          </b-form-group>
          <b-form-group label="Password" label-for="password">
            <b-form-input id="password" v-model="password" type="password" required></b-form-input>
          </b-form-group>

          <br>

          <b-alert variant="danger" :modelValue="errorLogin.length">
            {{ errorLogin }}
          </b-alert>

          <b-button type="submit" variant="primary" size="lg" class="my-2">Login</b-button>
        </b-form>
        <p>Don't have an account? <a href="#" @click.prevent="$router.push('/signup')">Signup</a></p>
      </b-col>      
    </b-row>
  </template>
  