<template>
  <div>
    <div class="mt-5"></div>
    <div class="row">
      <div class="col-sm-4 offset-sm-4 border py-5">
        <h3>Login</h3>
        <div class="form-group">
          <label>Username</label>
          <input type="input" class="form-control" v-model="username" @keydown.enter="submit">
        </div>
        <div class="form-group">
          <label>Password</label>
          <input :type="getTypeForPassword" class="form-control" v-model="password" @keydown.enter="submit">
          <input type="checkbox" v-model="show_password"> Show Password
        </div>
        <div v-if="errors.length">
          <div class="alert alert-danger" v-for="error in errors" :key="error">{{ error }}</div>
        </div>
        <div class="alert alert-success" v-if="message">{{ message }}</div>
        <button class="btn btn-primary btn-block" @click="submit">Login</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      base_url: `${process.env.VUE_APP_API || "http://localhost:8000"}/api/v1/be`,
      errors: [],
      message: "",
      username: "",
      password: "",
      show_password: false,
    }
  },
  methods: {
    submit() {

      axios.post(`${this.base_url}/login`, {withCredentials: true}, {
        auth: {
          username: this.username,
          password: this.password
        }
      }).then((response) => {
          localStorage.setItem("user_id", response.data.user_id);
          this.username = "";
          this.password = "";
          this.$router.push('/');
        })
        .catch(function (error) {
          console.log(error);
          return
        });
    }
  },
  computed: {
    getTypeForPassword() {
      return this.show_password ? 'text' : 'password';
    }
  }
}
</script>
