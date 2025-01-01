<template>
  <div class="register">
    <!-- Error alert button -->
    <div id="error" class="alert" v-if="alertError">
      <span
        class="closebtn"
        onclick="this.parentElement.style.display='none';"
        >&times;</span
      >
      ¡Algo salió mal! Vuelva a intentarlo.
    </div>
    <!-- Password button -->
    <div id="changepassword" class="changepassword" v-if="alertPassword">
      <span
        class="closebtn"
        onclick="this.parentElement.style.display='none';"
        >&times;</span
      >
      ¡Confirme tu contraseña correctamente!
    </div>
    <div class="container">
      <div class="title">Registro Administrador</div>

      <form id="form" @submit.prevent="handleSubmit">
        <div class="user_details">
          <div class="input_box">
            <span class="details">DNI:</span>
            <input
              id="dni_admin"
              v-model="dni"
              type="text"
              name="dni_admin"
              placeholder="DNI"
              maxlength="8"
              required
            />
          </div>

          <div class="input_box">
            <span class="details">Nombres:</span>
            <input
              id="nombres"
              v-model="nombres"
              type="text"
              name="nombres"
              placeholder="Nombres"
              required
            />
          </div>

          <div class="input_box">
            <span class="details">Apellidos:</span>
            <input
              id="apellidos"
              v-model="apellidos"
              type="text"
              name="apellidos"
              placeholder="Apellidos"
              required
            />
          </div>

          <div class="input_box">
            <span class="details">Correo electrónico:</span>
            <input
              id="correo"
              v-model="correo"
              type="text"
              name="correo"
              placeholder="Correo electrónico"
              required
            />
          </div>

          <div class="input_box">
            <span class="details">Contraseña:</span>
            <input
              id="password"
              v-model="password"
              type="password"
              name="password"
              placeholder="Contraseña"
              required
            />
          </div>

          <div class="input_box">
            <span class="details">Confirmar contraseña:</span>
            <input
              id="confirm_password"
              v-model="cpassword"
              type="password"
              name="confirm_password"
              placeholder="Confirmar contraseña"
              required
            />
          </div>
        </div>
        <div class="button">
          <input type="submit" value="Regístrate" />
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      dni: "",
      nombres: "",
      apellidos: "",
      correo: "",
      password: "",
      cpassword: "",

      alertPassword: false,
      alertError: false,
      welcome: false,
    };
  },
  methods: {
    async handleSubmit(event) {
      event.preventDefault();

      const path = `${process.env.VUE_APP_ROOT_API}:5001/register/register_admin`;

      const response = await fetch(path, {
        method: "POST",
        body: JSON.stringify({
          dni: this.dni,
          nombres: this.nombres,
          apellidos: this.apellidos,
          correo: this.correo,
          password: this.password,
          cpassword: this.cpassword,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      let data = await response.json();
      console.log("Response: ", response);
      console.log("Data: ", data);

      if(data['success']){
        this.welcome = true;
        this.$router.push({
        name: "login",
        })
      } else {
        if(data['message'] === 'Confirm correctly validation password'){
          this.alertPassword = true;
        }
        else {
          this.alertError = true;
        }
      }
    },
  },
};
</script>




<style scoped>
.register {
  display: flex;
  height: 100vh;
  justify-content: center;
  align-items: center;

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
  flex-direction: column;
}

.container {
  max-width: 700px;
  width: 100%;

  background-color: #ffffff;

  padding: 25px 30px;
  border-radius: 5%;
}

.container .title {
  font-size: 25px;
  font-weight: 500;
}

.container .title::before {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  height: 3px;
  width: 30px;
  background: linear-gradient(135deg, #71b7e6, #9b59b6);
}

.container form .user_details {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 20px 0 12px 0;
}

form .user_details .input_box {
  margin-bottom: 15px;
  width: calc(100% / 2 - 20px);
}

.user_details .input_box .details {
  display: block;
  font-weight: 500;
  margin-bottom: 5px;
  font-family: "Poppins", sans-serif;
}

/* Styles of Input Box */
.user_details .input_box input {
  height: 45px;
  width: 100%;
  outline: none;
  border-radius: 5px;
  border: 1px solid #ccc;
  padding-left: 15px;
  font-size: 16px;

  border-bottom-width: 2px;
  transition: all 0.3s ease;
}

.user_details .input_box input:focus,
.user_details .input_box input:valid {
  border-color: #9b59b6;
}

/* Boton registrarse */

form .button {
  height: 45px;
  margin: 45px 0;
}

form .button input {
  height: 100%;
  width: 100%;
  outline: none;

  color: #fff;

  border: none;

  font-size: 18px;
  font-weight: 500;
  border-radius: 10px;

  letter-spacing: 1px;

  background: linear-gradient(135deg, #71b7e6, #9b59b6);
}

form .button input:hover {
  background: linear-gradient(-135deg, #71b7e6, #9b59b6);
  cursor: pointer;
}

/* Error Alert */
/* The alert message box */



#error {
  width: 100%;
  padding: 20px;
  background-color: #f44336; /* Red */
  color: white;
  margin-bottom: 30px;
  border-radius: 5px;
  margin-top: -77px;
}

/* The close button */
.closebtn {
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
.closebtn:hover {
  color: black;
}

/* WELCOME */

#welcome {
  padding: 20px;
  background-color: #56f003; /* Red */
  color: white;
  margin-bottom: 15px;

  border-radius: 5px;
}

/* password */

#changepassword {
  width: 100%;
  padding: 20px;
  background-color: #ff9f21;
  color: white;
  margin-bottom: 30px;
  border-radius: 5px;
  margin-top: -77px;
}
</style>
