document.addEventListener("DOMContentLoaded", () => {

    /* ===============================
       1. AOS INITIALIZATION
    =============================== */
    if (typeof AOS !== "undefined") {
        AOS.init({
            duration: 1000,
            once: true
        });
    }

    /* ===============================
       2. CONTACT FORM (SAFE)
    =============================== */
    const contactForm = document.getElementById("contactForm");
    if (contactForm) {
        contactForm.addEventListener("submit", function (e) {
            e.preventDefault();
            alert("Your request has been sent! Our team will reach out to you within 24 hours.");
            this.reset();
        });
    }

    /* ===============================
       3. COUNTER LOGIC (SAFE)
    =============================== */
    const counters = document.querySelectorAll(".counter-value");
    const impactSection = document.querySelector(".impact-counter-area");

    if (counters.length && impactSection) {

        const speed = 200;

        const startCounters = () => {
            counters.forEach(counter => {

                const updateCount = () => {
                    const target = +counter.dataset.target;
                    const count = +counter.innerText.replace("+", "");
                    const inc = Math.ceil(target / speed);

                    if (count < target) {
                        counter.innerText = count + inc;
                        setTimeout(updateCount, 15);
                    } else {
                        counter.innerText = target + "+";
                    }
                };

                updateCount();
            });
        };

        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    startCounters();
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        observer.observe(impactSection);
    }

});


document.querySelectorAll('.impact-option').forEach(option => {
    option.addEventListener('click', function() {
        // Remove active class from others
        document.querySelectorAll('.impact-option').forEach(opt => opt.classList.remove('active'));
        // Add to clicked
        this.classList.add('active');
        
        // Populate the custom amount field with the value (optional)
        const customField = document.querySelector('.custom-input-field[type="number"]');
        if(customField) customField.value = this.getAttribute('data-amount');
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const modalDropdown = document.getElementById('modalServiceDropdown');
    const supportModal = new bootstrap.Modal(document.getElementById('supportModal'));

    // Listen for clicks on buttons with the .open-support-modal class
    document.querySelectorAll('.open-support-modal').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const serviceKey = this.getAttribute('data-service');
            
            // 1. Set the dropdown value
            if (serviceKey && modalDropdown) {
                modalDropdown.value = serviceKey;
            }

            // 2. Show the modal
            supportModal.show();
        });
    });
});


// faq js 

document.querySelectorAll('.faq-trigger').forEach(trigger => {
    trigger.addEventListener('click', () => {
        const parent = trigger.parentElement;
        
        // If the clicked item is already active, just close it
        if (parent.classList.contains('active')) {
            parent.classList.remove('active');
        } else {
            // Close all other items first
            document.querySelectorAll('.faq-item').forEach(item => {
                item.classList.remove('active');
            });
            // Open the clicked item
            parent.classList.add('active');
        }
    });
});


// donate copy js 

function copyAccount() {
    const accNum = "1234567890";
    navigator.clipboard.writeText(accNum).then(() => {
        alert("Account number copied to clipboard!");
    });
}


// flash message js 

document.addEventListener('DOMContentLoaded', function() {
    const flashContainer = document.getElementById('flash-container');
    if (flashContainer) {
        // Remove the element from DOM after 5 seconds
        setTimeout(() => {
            flashContainer.style.display = 'none';
            // Optional: completely remove from HTML
            flashContainer.remove();
        }, 5000); 
    }
});