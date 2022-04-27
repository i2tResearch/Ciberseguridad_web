<template>
  <div class="main">
    <v-container>
      <v-row class="mx-2" justify="center">
        <v-col
          style="background:whitesmoke; border-radius:20px;padding:25px;border:2px solid white"
          xs="10"
          sm="10"
          md="5"
          lg="5"
          xl="5"
        >
          <v-form lazy-validation ref="form" v-model="valid">
            <h1>Inicio de Sesión</h1>
            <br />
            <v-text-field
              @keyup.13="formSubmit"
              :rules="emailRules"
              label="E-mail"
              required
              v-model="email"
            ></v-text-field>
            <br />
            <br />
            <v-btn
              color="primary"
              style="margin:10px;background:#08799C"
              @click="formSubmit"
            >Ingresar</v-btn>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Axios from "axios";
import { mapActions } from 'vuex'

export default {
  name: "Login",
  data() {
    return {
      email: "",
      isOpen: false,
      valid: false,
      msg: "",
      emailRules: [
        v => !!v || "El correo electrónico es obligatorio",
        v => v.length >= 8 || "Digite un correo valido",
        v =>  v.length > 0 && /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || "Digite un correo valido"]
    };
  },
  beforeMount() {},
  methods: {
    ...mapActions(['updateAuthenticationState','updateEmailApp']),
    formSubmit() {
      if (this.$refs.form.validate()) {
        let formEmail = this.email;
        let url = this.$store.state.backend + "/api/notification/";
        console.log(url)
        var header = {
          'Access-Control-Allow-Headers':'Content-Type',
          'Access-Control-Allow-Origin': '*'
        }
        Axios.post(url, {
                email: formEmail,
              }, header)
              .then(response => {
                if (!(response.status == 400)) {
                    this.updateEmailApp(formEmail);
                    this.updateAuthenticationState(true);
                    this.$router.push({ name: this.$store.state.dir_routes.dash });
                }
                })
              .catch(error => {
                  //this.msg = error.response.data.message;
                  //this.isOpen = true;
                });
      }
    }
  }
};
</script>
<style scoped>
.main {
  background-image: url("./img/background.jpg");
  background-size: cover;
  min-height: 100vh;
  height: auto;
  width: 100vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}
</style>