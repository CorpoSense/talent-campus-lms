<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useApi } from '@/stores/api'

const api = useApi()

const myCourses = ref<any[]>([])
// const myCourses = ref<any[]>([{
//   'id': 1,
//   'title': 'Reporting Officer',
//   'description': 'Reporting Officer is one of the best course for those who want to start their journey to the Data world.',
//   'image': 'https://corposense.com/wp-content/uploads/2023/05/analysis-1841158-scaled.jpg'
// }])


onMounted( async () => {
  const courses = await api.getCourses()  
  console.log(courses);
  myCourses.value = courses;
})

</script>

<template>
  <div id="main">
    <Navbar />

    <main>
      <section id="courses" class="py-5">
        <div class="container">
          <h2 class="text-center mb-5">My Courses</h2>
          <div class="row">
            <div v-for="course in myCourses" :key="course.id" class="col-md-4 mb-4">
              <div class="card h-100">
                <img :src="course.image" class="card-img-top" :alt="course.title">
                <div class="card-body">
                  <h5 class="card-title">{{ course.title }}</h5>
                  <p class="card-text">{{ course.description }}</p>
                  
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>

    <Footer />

  </div>
</template>

<style>
@import 'bootstrap/dist/css/bootstrap.min.css';
@import 'bootstrap-icons/font/bootstrap-icons.css';

.card {
  transition: transform 0.3s ease-in-out;
}

.card:hover {
  transform: translateY(-5px);
}
</style>