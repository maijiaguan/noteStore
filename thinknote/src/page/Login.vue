<template>
  <div class="note-container">
    <div class="formbar">
      <div class="form-box">
        <input v-model="mobile" class="form-input" type="text" name="mobile" autocomplete="off" @change="onChange1" maxlength="11">
        <span class="form-label" :class="{'form-input-end-label': isActive1}">
          手机号
          <i v-if="(11 && /^((13|14|15|16|17|18|19)\d{9})$/).test(mobile)" class="el-icon-circle-check"></i>
          <i v-else-if="(11 && /^(([^1]{1}[3-9]{1}|[1]{1}[^3-9]{1})\d{9})$/).test(mobile)" class="el-icon-circle-close"></i>
        </span>s
        <el-button round class="phone-btn" :disabled="disabled1" @click="authMobile">{{codebtn}}</el-button>
      </div>

      <div class="form-box">
        <input v-model="code" class="form-input" :disabled="disabled2" type="text" name="mobile" autocomplete="off" @change="onChange2" maxlength="6">
        <span class="form-label" :class="{'form-input-end-label': isActive2}">验证码</span>
      </div>

      <button class="btn" @click="loginInfo">
        <span class="btn-word">登录</span>
      </button>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
export default {
  name: 'Register',
  data () {
    return {
      isActive1: false,
      isActive2: false,
      disabled1: false,
      disabled2: true,
      time: 0,
      codebtn: '获取验证码',
      mobile: '',
      code: '',
      msg: '123'
    }
  },
  methods: {
    onChange1 (e) {
      // 检查是否输入，更该提示span标签样式
      const { value } = e.target
      if (value === null || value === undefined || value === '') {
        // console.log("没检测到变化");
        this.isActive1 = false
      } else {
        // console.log("检测到变化"+value);
        this.isActive1 = true
      }
    },
    onChange2 (e) {
      const { value } = e.target
      if (value === null || value === undefined || value === '') {
        this.isActive2 = false
      } else {
        this.isActive2 = true
      }
    },
    getCode () {
      var apicode = 'http://127.0.0.1:8000/api/sendcode/'
      Axios.get(apicode, {
        params: {
          mobile: this.mobile
        }
      })
    },
    goLogin () {
      // 提交登录信息
      var apilogin = 'http://127.0.0.1:8000/api/login/'
      Axios({
        method: 'post',
        url: apilogin,
        data: {
          username: this.mobile,
          password: this.code
        },
        transformRequest: [
          function (data) {
            let ret = ''
            for (let it in data) {
              ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
            }
            ret = ret.substring(0, ret.lastIndexOf('&'))
            return ret
          }
        ],
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
      })
        .then(Response => {
          // console.log(Response.data)
          console.log(Response.data.access)
          console.log(Response.data.refresh)
          console.log(Response.data.username)
          let username = Response.data.username
          let access = Response.data.access
          let refresh = Response.data.refresh
          this.$cookies.set('username', username, '1d')
          this.$cookies.set('access', access, '1d')
          this.$cookies.set('refresh', refresh, '1d')
          this.$router.push({path: '/home'})
          // this.$emit('success', Response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    authMobile () {
      var reg = 11 && /^((13|14|15|16|17|18|19)\d{9})$/
      if (this.mobile === '') {
        this.$alert('<strong>请输入手机号码</strong>', '提示', {
          dangerouslyUseHTMLString: true,
          type: 'warning',
          center: true
        })
      } else if (!reg.test(this.mobile)) {
        this.$alert('<strong>手机号格式不正确</strong>', '提示', {
          dangerouslyUseHTMLString: true,
          type: 'warning',
          center: true
        })
      } else {
        this.time = 60
        this.disabled1 = true
        this.disabled2 = false
        this.timer()
        this.getCode()
      }
    },
    timer () {
      if (this.time > 0) {
        this.time--
        this.codebtn = this.time + 's'
        setTimeout(this.timer, 1000)
      } else {
        this.time = 0
        this.codebtn = '获取验证码'
        this.disabled1 = false
      }
    },
    loginInfo () {
      if (this.mobile === '') {
        this.$alert('<strong>手机号码不能为空</strong>', '提示', {
          dangerouslyUseHTMLString: true,
          type: 'warning',
          center: true
        })
      } else if (this.code === '') {
        this.$alert('<strong>验证码不能为空</strong>', '提示', {
          dangerouslyUseHTMLString: true,
          type: 'warning',
          center: true
        })
      } else {
        // 提交登录信息的函数
        this.goLogin()
      }
    }
  }
}
</script>

<style>
.note-container {
  display: flex;
  position: absolute;
  top: 2.3rem;
  left: 0;
  right: 0;
  bottom: 2.9rem;
}
.formbar {
  height: 94%;
  width: 380px;
  margin: auto;
  display: flex;
  flex-direction: column;
  min-height: 400px;
}
.form-box {
  border-radius: 15px;
  height: 3.8rem;
  margin-top: 1.6rem;
  border: 1px solid #D5D5D5;
  position: relative;
}
.form-input {
  width: 100%;
  border-radius: 15px;
  height: 2rem;
  position: absolute;
  border: none;
  padding: 2.6rem .9rem 1.0rem 1.1rem;
  outline: 0;
  outline-color: white;
  box-sizing: border-box;
  font-size: 19px;
}
.form-label {
  color: #5E5E5E;
  position: absolute;
  pointer-events: none;
  transition-timing-function: ease-in;
  transition-duration: .125s;
  white-space: nowrap;
  overflow: hidden;
  max-width: calc(100% - 32px);
  left: 1rem;
  top: 1.2rem;
  font-size: 17px;
  font-weight: 400;
}
.form-input:focus + .form-label {
  font-size: 12px;
  top: .7rem;
}
.form-input-end-label{
  font-size: 12px;
  top: .7rem;
}
.btn {
  border-radius: 15px;
  height: 3.8rem;
  background-color: #F9F2EB;
  margin-top: 3.2rem;
  border: 1px solid #D5D5D5;
  outline: 0;
  transition-duration: .145s;
}
.btn:hover {
  background-color: #f9eee3;
}
.btn:active {
  background-color: #fae1c9;
}
.btn-word {
  font-size: 24px;
  color: #5E5E5E;
}
.phone-btn {
  position: absolute;
  right: 0;
}
.el-button.is-round {
  border-radius: 13px;
}
.el-button--small, .el-button--small.is-round {
    padding: 23px 21px;
}
.el-icon-circle-check {
  color: #67C23A;
}
.el-icon-circle-close {
  color: red;
}
</style>
