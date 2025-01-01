<template>
  <div class="tareas">
    <section class="textos-header">
      <h2>Lista de tareas pendientes</h2>
    </section>

    <div class="anadir">
      <router-link to="/empleados">
        <button class="boton-anadir" role="button">
          Ver Empleados
        </button>
      </router-link>
    </div>

    <div v-for="(tarea, index) in tareas" :key="index">
      <div class="container" v-if="!tarea.completo">
        <div class="box">
            <div class="details">
                <h2>Tarea: {{tarea.titulo}}</h2> 
                <p>Descripción: {{tarea.descripcion}}</p>
                <p>Asignado: {{tarea.asignado}}</p>
            </div>
            <input @click="completeTarea(tarea.id_tarea)" class="completo" type="checkbox" autocomplete="off"/>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data(){
    return {
      tareas: [],
      showForm: true,
    }
  },

  methods: {
    getTareas(){
      const path = `${process.env.VUE_APP_ROOT_API}:5003/tareas`;
      axios
        .get(path)
        .then((response) => {
          let tareas = response.data.tareas;
          this.tareas = tareas;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    completeTarea(id){
      const path = `${process.env.VUE_APP_ROOT_API}:5003/tareas/update_tarea/${id}`;
      const headers = {
        'Content-Type': 'application/json'
      }

      axios
        .patch(path, {
          headers: headers,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },

  created() {
    if(localStorage.getItem("token")){
      this.getTareas();
    } else {
      this.$router.push("/login");
    }
  },
};
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600&display=swap');

.tareas{
    margin: 0;
    padding: 0;
    font-family: 'Poppins',sans-serif;
    background: linear-gradient(120deg, #2980b9, #8e44ad);
    height: calc(100vh + 1000px);
    
    background: -webkit-linear-gradient(to right, hsla(220, 52%, 70%, 0.863), hsla(274, 45%, 71%, 0.808)), url(../assets/Tambo-portada.jpg);
    background: linear-gradient(to right, #8ca6dbd0, #b993d6bd), url(../assets/Tambo-portada.jpg); 
    background-attachment: absolute;
    position: relative;
    background-size: cover;
}

.textos-header
{
    padding-top: 10px;
    text-align: center;
}
.textos-header h2
{
    font-family: 'Lobster', cursive;
    font-size: 50px;
    color: #fff;
}

.container{
    display: block;
    overflow: auto;
    
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    
    align-items: center; /* -> center <- */
    justify-content: flex-end;
    text-align: center;
}

.container .box {
    padding: 40px;
    margin: 10px;
    width: 800px;
    height: 130px;
    box-shadow: -1px 0 5px #000;
 
    display: flex;
    flex-direction: row;

    align-items: center;
    justify-content: center;
    text-align: center;
    
    background: rgb(177,34,195);
    background: linear-gradient(63deg, rgba(177,34,195,1) 0%, rgba(248,253,45,1) 100%);
    margin-bottom: 20px;
}

.container h2{
    text-align: left;
    border-bottom: 1px solid silver;
}

.container p{
    text-align: left;
}

.details
{
    width: 800px;
    margin-right: 10px;
}


input[type="checkbox"]
{
    width: 50px;
    height: 50px;
}

.anadir {
  position: relative;
  margin-top: 40px;
  align-items: center; /* -> center <- */
  justify-content: space-between;
  text-align: center;
}


/* Boton añadir */
.boton-anadir {
  appearance: button;
  background-color: #4423c5;
  border: solid transparent;
  border-radius: 16px;
  border-width: 0 0 4px;
  box-sizing: border-box;
  color: #ffffff;

  cursor: pointer;
  display: inline-block;

  font-family: "Brush Script MT", cursive;
  font-size: 15px;
  font-weight: 900;
  letter-spacing: 0.8px;
  line-height: 20px;
  margin: 0;
  outline: none;
  overflow: visible;
  padding: 13px 8px;
  text-align: center;
  text-transform: uppercase;
  touch-action: manipulation;
  transform: translateZ(0);
  transition: filter 0.2s;
  user-select: none;
  -webkit-user-select: none;
  vertical-align: middle;
  white-space: nowrap;
  width: 20%;
  margin: 10px;
}

.boton-anadir > a {
  text-decoration: none;
  color: #fff;
}

.boton-anadir:after {
  background-clip: padding-box;
  background-color: #643eff;
  border: solid transparent;
  border-radius: 16px;
  border-width: 0 0 4px;
  bottom: -4px;
  content: "";
  left: 0;
  position: absolute;
  right: 0;
  top: 0;
  z-index: -1;
}

.boton-anadir:main,
.boton-anadir:focus {
  user-select: auto;
}

.boton-anadir:hover:not(:disabled) {
  filter: brightness(1.1);
  -webkit-filter: brightness(1.1);
}

.boton-anadir:disabled {
  cursor: auto;
}
</style>
