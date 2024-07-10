// Función para manejar el cambio de estado de una evidencia
function toggleEvidencia(evidencia) {
    if (evidencia.classList.contains('sin-seleccionar')) {
        evidencia.classList.remove('sin-seleccionar');
        evidencia.classList.add('seleccionado');
    } else if (evidencia.classList.contains('seleccionado')) {
        evidencia.classList.remove('seleccionado');
        evidencia.classList.add('excluido');
    } else if (evidencia.classList.contains('excluido')) {
        evidencia.classList.remove('excluido');
        evidencia.classList.add('sin-seleccionar');
    }

    // Filtrar fantasmas basado en evidencias seleccionadas
    filtrarFantasmas();
}

// Función para filtrar los fantasmas según las evidencias seleccionadas y excluidas
function filtrarFantasmas() {
    const evidenciasSeleccionadas = document.querySelectorAll('.evidencia.seleccionado');
    const evidenciasExcluidas = document.querySelectorAll('.evidencia.excluido');
    const fantasmas = document.querySelectorAll('.fantasma');

    fantasmas.forEach(fantasma => {
        let compatible = true;

        // Verificar cada evidencia excluida
        evidenciasExcluidas.forEach(evidencia => {
            if (fantasma.dataset.evidencias.includes(evidencia.dataset.evidencia)) {
                compatible = false;
            }
        });

        // Verificar cada evidencia seleccionada si no está excluida
        if (compatible && evidenciasSeleccionadas.length > 0) {
            evidenciasSeleccionadas.forEach(evidencia => {
                if (!fantasma.dataset.evidencias.includes(evidencia.dataset.evidencia)) {
                    compatible = false;
                }
            });
        }

        // Mostrar u ocultar el fantasma según su compatibilidad
        if (compatible) {
            fantasma.style.display = 'block';
        } else {
            fantasma.style.display = 'none';
        }
    });
}


// Event listeners para las evidencias
const evidencias = document.querySelectorAll('.evidencia');
evidencias.forEach(evidencia => {
    evidencia.addEventListener('click', () => {
        toggleEvidencia(evidencia);
        filtrarFantasmas(); // Llamar a la función para filtrar fantasmas después de cambiar el estado
    });
});



