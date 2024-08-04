function toggleFavorite(button) {
  button.classList.toggle("active");
  if (button.classList.contains("active")) {
    button.textContent = "♥";
  } else {
    button.textContent = "♡";
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card");
  const itemsPerPage = 4;
  let currentPage = 1;

  function displayPage(page) {
    cards.forEach((card, index) => {
      card.style.display =
        Math.floor(index / itemsPerPage) + 1 === page ? "block" : "none";
    });
  }

  function updatePagination() {
    document.querySelectorAll(".pagination .page-item").forEach((item) => {
      item.classList.remove("active");
    });
    const currentPageItem = document.querySelector(
      `.pagination .page-item:nth-child(${currentPage + 1})`
    );
    if (currentPageItem) currentPageItem.classList.add("active");
  }

  document.querySelectorAll(".pagination .page-link").forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      const page = parseInt(link.getAttribute("data-page"), 10);
      if (!isNaN(page)) {
        currentPage = page;
        displayPage(currentPage);
        updatePagination();
      } else if (link.getAttribute("aria-label") === "Previous") {
        if (currentPage > 1) {
          currentPage--;
          displayPage(currentPage);
          updatePagination();
        }
      } else if (link.getAttribute("aria-label") === "Next") {
        if (currentPage < Math.ceil(cards.length / itemsPerPage)) {
          currentPage++;
          displayPage(currentPage);
          updatePagination();
        }
      }
    });
  });

  displayPage(currentPage);
  updatePagination();
});
