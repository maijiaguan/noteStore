import axios from 'axios'
// import router from '../router'
// import store from '../vuex/store'
// import * as types from '../vuex/mutation_types'
// import {Loading} from 'element-ui'

// 默认超时时间
axios.defaults.timeout = 50000

// 相对路径设置
axios.defaults.baseURL = 'http://127.0.0.1:8000'

// let loading

// // 开始加载
// function startLoading () {
//   loading = Loading.service({
//     lock: true,
//     text: '加载中...',
//     background: 'rgba(0, 0, 0, 0.2)'
//   })
// }

// // 结束加载
// function endLoading () {
//   loading.close()
// }

// let needLoadingRequestCount = 0

// export function showFullScreenLoading () {
//   if (needLoadingRequestCount === 0) {
//     startLoading()
//   }
//   needLoadingRequestCount++
// }

// export function tryHideFullScreenLoading () {
//   if (needLoadingRequestCount <= 0) return
//   needLoadingRequestCount--
//   if (needLoadingRequestCount === 0) {
//     endLoading()
//   }
// }

// // get方法
// export function get (url, params) {
//   return axios({
//     method: 'get',
//     url,
//     params,
//     headers: {
//       'Authorization': 'Bearer ' + this.$cookies.get('access')
//     }
//   })
// }

// export function post (url, data) {
//   return axios({
//     method: 'post',
//     url,
//     data,
//     headers: {
//       'Authorization': 'Bearer ' + this.$cookies.get('access')
//     }
//   })
// }

export default axios
