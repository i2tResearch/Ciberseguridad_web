<template>
<div>
   <div style="width:100%;display:flex;flex-direction:column;align-items:center;">
     <v-row v-if="numberOfData > 0">
       <h2 class="titles">Prediction's History Total : {{numberOfData}}</h2>
     </v-row>
     <v-row>
        <div v-if="numberOfData > 0"><apexchart type="pie" width="650px" :options="chartOptionsApex" :series="seriesApex" /></div>
        <div v-if="numberOfData == 0" class="welcome">
        <template>
  <v-card
    class="mx-auto"
    color="#26c6da"
    dark
    max-width="400"
  >
    <v-card-title>
      <span class="title font-weight-light">Bienvenido!</span>
    </v-card-title>

    <v-card-text class="headline font-weight-bold">
      No hay registros aun...
    </v-card-text>

    <v-card-actions>
      <v-list-item class="grow">
        <v-list-item-avatar color="grey darken-3">
          <v-img
            class="elevation-6"
            src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
          ></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title>Admin</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>
        </div>
        
     </v-row>
   </div>
</div>
</template>

<script>
import Vue from "vue";
import Axios from "axios";
import PieChart from "./Pie.js";
import VueApexCharts from "vue-apexcharts";
Vue.component("apexchart", VueApexCharts);

export default {
  name: "ReportChart",
  components: {
    PieChart,
    apexchart: VueApexCharts,
    timer: ""
  },
  data: () => {
    return {
      numberOfData: 0,
      seriesApex: [0, 0],
      chartOptionsApex: {
        labels: ["Benign", "Malign"],
        colors: ['#3FF581', '#FFA07A'],
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200
              },
              legend: {
                position: "bottom"
              }
            }
          }
        ]
      }
    };
  },
  created(){
    this.getInformation();
    this.timer = setInterval(this.fetchEventsList, 60000);
  },
  methods: {
    getInformation(){
      let url = this.$store.state.backend + "/api/database/0"
      Axios.get(url)
              .then(response => {
                if (!(response.status == 400)) {
                  this.updateChart(response.data)
                }})
              .catch(error => {});
    },
    updateChart(data) {
      let series = []
      let dataNumber = 0
      for(var i=0; i < data.length; i +=1){
        let temp = data[i].split(",")
        dataNumber += parseInt(temp[1])
        series.push(parseInt(temp[1]))
      }
      this.numberOfData = dataNumber
      this.seriesApex = series
    },
    fetchEventsList() {
      this.getInformation();
    }
  }
};
</script>

<style scoped>

.titles {
  color: white;
  
}

.welcome {
  height: 500px;

}

</style>