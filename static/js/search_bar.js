document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("searchInput");
  
  searchInput.addEventListener("input", function () {
    const searchValue = this.value.toLowerCase();
    const documentCards = document.querySelectorAll(".document-card");

    documentCards.forEach(card => {
      const titleElement = card.querySelector("p");
      if (titleElement) {
        const title = titleElement.textContent.toLowerCase();
        const matches = title.includes(searchValue);
        card.style.display = matches ? "block" : "none";
      }
    });
  });
});



