// DOM elements
const contactForm = document.getElementById("contactForm")

// Initialize the website
document.addEventListener("DOMContentLoaded", () => {
  // Set up scroll animations
  setupScrollAnimations()

  // Set up smooth scrolling for navigation links
  setupSmoothScrolling()

  // Set up contact form
  setupContactForm()

  // Add interactive effects
  setupInteractiveEffects()
})

// Set up scroll animations
function setupScrollAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("animate-in")

        // Animate product cards with stagger
        if (entry.target.classList.contains("products")) {
          const productCards = entry.target.querySelectorAll(".product-card")
          productCards.forEach((card, index) => {
            setTimeout(() => {
              card.classList.add("animate-in")
            }, index * 200)
          })
        }
      }
    })
  }, observerOptions)

  // Observe all elements with animate-on-scroll class
  document.querySelectorAll(".animate-on-scroll").forEach((el) => {
    observer.observe(el)
  })
}

// Set up smooth scrolling for navigation links
function setupSmoothScrolling() {
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault()
      const target = document.querySelector(this.getAttribute("href"))
      if (target) {
        const headerHeight = document.querySelector(".header").offsetHeight
        const targetPosition = target.offsetTop - headerHeight

        window.scrollTo({
          top: targetPosition,
          behavior: "smooth",
        })
      }
    })
  })
}

// Set up contact form


// Add some interactive effects
function setupInteractiveEffects() {
  // Hover effect on product cards
  document.querySelectorAll(".product-card").forEach((card) => {
    card.addEventListener("mouseenter", function () {
      this.style.transform = "translateY(-5px) scale(1.02)"
    })
    card.addEventListener("mouseleave", function () {
      this.style.transform = ""
    })
  })

  // Click effect on buttons
  document.querySelectorAll(".hero-button, .product-button, .contact-button, .form-submit").forEach((button) => {
    button.addEventListener("click", function () {
      this.style.transform = "scale(0.95)"
      setTimeout(() => {
        this.style.transform = ""
      }, 150)
    })
  })
}

// FAQS
const faqs = document.querySelectorAll(".faq-item");

faqs.forEach(faq => {
  faq.querySelector(".faq-question").addEventListener("click", () => {
    faq.classList.toggle("active");
  });
});

//CART
// Seleciona o botão do carrinho e o container do dropdown
const cartDropdown = document.querySelector('.master-container');
const cartToggles = document.querySelectorAll('.cart-toggle');

cartToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
        e.preventDefault(); // evita comportamento padrão do <a>
        e.stopPropagation();
        cartDropdown.classList.toggle('show');
    });
});

// Fecha ao clicar fora
document.addEventListener('click', (e) => {
    if (!cartDropdown.contains(e.target)) {
        cartDropdown.classList.remove('show');
    }
});

//Contador
document.querySelectorAll('.increment').forEach(btn => {
    btn.addEventListener('click', () => {
        const id = btn.dataset.target;
        const counter = document.getElementById(`counter-${id}`);
        const quantityInput = document.getElementById(`quantity-${id}`);
        let val = parseInt(counter.innerText);
        val += 1;
        counter.innerText = val;
        quantityInput.value = val;
    });
});

document.querySelectorAll('.decrement').forEach(btn => {
    btn.addEventListener('click', () => {
        const id = btn.dataset.target;
        const counter = document.getElementById(`counter-${id}`);
        const quantityInput = document.getElementById(`quantity-${id}`);
        let val = parseInt(counter.innerText);
        if (val > 1) val -= 1;
        counter.innerText = val;
        quantityInput.value = val;
    });
});

// Back to Top Button
    const backToTopButton = document.getElementById('back-to-top');

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) { // Show button after scrolling 300px
            backToTopButton.classList.add('show');
        } else {
            backToTopButton.classList.remove('show');
        }
    });

    backToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });




