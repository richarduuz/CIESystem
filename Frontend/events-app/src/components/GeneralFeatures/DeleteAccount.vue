<template>
  <div>
    <div>
      <label><b>Input the username</b></label>
      <input type="text" placeholder="Username" v-model.lazy="username" required>
      <br>
      <button @click="deleteAccount" :disabled="username.length === 0">Delete</button>
    </div>
  </div>
</template>

<script>
  export default {
    name: "DeleteAccount",
    data() {
      return {
        isShowForm: false,
        username: ""
      }
    },
    methods: {
      showForm(){
        this.isShowForm = ! this.isShowForm
      },
      deleteAccount(){
        if(confirm("You are going to delete a user account!")){
          let postData = {'username': this.username};
          let url = this.$store.state.url + "/deleteAccount";
          postData = JSON.stringify(postData);
          this.$http.post(url, postData, {emulateJSON: true})
            .then(response => response.json())
            .then(data => {
              if (data) {
                let result = data['result'];
                if (result === 'Okay'){
                  alert('Delete successfully')
                } else {
                  alert('Fail to delete\n' + data['reason'])
                }
              }
            })
            .catch(e => alert(e.status));
        }
      }
    }
  }
</script>

<style scoped>

</style>