<template>
  <div>
    <Navbar/>
    <SettingsApp/>
  </div>
</template>

<script>
import Navbar from "./layout/Navbar";
import SettingsApp from "./settings/SettingsApp";

export default {
  name: "Settings",
  components: {
    SettingsApp,
    Navbar
  },
}
</script>

<style scoped>

</style>
