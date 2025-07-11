// Animação de entrada
document.addEventListener('DOMContentLoaded', function () {
    const container = document.querySelector('.contato-container');
    container.style.opacity = '0';
    container.style.transform = 'translateY(30px)';

    setTimeout(() => {
        container.style.transition = 'all 0.8s ease-out';
        container.style.opacity = '1';
        container.style.transform = 'translateY(0)';
    }, 100);
});

// Efeito de hover na logo
const logoContainer = document.querySelector('.logo-container');
logoContainer.addEventListener('mouseenter', function () {
    this.style.transform = 'scale(1.05)';
    this.style.boxShadow = '0 15px 40px rgba(74, 144, 226, 0.3)';
});

logoContainer.addEventListener('mouseleave', function () {
    this.style.transform = 'scale(1)';
    this.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.1)';
});

// Efeito de clique na logo
logoContainer.addEventListener('click', function () {
    this.style.transform = 'scale(0.95)';
    setTimeout(() => {
        this.style.transform = 'scale(1.05)';
    }, 150);
});