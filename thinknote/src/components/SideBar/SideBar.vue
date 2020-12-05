<template>
  <div class="sidebar">
    <!-- 添加笔记 -->
    <div class="side-menu">
      <el-tooltip class="item" effect="light" content="添加笔记" placement="right">
        <el-button @click="noteEdit" class="iconSize" icon="el-icon-plus" circle></el-button>
      </el-tooltip>
    </div>
    <!-- 笔记列表 -->
    <div class="side-menu">
      <el-tooltip class="item" effect="light" content="笔记列表" placement="right">
        <el-button @click="noteLists" class="iconSize" icon="el-icon-tickets" circle></el-button>
      </el-tooltip>
    </div>
    <!-- 笔记夹 -->
    <div class="side-menu">
      <el-tooltip class="item" effect="light" content="文件夹" placement="right">
        <el-popover
          placement="right"
          width="260"
          trigger="click">
          <div class="box">
            <div class="folder-box">
              <div class="folder">
                <img src="@/assets/icon/files.png">
                <div class="folder-name">h5笔记&ensp;</div>
                <div class="folder-name"><i class="el-icon-edit"></i></div>
                <div class="notes-count">&ensp;6&ensp;条笔记</div>
              </div>
            </div>
            <el-button class="plus-btn" style="padding: 9px 15px;" round><i class="el-icon-plus"></i>文件夹</el-button>
          </div>
          <el-button @click="noteFolder" slot="reference" class="iconSize" icon="el-icon-folder" circle></el-button>
        </el-popover>
      </el-tooltip>
    </div>
    <!-- 标签 -->
    <div class="side-menu">
      <el-tooltip class="item" effect="light" content="标签" placement="right">
        <el-popover
          placement="right"
          width="260"
          trigger="click">
          <div class="box">
            <div class="a">
              <h4>标签</h4>
            </div>
            <div class="box-category">
              <li class="b" v-for="item in Category" :key="item.id">
                <span class="category-icon" :style="{backgroundColor: item.category_color}"></span>
                <span>{{ item.category_name }}</span>
                <el-popover
                  placement="bottom"
                  title="修改标签"
                  width="200"
                  trigger="click">
                  <div style="text-align: center; margin: 0">
                    <el-color-picker v-model="item.category_color" size="mini"></el-color-picker><br />
                    <el-button size="mini" type="text" @click="visible = false">取消</el-button>
                    <el-button type="text" size="mini" @click="visible = false">确定</el-button>
                  </div>
                  <span @click="editCategory" slot="reference"><i class="el-icon-edit"></i></span>
                </el-popover>
              </li>
            </div>
            <el-button class="plus-btn" style="padding: 9px 15px;" round><i class="el-icon-plus"></i>标签</el-button>
          </div>
          <el-button @click="noteCategory" slot="reference" class="iconSize" icon="el-icon-s-flag" circle></el-button>
        </el-popover>
      </el-tooltip>
    </div>
    <!-- 回收站 -->
    <div class="side-menu">
      <el-tooltip class="item" effect="light" content="回收站" placement="right">
        <el-popover
          placement="right"
          width="260"
          trigger="click">
          <div class="box">
            <div class="a">
              <h4>回收站</h4>
            </div>
          </div>
          <el-button @click="noteDel" slot="reference" class="iconSize" icon="el-icon-delete" circle></el-button>
        </el-popover>
      </el-tooltip>
    </div>
  </div>
</template>

<script>
// import Axios from 'axios'
import { eventBus } from '@/plugin/eventBus'
import CategoryBar from '@/components/CategoryBar/CategoryBar'
export default {
  name: 'SideBar',
  components: {
    CategoryBar
  },
  data () {
    return {
      visible: false,
      color: '',
      Category: []
    }
  },
  methods: {
    noteEdit () {
      this.$emit('toNoteLists')
    },
    noteLists () {
      console.log(1)
      this.$emit('getNoteLists')
    },
    noteFolder () {
      console.log(1)
    },
    noteCategory () {
      console.log(1)
    },
    noteDel () {
      console.log(1)
    },
    editCategory () {
      console.log(1234)
    }
  },
  mounted () {
    eventBus.$on('sendCategory', (category) => {
      this.Category = category
      console.log(this.Category)
      console.log(123456)
    })
  }
}
</script>

<style>
.sidebar {
  margin: .6rem 0.4rem;
  height: calc(100vh - 96px);
  /* background-color: rgb(103, 136, 142); */
  overflow: hidden;
}
.side-menu {
  /* background-color: rgb(255, 255, 255); */
  height: 56px;
  margin-top: 42px;
  padding: 3px 1px;
}
.iconSize {
  font-size: 31px;
}
.box {
  height: 280px;
  width: 235px;
}
.a {
  padding-left: 20px;
  padding-top: 15px;
  padding-bottom: 10px;
}
.b {
  padding-left: 20px;
  padding-top: 6px;
  padding-bottom: 4px;
}
.b:hover {
  background-color: rgba(200, 245, 182, 0.796);
}
.folder-box {
  /* background-color: rgb(236, 65, 65); */
  width: 100%;
  height: 240px;
  overflow-x: hidden;
}
.folder {
  background-color: rgba(223, 221, 221, 0.098);
  /* border-bottom: 1px solid palegoldenrod; */
  margin-bottom: 4px;
  /* height: 50px; */
  /* line-height: 50px; */
}
.folder img {
  display: inline-block;
  width: 50px;
  height: 50px;
}
.plus-btn {
  bottom: 10px;
  left: 90px;
  position: absolute;
}
.folder-name {
  display: inline-block;
  position: relative;
  bottom: 17px;
}
.notes-count {
  color: rgba(68, 67, 67, 0.616);
  font-size: 12px;
}
.box-category {
  width: 100%;
  height: 200px;
  overflow-x: hidden;
}
</style>
