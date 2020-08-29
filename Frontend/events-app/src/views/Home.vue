<template>
<div class="home">
  <section class="hero">
    <div class="hero-body">
      <div class="container">
        <h1 class="title">
          Welcome to the CIE Quotation and RFQ database
        </h1>
        <div id="nav">
        <router-link to="/login">Go to login</router-link>
        </div>
      </div>
    </div>
  </section>
</div>
</template>
<script>
export default {
  name: 'home',
  components: {
  }
}
</script>
<style lang="scss" scoped>.hero{
  text-align: center;
  background-size: cover;
  background-position: center;
  height: 400px;
}
.button{
  color: #42b983;
  font-weight:  bold;
}
</style>
