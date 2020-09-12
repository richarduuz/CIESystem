<template>
    <div>
        <div class="login_input">
            <label><b>Username:</b></label>
            <input type="text" placeholder="Enter Username" v-model="createUsername" required>
            <br>
            <label><b>Password:</b></label>
            <input type="password" placeholder="Enter your password" v-model="createPassword" required>
            <br>
            <label><b>Title:</b></label>
            <select v-model="createTitle" required>
                <option value="Sales">Sales</option>
                <option value="Buyer">Buyer</option>
            </select>
            <br>
            <div class="login_button">
                <button type="button" @click="createAccount" :disabled="!btnDisabled">Create account</button>
                </div>
            </div>
    </div>
</template>

<script>
    export default {
        name: "CreateAccount",
        computed:{
            btnDisabled() {
                if (this.createUsername.length * this.createPassword.length * this.createTitle.length !== 0){
                    return true
                } else {return false}
            }
        },
        data() {
            return {
                isShowForm: false,
                createTitle: '',
                createUsername: '',
                createPassword: ''
            }
        },
        methods: {
            showForm(){
                this.isShowForm = ! this.isShowForm
            },
            createAccount(){
                let url = this.$store.state.url + '/signup';
                let postData = {'username': this.createUsername, 'password': this.createPassword, 'title': this.createTitle};
                postData = JSON.stringify(postData);
                this.$http.post(url, postData, {emulateJSON: true})
                    .then(response => response.json())
                    .then(data => {
                        if(data){
                            let result = data['result'];
                            if (result === 'Okay'){
                                alert('create successfully')
                            } else {
                                alert('fail to create\n' + data['reason']);
                            }
                        }
                    })
                    .catch(e => alert(e.status))
            }
        }
    }
</script>

<style scoped>

</style>