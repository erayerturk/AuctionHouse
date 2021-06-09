<template>
  <div class="container m-3 p-3">
    <div class="col-sm-4 offset-sm-4 border py-5">
      <h3>Settings</h3>
      <div class="form-group">
        <label>Balance:</label>
        <input type="input" class="form-control" v-model="balance" @keydown.enter="saveSettings">
      </div>
      <div class="form-group">
        <label>Auto Bid Increase Amount:</label>
        <input type="input" class="form-control" v-model="bidIncrease" @keydown.enter="saveSettings">
      </div>
      <button class="btn btn-primary" @click="saveSettings">Save</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SettingsApp",
  data() {
    return {
      base_url: `${process.env.VUE_APP_API || "http://localhost:8000"}/api/v1/be`,
      balance: null,
      bidIncrease: null
    }
  },
  created() {
    this.getSettings()
  },
  methods: {
    saveSettings() {
        const userId = localStorage.getItem("user_id")
        axios.post(`${this.base_url}/save-settings`, {'user_id': userId, 'balance': this.balance, 'bid_increase': this.bidIncrease})
    },
    getSettings() {
        const userId = localStorage.getItem("user_id")
        axios.get(`${this.base_url}/get-settings?user_id=${userId}`).then((r) => {
          this.checked = r.data.auto_bid_status
          this.balance = r.data.balance
          this.bidIncrease = r.data.bid_increase
        })
    }
  }
}
</script>
