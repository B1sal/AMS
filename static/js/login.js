const forgotPasswordLink = document.getElementById("forgotPasswordLink");
    const popup = document.getElementById("popup1");

    // Add event listener to show/hide the popup
    forgotPasswordLink.addEventListener("click", function(e) {
      e.preventDefault();
      popup.classList.toggle("active");
    });

    // Close the popup when clicking on the overlay or close button
    popup.addEventListener("click", function(e) {
      if (e.target === popup || e.target.classList.contains("close")) {
        popup.classList.remove("active");
      }
    });