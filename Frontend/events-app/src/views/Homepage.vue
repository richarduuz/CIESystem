<template>
    <div v-if="$store.state.userId.length === 0">
        <h2>Please Login first</h2>
    </div>
    <div v-else class="homepage">
        <h2>欢迎来到主页{{$store.state.username}}</h2>
        <h2>{{$store.state.userTitle}}</h2>
        <br>
            <section>
                <div class="userFormFeatures">
                    <ul>
                        <div v-if="$store.state.userTitle === 'Buyer'">
                            <li><router-link :to="'/homepage/' + $store.state.username + '/uncompleted_forms'">Uncompleted Forms</router-link></li>
                        </div>
                        <div v-if="$store.state.userTitle === 'Sales'">
                            <li><router-link :to="'/homepage/' + $store.state.username + '/completed_forms'">Completed Forms</router-link></li>
                            <li><router-link :to="'/homepage/' + $store.state.username + '/pending_forms'">Pending Forms</router-link></li>
                            <li><router-link :to="'/homepage/' + $store.state.username + '/concerned_forms'">Concerned Forms</router-link></li>
                            <li><router-link :to="'/homepage/' + $store.state.username + '/create_form'">Create A New Form</router-link></li>
                        </div>
                        <li><router-link :to="'/homepage/' + $store.state.username + '/reset_my_password'">Reset My Password</router-link></li>
                        <div v-if="$store.state.userTitle === 'admin'">
                            <li><router-link :to="'/homepage/' + $store.state.username + '/reset_other_password'">Reset Other Password</router-link></li>
                            <li><router-link :to="'/homepage/' + $store.state.username + '/create_account'">Create New Account</router-link></li>
                            <li><router-link :to="'/homepage/' + $store.state.username + '/delete_account'">Delete An Account</router-link></li>
                        </div>
                    </ul>
                </div>
            </section>
        <router-view/>
    </div>
</template>

<script>
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
        }
    }
</script>

<style scoped>

    div.userFormFeatures{
        position: absolute;
        z-index: 906;
        top: 200px;
        left: 20px;
        float: left;
        padding: 7px;
        /*position: fixed;*/
        /*right: revert;*/
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

    div.homepage{
        /*background-color: #dfdfdf;*/
    }
</style>