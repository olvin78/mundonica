document.addEventListener('DOMContentLoaded', () => {
    const profileButton = document.querySelector('.cta-btn');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    const welcomeMessage = document.querySelector('.welcome-message');

    // Mostrar el mensaje de bienvenida y ocultarlo después de 3 segundos
    if (welcomeMessage) {
        welcomeMessage.classList.add('show'); // Aparece el mensaje

        setTimeout(() => {
            welcomeMessage.classList.remove('show'); // Desaparece después de 3 segundos
        }, 3000);
    }

    // Alternar el menú desplegable al hacer clic en el botón
    profileButton.addEventListener('click', (event) => {
        event.stopPropagation();
        dropdownMenu.classList.toggle('active');
    });

    // Cerrar el menú desplegable si se hace clic fuera
    document.addEventListener('click', (event) => {
        if (!profileButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.classList.remove('active');
        }
    });
});
