<template>
  <div>
    I am create Form
    <br>
    <table class="Form">
      <tr>
        <th>询价日期</th>
        <th>要求回复日期</th>
        <th>实际回复日期</th>
        <th>销售</th>
        <th>接单率</th>
        <th>客户要求时间</th>
        <th>客户</th>
        <th>品牌</th>
        <th>型号</th>
        <th>数量</th>
        <th>TP</th>
        <th>官网价格</th>
        <th>历史报价</th>
        <th>成本</th>
        <th>建议报价</th>
        <th>报价</th>
        <th>参考金额</th>
        <th>交期</th>
        <th>SPQ</th>
        <th>MOQ</th>
        <th>采购</th>
        <th>目前状态</th>
      </tr>
      <tr v-for="(entry, index) in entries" :key="index">
        <th v-for="(value, key) in entry" :key="key">{{value}}</th>
      </tr>

    </table>
    <input type="file" ref="file" id="file" @change="handleFileUpload">
    <button @click="submitForm">Submit</button>
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
        let form = new FormData();
        form.append('Quotation', this.file);
        this.$http.post('http://127.0.0.1:4000/extractQuotation', form, {headers: {'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}})
          .then(response => response.json())
          .then(data => {
            for(let item of data) {
              this.entries.push(item);
            }
          })
      },
      handleFileUpload(){
        this.file = this.$refs.file.files[0];
        console.log(typeof(this.file));
      }
    },

  }
</script>

<style scoped>
.Form table, th, td {
  border: 1px solid black;
}
</style>