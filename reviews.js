const slides = document.querySelector('.slides');
let boxes = document.querySelectorAll('.response-box');
const totalSlides = boxes.length;
const dotsContainer = document.querySelector('.dots');

let slideIndex = 1; // start at first real slide
let interval;

// Clone first & last slides for infinite loop
const firstClone = boxes[0].cloneNode(true);
const lastClone = boxes[totalSlides - 1].cloneNode(true);

firstClone.id = "first-clone";
lastClone.id = "last-clone";

slides.appendChild(firstClone);
slides.insertBefore(lastClone, boxes[0]);

boxes = document.querySelectorAll('.response-box');
const updatedTotal = boxes.length;

// Create dots
for (let i = 0; i < totalSlides; i++) {
  const dot = document.createElement("span");
  dot.classList.add("dot");
  if (i === 0) dot.classList.add("active");
  dot.addEventListener("click", () => {
    slideIndex = i + 1; // +1 because of clone
    updateSlide(true);
    resetInterval();
  });
  dotsContainer.appendChild(dot);
}
const dots = document.querySelectorAll(".dot");

// Set initial position
slides.style.transform = `translateX(-${slideIndex * 100}%)`;

// Next & Prev
document.querySelector('.next').addEventListener('click', () => {
  moveToNextSlide();
  resetInterval();
});

document.querySelector('.prev').addEventListener('click', () => {
  moveToPrevSlide();
  resetInterval();
});

function moveToNextSlide() {
  if (slideIndex >= updatedTotal - 1) return;
  slideIndex++;
  updateSlide();
}

function moveToPrevSlide() {
  if (slideIndex <= 0) return;
  slideIndex--;
  updateSlide();
}

function updateSlide(skipTransition = false) {
  if (!skipTransition) {
    slides.style.transition = "transform 0.6s ease-in-out";
  } else {
    slides.style.transition = "none";
  }
  slides.style.transform = `translateX(-${slideIndex * 100}%)`;

  // Update active class after transition
  setTimeout(() => {
    boxes.forEach(box => box.classList.remove("active"));
    boxes[slideIndex].classList.add("active");
    animateStars();
    updateDots();
  }, 100);
}

slides.addEventListener('transitionend', () => {
  if (boxes[slideIndex].id === "first-clone") {
    slides.style.transition = "none";
    slideIndex = 1;
    slides.style.transform = `translateX(-${slideIndex * 100}%)`;
  }
  if (boxes[slideIndex].id === "last-clone") {
    slides.style.transition = "none";
    slideIndex = totalSlides;
    slides.style.transform = `translateX(-${slideIndex * 100}%)`;
  }
});

function updateDots() {
  dots.forEach(dot => dot.classList.remove("active"));
  let current = slideIndex - 1;
  if (slideIndex === 0) current = totalSlides - 1;
  if (slideIndex === updatedTotal - 1) current = 0;
  dots[current].classList.add("active");
}

// Star Glow
function animateStars() {
  document.querySelectorAll('.reviews .fa-star.checked').forEach(star => {
    star.style.animation = "none";
    void star.offsetWidth;
    star.style.animation = "glow 0.5s forwards";
  });
}

// Auto-slide every 5s
function startAutoSlide() {
  interval = setInterval(moveToNextSlide, 5000);
}

function resetInterval() {
  clearInterval(interval);
  startAutoSlide();
}

// Start
boxes[slideIndex].classList.add("active");
animateStars();
updateDots();
startAutoSlide();
