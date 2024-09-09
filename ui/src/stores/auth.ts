
import { defineStore } from 'pinia'
import client from './client'

enum ConnectionType {
  JWT = 'jwt', BASIC_AUTH = 'basicAuth'
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    refresh: null,
    token: null,
  }),
  getters: {
    isAuthenticated: (state) => !!state.token,
  },
  actions: {
    async login(username: string, password: string, connectionType = ConnectionType.JWT) {
      try {
        if (connectionType == ConnectionType.JWT){
          const response = await client.post('/token/', {
            'username': username, 'password': password
          },{
            headers: { 'Content-Type': 'application/json' }
          })

          this.refresh = response.data.refresh
          this.token = response.data.access
          client.defaults.headers.common['Authorization'] = `Bearer ${this.token}`

        } else if (connectionType == ConnectionType.BASIC_AUTH) {

          const params = new URLSearchParams({ 'username': username, 'password': password })
          const response = await client.post('/token/', params, {
            withCredentials: true, // some cloud force this option
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
          })
          this.refresh = response.data.refresh
          this.token = response.data.access
          if (response.data.token_type === 'bearer') { 
            client.defaults.headers.common['Authorization'] = `Bearer ${this.token}`
          }
        }
      } catch (error) {
        throw error
      }
    },
    async signup(username: string, password: string) {
      try {
        const response = await client.post('/register/', { username: username, password: password, email: username })
        this.refresh = response.data.refresh
        this.token = response.data.token
        client.defaults.headers.common['Authorization'] = `Bearer ${this.token}`

      } catch (error: any) {
        console.error('Signup failed:', error.response.data.detail[0])
        throw error
      }
    },
    logout() {
      this.refresh = null
      this.token = null
      delete client.defaults.headers.common['Authorization']
    },
    async getCourses() {
      try {
        const courses = await client.get('/courses')
        return courses
      } catch (error) {
        console.error(error)
        throw error        
      }
    }
  },
})