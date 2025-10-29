// Smooth scroll animation
document.addEventListener('DOMContentLoaded', function () {
    const container = document.querySelector('.historia-container');
    container.style.opacity = '0';

    setTimeout(() => {
        container.style.transition = 'opacity 0.8s ease-out';
        container.style.opacity = '1';
    }, 100);
});

// Add hover effect to banner images
const bannerImages = document.querySelectorAll('.banner-image');
bannerImages.forEach((img, index) => {
    img.style.opacity = '0';
    img.style.transform = 'scale(0.9)';

    setTimeout(() => {
        img.style.transition = 'all 0.6s ease';
        img.style.opacity = '1';
        img.style.transform = 'scale(1)';
    }, 200 + (index * 150));
});

// Smooth reading experience
const paragraphs = document.querySelectorAll('.history-text p');
paragraphs.forEach((p, index) => {
    p.style.opacity = '0';
    p.style.transform = 'translateY(20px)';

    setTimeout(() => {
        p.style.transition = 'all 0.6s ease';
        p.style.opacity = '1';
        p.style.transform = 'translateY(0)';
    }, 500 + (index * 100));
});