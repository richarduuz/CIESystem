<template>
  <div>
    I am create Form
    <br>
    <table class="Form">
      <tr>
        <th v-for="attribute in $store.state.quotationAttributes" :key="attribute">{{attribute}}</th>
      </tr>
      <tr v-for="(entry, index) in entries" :key="index">
        <th v-for="(value, subIndex) in $store.state.quotationAttributes" :key="subIndex"><input v-model="entries[index][subIndex]"></th>
      </tr>
<!--      <tr v-for="(item, index) in newEntries" :key="index">-->
<!--        <th v-for="(attribute, subIndex) in $store.state.quotationAttributes" :key="subIndex"><input :id="'id'+index+subIndex"></th>-->
<!--      </tr>-->
    </table>
    <input type="file" ref="file" id="file" @change="handleFileUpload">
    <button :disabled="file === undefined" @click="submitForm">Submit</button>
    <button @click="confirmForm">Confirm</button>
    <button @click="createNewEntry">Create New Entry</button>
  </div>
</template>

<script>
  export default {
    name: "CreateForm",
    data() {
      return {
        file: undefined,
        newEntries: [],
        entries: [],
        confirmedForm: []
      }
    },
    methods: {
      submitForm() {
        let url = this.$store.state.url + "/extractQuotation";
        let form = new FormData();
        form.append('Quotation', this.file);
        this.$http.post(url, form, {headers: {'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}})
          .then(response => response.json())
          .then(data => {
            if (data['status'] === 'Okay'){
              for(let item of data['body']) {
                for(let key in item){if (item[key] === 'nan'){item[key] = ''}}
                let entry = [];
                for (let attribute of this.$store.state.quotationAttributes){
                  entry.push(item[attribute])
                }
                this.entries.push(entry)
              }
            } else {
              alert("表格样式无法解析")
            }
          })
      },

      handleFileUpload(){
        if (this.checkFilename(this.$refs.file.files[0].name)){
          this.file = this.$refs.file.files[0]
        } else {
          this.$refs.file.files = undefined;
          alert("file type does not support")
        }
      },

      confirmForm(){
        if(confirm("确认提交表格吗？")){
          let url = this.$store.state.url + "/confirmQuotation";
          console.log(url);
          this.confirmedForm = {};
          for (let item of this.entries){
            this.confirmedForm.push(this.formDict((item)))
          }
          let postData = this.confirmedForm;
          postData = JSON.stringify(postData);
          this.$http.post(url, postData, {emulateJSON: true})
            .then(response => response.json())
            .then(data => {
              if (data){
                alert("get response");
              }
            });
          console.log(this.confirmedForm);
        }
      },

      checkFilename(filename){
        let name = filename.split('.');
        name = name[name.length-1];
        let result = false;
        name === 'xlsx' || name === 'xls' ? result = true : result ;
        return result
      },

      createNewEntry(){
        this.entries.push([]);
        console.log(this.entries);
      },

      formDict(item){
        let doc = {};
        for (let i = 0; i<this.$store.state.quotationAttributes.length; i++){
          if (this.$store.state.quotationAttributes[i]  === '销售'){
            item[i] = this.$store.state.username;
          }
          doc[this.$store.state.quotationAttributes[i]] = item[i];
        }
        return doc
      }
    },

  }
</script>

<style scoped>
.Form table, th, td {
  border: 1px solid black;
}
  div {
    overflow-x: auto;
  }
  th {
    width: 155px;
  }

</style>