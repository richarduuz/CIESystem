<template>
  <div>
    I am from create form
    <button @click="test">test</button>
    <br>
    <div class="FormDiv">
      <table class="Form">
        <tr>
          <th v-for="attribute in $store.getters.displayAttributes" :key="attribute">{{attribute}}</th>
          <th>是否视为重要项目</th>
        </tr>
        <tr v-for="(entry, index) in displayEntries" :key="index">
          <th v-for="(value, subIndex) in $store.getters.displayAttributes" :key="subIndex">
            <input class="FormInput" v-model="displayEntries[index][subIndex]" :disabled="$store.getters.systemAttributes.includes($store.getters.displayAttributes[subIndex])">
          </th>
          <th>
            <select v-model="isImportant[index]" required>
              <option value="No" selected>No</option>
              <option value="Yes">Yes</option>
            </select>
          </th>
        </tr>
      </table>
    </div>
    <div>
      <input type="file" ref="file" id="file" @change="handleFileUpload">
      <button :disabled="file === undefined" @click="submitForm">Submit</button>
      <button @click="confirmForm">Confirm</button>
      <button @click="createNewEntry">Create New Entry</button>
    </div>
  </div>

</template>

<script>
  export default {
    name: "CreateForm",
    data() {
      return {
        file: undefined,
        displayEntries: [],
        confirmedForm: [],
        isImportant: []
      }
    },
    methods: {
      test() {
        console.log(this.confirmedForm)
      },

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
                for (let attribute of this.$store.getters.displayAttributes){
                  entry.push(item[attribute])
                }
                this.displayEntries.push(entry)
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
          this.confirmedForm = [];
          for (let i = 0; i<this.displayEntries.length; i++){
            this.confirmedForm.push(this.formDict(this.displayEntries[i], this.isImportant[i]))
          }
          let postData = {"userId": this.$store.state.userId, "username": this.$store.state.username,
            "userTitle": this.$store.state.userTitle, "body": this.confirmedForm};
          console.log(postData);
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
        this.displayEntries.push([]);
        console.log(this.displayEntries);
      },

      formDict(item, isImportant){
        let doc = {};
        for (let i = 0; i<this.$store.getters.displayAttributes.length; i++){
          doc[this.$store.getters.displayAttributes[i]] = item[i];
        }
        for (let attribute of this.$store.getters.aDisplayAttributes){
          doc[attribute] = "";
        }
        doc['isImportant'] = isImportant;
        return doc
      }
    },

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
  }

</style>