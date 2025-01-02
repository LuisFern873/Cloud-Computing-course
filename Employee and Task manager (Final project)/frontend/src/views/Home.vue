<template>
  <!-- src="../assets/logo.png" -->
  <header class="header" id="inicio">
    <!--Transición-->
    <img src="../assets/wave.png" alt="" class="wave" />

    <!--Textos e imágenes Header-->
    <div class="container">
      <section class="textos-header">
        <h1>Sistema de administración de empleados y tareas</h1>
        <img src="../assets/Tambo-logo.png" alt="" class="logo" />
        <h2>Cada vez más cerca</h2>
      </section>

      <div class="botones">
        <router-link to="/login">
          <button class="button-19" role="button">Iniciar Sesión</button>
        </router-link>
        <router-link to="/register">
          <button class="button-18" role="button">Regístrate</button>
        </router-link>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style scoped>
header {
  /* Espacio encabezado */
  width: 100%;
  height: 600px;
  /* Degradado y foto portada*/

  background: #b993d6; /* fallback for old browsers */
  background: -webkit-linear-gradient(
      to right,
      hsla(220, 52%, 70%, 0.863),
      hsla(274, 45%, 71%, 0.808)
    ),
    url(../assets/Tambo-portada.jpg);
  background: linear-gradient(to right, #8ca6dbd0, #b993d6bd),
    url(../assets/Tambo-portada.jpg);

  /* Posición estática - Portada */
  background-attachment: fixed;
  position: relative;
  /* Tamaño - Portada */
  background-size: cover;
}

.container {
  margin-top: -20px;
}

/* Logo y textos del encabezado */
header .textos-header {
  /* Márgenes */
  display: flex;
  align-items: center;
  /* Tamaño y espacio */
  height: 430px;
  width: 100%;
  /* Centro */
  justify-content: center;
  flex-direction: column;
  text-align: center;
}

.textos-header h1 {
  font-size: 50px;
  color: #fff;
  margin-top: 100px;
}

.textos-header h2 {
  font-size: 40px;
  font-weight: 300;
  color: #fff;
}

.logo {
  width: 30%;
  padding: 20px;
}
.wave {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 10%;
}

.botones {
  justify-content: center;
  flex-direction: center;
  text-align: center;
  margin-top: 20px;
}

/* CSS */
.button-19 {
  appearance: button;
  background-color: #dbd415;
  border: solid transparent;
  border-radius: 16px;
  border-width: 0 0 4px;
  box-sizing: border-box;
  color: #fa2e86;

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
  width: 13%;

  margin-right: 60px;
}

.button-19 > a {
  text-decoration: none;
}

.button-19:after {
  background-clip: padding-box;
  background-color: #fff712;
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

.button-19:main,
.button-19:focus {
  user-select: auto;
}

.button-19:hover:not(:disabled) {
  filter: brightness(1.1);
  -webkit-filter: brightness(1.1);
}

.button-19:disabled {
  cursor: auto;
}

/* CSS */
.button-18 {
  appearance: button;
  background-color: #dbd415;
  border: solid transparent;
  border-radius: 16px;
  border-width: 0 0 4px;
  box-sizing: border-box;
  color: #fa2e86;

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
  width: 13%;
}

.button-18 > a {
  text-decoration: none;
}

.button-18:after {
  background-clip: padding-box;
  background-color: #fff712;
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

.button-18:main,
.button-18:focus {
  user-select: auto;
}

.button-18:hover:not(:disabled) {
  filter: brightness(1.1);
  -webkit-filter: brightness(1.1);
}

.button-18:disabled {
  cursor: auto;
}
</style>
