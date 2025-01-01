<template>
<div class="popup-form-edit" v-if="showAll">
    <div class="popup">
        <div class="closebtn" @click="ToggleForm">&times;</div>
        <form class="form" @submit.prevent="editEmpleado(empleado)" id="form-edit" action="/empleados/update_empleado" method="put">
            <h2>¿Qué dato necesitas editar?</h2>
            <div class="form-element">
                <li>DNI <input @click="ToggleFormDni" type="radio" name="gender" id="radio_dni" value='dni'></li>
                <li>Nombres <input @click="ToggleFormNombres" type="radio" name="gender" id="radio_nombres" value='nombres'></li>
                <li>Apellidos <input @click="ToggleFormApellidos" type="radio" name="gender" id="radio_apellidos" value='apellidos'></li>
            </div>
            <div v-if="showFormDni" class="popup-form-edit-dni" id="popup-form-edit-dni">
                <div class="form-element">
                    <h2>Ingresa el nuevo dni</h2>
                    <input v-model="dni" type="text" id="nuevo_dni" placeholder="DNI">
                </div>
            </div>
            <div v-if="showFormNombres" class="popup-form-edit-nombres" id="popup-form-edit-nombres">
                <div class="form-element">
                    <h2>Ingresa los nuevos nombres</h2>
                    <input v-model="nombres" type="text" id="nuevos_nombres" placeholder="Nombres">
                </div>
            </div>
            <div v-if="showFormApellidos" class="popup-form-edit-apellidos" id="popup-form-edit-apellidos">
                <div class="form-element">
                    <h2>Ingresa los nuevos apellidos</h2>
                    <input v-model="apellidos" type="text" id="nuevos_apellidos" placeholder="Apellidos">
                </div>
            </div>

            <div class="form-element">
                <button class="boton-editar-dato" role="button" >Editar</button>
            </div>
        </form>
        
    </div>
</div>
</template>

<script>
import axios from "axios";

export default {
    name: 'Editar',
    data(){
        return {
            showAll: true,
            showFormDni: false,
            showFormNombres: false,
            showFormApellidos: false,

            dni: "",
            nombres: "",
            apellidos: "",
        }
    },

    props: ['empleado'],

    methods: {
        ToggleForm(){
            this.showAll = false
        },
        ToggleFormDni(){
            this.showFormDni = true;
            this.showFormNombres = false;
            this.showFormApellidos = false;
        },
        ToggleFormNombres(){
            this.showFormDni = false;
            this.showFormNombres = true;
            this.showFormApellidos = false;
        },
        ToggleFormApellidos(){
            this.showFormDni = false;
            this.showFormNombres = false;
            this.showFormApellidos = true;
        },

        async editEmpleado(empleado){
            const path = `${process.env.VUE_APP_ROOT_API}:5002/empleados/update_empleado/${empleado}`;
            
            const response = await fetch(path, {
                method: "PATCH",
                body: JSON.stringify({
                    edit_dni_empleado: this.dni,
                    edit_nombres: this.nombres,
                    edit_apellidos: this.apellidos,
                }),
                headers: {
                  "Content-Type": "application/json",
                },
            });

            let data = await response.json();
            console.log("Response: ", response);
            console.log("Data: ", data);

        }
    }
}
</script>

<style scoped>
/* FORM */

.popup-form-edit
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

#radio_dni, #radio_nombres, #radio_apellidos
{
  outline: none;
  float: right;
}


/* BOTON*/
.boton-editar, .boton-editar-dato{

    appearance: button;
    background-color: #1955ae;
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

    margin: 10px;
}
  
.boton-editar > a, .boton-editar-dato > a {
    text-decoration: none;
    color: #fff;
}
  
.boton-editar:after, .boton-editar-dato:after {
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

.boton-editar:disabled{
  cursor: auto;
}

.boton-editar-dato:hover:not(:disabled) {
  cursor: pointer;
}

.popup-form-edit-dni, .popup-form-edit-nombres, .popup-form-edit-apellidos
{
  display: block;
}


</style>