<script setup lang="ts">
import { ref } from 'vue'

    const featuredCourses = ref([
      { id: 1, title: 'Introduction to AI', description: 'Learn the basics of Artificial Intelligence', image: 'ai-course.jpg' },
      { id: 2, title: 'Data Science Fundamentals', description: 'Master the essentials of data analysis', image: 'data-science.jpg' },
      { id: 3, title: 'Web Development Bootcamp', description: 'Build modern web applications', image: 'web-dev.jpg' },
    ]);

    const features = ref([
      { id: 1, title: 'Personalized Learning', description: 'Tailored courses adapted to your goals', icon: 'bi bi-person-check' },
      { id: 2, title: 'Expert Mentorship', description: 'Guidance from industry professionals', icon: 'bi bi-people' },
      { id: 3, title: 'Career Opportunities', description: 'Direct connections with top employers', icon: 'bi bi-briefcase' },
    ]);

    const partners = ref([
      { id: 1, name: 'Tech Co', logo: 'tech-co-logo.png' },
      { id: 2, name: 'Innovate Inc', logo: 'innovate-logo.png' },
      { id: 3, name: 'Future Systems', logo: 'future-systems-logo.png' },
      { id: 4, name: 'Global Edu', logo: 'global-edu-logo.png' },
    ]);

    const testimonials = ref([
      { id: 1, text: 'TalentCampus helped me transition into a new career in tech. The courses and mentorship were invaluable.', author: 'Jane Doe', role: 'Software Developer' },
      { id: 2, text: 'The personalized learning path kept me motivated and on track to achieve my goals.', author: 'John Smith', role: 'Data Analyst' },
      { id: 3, text: 'I landed my dream job thanks to the skills I gained and the connections I made through TalentCampus.', author: 'Emily Brown', role: 'UX Designer' },
    ]);

</script>

<template>
  <div id="app">
    <header class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <a class="navbar-brand" href="#">TalentCampus</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link" href="#courses">Courses</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#features">Features</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#partners">Partners</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#testimonials">Testimonials</a>
            </li>
          </ul>
          <div class="d-flex">
            <button class="btn btn-outline-primary me-2">Sign In</button>
            <button class="btn btn-primary">Register</button>
          </div>
        </div>
      </div>
    </header>

    <main>
      <section class="text-dark py-5">
        <div class="container">
          <div class="row align-items-center">
            <div class="col-lg-6">
              <h1 class="display-4 fw-bold mb-3">Empower Your Future with TalentCampus</h1>
              <p class="lead mb-4">Unlock your potential with personalized learning paths, expert mentorship, and career opportunities.</p>
              <button class="btn btn-light btn-lg">Get Started</button>
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

      <section id="partners" class="py-5">
        <div class="container">
          <h2 class="text-center mb-5">Our Partners</h2>
          <div class="row align-items-center">
            <div v-for="partner in partners" :key="partner.id" class="col-md-3 col-6 mb-4">
              <img :src="partner.logo" :alt="partner.name" class="img-fluid">
            </div>
          </div>
        </div>
      </section>

      <section id="testimonials" class="bg-primary text-white py-5">
        <div class="container">
          <h2 class="text-center mb-5">What Our Students Say</h2>
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