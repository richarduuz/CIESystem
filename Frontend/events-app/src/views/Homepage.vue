<template>
    <div>
        <h2>This is the homepage</h2>
        <h2>{{userId}}</h2>
        <h2>{{username}}</h2>
        <br>
        <create-account v-if="userTitle=='admin'"></create-account>
        <br>
        <reset-psw :username="username" :userId="userId"></reset-psw>
    </div>
</template>

<script>
    import CreateAccount from '../views/CreateAccount'
    import ResetPsw from '../views/ResetPsw'
    export default {
        name: "Homepage",
        data() {
            return {
                isShowForm: false,
                isShow: false,
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
        methods: {},
        components: {
            CreateAccount,
            ResetPsw
        }
    }
</script>

<style scoped>

</style>