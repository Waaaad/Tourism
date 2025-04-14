const navMenu = document.querySelector(".nav-menu"),
  navToggle = document.querySelector(".nav-toggle"),
  navClose = document.querySelector(".nav-close");

// إظهار القائمة
if (navToggle) {
  navToggle.addEventListener("click", () => {
    navMenu.classList.add("show-menu");
    navToggle.style.display = "none";
    navClose.style.display = "block";
  });
}

// إخفاء القائمة
if (navClose) {
  navClose.addEventListener("click", () => {
    navMenu.classList.remove("show-menu");
    navToggle.style.display = "block";
    navClose.style.display = "none";
  });
}
