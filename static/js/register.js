// Manipulação do arquivo de avatar
document.getElementById('avatar').addEventListener('change', function (e) {
    const fileStatus = document.getElementById('fileStatus');
    if (e.target.files.length > 0) {
        fileStatus.textContent = e.target.files[0].name;
    } else {
        fileStatus.textContent = 'Nenhum arquivo escolhido';
    }
});

// Manipulação do formulário
document.getElementById('cadastroForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Validação das senhas
    const senha = document.getElementById('senha').value;
    const confirmarSenha = document.getElementById('confirmarSenha').value;

    if (senha !== confirmarSenha) {
        alert('As senhas não coincidem. Por favor, verifique.');
        return;
    }

    // Simular processamento
    const btn = document.querySelector('.cadastrar-btn');
    const originalText = btn.textContent;

    btn.textContent = 'Cadastrando...';
    btn.disabled = true;

    setTimeout(() => {
        btn.textContent = originalText;
        btn.disabled = false;
        showSuccessModal();
    }, 2000);
});

// Funções do modal de sucesso
function showSuccessModal() {
    document.getElementById('successModal').style.display = 'flex';
}

function closeSuccessModal() {
    document.getElementById('successModal').style.display = 'none';
    document.getElementById('cadastroForm').reset();
    document.getElementById('fileStatus').textContent = 'Nenhum arquivo escolhido';
}

// Fechar modal clicando fora
document.getElementById('successModal').addEventListener('click', function (e) {
    if (e.target === this) {
        closeSuccessModal();
    }
});

// Animação de entrada
document.addEventListener('DOMContentLoaded', function () {
    const container = document.querySelector('.cadastro-container');
    container.style.opacity = '0';
    container.style.transform = 'translateY(30px)';

    setTimeout(() => {
        container.style.transition = 'all 0.8s ease-out';
        container.style.opacity = '1';
        container.style.transform = 'translateY(0)';
    }, 100);
});

// Validação em tempo real
const inputs = document.querySelectorAll('.form-input');
inputs.forEach(input => {
    input.addEventListener('blur', function () {
        if (this.hasAttribute('required') && this.value.trim() === '') {
            this.style.borderColor = '#ff6b6b';
        } else {
            this.style.borderColor = '#4a90e2';
        }
    });

    input.addEventListener('focus', function () {
        this.style.borderColor = '#4a90e2';
    });
});