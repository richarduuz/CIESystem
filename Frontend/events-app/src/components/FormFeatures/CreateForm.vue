<template>
  <div>
    I am create Form
    <br>
    <table class="Form">
      <tr>
        <th v-for="attribute in this.$store.state.quotationAttributes" :key="attribute">{{attribute}}</th>
      </tr>
      <tr v-for="(entry, index) in entries" :key="index">
        <th v-for="(value, subIndex) in entry" :key="subIndex"><input v-model="entries[index][subIndex]"></th>
      </tr>
    </table>
    <input type="file" ref="file" id="file" @change="handleFileUpload">
    <button @click="submitForm">Submit</button>
    <button @click="confirmForm">Confirm</button>
  </div>
</template>

<script>
  export default {
    name: "CreateForm",
    data() {
      return {
        file: undefined,
        entries: []
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
        this.file = this.$refs.file.files[0];
      },
      confirmForm(){
        //TODO send to confirm one to server
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