// Get the modal
var modal = document.getElementById("newsletterModal");

// Get the <span> element that closes the modal
var closeDiv = document.getElementsByClassName("close")[0];


document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        modal.style.display = "block";
    }, 2000)
    closeDiv.addEventListener("click", function () {
        modal.style.display = "none";
    })
})