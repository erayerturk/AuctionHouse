<template>
  <div>
    <Navbar/>
    <div class="container border  p-5">
      <div class="row">
        <div class="col-md-3">
          <img v-bind:src="'http://127.0.0.1:8000' + this.image" width="150px"/>
        </div>
        <div class="col-md-8">
          <h3>{{ this.name }}</h3>
          <p>{{ this.description }}</p>
        </div>
      </div>
      <div class="row">
        <div class="col-md-3">
          <div>Current Bid: <strong>${{ this.current_bid_price }}</strong></div>
          <div>
            <label for="checkbox">Auto Bid</label>
            <input type="checkbox" id="checkbox" v-model="checked" @change="changeAutoBidStatus">
          </div>
        </div>

        <div class="col-md-9">
          <label for="bid">Bid Amount:</label>
          <input type="number" id="bid" v-model="bid">
          <button class="btn btn-primary" @click="addBid">Make Bid</button>
        </div>
      </div>






    </div>
    <div></div>
    <div class="border m-md-3 p-3">
      <h4 align="center">Historical Bids</h4>
      <div v-for="bid in historical_bid_array" :key="bid.id">User: {{bid.user}} -- Time: {{bid.timestamp}} -- Bid Amount: {{bid.bid_price}}</div>
    </div>
  </div>
</template>

<script>
import Navbar from "./layout/Navbar";
import axios from "axios";

export default {
  name: "Details",
  components: {
    Navbar
  },
  props: ['id'],
  data() {
    return {
      base_url: `${process.env.VUE_APP_API || "http://localhost:8000"}/api/v1/be`,
      current_bid_price: 0,
      item_id: null,
      image: null,
      name: null,
      description: null,
      checked: false,
      user_id: null,
      bid: null,
      historical_bid_array: null,
      timer: null
    }
  },
  created() {
    this.checkLogin();
    this.loadAntiqueItemDetails();
    this.getAutoBidStatus();
    this.getHistoricalBids();
    this.timer = setInterval(this.getHistoricalBids, 3000)
    // this.queryId = this.$route.params.id;
  },
  methods: {
    checkLogin() {
      if (!localStorage.getItem("user_id")) {
        // redirect
        this.$router.push('login');
      }
    },
    loadAntiqueItemDetails() {
      axios.get(`${this.base_url}/item-details/${this.id}`).then(
        (r) => {
          this.item_id = r.data.id
          this.name = r.data.name
          this.description = r.data.description
          this.image = r.data.image
        }
      )
    },
    changeAutoBidStatus() {
      const userId = localStorage.getItem("user_id")
      axios.post(`${this.base_url}/change-auto-bid/${this.id}?to_activate=${this.checked}&user_id=${userId}`)
    },
    getAutoBidStatus() {
      const userId = localStorage.getItem("user_id")
      axios.get(`${this.base_url}/get-auto-bid/${this.id}?user_id=${userId}`).then((r) => {
        this.checked = r.data.auto_bid_status
      })
    },
    getHistoricalBids() {
      const userId = localStorage.getItem("user_id")
      axios.get(`${this.base_url}/get-historical-bids/${this.id}?user_id=${userId}`).then((r) => {
        if(r.data.historical_bid.length > 0) {

          this.current_bid_price = r.data.historical_bid[0].bid_price

        }
        // this.bid = this.current_bid_price + 1
        this.historical_bid_array = r.data.historical_bid
      })
    },
    addBid() {
      const userId = localStorage.getItem("user_id")
      axios.post(`${this.base_url}/add-bid/${this.id}?user_id=${userId}`, {'bid_price': this.bid})
    },
    cancelAutoUpdate () {
      clearInterval(this.timer);
    }
  },
  beforeDestroy () {
    this.cancelAutoUpdate();
  }
}
</script>
