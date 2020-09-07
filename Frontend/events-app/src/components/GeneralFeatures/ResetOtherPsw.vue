<template>
  <div>
    <div>
      <label><b>Input the username</b></label>
      <input type="text" placeholder="username" v-model="username" required>
      <br>
      <label><b>Input your new password</b></label>
      <input type="password" placeholder="new password" v-model.lazy="newPassword" required>
      <br>
      <label><b>Confirm your new password</b></label>
      <input type="password" placeholder="new password" v-model.lazy="confirmNP" required>
      <br>
      <button @click="resetPassword" :disabled="!(newPassword === confirmNP) || newPassword.length === 0">reset password</button>
      <br>
      <label v-show="newPassword !== confirmNP && confirmNP.length !== 0"><b>The second password doesn't match the first one!</b></label>
    </div>
  </div>
</template>

<script>
  export default {
    name: "ResetOtherPsw",
    data() {
      return {
        isShowForm: false,
        username: "",
        newPassword: "",
        confirmNP: ""
      }
    },
    methods: {
      resetPassword(){
        let url = this.$store.state.url + "/resetOtherPSW";
        let postData = {'username': this.username, 'password': this.newPassword};
        postData = JSON.stringify(postData);
        this.$http.post(url, postData, {emulateJSON: true})
          .then(response => response.json())
          .then(data => {
            if(data){
              let result = data['result'];
              if (result === 'Okay'){
                alert('Reset successfully')
              } else {
                alert('Reset failed')
              }
            }
          })
      },
      showForm() {
        this.isShowForm = ! this.isShowForm
  }
    }
  }
</script>

<style scoped>

</style>