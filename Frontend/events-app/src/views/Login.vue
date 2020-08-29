<template>
    <div class="login">
        <div class="login_input">
        <label><b>Username:</b></label>
        <input type="text" placeholder="Enter Username" ref="uname" required>
        <br>

        <label><b>Password:</b></label>
        <input type="password" placeholder="Enter your password" ref="psw" required>
        <br>
        </div>
        <div class="login_button">
        <button type="button" @click="submit">Login</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                username: "",
                psw: "",
                userId: "",
                userTitle: ""
            }
        },
        methods: {
            submit() {
                // alert("button test")
                this.username = this.$refs.uname.value;
                this.psw = this.$refs.psw.value;
                var postData = {"username": this.username, "password": this.psw};
                postData = JSON.stringify(postData);
                this.$http.post('http://127.0.0.1:4000/login', postData, {emulateJSON: true})
                    .then(response=>response.json())
                    .then(data=>{
                        if (data){
                            var result = data['result'];
                            console.log(result);
                            if (result === 'Okay'){
                                this.userId = data['userid'];
                                this.userTitle = data['userTitle']
                                console.log('go to homepage');
                                console.log('user is',this.username, this.userId);
                                this.toHomepage();
                            }
                            else if (result === 'False'){
                                alert('Wrong password or user not exists')
                            }
                            else if (result === 'error'){
                                alert('Internal error')
                            }
                        }
                    })
            },
            toHomepage(){
                this.$router.push({
                    path: '/homepage',
                    query: {
                        username: this.username,
                        userId: this.userId,
                        userTitle: this.userTitle
                    }
                })
            }
        },
        components: {
        }
    }
</script>

<style scoped>.login{
    text-align: center;
}.login_input {
    text-align: match-parent;
}

</style>