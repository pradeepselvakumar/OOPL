document.addEventListener("DOMContentLoaded", function() {
    const tocBtn = document.querySelector(".toc-btn");
    const tocList = document.querySelector(".toc-list");

    tocBtn.addEventListener("click", function() {
        tocList.classList.toggle("show");
    });
});
