<template>
  <div>
    <search-bar></search-bar>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue';

export default {
  name: 'HomePage',
  components: {
    SearchBar,
  },
}
</script>
在上面的代码中，我们从组件文件中导入 SearchBar 组件，并在页面中使用它。

5. 运行项目

在命令行中，进入到您的项目目录中，并运行以下命令来启动项目：