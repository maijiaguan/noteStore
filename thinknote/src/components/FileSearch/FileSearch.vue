<template>
  <div class="searchbar">
    <input placeholder="搜索笔记" v-model="keyword" class="search">
    <el-popover
        placement="bottom"
        width="260"
        offset='10'
        trigger="click">
        <div v-if="Object.keys(result).length !== 0">
          <el-dropdown-item v-for="item in result" :key="item.note_uid">{{ item.note_title }}</el-dropdown-item>
        </div>
        <div v-else>
          <el-dropdown-item>无结果</el-dropdown-item>
        </div>
        <el-button @click="searchNote" slot="reference" icon="el-icon-search" style="padding: 9px 15px;"></el-button>
        <!-- <el-button @click="noteFolder" slot="reference" class="iconSize" icon="el-icon-folder" circle></el-button> -->
      </el-popover>
  </div>
</template>

<script>
import Axios from 'axios'
export default {
  name: 'FileSearch',
  data () {
    return {
      restaurants: [],
      keyword: ''
    }
  },
  methods: {
    searchNote () {
      Axios({
        methods: 'get',
        url: 'http://127.0.0.1:8000/api/searchnote/',
        params: {
          keyword: this.keyword
        },
        headers: {
          Authorization: 'Bearer ' + this.$cookies.get('access')
        }
      })
        .then((response) => {
          console.log(response.data)
          this.restaurants = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  computed: {
    result () {
      console.log(123)
      return this.restaurants
    }
  }
}
</script>

<style>
  .searchbar {
    width: 100%;
    height: 60px;
    background-color: rgba(237, 235, 233, 0.411);
    border-right: 1px solid rgb(210, 210, 210);
  }
  .el-input--small .el-input__inner {
    height: 54px;
    width: 180%;
  }
  .search {
    width: 260px;
    height: 40px;
    margin: 5px 0 0 5px;
    border-color: rgba(213, 213, 213, 0.207);
  }
</style>
