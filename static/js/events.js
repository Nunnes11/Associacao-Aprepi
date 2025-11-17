// Modal functions
function openModal(type, src) {
    const modal = document.getElementById('mediaModal');
    const modalContent = document.getElementById('modalContent');

    if (type === 'image') {
        modalContent.innerHTML = `<img src="${src}" class="modal-content" alt="Imagem do evento">`;
    } else if (type === 'video') {
        // Criar elemento <video> nativo para reproduzir arquivos locais (mp4, webm, etc.)
        // Detecta tipo básico pelo sufixo do arquivo (fallback sem type é aceito pela maioria dos browsers)
        let typeAttr = '';
        if (src.endsWith('.mp4')) {
            typeAttr = 'video/mp4';
        } else if (src.endsWith('.webm')) {
            typeAttr = 'video/webm';
        } else if (src.endsWith('.ogg') || src.endsWith('.ogv')) {
            typeAttr = 'video/ogg';
        }

        const typeSource = typeAttr ? `<source src="${src}" type="${typeAttr}">` : `<source src="${src}">`;

        modalContent.innerHTML = `<video class="modal-content" controls autoplay playsinline>${typeSource}Seu navegador não suporta a tag de vídeo.</video>`;
    }

    modal.style.display = 'flex';
}

function closeModal() {
    const modal = document.getElementById('mediaModal');
    modal.style.display = 'none';
    const modalContent = document.getElementById('modalContent');
    // Caso haja um <video>, pausar e remover a fonte para liberar o player
    const videoEl = modalContent.querySelector('video');
    if (videoEl) {
        try {
            videoEl.pause();
            // Remover src e dar load para liberar o resource
            const sources = videoEl.getElementsByTagName('source');
            for (let i = sources.length - 1; i >= 0; i--) {
                sources[i].src = '';
            }
            videoEl.removeAttribute('src');
            videoEl.load();
        } catch (e) {
            console.warn('Erro ao pausar/limpar vídeo do modal', e);
        }
    }
    modalContent.innerHTML = '';
}

// Close modal when clicking outside content
var mediaModal = document.getElementById('mediaModal');
if (mediaModal) {
    mediaModal.addEventListener('click', function (e) {
        if (e.target === this) {
            closeModal();
        }
    });
}

// Close modal with ESC key
document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        closeModal();
    }
});

// Staggered animation for cards
document.addEventListener('DOMContentLoaded', function () {
    const cards = document.querySelectorAll('.event-card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });
});