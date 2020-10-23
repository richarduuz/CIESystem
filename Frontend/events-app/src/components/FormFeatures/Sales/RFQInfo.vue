<template>
  <div>
    <h2>I am the RFQInfo</h2>
    <button @click="test">RFQinfo</button>
    <div v-for="(item, index) in RFQResponse" :key="index">
      <RFQCard :rfq="item[0]" :buyer="item['采购']"></RFQCard>
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
      }
    },
    methods: {
      test() {
        console.log(this.RFQResponse[0]['采购']);
      }
    },
    components:{
      RFQCard
    }
  }
</script>

<style scoped>

</style>