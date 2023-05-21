<template>
  <div>
    <el-header>
      <el-input placeholder="搜索商家" v-model="searchText" prefix-icon="el-icon-search"></el-input>
    </el-header>
    <el-main>
      <el-card v-for="merchant in filteredMerchants" :key="merchant.id">
        <span slot="header">{{ merchant.name }}</span>
        <p>{{ merchant.rating }} 分</p>
        <p>{{ merchant.tags }}</p>
      </el-card>
    </el-main>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  setup() {
    // 硬编码商家数据
    const merchants = [
      { id: 1, name: '麦当劳', rating: 4.5, tags: '快餐' },
      { id: 2, name: '星巴克', rating: 4.2, tags: '咖啡' },
      { id: 3, name: '肯德基', rating: 3.8, tags: '快餐' },
      { id: 4, name: '必胜客', rating: 4.1, tags: '披萨' },
      { id: 5, name: '华莱士', rating: 3.7, tags: '快餐' },
      { id: 6, name: '麻辣烫', rating: 4.3, tags: '火锅' },
    ]

    // 定义搜索框的文本
    const searchText = ref('')

    // 计算过滤后的商家列表
    const filteredMerchants = computed(() => {
      return searchText.value
        ? merchants.filter(merchant => merchant.name.toLowerCase().includes(searchText.value.toLowerCase()))
        : merchants
    })

    // 返回数据和方法
    return {
      searchText,
      filteredMerchants,
    }
  },
}
</script>