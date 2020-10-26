<template>
  <div>
    <button @click="test">RFQCard</button>
    <div class="card">
      <div v-for="(value, key) in rfqBest" v-show="key !== '最优报价？'" :key="key">
        <label>{{key}}: </label>
        <span>{{value}}</span>
      </div>
    </div>
    <button @click="$emit('showModal', rfqAll)">查看所有报价</button>
  </div>
</template>

<script>
  export default {
    name: "RFQCard",
    methods: {
      test(){
        console.log(this.rfqAll);
      }
    },
    props: {
      rfqBest: {
        type: Object,
        default(){return {}}
      },
      rfqAll: {
        type: Array,
        default(){return {}}
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
  width: 200px;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
</style>