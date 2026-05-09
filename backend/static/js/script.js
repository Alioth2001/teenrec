// Basic interactivity for TeenRec

document.addEventListener("DOMContentLoaded", function() {
    console.log("TeenRec frontend loaded!");

    // Example: highlight buttons on click
    const buttons = document.querySelectorAll("button");
    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            btn.style.backgroundColor = "#2e7d32";
        });
    });
});
