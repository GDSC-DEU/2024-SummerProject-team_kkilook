function toggleFavorite(button) {
  button.classList.toggle("active");
  if (button.classList.contains("active")) {
    button.textContent = "♥";
  } else {
    button.textContent = "♡";
  }
}
