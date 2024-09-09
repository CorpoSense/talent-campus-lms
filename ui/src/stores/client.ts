import axios from 'axios'

const client = axios.create({
    baseURL: `${(import.meta.env.DEV?import.meta.env.VITE_HOSTNAME:'')}/api`,
    // withCredentials: true,  // This is for CSRF/session based authentication
})

// This is required for CSRF token
if (/*import.meta.env.PROD && */ import.meta.env.VITE_USE_CSRF_TOKEN){
  client.interceptors.request.use(function (config) {
    const token = document.cookie.split('; ').find(row => row.startsWith('csrftoken='))
    if (token) {
      config.headers['X-CSRFToken'] = token.split('=')[1]
    }
    return config
  }, function (error) {
    return Promise.reject(error)
  })
}

export default client