document.addEventListener("DOMContentLoaded", function(){
    const rect = document.getElementById("rectangle");
    rect.addEventListener("dblclick", function(){
        this.style.backgroundColor = this.style.backgroundColor === "transparent" ? "blue": "transparent";
    })
})