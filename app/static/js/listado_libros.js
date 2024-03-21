(function () {
    const btnComprarLibro = document.querySelectorAll('.btnComprarLibro');
    let isbnLibroSeleccionado = null;
    const csrf_token = document.querySelector("[name='csrf-token']").value;
    btnComprarLibro.forEach((btn) => {
        btn.addEventListener('click', function () {
            isbnLibroSeleccionado = this.id;
            confirmarCompra();
        });
    });
    const confirmarCompra = () => {
        const textoConfirmacion = 'Comprar';
        Swal.fire({
            title: '¿Confirmar la compra del libro seleccionado?',
            inputAttributes: {
                autocapitalize: 'off'
            },
            showCancelButton: true,
            confirmButtonText: textoConfirmacion,
            showLoaderOnConfirm: true,
            preConfirm: async () => {
                try {
                    console.log(window.origin)
                    const response = await fetch(`${window.origin}/comprarLibro`, {
                        method: 'POST',
                        mode: 'same-origin',
                        credentials: 'same-origin',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRF-TOKEN': csrf_token
                        },
                        body: JSON.stringify({
                            'isbn': isbnLibroSeleccionado
                        })
                    });
                    if (!response.ok) {
                        notificacionSwal('Error en la respuesta:', response.statusText, 'error', 'Cerrar');
                        return;
                    }
                    const data = await response.json();
                    if(data.exito){
                           notificacionSwal('Éxito', 'Libro comprado', 'success', 'Cerrar');
                    }else{
                        notificacionSwal('Alerta', data.mensaje, 'warning', 'Cerrar');

                    }
                } catch (error) {
                    console.error('Error al procesar la solicitud:', error);
                }
            },
            allowOutsideClick: () => false,
            allowEscapeKey: () => false
        });
    };
    
})();
