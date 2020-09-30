<template>
  <div>
    <button @click="test"></button>
    <div v-if="displayEntries.length === 0">
      <h2>请添加表格</h2>
    </div>
    <div v-else>
      I am from create form
      <br>
      <quo-forms :display-entries="displayEntries" @formValueChanged="formValueChanged">
        <th slot="isImportant">是否视为重要项目</th>
        <template slot-scope="slot">
          <select v-model="isImportant[slot.data['index']]" required>
            <option value="No">No</option>
            <option value="Yes">Yes</option>
          </select>
        </template>
      </quo-forms>
    </div>
    <div class="BtnDiv">
        <input type="file" ref="file" id="file" @change="handleFileUpload">
        <button :disabled="file === undefined" @click="submitForm">Submit</button>
        <button @click="confirmForm">Confirm</button>
        <button @click="createNewEntry">Create New Entry</button>
    </div>
    <form-rows :rows="displayEntries.length"></form-rows>
  </div>
</template>

<script>
  import quoForms from '../quoForms';
  import FormRows from '../FormRows'
  import {exportDisplayForm} from '../../../functions/functions'

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
        console.log(this.displayEntries)
      },

      submitForm() {
        let url = this.$store.state.url + "/extractQuotation";
        let form = new FormData();
        form.append('Quotation', this.file);
        this.$http.post(url, form, {headers: {'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}})
          .then(response => response.json())
          .then(data => {
            if (data['status'] === 'Okay'){
              this.displayEntries = exportDisplayForm(data['body'], this.$store.getters.displayAttributes);
              for (let i = 0; i<this.displayEntries.length; i++){
                this.isImportant[i] = 'No'
              }
            } else {
              alert("表格样式无法解析")
            }
          })
          .catch(e => {
            alert(e.status)
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
                alert("已录入数据库");
                this.toHomepage()
              }
            })
            .catch(e => {
              alert(e.status)
            });
        }
      },

      formValueChanged(value){
        this.displayEntries[value[0]][value[1]] = value[2];
      },

      createNewEntry(){
        this.displayEntries.push([]);
        this.isImportant.push('No')
      },




      checkFilename(filename){
        let name = filename.split('.');
        name = name[name.length-1];
        let result = false;
        name === 'xlsx' || name === 'xls' ? result = true : result ;
        return result
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
      },
      toHomepage(){
                let path = '/homepage/' + this.$store.state.username;
                this.$router.push({
                    path
                })
            }
    },
    components: {
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
  }

  div.BtnDiv{
    position: absolute;
    top: 460px;
    right: 25%;
  }

</style>