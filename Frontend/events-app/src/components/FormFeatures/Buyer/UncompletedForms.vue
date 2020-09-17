<template>
  <div>
    <h2>This is uncompleted forms</h2>
    <button @click="test()"></button>
    <quo-forms :displayEntries="displayEntries" @formValueChanged="formValueChanged">
    </quo-forms>
    <button @click="submitForm">提交</button>
  </div>
</template>

<script>
  import quoForms from '../quoForms';
  import {exportDisplayForm} from '../../../functions/functions'

  export default {
    name: "UncompletedForms",


    asyncComputed: {
      displayEntries() {
        let url = this.$store.state.url + '/uncompletedForms';
        return this.$http.get(url)
          .then(response => response.json())
          .then(data => this.processingData(data))
      }
    },
    methods: {
      test(){
        console.log(this.wholeForms)
      },
      formInputClassActive(item){
        return this.$store.getters.systemAttributes.includes(item)
      },
      formValueChanged(value){
        this.wholeForms[value[0]]

        this.displayEntries[[value[0]]][value[1]] = value[2];
        let doc = {};
        doc[this.$store.getters.displayAttributes[value[1]]] = value[2];
        this.changedValues[value[0]] = doc;
        console.log(this.changedValues)
      },
      submitForm(){
        let url = this.$store.state.url + '/confirmQuotationPrice';
        this.confirmedForm = [];
        for (let i = 0; i<this.displayEntries.length; i++){
          this.confirmedForm.push(this.formDict(this.displayEntries[i]))
        }
        let postData = {"userId": this.$store.state.userId, "username": this.$store.state.username,
            "userTitle": this.$store.state.userTitle, "body": this.confirmedForm};
        postData = JSON.stringify(postData);
        this.$http.post(url, postData, {emulateJSON: true})
          .then(response => response.json())
          .then(data => {
            if (data){
              alert('Okay')
            }
          })
          .catch(()=> alert("error"))
      },



      //---------------Internal Functions---------------//
      processingData(data) {
        let result = [];
        this.exportWholeForm(data);
        this.exportquoId(data);
        result = exportDisplayForm(data['body'], this.$store.getters.displayAttributes);
        return result
      },
      exportWholeForm(data){
        for (let item of data['body']) {
          this.wholeForms.push(item);
        }
      },
      exportquoId(data){
        for(let item of data['body']){
          this.changedValues.push({'quoId': item['quoId']})
        }
      },
      formDict(item){
        let doc = {};
        for (let i = 0; i<this.$store.getters.displayAttributes.length; i++){
          doc[this.$store.getters.displayAttributes[i]] = item[i];
        }
        for (let attribute of this.$store.getters.aDisplayAttributes){
          doc[attribute] = "";
        }
        return doc
      }
    },
    data() {
      return {
        confirmedForm: [],
        wholeForms: [],
        changedValues: []
      }
    },
    components:{
      quoForms
    }
  }
</script>

<style scoped>
  .FormDiv {
    overflow-x: auto;
  }
.Form table, th, td {
  border: 1px solid black;
}
  th {
    max-width: 100%;
    white-space: nowrap;
  }
  .FormInput {
    max-width: 100%;
    white-space: nowrap;
    background-color: #d3d3d3;
  }

</style>