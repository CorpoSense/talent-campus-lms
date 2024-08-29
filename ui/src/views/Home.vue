<script setup lang="ts">
import { ref } from 'vue'

    const featuredCourses = ref([
      { id: 1, title: 'Introduction to AI', description: 'Learn the basics of Artificial Intelligence', image: 'ai-course.jpg' },
      { id: 2, title: 'Data Science Fundamentals', description: 'Master the essentials of data analysis', image: 'data-science.jpg' },
      { id: 3, title: 'Full Stack Development Bootcamp', description: 'Build modern full stack web applications', image: 'web-dev.jpg' },
    ]);

    const features = ref([
      { id: 1, title: 'Personalized Learning', description: 'Tailored courses adapted to your goals', icon: 'bi bi-person-check' },
      { id: 2, title: 'Expert Mentorship', description: 'Guidance from industry professionals', icon: 'bi bi-people' },
      { id: 3, title: 'Career Opportunities', description: 'Direct connections with top employers', icon: 'bi bi-briefcase' },
    ]);

    const clients = ref([
      { id: 1, name: 'Tech Co', logo: 'clients/pharmalliance_logo.png' },
      { id: 2, name: 'Innovate Inc', logo: 'clients/Linde_logo.png' },
      { id: 3, name: 'Future Systems', logo: 'clients/lncpp_logo.png' },
      { id: 4, name: 'Global Edu', logo: 'clients/yalidine.png' },
    ]);

    const testimonials = ref([
      { id: 1, text: 'I had the chance to be part of an amazing team, mentored by an awesome developer with strong knowledge in software architecture and data science. We collaborated on several projects during my journey as a software developer. The knowledge I gained from CorpoSense is unparalleled and incomparable to any other place.', author: 'Ammar DJEBABLA', role: 'Full Stack Developer' },
      { id: 2, text: 'I had the privilege of completing my end-of-study project with CorpoSense Campany, and the experience was nothing short of exceptional. Their professionalism stood out from day one. The team at CorpoSense demonstrated a deep understanding of industry standards and provided invaluable insights that greatly enhanced my project. Their support and guidance were consistent and thorough, ensuring that I had everything I needed to succeed. I highly recommend CorpoSense to anyone seeking top-tier consulting services.', author: 'Meriem B.', role: 'Data Analyst' },
      { id: 3, text: "Learning machine learning and programming through CorpoSense Company has been an exceptional experience. Their expertise and guidance made complex concepts easy to understand. The hands-on projects provided practical insights, greatly enhancing my technical skills and opening new research opportunities. I highly recommend CorpoSense for anyone looking to build a solid machine learning and programming foundation.", author: 'Mahedi MAHALAL', role: 'Assistant Professor at UNH' },
      { id: 3, text: "Joining CorpoSense has been a transformative experience for me as a web developer. From day one, I was welcomed into a collaborative team environment where I had the opportunity to learn and grow. Over the years, I've had the chance to work with new technologies and take on challenging project that significantly enhanced my skills. The company's dedication to continuous Learning and innovation is inspiring, and I'm proud to be part of a team that values and nurtures talent.", author: 'Imene BARAITAME', role: 'Assistant Professor Math' },
    ]);

</script>

<template>
  <div id="main">
    <Navbar />

    <main>
      <section class="text-dark py-5">
        <div class="container">
          <div class="row align-items-center">
            <div class="col-lg-6">
              <h1 class="display-4 fw-bold mb-3">Empower Your Future with TalentCampus</h1>
              <p class="lead mb-4">Unlock your potential with personalized learning paths, expert mentorship, and career opportunities.</p>
              <b-button variant="outline-success" size="lg" class="mb-2">Get Started</b-button>
            </div>
            <div class="col-lg-6">
              <img src="/public/hero-image.jpeg" alt="Students learning" class="img-fluid rounded">
            </div>
          </div>
        </div>
      </section>

      <section id="courses" class="py-5">
        <div class="container">
          <h2 class="text-center mb-5">Featured Courses</h2>
          <div class="row">
            <div v-for="course in featuredCourses" :key="course.id" class="col-md-4 mb-4">
              <div class="card h-100">
                <img :src="course.image" class="card-img-top" :alt="course.title">
                <div class="card-body">
                  <h5 class="card-title">{{ course.title }}</h5>
                  <p class="card-text">{{ course.description }}</p>
                  <a href="#" class="btn btn-primary">Learn More</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="features" class="bg-light py-5">
        <div class="container">
          <h2 class="text-center mb-5">Key Features</h2>
          <div class="row">
            <div v-for="feature in features" :key="feature.id" class="col-md-4 mb-4">
              <div class="text-center">
                <i :class="feature.icon + ' display-4 text-primary mb-3'"></i>
                <h4>{{ feature.title }}</h4>
                <p>{{ feature.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="clients" class="py-5">
        <div class="container">
          <h2 class="text-center mb-5">Some of our Clients</h2>
          <div class="row align-items-center">
            <div v-for="partner in clients" :key="partner.id" class="col-md-3 col-6 mb-4">
              <img :src="partner.logo" :alt="partner.name" class="img-fluid">
            </div>
          </div>
        </div>
      </section>

      <section id="testimonials" class="bg-primary text-white py-5">
        <div class="container">
          <h2 class="text-center mb-5">Testimonials</h2>
          <div class="row">
            <div v-for="testimonial in testimonials" :key="testimonial.id" class="col-md-4 mb-4">
              <div class="card bg-light text-dark h-100">
                <div class="card-body">
                  <p class="card-text">{{ testimonial.text }}</p>
                  <footer class="blockquote-footer mt-3">
                    {{ testimonial.author }}
                    <cite title="Source Title">{{ testimonial.role }}</cite>
                  </footer>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="py-5">
        <div class="container text-center">
          <h2 class="mb-4">Ready to Start Your Learning Journey?</h2>
          <button class="btn btn-primary btn-lg">Explore Courses</button>
        </div>
      </section>
    </main>

    <footer class="bg-dark text-white py-4">
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <h5>TalentCampus</h5>
            <p>Empowering Tomorrow's Innovators Today</p>
          </div>
          <div class="col-md-4">
            <h5>Quick Links</h5>
            <ul class="list-unstyled">
              <li><a href="#" class="text-white">About Us</a></li>
              <li><a href="#" class="text-white">Courses</a></li>
              <li><a href="#" class="text-white">Career Resources</a></li>
              <li><a href="#" class="text-white">Contact Us</a></li>
            </ul>
          </div>
          <div class="col-md-4">
            <h5>Connect With Us</h5>
            <div class="d-flex">
              <a href="#" class="text-white me-3"><i class="bi bi-facebook"></i></a>
              <a href="#" class="text-white me-3"><i class="bi bi-twitter"></i></a>
              <a href="#" class="text-white me-3"><i class="bi bi-linkedin"></i></a>
              <a href="#" class="text-white"><i class="bi bi-instagram"></i></a>
            </div>
          </div>
        </div>
        <hr class="my-4">
        <div class="text-center">
          <p>&copy; 2024 TalentCampus. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<style>
@import 'bootstrap/dist/css/bootstrap.min.css';
@import 'bootstrap-icons/font/bootstrap-icons.css';

/* Add any custom styles here */
.hero {
  background: linear-gradient(45deg, #bebfc0, #6610f2);
}

.card {
  transition: transform 0.3s ease-in-out;
}

.card:hover {
  transform: translateY(-5px);
}
</style>