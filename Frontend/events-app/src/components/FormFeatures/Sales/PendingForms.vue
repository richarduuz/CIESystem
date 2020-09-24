<template>
  <div>
    I am Pending Forms
    <div v-if="displayEntries.length !== 0">
      <quo-forms :displayEntries="Object.values(displayEntries)">
      </quo-forms>
    </div>
    <h2 v-else>目前没有请求的报价单</h2>
  </div>
</template>

<script>
  import {exportDisplayForm} from "../../../functions/functions";
  import quoForms from '../quoForms';


  export default {
    name: "PendingForms",
    asyncComputed: {
      displayEntries: {
        get(){
          let url = this.$store.state.url + '/pendingForms';
          return this.$http.get(url)
            .then(response => response.json())
            .then(data => this.processingData(data))
        },
        default: {}
      }
    },
    methods:{
      processingData(data){
        let result = {};
        this.exportWholeForm(data);
        let tmp = exportDisplayForm(data['body'], this.$store.getters.displayAttributes);
        for (let i = 0; i<tmp.length; i++){
          result[this.wholeForms[i]['quoId']] = tmp[i]
        }
        console.log(tmp);
        return tmp
      },
       exportWholeForm(data){
        for (let item of data['body']) {
          this.wholeForms.push(item);
        }
      },
    },
    data() {
      return {
        wholeForms: [],
      }
    },
    components: {
      quoForms
    }
  }
</script>

<style scoped>

</style>