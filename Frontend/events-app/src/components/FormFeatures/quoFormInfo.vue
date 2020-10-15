<template>
  <div class="quoFormInfo" v-show="selectedEntry.length > 0">
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
          <div v-for="(value, key) in item" :key="key" v-show="key !== '最优报价？'">
            {{key+ ': '}}
            <input v-model="RFQResponse[index][key]"></input>
          </div>
          <br>
        </div>
        <div class="bestResponse">
          <div>选择一个报价作为最优报价</div>
          <select  v-model="bestIndex" required style="width: 60px">
            <option v-for="(value, index) in RFQResponse" :key="index" :value="index">{{'第' + (index + 1) + '个'}}</option>
          </select>
        </div>
      </div>
      <div>
        <button @click="addRFQResponseEntry">增加报价</button>
        <button @click="submitRFQResponse" :disabled="RFQResponse.length === 0 || bestIndex === -1">提交报价</button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "quoFormInfo",
    props: {
      selectedEntry: {
        type: String,
        default: ""
      },
    },
    watch: {
      selectedEntry: function(val) {
        this.RFQResponse = [];
        this.bestIndex = -1;
        // if (val !== undefined){
        //   this.selectedEntry = val;
        // }
        for (let i of this.$parent.displayRFQ){
          if (i['quoId'] === val){
            let tmp = i['回复内容'];
            for (let j =0; j< tmp.length; j++){
              this.RFQResponse.push(tmp[j]);
              if (tmp[j]['最优报价？'] === true){
                this.bestIndex = j
              }
            }
          }
        }
      }
    },
    methods: {
      update(){},

      test() {
        console.log(this.RFQResponse)
      },
      addRFQResponseEntry() {
        this.RFQResponse.push(Object.assign({}, this.$store.state.RFQTemplate))
      },
      removeRFQResponseEntry(index) {
        this.RFQResponse.splice(index, 1)
      },
      submitRFQResponse(){
        let url = this.$store.state.url + "/confirmRFQ";
        let postData = {"userId": this.$store.state.userId, "username": this.$store.state.username,
            "userTitle": this.$store.state.userTitle,};
        this.setBestResponse();
        postData['quoId'] = this.selectedEntry;
        postData['body'] = this.RFQResponse;
        postData = JSON.stringify(postData);
        this.$http.post(url, postData, {emulateJSON: true})
          .then(res => res.json())
          .then(data => {
            if (data['status'] === 'Okay'){
              alert(data['message']);
              // this.selectedEntry = "";
              this.RFQResponse = [];
              this.$emit("selectedEntryClear", this.selectedEntry);
            }
          })
          .catch(() => alert("error"));
        console.log(postData)
      },

      //-------Inner methods------
      setBestResponse(){
        for(let i = 0; i < this.RFQResponse.length; i++){
          if (i !== this.bestIndex){
            this.RFQResponse[i]['最优报价？'] = false
          } else {
            this.RFQResponse[i]['最优报价？'] = true
          }
        }
      },
      goToCurrentPage(){
         let path = '/homepage/' + this.$store.state.username + '/uncompleted_forms';
                this.$router.push({
                    path
                })
      }
    },
    data() {
      return {
        RFQResponse: [],
        bestIndex: -1
      }
    }
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
    position: relative;
  }

  .removeBtn{
    position: absolute;
    top: 45%;
    left: 75%;
  }

  .bestResponse {
    position: absolute;
    top: 50%;
    left: 15%;
  }



</style>