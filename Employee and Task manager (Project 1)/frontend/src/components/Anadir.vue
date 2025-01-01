<template>
  <div class="popup-form" v-if="showForm">
    <div class="popup">
      <div class="closebtn" @click="CloseForm">&times;</div>
      <form class="form" id="form-add" @submit.prevent="handleSubmit">
        <h2>Ingrese los datos del empleado</h2>
        <div class="form-element">
          <label for="dni">Dni:</label>
          <input
            type="text"
            v-model="dni_empleado"
            id="dni_empleado"
            placeholder="Dni"
            maxlength="8"
            required
          />
        </div>
        <div class="form-element">
          <label for="nombres">Nombres:</label>
          <input
            type="text"
            v-model="nombres"
            id="nombres"
            placeholder="Nombres"
            required
          />
        </div>
        <div class="form-element">
          <label for="apellidos">Apellidos:</label>
          <input
            type="text"
            v-model="apellidos"
            id="apellidos"
            placeholder="Apellidos"
            required
          />
        </div>
        <div class="form-element">
          <label for="genero">Género:</label>
          Femenino:
          <input
            type="radio"
            name="gender"
            id="female"
            v-model="genero"
            value="F"
          />
          Masculino:
          <input
            type="radio"
            name="gender"
            id="male"
            v-model="genero"
            value="M"
          />
        </div>
        <div class="form-element">
          <a>
            <button class="boton-aceptar" role="button">Aceptar</button>
          </a>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Anadir",
  data() {
    return {
      dni_empleado: "",
      nombres: "",
      apellidos: "",
      genero: "",
      showForm: true,
    };
  },

  props: ['admin'],

  methods: {
    handleSubmit() {

      const path = `${process.env.VUE_APP_ROOT_API}:5002/empleados/new_empleado`;

      const headers = {
        "Content-Type": "application/json",
      };

      console.log("ADMIN:", this.admin);

      var data = JSON.stringify({
        dni_empleado: this.dni_empleado,
        nombres: this.nombres,
        apellidos: this.apellidos,
        genero: this.genero,
        admin: this.admin,
      });

      console.log("DATA:", data);

      axios.post(path, {
          body: data,
          headers: headers,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
          this.showForm = false;
        });
    },

    CloseForm() {
      this.showForm = false;
    },

    created(){
      console.log("CURRENT: ", this.currentUserDni);
    }
  },
};
</script>

<style scoped>
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
