//function es la forma de decirle que se dispare una accion cuando se carga el documento

(function () {
    
        //creo una constante que contenga todos los elementos que contengan la clase btnEliminacion
        // es una constante del tipo lista
        const btnEliminacion = document.querySelectorAll(".btnEliminacion");
    
        //recorro la constante y a cada elemento le asigno una escucha
        btnEliminacion.forEach((btn) => {
            //
            btn.addEventListener("click", (e) => {
                if (!confirm("¿Desea eliminar este registro?")) {
                    //si no se acepta el alert no se hace la accion
                    e.preventDefault();
                }
            });
        })
    })();
    