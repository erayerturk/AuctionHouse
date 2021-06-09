<template>
  <div>
    <div class="border p-4 m-1">
      <img :src="createImagePath(auction)" width="150px"/>
      <p>{{ auction.name }}</p>
      <router-link class="btn btn-primary" :to="`/item-details/${auction.id}`">Bid Now</router-link>
    </div>
  </div>

</template>

<script>
export default {
  name: "AuctionSingle",
  props: ['auction'],
  methods: {
    createImagePath(auction) {
      return `${process.env.VUE_APP_API || "http://localhost:8000"}${auction.image}`
    }
  }
}
</script>

<style scoped>

</style>
