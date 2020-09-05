<template>
    <div v-if="$store.state.userId.length === 0">
        <h2>Please Login first</h2>
    </div>
    <div v-else>
        <h2>This is the homepage</h2>
        <h2>{{$store.state.userId}}</h2>
        <h2>{{$store.state.username}}</h2>
        <br>
        <div class="userFeatures">
            <create-account v-if="$store.state.userTitle === 'admin'"></create-account>
            <reset-other-psw v-if="$store.state.userTitle === 'admin'"></reset-other-psw>
            <delete-account v-if="$store.state.userTitle === 'admin'"></delete-account>
            <button @click="showForm">I want to reset my password</button>
            <reset-psw v-show="isShowForm"></reset-psw>
        </div>
    </div>
</template>

<script>
    import CreateAccount from '../components/GeneralFeatures/CreateAccount'
    import ResetPsw from '../components/GeneralFeatures/ResetPsw'
    import ResetOtherPsw from '../components/GeneralFeatures/ResetOtherPsw'
    import DeleteAccount from '../components/GeneralFeatures/DeleteAccount'
    export default {
        name: "Homepage",
        data() {
            return {
                isShowForm: false
            }
        },
        computed: {
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
.userFeatures{
    text-align: left;
}


</style>