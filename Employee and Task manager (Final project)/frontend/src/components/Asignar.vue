<template>
<div class="popup-form-task" v-if="showForm">
    <div class="popup">
        <div class="closebtn" @click="closeForm">&times;</div>
        <form class="form" id="form-task" @submit.prevent="AsignarTarea(empleado)">
            <h2>Ingrese los datos de la tarea</h2>
            <div class="form-element">
                <label for="titulo">Título:</label>
                <input id="titulo" v-model="titulo" type="text" placeholder="Título" required>
            </div>
            <div class="form-element">
                <label for="descripcion">Descripción:</label>
                <textarea id = "descripcion" v-model="descripcion" rows = "5" cols = "41" placeholder="Descripción" required></textarea>
            </div>
            <div class="form-element">
                <button class="boton-asignar" role="button" >Asignar</button>
            </div>
        </form>
    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Asignar',
    data(){
        return {
            titulo: "",
            descripcion: "",
            showForm: true,
        }
    },
    props: ['empleado'],

    methods: {
        async AsignarTarea(empleado){
            const path = `${process.env.VUE_APP_ROOT_API}:5003/tareas/asignar_tarea/${empleado}`;

            const headers = {
                'Content-Type': 'application/json'
            }

            const response = await fetch(path, {
              method: "POST",
              body: JSON.stringify({
                  titulo: this.titulo,
                  descripcion: this.descripcion,
              }),
              headers: headers,
            })
            .then((response) => {
              console.log(response);
              this.showForm = false;
            })
            .catch((error) => {
              console.log(error);
              this.fshowForm = false;
            });
        },

        closeForm(){
            this.showForm = false;
        }
    }
}
</script>

<style>

.popup-form-task
{
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  position: fixed;
  top: 0;
  overflow: auto;
  /* properties that will be modified*/
  display: block; /* -> block */
  transition: top 0ms ease-in-out 0ms, opacity 200ms ease-in-out 0ms, transform 20ms ease-in-out 0ms;
}

.popup
{
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


.popup .closebtn
{
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

.popup .form h2
{
    text-align: center;
    color: #222;
    margin: 10px 0px 20px;
    font-size: 25px;
}

.popup .form .form-element
{
    margin: 15px 0px;
}

.popup .form .form-element label
{
    font-size: 14px;
    color: #222;
}

.popup .form .form-element input[type="text"], textarea
{
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
  
    font-family: 'Brush Script MT', cursive;
    font-size: 15px;
    font-weight: 900;
    letter-spacing: .8px;
    line-height: 20px;
    margin: 0;
    outline: none;
    overflow: visible;
    padding: 13px 8px;
    text-align: center;
    text-transform: uppercase;
    touch-action: manipulation;
    transform: translateZ(0);
    transition: filter .2s;
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
  
    font-family: 'Brush Script MT', cursive;
    font-size: 15px;
    font-weight: 900;
    letter-spacing: .8px;
    line-height: 20px;
    margin: 0;
    outline: none;
    overflow: visible;
    padding: 13px 8px;
    text-align: center;
    text-transform: uppercase;
    touch-action: manipulation;
    transform: translateZ(0);
    transition: filter .2s;
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

/* Boton agregado exitosamente */
.ad, .success-tarea-alert
{
    display: none;
}

#welcome, #success-tarea
{
    padding: 5px;
    margin: 10px;
    width: 500px;
    height: 40px;

    background-color: #56f003; /* Red */
    color: white;

    margin-bottom: 15px;

    border-radius: 5%;

    justify-content: center;
    text-align: center;

    font-size: 24px;
}

#new-box
{
  display: none;
}


/* Error Alert */
/* The alert message box */

.alert
{
    display: none;
}

#error
{
    padding: 20px;
    background-color: #f44336; /* Red */
    color: white;
    margin-bottom: 15px;
    border-radius: 5px;
}

/* Empleado eliminado exitosamente*/

.del
{
    display: none;
}

#eliminar
{
    padding: 5px;
    margin: 10px;
    width: 500px;
    height: 40px;

    background-color: #28c13c; /* Red */
    color: white;

    margin-bottom: 15px;

    border-radius: 5%;

    justify-content: center;
    text-align: center;

    font-size: 24px;
}



.alert
{
    display: none;
}

#error
{
    padding: 20px;
    background-color: #f44336; /* Red */
    color: white;
    margin-bottom: 15px;
    border-radius: 5px;
}

/* Empleado editado exitosamente*/

.success-edit-alert
{
    display: none;
}

#success-edit
{
    padding: 5px;
    margin: 10px;
    width: 500px;
    height: 40px;
    background-color: #268ecf;
    color: white;
    margin-bottom: 15px;
    border-radius: 5%;
    justify-content: center;
    text-align: center;
    font-size: 24px;
}

/* The close button */
.closebtn 
{
    margin-left: 15px;
    color: white;
    font-weight: bold;
    float: right;
    font-size: 22px;
    line-height: 20px;
    cursor: pointer;
    transition: 0.3s;
}
  
/* When moving the mouse over the close button */
.closebtn:hover 
{
    color: black;
}

#hombre
{
  display: none;
}

#mujer
{
  display: none;
}

#radio_dni, #radio_nombres, #radio_apellidos
{
  outline: none;
  float: right;
}

.popup-form-edit-dni, .popup-form-edit-nombres, .popup-form-edit-apellidos
{
  display: none;
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

  font-family: 'Brush Script MT', cursive;
  font-size: 15px;
  font-weight: 900;
  letter-spacing: .8px;
  line-height: 20px;
  margin: 0;
  outline: none;
  overflow: visible;
  padding: 13px 8px;
  text-align: center;
  text-transform: uppercase;
  touch-action: manipulation;
  transform: translateZ(0);
  transition: filter .2s;
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
</style>