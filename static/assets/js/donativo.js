

//Contenedor del mensaje de para mencionar el ultimo donativo -->


// Función para mostrar el mensaje
function showDonationMessage(donorName) {
    const messageElement = document.getElementById('donation-message');
    const textElement = document.getElementById('donation-text');

    // Reemplazar el marcador de texto con el nombre del donante
    textElement.innerHTML = `¡Gracias, <span style="color: #FFD700;">${donorName}</span>! Tu donativo ayuda a construir el futuro de MundoNica.`;

    // Mostrar el mensaje
    messageElement.style.display = 'flex';

    // Crear efecto de chispas
    generateSparks();

    // Ocultar el mensaje automáticamente después de 6 segundos
    setTimeout(() => {
        messageElement.style.animation = 'fadeOutSlideUp 0.8s ease-out';
        setTimeout(() => {
            messageElement.style.display = 'none';
        }, 800); // Tiempo de la animación fadeOut
    }, 6000);
}

// Función para generar chispas
function generateSparks() {
    const sparksContainer = document.getElementById('sparks');
    sparksContainer.innerHTML = ''; // Limpiar chispas anteriores

    for (let i = 0; i < 30; i++) {
        const spark = document.createElement('div');
        spark.className = 'spark';
        spark.style.left = `${Math.random() * 100}%`;
        spark.style.animationDelay = `${Math.random() * 2}s`;
        sparksContainer.appendChild(spark);
    }
}

// Ejemplo de uso
showDonationMessage('Luis Méndez');

//Contenedor del mensaje de para mencionar el ultimo donativo


//prueba para mostrar el mapa en la página principals
