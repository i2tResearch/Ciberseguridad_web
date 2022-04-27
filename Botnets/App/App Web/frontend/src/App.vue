<template>
  <v-app>
    <div id="app">
        <Navbar v-if="this.$store.state.authenticated" />
        <router-view/>
        <Footer/>
      </div>
  </v-app>
  
</template>

<script>
import Navbar from './components/Navbar/Navbar'
import Footer from './components/Footer/Footer'

export default {
  name: 'App',
  components: {
    Navbar,
    Footer
  },
  data: () => ({
    
  }),
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
