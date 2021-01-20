<template>
  <div class="filters">
    <span class="filter active">全部</span>
    <span class="filter">已完成</span>
    <span class="filter">未完成</span>
  </div>
</template>

<script>
export default { name: "TodoFilters" };
</script>

<style>
:root {
  --filters-color: #c0c2ce;
  --actived-color: #6b729c;
}

/* 过滤器 */
.filters {
  display: flex;
  margin: 24px 2px;
  color: var(--filters-color);
  font-size: 14px;
}

.filters .filter {
  margin-right: 14px;
  transition: 0.8s;
}

.filters .filter.active {
  color: var(--actived-color);
  transform: scale(1.2);
}
</style>