<template>
    <div>
        <button @click="showForm">Create a user teammate account</button>
        <div class="login_input" v-show="isShowForm">
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
                //TODO http request create account
                let postData = {'username': this.createUsername, 'password': this.createPassword, 'title': this.createTitle};
                postData = JSON.stringify(postData);
                this.$http.post('http://127.0.0.1:4000/signup', postData, {emulateJSON: true})
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
            }
        }
    }
</script>

<style scoped>

</style>