<template>
  <div>
    <button @click="test">Pending</button>
    <div v-if="Object.keys(displayEntries).length !== 0">
      <quo-forms :displayEntries="Object.values(displayEntries)" :quo-id-index="quoIdIndex">
        <th slot="isImportant">查看详情</th>
        <template slot-scope="slot">
          <button @click="showRFQInfo(slot.data['quoId'])">查看</button>
        </template>
      </quo-forms>
      <form-rows :rows="Object.keys(displayEntries).length"></form-rows>
    </div>
    <h2 v-else>目前没有请求的报价单</h2>
    <div class="rfq">
      <RFQInfo :r-f-q-response="rfqSpecificResponse" :r-f-q-best-response="rfqBestResponse"></RFQInfo>
    </div>
  </div>
</template>

<script>
  import {exportDisplayForm} from "../../../functions/functions";
  import quoForms from '../quoForms';
  import FormRows from '../FormRows';
  import RFQInfo from './RFQInfo';


  export default {
    name: "PendingForms",
    asyncComputed: {
      displayEntries: {
        get(){
          let url = this.$store.state.url + '/pendingForms/' + this.$store.state.userId;
          return this.$http.get(url)
            .then(response => response.json())
            .then(data => this.processingData(data))
            .catch(e => alert(e.status))
        },
        default: {}
      }
    },
    methods:{
      test(){
        console.log(Object.keys(this.displayEntries).length);
      },
      showRFQInfo(quoId){
        this.rfqSpecificResponse = [];
        for (let item of this.rfqWholeResponse){
          if(item['quoId'] === quoId){
            item['回复内容']['采购'] = item['采购'];
            this.rfqSpecificResponse.push(item['回复内容'])
          }
        }
        for (let items of this.rfqSpecificResponse){
          for (let item of items){
            if(item['最优报价？'] === true){
              item['采购'] = items['采购']
              this.rfqBestResponse.push(item)
              break
            }
          }
        }
      },
      processingData(data){
        this.displayEntries = {};
        let result = {};
        this.exportWholeForm(data);
        for (let item of data['body']['quo_result']){
          this.quoIdIndex.push(item['quoId'])
        }
        for (let item of data['body']['rfq_result']){
          this.rfqWholeResponse.push(item)
        }
        console.log(this.rfqWholeResponse);

        let tmp = exportDisplayForm(data['body']['quo_result'], this.$store.getters.displayAttributes);
        // for (let i = 0; i<tmp.length; i++){
        //   result[this.wholeForms[i]['quoId']] = tmp[i]
        // }
        for (let i = 0; i < tmp.length; i++){
          result[this.quoIdIndex[i]] = tmp[i]
        }
        return result
      },
       exportWholeForm(data){
        this.wholeForms = data['body']
      },
    },
    data() {
      return {
        wholeForms: [],
        quoIdIndex: [],
        rfqWholeResponse: [],
        rfqSpecificResponse: [],
        rfqBestResponse: []
      }
    },
    components: {
      quoForms,
      FormRows,
      RFQInfo
    }
  }
</script>

<style scoped>
  div.rfq{
    position: absolute;
    right: 20px;
    top: 68%;
    width: 80%;
    height: 250px;
    border: 1px solid blue;
    overflow-y: auto;
  }
</style>