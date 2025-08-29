
const botoes = document.querySelectorAll("nav button");
botoes.forEach(botao => {
  botao.addEventListener("click", () => {
    const destino = botao.getAttribute("data-link");
    window.location.href = destino;
  });
});
