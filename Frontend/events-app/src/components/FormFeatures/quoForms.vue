<template>
  <div class="FormDiv">
      <table class="Form">
        <thead>
          <tr class="attributes">
            <th v-for="attribute in $store.getters.displayAttributes" :key="attribute">{{attribute}}</th>
            <slot name="isImportant"></slot>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(entry, index) in displayEntries" :key="index">
            <td v-for="(value, subIndex) in $store.getters.displayAttributes" :key="subIndex">
              <input :class="{FormInput: formInputClassActive($store.getters.displayAttributes[subIndex])}"
                     v-model="displayEntries[index][subIndex]"
                     :disabled="formInputClassActive($store.getters.displayAttributes[subIndex])"
                      @change="displayValueChanged([index, subIndex, $event.target.value])">
            </td>
            <td>
              <slot :data="index"></slot>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
</template>

<script>
  import {getDisplayAttributeIndex} from '../../functions/functions'

  export default {
    name: "quoForms",
    props:['displayEntries'],
    methods: {
      formInputClassActive(item){
        return this.$store.state.systemAttributes.includes(item) || this.$store.getters.uneditableAttributes.includes(item)
      },
      displayValueChanged(value){
        this.$emit("formValueChanged", value);
        if (this.$store.getters.displayAttributes.includes("quoId")){
          let index = getDisplayAttributeIndex("quoId", this.$store.getters.displayAttributes);
          value[0] = this.displayEntries[value[0]][index];
          this.$emit("formValueChangedId", value);
        }
        //TODO emit the quoId
      }
    }
  }
</script>

<style scoped>
  .FormDiv {

    position: absolute;
    overflow-x: auto;
    height: 250px;
    width: 80%;
    right: 20px;
    border: 1px solid black;

  }
.Form table, th, td {
  border: 1px solid black;

}
  th {
    max-width: 100%;
    white-space: nowrap;
  }
  .FormInput {
    max-width: 100%;
    white-space: nowrap;
    background-color: #d3d3d3;
  }

  th{
    position: sticky;
    top: 0;
    background-color: white;
  }

</style>