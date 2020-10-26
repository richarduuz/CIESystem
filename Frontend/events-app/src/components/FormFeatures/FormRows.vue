<template>
  <div class="formRows">
    <h2>表格一共有{{rows}}行</h2>
  </div>
</template>

<script>
  export default {
    name: "FormRows",
    props: {
      rows: {
        type: Number,
        default: 100
      }
    },
    watch: {
      rows: (newValue) => {
        console.log("watch here");
        this.rows = newValue;
      }
    },
    methods: {
      test() {
        console.log(this.rows);
      }
    }
  }
</script>

<style scoped>
div.formRows{
  position: absolute;
  top: 460px;
  right: 10%;
}
</style>