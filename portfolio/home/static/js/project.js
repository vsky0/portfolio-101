let slideIndex = 1;
showSlides(slideIndex)

function moveSlide(n) {
    /**
     * this function moves the slides/images of the projects.
     */
    slideIndex += n
    showSlides(slideIndex)
}

function showSlides(n) {
    /**
     * This function is used for moving the images of the project in circular way.
     */
    let slides = document.getElementsByClassName("carusel-item")
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length;
    }

    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"
    }
    slides[slideIndex - 1].style.display = "flex"
}