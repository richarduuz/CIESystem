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
        <br>
        <div class="userFormFeatures">
            <ul>
                <li>
                    <router-link :to="'/homepage/' + $store.state.username + '/form_history'">My Form History</router-link>
                </li>
                <li>
                    <router-link :to="'/homepage/' + $store.state.username + '/create_form'">Create A New Form</router-link>
                </li>
            </ul>
        </div>
        <router-view/>
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
            },
            showSubMyForms(){

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

    div.userFormFeatures{
        text-align: left;
    }

    ul{
        list-style-type: none;
        margin: 0;
        padding: 0;
        width: 200px;
        background-color: #f1f1f1;
    }

    li a {
        display: block;
        color: #000;
        padding: 8px 16px;
        text-decoration: none;
    }
    li a:hover {
        background-color: #555;
        color: white;
    }
</style>