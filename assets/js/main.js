/*=============== SWIPER JS PREWEDDING (COVERFLOW) ===============*/
let swiperCards = new Swiper(".prewed-swiper", {
  effect: 'coverflow',
  grabCursor: true,
  centeredSlides: true,
  loop: true,
  slidesPerView: 'auto',
  coverflowEffect: {
    rotate: 30,
    stretch: 0,
    depth: 150,
    modifier: 1,
    slideShadows: true,
  },
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".prewed-swiper .swiper-button-next",
    prevEl: ".prewed-swiper .swiper-button-prev",
  },
  pagination: {
    el: ".prewed-swiper .swiper-pagination",
    clickable: true,
  },
});