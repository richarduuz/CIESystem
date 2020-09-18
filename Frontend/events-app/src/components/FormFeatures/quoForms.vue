<template>
  <div class="FormDiv">
      <table class="Form">
        <tr>
          <th v-for="attribute in $store.getters.displayAttributes" :key="attribute">{{attribute}}</th>
          <slot name="isImportant"></slot>
        </tr>
        <tr v-for="(entry, index) in displayEntries" :key="index">
          <th v-for="(value, subIndex) in $store.getters.displayAttributes" :key="subIndex">
            <input :class="{FormInput: formInputClassActive($store.getters.displayAttributes[subIndex])}"
                   v-model="displayEntries[index][subIndex]"
                   :disabled="formInputClassActive($store.getters.displayAttributes[subIndex])"
                    @change="displayValueChanged([index, subIndex, $event.target.value])">
          </th>
          <th>
            <slot :data="index"></slot>
          </th>
        </tr>
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
        return this.$store.getters.systemAttributes.includes(item)
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
    overflow-x: auto;
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

</style>