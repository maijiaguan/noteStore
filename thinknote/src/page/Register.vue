<template>
  <div class="note-container">
    <div class="formbar">
      <div class="form-box">
        <input v-model="mobile" class="form-input" type="text" name="mobile" autocomplete="off" @change="onChange1" maxlength="11">
        <span class="form-label" :class="{'form-input-end-label': isActive1}">
          手机号
          <i v-if="(11 && /^((13|14|15|16|17|18|19)\d{9})$/).test(mobile)" class="el-icon-circle-check"></i>
          <i v-else-if="(11 && /^(([^1]{1}[3-9]{1}|[1]{1}[^3-9]{1})\d{9})$/).test(mobile)" class="el-icon-circle-close"></i>
        </span>
        <el-button round class="phone-btn" :disabled="disabled1" @click="authMobile">{{codebtn}}</el-button>
      </div>

      <div class="form-box">
        <input v-model="code" class="form-input" :disabled="disabled2" type="text" name="mobile" autocomplete="off" @change="onChange5" maxlength="4">
        <span class="form-label" :class="{'form-input-end-label': isActive5}">验证码</span>
      </div>

      <div class="form-box">
        <input v-model="username" class="form-input" type="text" name="username" autocomplete="off" @change="onChange2">
        <span class="form-label" :class="{'form-input-end-label': isActive2}">用户名</span>
      </div>

      <div class="form-box">
        <input v-model="pwd1" class="form-input" type="password" name="pwd" @change="onChange3">
        <span class="form-label" :class="{'form-input-end-label': isActive3}">密码</span>
      </div>

      <div class="form-box">
        <input v-model="pwd2" class="form-input" type="password" name="pwd" @change="onChange4">
        <span class="form-label" :class="{'form-input-end-label': isActive4}">
          确定密码
          <i v-if="pwd1 === pwd2 && pwd2 !== ''" class="el-icon-circle-check"></i>
          <i v-else-if="pwd1 !== pwd2 && pwd2 !== ''" class="el-icon-circle-close"></i>
        </span>
      </div>

      <button class="btn" @click="registerInfo">
        <span class="btn-word">注册</span>
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
      isActive3: false,
      isActive4: false,
      isActive5: false,
      disabled1: false,
      disabled2: true,
      time: 0,
      codebtn: '获取验证码',
      mobile: '',
      username: '',
      pwd1: '',
      pwd2: '',
      code: ''
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
    onChange3 (e) {
      const { value } = e.target
      if (value === null || value === undefined || value === '') {
        this.isActive3 = false
      } else {
        this.isActive3 = true
      }
    },
    onChange4 (e) {
      const { value } = e.target
      if (value === null || value === undefined || value === '') {
        this.isActive4 = false
      } else {
        this.isActive4 = true
      }
    },
    onChange5 (e) {
      const { value } = e.target
      if (value === null || value === undefined || value === '') {
        this.isActive5 = false
      } else {
        this.isActive5 = true
      }
    },
    getCode () {
      const host = 'http://127.0.0.1:8000'
      var apicode = host + '/sendcode/'
      Axios.get(apicode, {
        params: {
          mobile: this.mobile
        }
      })
    },
    goRegister () {
      // 提交完整的注册信息
      var apiregister = 'http://127.0.0.1:8000/register/'
      Axios.get(apiregister, {
        params: {
          mobile: this.mobile,
          code: this.code,
          username: this.username,
          pwd1: this.pwd1,
          pwd2: this.pwd2
        }
      })
        .then((Response) => {
          console.log(Response.data)
          alert(Response.data)
        })
        .catch((error) => {
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
    registerInfo () {
      console.log(1)
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
      } else if (this.username === '') {
        this.$alert('<strong>用户名不能为空</strong>', '提示', {
          dangerouslyUseHTMLString: true,
          type: 'warning',
          center: true
        })
      } else if (this.pwd1 === '') {
        this.$alert('<strong>密码不能为空</strong>', '提示', {
          dangerouslyUseHTMLString: true,
          type: 'warning',
          center: true
        })
      } else if (this.pwd2 === this.pwd1) {
        // 提交注册信息的函数
        this.goRegister()
      } else {
        this.$alert('<strong>两个密码不一致</strong>', '提示', {
          dangerouslyUseHTMLString: true,
          type: 'warning',
          center: true
        })
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
