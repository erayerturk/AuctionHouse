<template>
  <header>
    <nav>
      <h1>
        <router-link to="/">Auction House</router-link>
      </h1>
      <ul>
        <li>
          <router-link to="/settings">Settings</router-link>
        </li>
        <li>
          <a class="test" @click="logout">Logout</a>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: "navbar",
  methods: {
    logout() {
      localStorage.clear();
      this.$router.push('/login');
    }
  }
}

</script>

<style scoped>
header {
  width: 100%;
  height: 5rem;
  background-color: #1e568e;
  display: flex;
  justify-content: center;
  align-items: center;
}



header a {
  text-decoration: none;
  color: #dcc3d3;
  display: inline-block;
  padding: 0.75rem 1.5rem;
  border: 1px solid transparent;
}

a:active,
a:hover,
a.router-link-active {
  border: 1px solid #f391e3;
}

h1 {
  margin: 0;
}

h1 a {
  color: white;
  margin: 0;
}

h1 a:hover,
h1 a:active,
h1 a.router-link-active {
  border-color: transparent;
}

header nav {
  width: 90%;
  margin: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

header ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

li {
  margin: 0 0.5rem;
}
</style>
