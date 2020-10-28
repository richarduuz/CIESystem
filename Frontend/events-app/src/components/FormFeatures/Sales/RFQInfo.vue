<template>
  <div>
    <button @click="test">RFQinfo</button>
    <modal name="test-modal" :scrollable="true" :height="'auto'">
      <div v-for="(item, index) in Info2Modal" :key="index">
        <div v-for="(value, key) in item" v-show="key !== '最优报价？'" :key="key">
          <label>{{key}}: </label>
          <span>{{value}}</span>
        </div>
        <br>
      </div>
    </modal>
    <div class="CardContainer">
      <div v-for="(item, index) in RFQBestResponse" :key="index">
        <RFQCard :rfq-best="item" :rfq-all="RFQResponse[index]" @showModal="feedInfo2Modal"></RFQCard>
      </div>
    </div>
  </div>
</template>

<script>
  import RFQCard from './RFQCard'

  export default {
    name: "RFQInfo",
    props: {
      RFQResponse: {
        type: Array,
        default() {
          return []
        }
      },
      RFQBestResponse: {
        type: Array,
        default() {
          return []
        }
      }
    },
    methods: {
      test() {
        console.log(this.showInfoModal);
      },
      feedInfo2Modal(rfqAll){
        this.Info2Modal = []
        for(let item of rfqAll){
          this.Info2Modal.push(item)
        }
        this.$modal.show('test-modal')
      }
    },
    data() {
      return {
        showInfoModal: false,
        Info2Modal: []
      }
    },
    components:{
      RFQCard,
    }
  }
</script>

<style scoped>
  .CardContainer{
    height: 100%;
    width: 100%;
    display: flex;
  }
  .InfoModal{
    display: none; /* Hidden by default */
    position: absolute; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top: 100px; /* Location of the box */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
  }
  .InfoModalContent{
    background-color: #fefefe;
    margin: auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
  }
  .close:hover,
  .close:focus{
      color: #000;
  text-decoration: none;
  cursor: pointer;
  }
</style>