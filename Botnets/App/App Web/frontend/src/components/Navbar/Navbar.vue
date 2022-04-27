<template>
  <div>
  <b-navbar toggleable="lg" type="dark" variant="dark" class="navbar-default">
    <b-navbar-brand href="#" class="main_title">Command and Control Detector</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item @click="redirectMainPage()">Main Page</b-nav-item>
        <b-nav-item @click="redirectAboutPage()">About us</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown right>
          <template v-slot:button-content>
            <em>{{ email }}</em>
          </template>
          <b-dropdown-item @click="closeSection()" v-if="this.$store.state.isWaiting">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      email: this.$store.state.email
    };
  },
  methods: {
    ...mapActions(["updateDashStates", "updateAuthenticationState"]),
    closeSection() {
      this.updateDashStates(true);
      this.updateAuthenticationState(false);
      this.$router.push({ name: this.$store.state.dir_routes.login });
    },
    redirectMainPage(){
      console.log(this.$router.currentRoute.name)
      if(this.$router.currentRoute.name == "Dash"){
        this.$router.go(this.$router.currentRoute)
      }
      else{
         this.$router.push({ name: this.$store.state.dir_routes.dash });
      }
    },
    redirectAboutPage(){
      this.$router.push({ name: this.$store.state.dir_routes.about});
    }
  }
};
</script>

<style scoped>

.main_title{
  margin-left: 20px;
}

</style>
