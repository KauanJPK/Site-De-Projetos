
const botoes = document.querySelectorAll("nav button");
botoes.forEach(botao => {
  botao.addEventListener("click", () => {
    const destino = botao.getAttribute("data-link");
    window.location.href = destino;
  });
});
const toggle = document.getElementById("menu-toggle");
    const nav = document.querySelector(".nav-top");

    toggle.addEventListener("click", () => {
      toggle.classList.toggle("active");
      nav.classList.toggle("show");
    });
