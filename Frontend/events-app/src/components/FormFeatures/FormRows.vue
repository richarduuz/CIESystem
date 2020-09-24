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
        default: 0
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