<template>

  <div>
    <div class="mt-5"></div>

    <div class="p-2"><h3>Antique Items</h3></div>

    <div id="auc" v-if="auctions" class="container">
      <div class="row">
        <div class="search-wrapper panel-heading col-sm-4 ml-auto m-2">
          <input class="form-control" type="text" v-model="searchQuery" placeholder="Search" />
        </div>
      </div>
      <div class="row">
        <div v-for="auction in resultQuery" :key="auction.id" class="col-md-3">
          <AuctionSingle :auction="auction"/>
        </div>
      </div>
    </div>
    <div v-else>No Items</div>

  </div>

</template>

<script>
import AuctionSingle from "./AuctionSingle";
import axios from "axios";

export default {
  name: "AuctionApp",
  components: {
    AuctionSingle
  },

  data() {
    return {
      base_url: `${process.env.VUE_APP_API || "http://localhost:8000"}/api/v1/be`,
      searchQuery: null,
      perPage: 10,
      page: 1,
      auctions: []
    }
  },
  computed: {
    rows() {
      return this.auctions.length
    },
    resultQuery(){
      if(this.searchQuery){
        return this.auctions.filter((item)=>{
          return this.searchQuery.toLowerCase().split(' ').every(v => item.name.toLowerCase().includes(v))
        })
      }else{
        return this.auctions;
      }
    }
  },
  created() {
    this.loadAntiqueItems();
  },
  methods: {
    loadAntiqueItems() {
      axios.get(`${this.base_url}/list-antique-items?per_page=12&page=1`).then((r) => {
        console.log(r)
        r.data.antique_items.forEach((x) => {
            this.auctions.push(x)
          }
        )
      })
    },
    clickCallback: function (page) {
      console.log(page)
    }
  }
}
</script>

