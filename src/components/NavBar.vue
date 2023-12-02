<template>
  <nav class="navbar navbar-dark bg-dark flex-column">
    <ul class="navbar-nav">
      <li class="nav-item">
        <router-link class="nav-link" to="/">
          <font-awesome-icon :icon="['fas', 'earth-americas']" />
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link" to="/plots">
          <font-awesome-icon :icon="['fas', 'chart-simple']" />
        </router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
</script>

<style scoped>
.navbar {
  position: fixed;
  left: 0;
  top: 0;
  height: 100%;
  width: 50px; 
  vertical-align: middle;
}

.navbar-nav {
  position: relative;
  top: 50%;
  transform: translateY(-50%);
}
.nav-item .nav-link {
  display: flex;
  justify-content: center;
}
</style>