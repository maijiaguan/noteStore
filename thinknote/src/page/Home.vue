<template>
  <div class="main">
    <div class="side-bar">
      <side-bar @toNoteLists="toNoteLists" @getNoteLists="getNoteLists"></side-bar>
      <el-row class="demo-avatar demo-basic">
        <el-col :span="12">
          <div class="demo-basic--circle">
            <div class="block">
              <el-popover
                placement="right"
                width="280"
                trigger="click">
                <div class="box">
                  <el-avatar :size="50" :src="circleUrl"></el-avatar>
                  <p>{{ username }}</p>
                  <el-button @click="logout" class="plus-btn" style="padding: 9px 15px;" round>退出登录</el-button>
                </div>
                <el-avatar @click="getInfo" slot="reference" :size="50" :src="circleUrl"></el-avatar>
              </el-popover>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="note-list">
      <file-search></file-search>
      <note-list ref="fromSideBar"></note-list>
    </div>
    <div class="edit-view">
      <note-edit v-model="detail" :isClear="isClear" @change="change" :key="note_uid"></note-edit>
    </div>
  </div>
</template>

<script>
import NoteEdit from '@/components/NoteEdit/NoteEdit'
import NoteList from '@/components/NoteList/NoteList'
import SideBar from '@/components/SideBar/SideBar'
import FileSearch from '@/components/FileSearch/FileSearch'
// import Axios from 'axios'
// import debounce from '@/plugin/debounce'

export default {
  name: 'Home',
  components: {
    NoteEdit,
    NoteList,
    SideBar,
    FileSearch
  },
  data () {
    return {
      username: this.$cookies.get('username'),
      note_uid: '',
      lists: [],
      text: '',
      isClear: false,
      detail: '',
      circleUrl: 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'
    }
  },
  methods: {
    toNoteLists () {
      this.$refs.fromSideBar.noteAdd()
    },
    getNoteLists () {
      this.$refs.fromSideBar.getNoteLists()
    },
    change (val) {
      console.log(val)
      // debounce(value => {
      //   // func
      // }, 10000)
    },
    getInfo () {
      console.log(1)
    },
    logout () {
      console.log(6)
      this.$cookies.remove('username')
      this.$cookies.remove('access')
      this.$cookies.remove('refresh')
      this.$router.push({path: '/login'})
    }
  }
}
</script>

<style>
.main {
  /* border: 1px solid red; */
  display: flex;
  height: 100vh;
}
.side-bar {
  width: 65px;
  min-width: 65px;
  background-color: rgba(231, 231, 231, 0.692);
  border-right: 1px solid rgb(210, 210, 210);
}
.note-list {
  width: 320px;
  min-width: 320px;
  /* display: none; */
}
.edit-view {
  flex: 1;
  min-width: 740px;
}
.demo-avatar {
  margin-left: 8px;
}
el-popover {
    background: #c1c1c1e8;
}
</style>
