<template>
  <div class="category-bar">
    <div class="category-box" v-for="item in categories" :key="item.id">
      <div @click="searchCategory(item.id)" class="category-a">
        <div :style="{backgroundColor: item.category_color}" class="category-icon" :title="item.category_name"></div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import { eventBus } from '@/plugin/eventBus'
export default {
  name: 'CategoryBar',
  data () {
    return {
      categories: [],
      lists: []
    }
  },
  mounted () {
    this.getCategory()
  },
  methods: {
    getCategory () {
      Axios({
        methods: 'get',
        url: 'http://127.0.0.1:8000/api/category/',
        headers: {
          Authorization: 'Bearer ' + this.$cookies.get('access')
        }
      })
        .then((response) => {
          console.log(response.data)
          this.categories = response.data
          eventBus.$emit('sendCategory', this.categories)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // 标签查找笔记
    searchCategory (ci) {
      // console.log(ci)
      Axios({
        methods: 'get',
        url: 'http://127.0.0.1:8000/api/categorynotes/' + ci,
        headers: {
          Authorization: 'Bearer ' + this.$cookies.get('access')
        }
      })
        .then((response) => {
          console.log(response.data)
          this.lists = response.data
          this.$emit('sendCategoryNotes', this.lists)
          // return this.lists
        })
        .catch((error) => {
          console.log(error)
        })
      // this.$emit('sendCategoryNotes', this.lists)
    }
    // toNotes (category) {
    // eventBus.$emit('sendCategory', this.category)
    // }
  }
}
</script>

<style>
.category-bar {
  /* border: 1px solid red; */
  position: absolute;
  width: 180px;
  height: 42px;
  /* left: 160px; */
  right: 0;
  /* bottom: 0.1rem; */
  /* display: flex; */
  overflow-x: hidden;
}
.category-box {
  width: 38px;
  height: 38px;
  /* border: 1px solid red; */
  line-height: 42px;
  text-align: center;
  display: inline-block;
}
.category-icon {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  /* margin: 10px; */
  box-shadow: #5E5E5E 0px 1px 5px 1px;
  display: inline-block;
  transition: all .27s;
}
.category-a:hover .category-icon {
  border: 1px solid #fcf2f2;
  transform: scale(1.4);
  color: #61f77a;
}
</style>
