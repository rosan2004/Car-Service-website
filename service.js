// Scroll reveal animation using Intersection Observer
document.addEventListener("DOMContentLoaded", () => {
  const reveals = document.querySelectorAll(".reveal");

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
        obs.unobserve(entry.target); // animate once
      }
    });
  }, { threshold: 0.2 });

  reveals.forEach(reveal => observer.observe(reveal));
});
