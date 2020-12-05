<template>
  <div>
    <div class="list-header">
      <div class="note-counts">笔记&nbsp;&nbsp;25</div>
      <category-bar @sendCategoryNotes="sendCategoryNotes"></category-bar>
    </div>
    <div class="list-view">
      <div class="list-box" v-for="item in noteLists" :key="item.note_uid">
        <div class="list-container">
          <div class="note-title">{{ item.note_title }}</div>
          <!-- 判断是否有标签 cl为Category的item，找到匹配的标签id，取出该id的颜色-->
          <!-- 不用item.category.category_color的原因是无法与CategoryBar数据双向绑定 -->
          <div v-if="item.category" :style="{backgroundColor: Category.find((cl) => cl.id === item.category.id).category_color}" class="category-icon category-icon-select"></div>
          <!-- <div v-if="item.category" :style="{backgroundColor: item.category.category_color}" class="category-icon category-icon-select"></div> -->
          <span class="delete-btn"><i class="el-icon-delete"></i></span>
          <div class="note-add-time" @change="getNoteLists()">{{ item.note_last_time}}</div>
          <div class="note-article" @change="getNoteLists()">{{ item.note_content_v1}}</div>
          <div class="note-version">v1</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CategoryBar from '@/components/CategoryBar/CategoryBar'
import Axios from 'axios'
import { eventBus } from '@/plugin/eventBus'
export default {
  name: 'NoteList',
  components: {
    CategoryBar
  },
  data () {
    return {
      Category: [],
      lists: []
    }
  },
  mounted () {
    this.getNoteLists()
    eventBus.$on('sendCategory', (category) => {
      this.Category = category
      console.log(this.Category)
      console.log(1234)
    })
  },
  methods: {
    // 查找笔记列表
    getNoteLists () {
      Axios({
        methods: 'get',
        url: 'http://127.0.0.1:8000/api/notelists/',
        headers: {
          Authorization: 'Bearer ' + this.$cookies.get('access')
        }
      })
        .then((response) => {
          console.log(response.data)
          this.lists = response.data
          // return this.lists
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // 添加笔记
    noteAdd () {
      var apiAddNote = 'http://127.0.0.1:8000/api/notes/'
      Axios({
        method: 'post',
        url: apiAddNote,
        data: {},
        headers: {
          Authorization: 'Bearer ' + this.$cookies.get('access')
        }
      })
        .then(response => {
          // console.log(response.data)
          // console.log(response.data[12].category.category_color)
          this.lists.unshift(response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    sendCategoryNotes (payload) {
      // console.log(payload)
      this.lists = payload
    }
  },
  computed: {
    noteLists () {
      console.log(12)
      return this.lists
    }
  }
}
</script>

<style>
.list-header {
  height: 45px;
  background-color: rgba(237, 235, 233, 0.411);
  position: relative;
  border-bottom: 1px solid rgb(210, 210, 210);
  border-right: 1px solid rgb(210, 210, 210);
}
.list-view {
  height: calc(100vh - 108px);
  overflow-x: hidden;
}
.list-box {
  height: 145px;
}
.list-container {
  /* background-color: rgba(244, 244, 244, 0.536); */
  border-bottom: 1px solid rgb(193, 192, 192);
  height: 145px;
  /* margin: 14px; */
  padding-left: 14px;
}
.note-counts {
  display: inline-block;
  position: absolute;
  /* border: 1px solid red; */
  color: rgb(133, 133, 133);
  width: 100px;
  font-weight: 500;
  padding-left: 14px;
  padding-top: 10px;
}
.note-title {
  /* border: 1px solid red; */
  height: 30px;
  width: 220px;
  /* font-family: Canela; */
  overflow: hidden;
  display: inline-block;
  font-size: 18px;
  padding-top: 10px;
}
.note-add-time {
  /* border: 1px solid red; */
  height: 20px;
  width: 220px;
  /* font-family: Canela; */
  font-size: 12px;
  /* display: inline-block; */
}
.note-article {
  /* border: 1px solid red; */
  height: 50px;
  /* width: 220px; */
  font-size: 13px;
  color: rgba(73, 73, 73, 0.659);
  overflow: hidden;
}
.note-version {
  /* border: 1px solid red; */
  height: 28px;
  /* width: 220px; */
}
.list-box:hover {
  background-color: rgba(176, 230, 132, 0.274);
}
.category-icon-select {
  margin-left: 10px;
}
.delete-btn {
  /* background-color: rgb(168, 88, 88); */
  display: inline-block;
  width: 25px;
  height: 25px;
  display: none;
}
.delete-btn > i {
    color: rgb(96, 98, 102);
    font-size: 1.5em;
    vertical-align: middle;
    /* margin: 0px 20px; */
}
</style>
