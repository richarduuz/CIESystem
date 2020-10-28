import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userId: "",
    username: "",
    userTitle: "",
    url: "http://127.0.0.1:4000",
    quotationAttributes: ["销售","询价日期","紧急程度", "实际回复日期", "接单率", "客户交期", "客户","客户人名", "品牌", "型号",
      "单次数量", "年用量", "TP", "官网价格$", "历史成本", "曾报价", "SPQ", "销售状态", "quoId"],
    systemAttributes: ["销售", "询价日期", "实际回复日期", "销售状态"],
    RFQTemplate: {"现成本": "", "建议报价": "", "采购说明": "", "净成本": "", "劳务费用": "", "供应商": "", "交期": ""},

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
        return ["销售","询价日期","紧急程度", "实际回复日期", "接单率", "客户交期", "客户","客户人名", "品牌", "型号",
      "单次数量", "年用量", "TP", "官网价格$", "历史成本", "曾报价", "SPQ", "销售状态", "quoId"]
      } else if (state.userTitle === 'Buyer'){
        return ["询价日期", "紧急程度", "销售", "接单率", "客户交期", "采购交期", "客户", "品牌", "型号",
      "单次数量", "TP", "官网价格$", "历史报价", "交期", "SPQ", "MOQ","quoId"]
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
        return ["接单率","客户要求时间","客户","品牌","型号","数量","TP","历史报价" ,"SPQ" ,"MOQ", "紧急程度", "客户交期",
          "采购交期", "单次数量", "官网价格$", "交期", "quoId"]
      }
    }
  }
})

