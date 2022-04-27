<template>
  <div class="main">
    <v-row>
      <v-col>
        <Listview />
      </v-col>
      <v-col>
       <ReportChart />
      </v-col>
    </v-row>
    <v-row>
      <v-col class="options">
        <div>
          <h3>:: Options ::</h3>
        </div>
        <br />
        <div>
          <v-btn color="success" dark @click="start()" v-if="this.$store.state.isWaiting">Start Scan</v-btn>
          <v-btn color="error" dark @click="stop()" v-if="!this.$store.state.isWaiting">Stop Scan</v-btn>
        </div>
      </v-col>
      <v-col class="state">
        <div>
          <h3>:: State ::</h3>
        </div>
        <br />
        <div>
          <v-chip large class="ma-2" color="green" text-color="white" v-if="!this.$store.state.isWaiting">Running...</v-chip>
          <v-chip large class="ma-2" color="orange" text-color="white" v-if="this.$store.state.isWaiting">Stopped...</v-chip>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import Axios from "axios";
import Listview from "./../../components/Listview/Listview";
import ReportChart from "./../../components/ReportChart/Piechart";
import { mapActions } from "vuex";
import Vue from "vue";

export default {
  components: {
    Listview,
    ReportChart
  },
  data() {
    return {
      //timer: ""
    };
  },
  created() {
    //this.timer = setInterval(this.fetchEventsList, 60000);
  },
  methods: {
    ...mapActions(["updateDashStates"]),
    start() {
      let url = this.$store.state.backend + "/api/mining/0";
      this.updateDashStates(false);
      Axios.get(url)

    },
    stop() {
      let url = this.$store.state.backend + "/api/mining/1";
      this.updateDashStates(true);
      Axios.get(url)
    },
    updated() {},
    fetchEventsList() {
      //this.$router.go(this.$router.currentRoute);
    },
    cancelAutoUpdate() {
      //clearInterval(this.timer);
    }
  },

  beforeDestroy() {
    clearInterval(this.timer);
  }
};
</script>

<style scoped>
.options {
  border: 2px solid black;
  margin: 200px 100px 50px 100px;
  background-color: black;
  opacity: 0.9;
  color: white;
  height: 150px;

}
.state {
  border: 2px solid black;
  margin: 200px 100px 50px 100px;
  background-color: black;
  opacity: 0.9;
  color: white;
  height: 150px;

}
.main{
  background-image: url("./img/background.jpg");
  background-size: cover;
  height:950px

}


</style>
