import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userId: "",
    username: "",
    userTitle: "",
    url: "http://127.0.0.1:4000",
    quotationAttributes: ["询价日期", "要求回复日期", "实际回复日期", "销售", "接单率", "客户要求时间", "客户", "品牌", "型号",
      "数量", "TP", "官网价格$", "历史报价", "成本", "建议报价", "报价", "参考金额", "供应商", "交期", "SPQ", "MOQ", "采购", "目前状态", "quoId"],
    systemAttributes: ["询价日期", "实际回复日期", "quoId" ,"销售", "采购", "目前状态"]
  },
  mutations: {
    setUserId(state, userId){
      state.userId = userId
    },
    setUsername(state, username){
      state.username = username
    },
    setUserTitle(state, userTitle){
      state.userTitle = userTitle
    }
  },
  actions: {

  },
  getters: {
    displayAttributes(state) {
      if (state.userTitle === 'Sales')
      {
        return ["询价日期", "要求回复日期", "实际回复日期", "接单率", "客户要求时间", "客户", "品牌", "型号",
      "数量", "TP", "官网价格$", "历史报价", "成本", "建议报价", "报价", "参考金额", "交期", "SPQ", "MOQ", "目前状态", "quoId"]
      } else if (state.userTitle === 'Buyer'){
        return ["询价日期", "要求回复日期", "实际回复日期", "接单率", "客户要求时间", "客户", "品牌", "型号",
      "数量", "TP", "官网价格$", "历史报价", "成本", "建议报价", "报价", "参考金额", "供应商", "交期", "SPQ", "MOQ", "采购", "目前状态", "quoId"]
      }
      //TODO add if title is admin
    },
    aDisplayAttributes(state, getters) {
      return state.quotationAttributes.filter(attribute => {
        return getters.displayAttributes.indexOf(attribute) === -1;
      })
    },
    uneditableAttributes(state){
      if (state.userTitle === 'Sales'){
        return ["成本", "建议报价", "报价", "参考金额", "交期"]
      } else if (state.userTitle === 'Buyer'){
        return ["接单率","客户要求时间","客户","品牌","型号","数量","TP","历史报价" ,"SPQ" ,"MOQ"]
      }
    }
  }
})

