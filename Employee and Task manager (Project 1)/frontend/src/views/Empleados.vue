<template>
  <div class="empleados">
    <section class="textos-header">
      <h2>Lista de empleados</h2>
      <p style="color: white; font-size: 25px">
        ¡Bienvenido! {{ this.currentUser }}
        <!-- {{ this.currentUserDni }} -->
      </p>
    </section>

    <div class="anadir">
      <button
        id="show-form"
        @click="toggleFormAnadir"
        class="boton-anadir"
        role="button"
      >
        Añadir empleado
      </button>
      <router-link to="/tareas">
        <button id="show-form" class="boton-anadir" role="button">
          Ver tareas
        </button>
      </router-link>
      <router-link to="/login">
        <button id="show-form" @click="logout" class="boton-anadir" role="button">Logout</button>
      </router-link>
    </div>
    <div v-for="(empleado, index) in empleados" :key="index" class="container">
      <div class="box">
        <img
          v-if="empleado.genero == 'M'"
          src="../assets/empleado_hombre.png"
        />
        <img v-else src="../assets/empleado_mujer.png" />

        <div class="details">
          <h3>Ficha Empleado</h3>
          <li>Dni: {{ empleado.dni_empleado }}</li>
          <li>Nombres: {{ empleado.nombres }}</li>
          <li>Apellidos: {{ empleado.apellidos }}</li>
          <li>Género: {{ empleado.genero }}</li>
          <li>Admin: {{ empleado.admin }}</li>
        </div>
        <div class="botones">
          <button class="boton-tarea" role="button" @click="toggleFormAsignar(empleado.dni_empleado)">Asignar Tarea</button>
          <button class="boton-eliminar" role="button" @click="deleteEmpleado(empleado.dni_empleado)">Eliminar</button>
          <button class="boton-editar" role="button" @click="toggleFormEditar(empleado.dni_empleado)">Editar</button>
        </div>
      </div>
    </div>

    <Anadir v-if="showAnadir" :admin="currentUserDni"></Anadir>
    <Asignar v-if="showAsignar" :empleado="empleadoAsignado"></Asignar>
    <Editar v-if="showEditar" :empleado="empleadoEditado"></Editar>

  </div>
</template>

<script>
import axios from "axios";
import Anadir from "../components/Anadir.vue";
import Asignar from "../components/Asignar.vue";
import Editar from "../components/Editar.vue";

export default {
  data() {
    return {
      empleados: [],
      currentUserDni: null,

      showAnadir: false,
      showAsignar: false,
      showEditar: false,

      empleadoAsignado: "",
      empleadoEditado: "",
    }
  },

  components: {
    Anadir,
    Asignar,
    Editar
  },

  props: {
    currentUser: {
      type: String,
    },
  },

  methods: {
    // LISTA DE EMPLEADOS :)
    getEmpleados() {
      const path = `${process.env.VUE_APP_ROOT_API}:5002/empleados`;
      axios
        .get(path)
        .then((response) => {
          console.log(response);
          let empleados = response.data.empleados;
          this.empleados = empleados;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    
    // ELIMINAR UN EMPLEADO POR SU DNI
    deleteEmpleado(empleado){
      const path = `${process.env.VUE_APP_ROOT_API}:5002/empleados/delete_empleado/${empleado}`;
      axios
        .delete(path)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    
    // Logout
    logout(){
      localStorage.clear();
      this.$router.push("/login");
    },

    // POP-UP FORMS
    toggleFormAnadir() {
      this.showAnadir = !this.showAnadir;
    },

    toggleFormAsignar(empleado) {
      this.showAsignar = !this.showAsignar;
      this.empleadoAsignado = empleado;
      console.log(this.empleadoAsignado);
    },

    toggleFormEditar(empleado){
      this.showEditar = !this.showEditar;
      this.empleadoEditado = empleado;
      console.log(this.empleadoEditado);
    }
  },

  created() {
    if(localStorage.getItem("token")){
      this.getEmpleados();
      this.currentUserDni = localStorage.getItem("admin");
      console.log(this.currentUserDni);

    } else {
      this.$router.push("/login");
    }
    
  },
};
</script>

<style scoped>
.empleados {
  height: calc(100vh + 1000px);
  background: -webkit-linear-gradient(
      to right,
      hsla(220, 52%, 70%, 0.863),
      hsla(274, 45%, 71%, 0.808)
    ),
    url(../assets/Tambo-portada.jpg);
  background: linear-gradient(to right, #8ca6dbd0, #b993d6bd),
    url(../assets/Tambo-portada.jpg);

  background-attachment: absolute;
  position: relative;
  background-size: cover;
}

.container {
  width: 100%;
  display: block;
  overflow: auto;

  margin-top: 50px;
  display: flex;
  flex-direction: column;

  align-items: center; /* -> center <- */
  justify-content: flex-end;
  text-align: center;
}

.textos-header {
  padding-top: 10px;
  text-align: center;
}
.textos-header h2 {
  font-family: "Lobster", cursive;
  font-size: 50px;
  color: #fff;
}

.anadir {
  position: relative;
  margin-top: 40px;
  margin-bottom: -20px;
  align-items: center; /* -> center <- */
  justify-content: space-between;
  text-align: center;
}

.box {
  padding: 40px;
  margin: 10px;
  width: 700px;
  height: 250px;
  box-shadow: -1px 0 5px #000;

  display: flex;
  flex-direction: row;

  align-items: center;
  justify-content: space-around;
  text-align: center;

  background: rgb(177, 34, 195);
  background: linear-gradient(
    63deg,
    rgba(177, 34, 195, 1) 0%,
    rgba(248, 253, 45, 1) 100%
  );
  margin-bottom: 20px;
}

.botones {
  display: flex;
  flex-direction: column;
  margin-left: 30px;
}

.details {
  display: flex;
  flex-direction: column;
  align-items: none;
  justify-content: none;
  text-align: none;
}

img {
  width: 215px;
  height: 200px;
  margin: 15px;
  margin-left: -15px;
}

h2 {
  font-size: 40px;
  font-weight: 300;
  color: #fff;
  font-family: "Poppins", sans-serif;
}

/* Botones */

/* Botón tarea */
.boton-tarea {
  appearance: button;
  background-color: #32d016;
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
  width: 100%;

  margin: 10px;
}

.boton-tarea > a {
  text-decoration: none;
  color: #fff;
}

.boton-tarea:after {
  background-clip: padding-box;
  background-color: #65ff12;
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

.boton-tarea:main,
.boton-tarea:focus {
  user-select: auto;
}

.boton-tarea:hover:not(:disabled) {
  filter: brightness(1.1);
  -webkit-filter: brightness(1.1);
}

.boton-tarea:disabled {
  cursor: auto;
}

/* Botón eliminar */

.boton-eliminar {
  appearance: button;
  background-color: #ac1c64;
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
  width: 100%;

  margin: 10px;
}

.boton-eliminar > a {
  text-decoration: none;
  color: #fff;
}

.boton-eliminar:after {
  background-clip: padding-box;
  background-color: #ff359a;
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

.boton-eliminar:main,
.boton-eliminar:focus {
  user-select: auto;
}

.boton-eliminar:hover:not(:disabled) {
  filter: brightness(1.1);
  -webkit-filter: brightness(1.1);
}

.boton-eliminar:disabled {
  cursor: auto;
}

.boton-editar,
.boton-editar-dato {
  appearance: button;
  background-color: #1955ae;
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
  width: 100%;

  margin: 10px;
}

.boton-editar > a,
.boton-editar-dato > a {
  text-decoration: none;
  color: #fff;
}

.boton-editar:after,
.boton-editar-dato:after {
  background-clip: padding-box;
  background-color: #2777f0;
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

.boton-editar:main,
.boton-editar:focus {
  user-select: auto;
}

.boton-editar-dato:main,
.boton-editar-datp:focus {
  user-select: auto;
}

.boton-editar:hover:not(:disabled) {
  filter: brightness(1.1);
  -webkit-filter: brightness(1.1);
}

.boton-editar-dato:hover:not(:disabled) {
  filter: brightness(1.1);
  -webkit-filter: brightness(1.1);
}

.boton-editar:disabled {
  cursor: auto;
}

.boton-editar-dato:hover:not(:disabled) {
  cursor: pointer;
}

/* Botón eliminar */

.boton-eliminar {
  appearance: button;
  background-color: #ac1c64;
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
  width: 100%;

  margin: 10px;
}

.boton-eliminar > a {
  text-decoration: none;
  color: #fff;
}

.boton-eliminar:after {
  background-clip: padding-box;
  background-color: #ff359a;
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

.boton-eliminar:main,
.boton-eliminar:focus {
  user-select: auto;
}

.boton-eliminar:hover:not(:disabled) {
  filter: brightness(1.1);
  -webkit-filter: brightness(1.1);
}

.boton-eliminar:disabled {
  cursor: auto;
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

/* Boton asignar TAREA */
.boton-asignar {
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
  width: 100%;
}

.boton-asignar > a {
  text-decoration: none;
  color: #fff;
}

.boton-asignar:after {
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

.boton-asignar:main,
.boton-asignar:focus {
  user-select: auto;
}

.boton-asignar:hover:not(:disabled) {
  filter: brightness(1.1);
  -webkit-filter: brightness(1.1);
}

.boton-asignar:disabled {
  cursor: auto;
}

/* POPUP */

.popup-form,
.popup-form-task,
.popup-form-edit {
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  position: fixed;
  top: 0;
  overflow: auto;

  /* properties that will be modified*/
  display: block; /* -> block */
  transition: top 0ms ease-in-out 0ms, opacity 200ms ease-in-out 0ms,
    transform 20ms ease-in-out 0ms;
}

.popup {
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(1.25);
  width: 380px;
  padding: 20px 30px;
  background: #fff;
  box-shadow: 2px 2px 5px 5px rgba(0, 0, 0, 0.15);
  border-radius: 5%;
  position: fixed;
  opacity: 1;
}

.popup-form.active,
.popup-form-task.active,
.popup-form-edit.active {
  opacity: 1;
  z-index: 0;
  transform: scale(1);
}

.popup .closebtn {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 15px;
  height: 15px;

  background: #888;
  color: #eee;
  text-align: center;
  line-height: 15px;
  border-radius: 15px;
  cursor: pointer;
}

.popup .form h2 {
  text-align: center;
  color: #222;
  margin: 10px 0px 20px;
  font-size: 25px;
}

.popup .form .form-element {
  margin: 15px 0px;
}

.popup .form .form-element label {
  font-size: 14px;
  color: #222;
}

.popup .form .form-element input[type="text"],
textarea {
  margin-top: 5px;
  display: block;
  width: 100%;
  padding: 10px;
  outline: none;
  border: 1px solid #aaa;
  border-radius: 5px;
}

.boton-aceptar {
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
  width: 100%;
}

.boton-aceptar > a {
  text-decoration: none;
  color: #fff;
}

.boton-aceptar:after {
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

.boton-aceptar:main,
.boton-aceptar:focus {
  user-select: auto;
}

.boton-aceptar:hover:not(:disabled) {
  filter: brightness(1.1);
  -webkit-filter: brightness(1.1);
}

.boton-aceptar:disabled {
  cursor: auto;
}

.boton-aceptar {
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
  width: 100%;
}

.boton-aceptar > a {
  text-decoration: none;
  color: #fff;
}

.boton-aceptar:after {
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

.boton-aceptar:main,
.boton-aceptar:focus {
  user-select: auto;
}

.boton-aceptar:hover:not(:disabled) {
  filter: brightness(1.1);
  -webkit-filter: brightness(1.1);
}

.boton-aceptar:disabled {
  cursor: auto;
}
</style>
