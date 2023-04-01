document.addEventListener('DOMContentLoaded', () => {

    // Слайдер картинок

    const swiperIMG = new Swiper('.slider-img', {
        loop: false,
        speed: 3000,
        parallax: true,
        autoplay: {
            delay: 5000,
        },
    })
    // Слайдер текста

    const swiperText = new Swiper('.slider-text', {
        loop: false,
        speed: 3000,
        mousewheel: {
            invert: true,
        },
        keyboard: {
            enabled: true,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        scrollbar: {
            el: '.swiper-scrollbar',
            draggable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },

    })
    swiperIMG.controller.control = swiperText
    swiperText.controller.control = swiperIMG

})

