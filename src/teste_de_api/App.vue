<template>
  <div id="app">
    <h1>Busca por Operadoras de Saúde</h1>
    <input
      v-model="query"
      @input="search"
      placeholder="Digite o nome ou CNPJ da operadora"
    />
    <ul v-if="operadoras.length > 0">
      <li v-for="operadora in operadoras" :key="operadora.cnpj">
        <strong>{{ operadora.razao_social }}</strong
        ><br />
        CNPJ: {{ operadora.cnpj }}<br />
      </li>
    </ul>
    <p v-else>Nenhuma operadora encontrada</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      query: "",
      operadoras: [],
    };
  },
  methods: {
    search() {
      // Chama a API para buscar as operadoras
      axios
        .get(`http://localhost:5000/search?query=${this.query}`)
        .then((response) => {
          this.operadoras = response.data;
        })
        .catch((error) => {
          console.error("Erro na busca:", error);
        });
    },
  },
};
</script>

<style scoped>
#app {
  text-align: center;
  margin-top: 50px;
}

input {
  padding: 10px;
  font-size: 16px;
  width: 300px;
  margin-bottom: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
  font-size: 18px;
}
</style>
