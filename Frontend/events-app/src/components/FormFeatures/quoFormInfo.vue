<template>
  <div class="quoFormInfo">
    I am from info
    <button @click="test"></button>
    <div>
      <div>
        <div class="quoFormInfoTitle">
          <label>QuoId: {{selectedEntry}}</label>
          <br>
        </div>
        <div class="subQuoFormInfo" v-for="(item, index) in RFQResponse" :key="index">
          <button v-show="index !== 0" class="removeBtn" @click="removeRFQResponseEntry(index)">删除</button>
          <div v-for="(value, key) in item" :key="key">
            {{key+ ': '}}
            <input v-model="RFQResponse[index][key]"></input>
          </div>
          <br>
        </div>
      </div>
      <div>
        <button @click="addRFQResponseEntry">增加报价</button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "quoFormInfo",
    props: {
      selectedEntry: {
        type: String
      }
    },
    watch: {
      selectedEntry: function(val) {
        if (val !== undefined){
          this.selectedEntry = val;
        }
      }
    },
    methods: {
      test() {
        console.log(this.selectedEntry)
      },
      addRFQResponseEntry() {
        this.RFQResponse.push(this.$store.state.RFQTemplate)
      },
      removeRFQResponseEntry(index) {
        this.RFQResponse.splice(index, 1)
      }
    },
    data() {
      return {
        RFQResponse: [this.$store.state.RFQTemplate]
      }
    },
  }
</script>

<style scoped>
  .quoFormInfo{
    position: absolute;
    right: 20px;
    top: 68%;
    width: 80%;
    height: 250px;
    border: 1px solid blue;
    overflow-y: auto;
  }
  .quoFormInfoTitle{
    text-align: center;
  }

  .subQuoFormInfo{
    background-color: #f1f1f1;
  }

  .removeBtn{
    position: relative;
    top: 85px;
    right: -200px;
  }
</style>