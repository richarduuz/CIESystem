<template>
  <div>
    <h2>This is uncompleted forms</h2>
    <button @click="test()"></button>
    <div>
      <h2 v-if="Object.keys(displayEntries).length === 0">目前没有请求的报价单</h2>
      <div v-else>
        <quo-forms :displayEntries="Object.values(displayEntries)" @formValueChangedId="formValueChangedId" @formValueChanged="formValueChanged">
        </quo-forms>
      </div>
    </div>
    <button @click="submitForm" class="submitBtn">提交</button>
    <form-rows :rows="Object.keys(displayEntries).length"></form-rows>
    <div class="infoDiv">I am test division</div>
  </div>
</template>

<script>
  import quoForms from '../quoForms';
  import FormRows from '../FormRows'
  import {exportDisplayForm, getDisplayAttribute} from '../../../functions/functions'

  export default {
    name: "UncompletedForms",
    asyncComputed: {
      displayEntries: {
        get() {
          let url = this.$store.state.url + '/uncompletedForms';
          return this.$http.get(url)
            .then(response => response.json())
            .then(data => this.processingData(data))
        },
        default: {}
      }
    },
    methods: {
      test(){
        let test = {}
        console.log(Object.keys(test).length)
      },
      formValueChangedId(value){
        let quoId = value[0];
        let attribute = getDisplayAttribute(value[1], this.$store.getters.displayAttributes)
        this.changedValues[quoId][attribute] = value[2]
      },
      formValueChanged(value){
        this.displayEntries[value[0]][value[1]] = value[2]
      },
      submitForm(){
        if (confirm("确定要提交吗")){
          let url = this.$store.state.url + '/confirmQuotationPrice';
        let postData = {"userId": this.$store.state.userId, "username": this.$store.state.username,
            "userTitle": this.$store.state.userTitle, "body": this.changedValues};
        postData = JSON.stringify(postData);
        this.$http.post(url, postData, {emulateJSON: true})
          .then(response => response.json())
          .then(data => {
            if (data){
              alert(data['status'], data['message'])
              this.toHomepage()
            }
          })
          .catch(()=> alert("error"))
        }
      },


      //---------------Internal Functions---------------//
      processingData(data) {
        let tmp = [];
        let result = {};
        this.exportWholeForm(data);
        this.exportquoId(data);
        tmp = exportDisplayForm(data['body'], this.$store.getters.displayAttributes);
        for (let i = 0; i<tmp.length; i++){
          result[this.wholeForms[i]['quoId']] = tmp[i]
        }
        return tmp
      },
      exportWholeForm(data){
        for (let item of data['body']) {
          this.wholeForms.push(item);
        }
      },
      exportquoId(data){
        for(let item of data['body']){
          this.changedValues[item['quoId']] = {}
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
      },
      toHomepage(){
                let path = '/homepage/' + this.$store.state.username;
                this.$router.push({
                    path
                })
            }
    },
    data() {
      return {
        confirmedForm: [],
        wholeForms: [],
        changedValues: {}
      }
    },
    components:{
      quoForms,
      FormRows
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
  .infoDiv{
    position: absolute;
    right: 20px;
    top: 65%;
    width: 80%;
    border: 1px solid blue;
  }

  button.submitBtn{
    position: absolute;
    top: 460px;
    right: 40%;
  }

</style>