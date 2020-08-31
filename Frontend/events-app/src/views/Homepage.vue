<template>
    <div v-if="typeof(userId) === 'undefined'">
        <h2>Please Login first</h2>
    </div>
    <div v-else>
        <h2>This is the homepage</h2>
        <h2>{{userId}}</h2>
        <h2>{{username}}</h2>
        <br>
        <create-account v-if="userTitle === 'admin'"></create-account>
        <br>
        <reset-other-psw v-if="userTitle === 'admin'"></reset-other-psw>
        <br>
        <delete-account v-if="userTitle === 'admin'"></delete-account>
        <br>
        <button @click="showForm">I want to reset my password</button>
        <reset-psw v-show="isShowForm" :username="username" :userId="userId"></reset-psw>
    </div>
</template>

<script>
    import CreateAccount from '../views/CreateAccount'
    import ResetPsw from '../views/ResetPsw'
    import ResetOtherPsw from '../views/ResetOtherPsw'
    import DeleteAccount from '../views/DeleteAccount'
    export default {
        name: "Homepage",
        data() {
            return {
                isShowForm: false
            }
        },
        computed: {
            userId() {
                return this.$route.query['userId']
            },
            username() {
                return this.$route.query['username']
            },
            userTitle() {
                return this.$route.query['userTitle']
            }
        },
        methods: {
            showForm(){
                this.isShowForm = ! this.isShowForm
            }
        },
        components: {
            CreateAccount,
            ResetPsw,
            ResetOtherPsw,
            DeleteAccount
        }
    }
</script>

<style scoped>

</style>