
import { defineStore } from 'pinia'
import client from './client'


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