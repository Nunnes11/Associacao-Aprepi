// Adicionar efeito de fade-in suave ao carregar a página
document.addEventListener('DOMContentLoaded', function () {
    const container = document.querySelector('.about-container');
    if (container) {
        container.style.opacity = '0';
        container.style.transform = 'translateY(30px)';

        setTimeout(() => {
            container.style.transition = 'all 0.8s ease-out';
            container.style.opacity = '1';
            container.style.transform = 'translateY(0)';
        }, 100);
    }

    // Efeito hover na imagem
    const imageSection = document.querySelector('.image-section');
    if (imageSection) {
        imageSection.addEventListener('mouseenter', function () {
            const img = this.querySelector('img');
            if (img) img.style.transform = 'scale(1.05)';
        });

        imageSection.addEventListener('mouseleave', function () {
            const img = this.querySelector('img');
            if (img) img.style.transform = 'scale(1)';
        });
    }
});
