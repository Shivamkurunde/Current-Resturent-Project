function display(sectionId) {
    const el = document.getElementById(sectionId);
    if (el) {
        el.scrollIntoView({ behavior: "smooth" });
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const banner = document.querySelector(".Banner-section-bg-container");
    if (banner) {
        banner.classList.add("show");
    }
});
