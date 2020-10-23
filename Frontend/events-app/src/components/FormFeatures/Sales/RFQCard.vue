<template>
  <div>
    <button @click="test">RFQCard</button>
    <div class="card">
      <div v-for="(value, key) in rfq" v-show="key !== '最优报价？'" :key="key">
        <label>{{key}}: </label>
        <span>{{value}}</span>
      </div>
      <label>采购: </label>
      <span>{{buyer}}</span>
    </div>
  </div>
</template>

<script>
  export default {
    name: "RFQCard",
    methods: {
      test(){
        console.log(this.buyer);
      }
    },
    props: {
      rfq: {
        type: Object,
        default(){return {}}
      },
      buyer: {
        type: String,
        default: ""
      }
    }
  }
</script>

<style scoped>
  .container {
  padding: 2px 16px;
}
  .card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 40%;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
</style>