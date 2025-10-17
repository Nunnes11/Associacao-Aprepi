// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function () {
    // Add click handlers for mobile dropdown menus
    const navItems = document.querySelectorAll('.nav-item');

    navItems.forEach(item => {
        const link = item.querySelector('.nav-link');
        const dropdown = item.querySelector('.dropdown');

        if (dropdown && window.innerWidth <= 768) {
            link.addEventListener('click', function (e) {
                e.preventDefault();
                dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
            });
        }
    });

    // Smooth animations
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';

        setTimeout(() => {
            card.style.transition = 'all 0.6s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
});

// Handle responsive behavior
window.addEventListener('resize', function () {
    const dropdowns = document.querySelectorAll('.dropdown');
    if (window.innerWidth > 768) {
        dropdowns.forEach(dropdown => {
            dropdown.style.display = '';
        });
    }
});