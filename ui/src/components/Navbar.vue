<script lang="ts" setup>
import { usePreferredLanguage, getSupportedLanguages } from '../composables/locale'
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const title = import.meta.env.VITE_APP_TITLE

const preferredLanguage = ref(usePreferredLanguage())
const supportedLanguages = getSupportedLanguages()
const switchLanguageTo = (lang: string) => {
  preferredLanguage.value = lang
}


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
      
      <template v-if="isLoggedIn">
        <BNavItem to="/courses" variant="outline-success">My Courses</BNavItem>
        <BNavItem to="/" variant="info" @click="doLogout">Logout</BNavItem>
      </template>
      <template v-else>
        <BNavItem to="/login" variant="outline-success">Signin</BNavItem>
        <BNavItem to="/register" variant="info">Register</BNavItem>
      </template>

      <BNavItemDropdown right>
        <template #button-content>
          <b-icon name="globe" :size="24" /> {{ preferredLanguage?.toLocaleUpperCase() }}
        </template>
        <BDropdownItem href="#" v-for="lang in supportedLanguages" :key="lang" @click="switchLanguageTo(lang)">
          {{ lang?.toLocaleUpperCase() }}
        </BDropdownItem>
      </BNavItemDropdown>

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