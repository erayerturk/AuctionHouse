<template>
  <div>
    <Navbar/>
    <AuctionApp/>
  </div>
</template>

<script>
import AuctionApp from './auction/AuctionApp';
import Navbar from "./layout/Navbar";

export default {
  name: "Home",
  components: {
    AuctionApp,
    Navbar
  },
  data() {
    return {}
  },
  created() {
    this.checkLogin();
  },
  methods: {
    checkLogin() {
      if (!localStorage.getItem("user_id")) {
        // redirect
        this.$router.push('login');
      }
    }
  }
}
</script>
