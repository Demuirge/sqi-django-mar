// Function to Toggle Review Form Visibility
function toggleReviewForm() {
    var formContainer = document.getElementById("reviewFormContainer");
    if (formContainer.style.display === "none" || formContainer.style.display === "") {
        formContainer.style.display = "block";
    } else {
        formContainer.style.display = "none";
    }
}

// Ensure Form is Open If Errors Exist
document.addEventListener("DOMContentLoaded", function() {
    var formContainer = document.getElementById("reviewFormContainer");
    if (formContainer.querySelector(".book-detail-error")) {
        formContainer.style.display = "block";
    }
});

// Ensure JavaScript Doesn't Block Form Submission
document.addEventListener("DOMContentLoaded", function() {
    var reviewForm = document.querySelector(".book-detail-form");
    if (reviewForm) {
        reviewForm.addEventListener("submit", function(event) {
            console.log("Submitting form..."); // Debugging message
        });
    }
});

