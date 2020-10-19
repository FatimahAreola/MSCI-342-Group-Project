<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button v-on:click="test_axios">Test access to our backend</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  data() {
    return {

    }
  },
  props: {
    msg: String
  },
  mounted() {
    this.test_axios()
  },
methods: {
    test_axios: function () {
      const baseURI = '/api/hello'
      axios.get(baseURI)
      .then((result) => {
        console.log(result)
      }).catch(function (error) {
           console.log(error);
        });
    }
  },
}
</script>