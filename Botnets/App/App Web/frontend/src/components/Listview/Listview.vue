<template>
  <v-card max-width="600" class="mx-auto">
    <v-toolbar color="cyan" dark>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>History</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-toolbar>

    <v-list three-line max-height="500px" class="overflow-y-auto">
      <template v-for="(item, index) in items">
        <v-subheader v-if="item.header" :key="item.header" v-text="item.header"></v-subheader>

        <v-divider v-else-if="item.divider" :key="index" :inset="item.inset"></v-divider>

        <v-list-item v-else :key="item.title" @click>
          <v-list-item-avatar>
            <v-img :src="item.avatar"></v-img>
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title v-html="item.title"></v-list-item-title>
            <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-card>
</template>

<script>

import Axios from "axios";


export default {
  data: () => ({
    items: [],
    timer: ""
  }),
  created() {
    this.getInformation();
    this.timer = setInterval(this.fetchEventsList, 60000);

  },
  methods: {
    getInformation(){
      let url = this.$store.state.backend + "/api/database/1"
      Axios.get(url)
              .then(response => {
                if (!(response.status == 400)) {
                  this.updateListView(response.data)
                }})
              .catch(error => {});
    },
    updateListView(predictions){
      let schema = []
      let row = {}
      if(predictions.length > 0){
        for(var i=predictions.length-1; i >= 0; i-=1){
                let temp = predictions[i].split(",")
                let prediction = temp[0]
                let datetime = temp[1].split("T")
                let message = temp[2]
                row = {
                  avatar: "",
                  title: prediction + " ====> [Day : " + datetime[0] + "] [Hour : " + datetime[1] + "]",
                  subtitle: message

                }
                if(prediction == "Malign"){
                  row.avatar = "http://icon-library.com/images/exit-icon-png/exit-icon-png-18.jpg"
                }
                else{
                  row.avatar = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Check_green_icon.svg"
                }
                schema.push(row)
                row = { divider: true, inset: true }
                schema.push(row)
              }
      }
      else{
        row = {
                  avatar: "https://cdn1.iconfinder.com/data/icons/cursor-pointers/24/6-512.png",
                  title: "Sin Registros..." ,
                  subtitle: "No tienes escaneos todavia!"
          }
        schema.push(row)
        row = { divider: true, inset: true }
        schema.push(row)
      }
      this.items = schema
    },
    fetchEventsList() {
      this.getInformation();
    }
  }
};
</script>
    