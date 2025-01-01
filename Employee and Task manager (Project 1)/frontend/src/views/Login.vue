<template>
  <div class="login">
    <div class="center">
      <h1>Login</h1>

      <form id="form-login" @submit.prevent="handleSubmit">
        <div class="txt_field">
          <input id="dni_admin_login" v-model="dni" type="text" required />
          <span></span>
          <label> DNI </label>
        </div>
        <div class="txt_field">
          <input
            id="password_login"
            v-model="password"
            type="password"
            required
          />
          <span></span>
          <label> Contraseña </label>
        </div>
        <input type="submit" value="Inicia Sesión" />
      </form>
    </div>
    <!-- Password alert button -->
    <div id="error" class="alert" v-if="passwordAlert">
      <span class="closebtn" onclick="this.parentElement.style.display='none';"
        >&times;</span
      >
      ¡Combinación de DNI/contraseña inválida!
    </div>
    <!-- Error alert button -->
    <div id="error" class="alert" v-if="errorAlert">
      <span class="closebtn" onclick="this.parentElement.style.display='none';"
        >&times;</span
      >
      ¡Algo salió mal! Inténtelo de nuevo.
    </div>

    <!-- Welcome (Admin registrado correctamente) -->
    <div id="welcome" class="ad" v-if="welcome">
      <span
        class="closebtn"
        onclick="this.parentElement.style.display='none';"
        >&times;</span
      >
      Administrador registrado correctamente.
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      dni: "",
      password: "",
      passwordAlert: false,
      errorAlert: false,
    };
  },
  props: ['welcome'],

  methods: {
    async handleSubmit(event) {
      event.preventDefault();

      const path = `${process.env.VUE_APP_ROOT_API}:5001/login/log_admin`;

      const response = await fetch(path, {
        method: "POST",
        body: JSON.stringify({
          dni: this.dni,
          password: this.password,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      let data = await response.json();
      console.log("Response: ", response);
      console.log("Data: ", data);

      if (data["success"]) {
        localStorage.setItem("token", data["token"]);
        localStorage.setItem("admin", data["admin"]["dni_admin"]);

        this.$router.push({
          name: "empleados",
          params: {
            currentUser: data["admin"]["nombres"] + " " + data["admin"]["apellidos"],
          },
        });
      } else {

        if(data['message'] === "Incorrect dni/password combination"){
          this.passwordAlert = true
        }
        else{
          this.errorAlert = true
        }
      }
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600&display=swap");

.login {
  margin: 0;
  padding: 0;
  font-family: "Poppins", sans-serif;
  background: linear-gradient(120deg, #2980b9, #8e44ad);
  height: 100vh;
  overflow: hidden;

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

.center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 400px;
  border-radius: 10px;
  background-color: white;
}

.center h1 {
  text-align: center;
  padding: 0 0 20px 0;
  border-bottom: 1px solid silver;
}

.center form {
  padding: 0 40px;
  box-sizing: border-box;
}

form .txt_field {
  position: relative;
  border-bottom: 2px solid #adadad;
  margin: 30px 0;
}

.txt_field input {
  width: 100%;
  padding: 0 5px;
  height: 40px;
  font-size: 16px;
  border: none;
  background: none;
  outline: none;
}

.txt_field label {
  position: absolute;
  top: 50%;
  left: 5px;
  color: #adadad;
  transform: translateY(-50%);
  font-size: 16px;
  pointer-events: none;
  transition: 0.5s;
}

.txt_field span::before {
  content: "";
  position: absolute;
  top: 40px;
  left: 0;
  width: 0%;
  height: 2px;
  background: #2691d9;
  transition: 0.5s;
}

.txt_field input:focus ~ label,
.txt_field input:valid ~ label {
  top: -5px;
  color: #2691d9;
}

.txt_field input:focus ~ span::before,
.txt_field input:valid ~ span::before {
  width: 100%;
}

input[type="submit"] {
  margin: 30px 0;
  width: 100%;
  height: 50px;
  border: 1px solid;
  background: #2691d9;
  border-radius: 25px;
  font-size: 18px;
  color: #e9f4fb;
  font-weight: 700;
  cursor: pointer;
  outline: none;
}

input[type="submit"]:hover {
  border-color: #2691d9;
  transition: 0.5s;
}

#error {
  padding: 20px;
  background-color: #f44336; /* Red */
  color: white;
  margin-bottom: 15px;

  border-radius: 5px;
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
</style>
