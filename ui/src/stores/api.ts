
import { defineStore } from 'pinia'
import axios from 'axios'


const client = axios.create({
  baseURL: `${import.meta.env.VITE_HOSTNAME}`,
})

export const useApi = defineStore('api', {
  state: () => ({
    courses: [],
  }),
  getters: {
    nbrOfCourses: (state) => state.courses?.length,
  },
  actions: {
    async getCourses() {
      try {
        const courses = await client.get('/courses')
        if (courses.data){
          return courses.data['results']
        }
      } catch (error) {
        console.error(error)
        throw error        
      }
    }
  },
})