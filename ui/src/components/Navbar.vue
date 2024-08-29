<script lang="ts" setup>
// import { usePreferredLanguage, getSupportedLanguages } from '../composables/locale'
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

// const preferredLanguage = usePreferredLanguage()
// const supportedLanguages = getSupportedLanguages()
const title = import.meta.env.VITE_APP_TITLE

const auth = useAuthStore()
const router = useRouter()

const isLoggedIn = computed(() => auth.isAuthenticated);

const doLogout = () => {
  auth.logout()
  router.push('/')
}


</script>

<template>
<BNavbar toggleable="lg" variant="primary" v-b-color-mode="'dark'">
  <BNavbarBrand href="#">{{ title }}</BNavbarBrand>
  <BNavbarToggle target="nav-collapse" />
  <BCollapse id="nav-collapse" is-nav>
    <BNavbarNav>
      <BNavItem href="#courses">Courses</BNavItem>
      <BNavItem href="#features">Features</BNavItem>
      <BNavItem href="#partners">Partners</BNavItem>
      <BNavItem href="#testimonials">Testimonials</BNavItem>
    </BNavbarNav>

    <!-- Right aligned nav items -->
    <BNavbarNav class="ms-auto mb-2 mb-lg-0">
      
      <BNavItem to="/" variant="info" v-if="isLoggedIn" @click="doLogout">Logout</BNavItem>
      <template v-else>
        <BNavItem to="/login" variant="outline-success">Signin</BNavItem>
        <BNavItem to="/register" variant="info">Register</BNavItem>
      </template>


      <!-- BNavItemDropdown :text="preferredLanguage?.toUpperCase()" right>
        <BDropdownItem href="#" v-for="lang in supportedLanguages" :key="lang">{{ lang?.toLocaleUpperCase() }}</BDropdownItem>
      </BNavItemDropdown -->
    </BNavbarNav>

    <!-- <BNavForm class="d-flex">
      <BFormInput class="me-2" placeholder="Search" />
      <BButton type="submit" variant="outline-success">Search</BButton>
    </BNavForm> -->
  </BCollapse>
</BNavbar>

</template>


<style>

</style>