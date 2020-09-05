<template>
  <div>
    <label><b>Input your old password</b></label>
    <input type="password" placeholder="old password" v-model="formerPassword" required>
    <br>
    <button @click="checkPassword">check old password</button>
    <br>
    <div v-show="isRightPassword">
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
      name: "ResetPsw",
      data() {
        return {
          formerPassword: '',
          isRightPassword: false,
          newPassword: '',
          confirmNP: '',
        }
      },
      props: {
      },
      methods: {
        resetPassword(){
          //TODO change password
          let postData = {'userId': this.$store.state.userId, 'password': this.newPassword};
          postData = JSON.stringify(postData);
          this.$http.post('http://127.0.0.1:4000/resetPSW', postData, {emulateJSON: true})
            .then(response => response.json())
            .then(data => {
              if (data){
                let result = data['result'];
                if (result === 'Okay'){ alert('reset finished') }
                else { alert('reset failed')}
              }
            })
        },
        checkPassword(){
          let postData = {'userId': this.$store.state.userId, 'password': this.formerPassword};
          postData = JSON.stringify(postData);
          this.$http.post('http://127.0.0.1:4000/authPSW',postData, {emulateJSON: true})
            .then(response => response.json())
            .then(data => {
              if(data){
                let result = data['result'];
                if (result === 'Okay') {this.isRightPassword = true}
                else {alert('Old Password Wrong!')}
              }
            })
        }
      }
    }
</script>

<style scoped>

</style>