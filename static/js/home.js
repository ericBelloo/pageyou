

$('document').ready(function(){
    $('#id_capital_prestado').on('click', function () {
        window.location = '/inversion-inicial/';
    });

    /*
    * Opciones para el  Pago del capital y los intereses al final del plazo.
    * */
    $(document).on('click','#btn_capital', function () {
        $('#table_body_capital').children().remove();
        let prestamo = parseFloat($('#id_prestamo_capital').val());
        let interes = parseFloat($('#id_interes_capital').val());
        let periodo = parseInt($('#id_periodo_capital').val());

        let divisor = Math.pow((1+interes), ((-1)*periodo))
        let r = (prestamo * interes)/(1-divisor);
        for(let i = 0; i <= periodo; i++){
            if(i === 0){
                $('#table_body_capital').append('<tr>'+
                        '<th>0</th>'+
                        '<th></th>'+
                        '<th></th>'+
                        '<th></th>'+
                        '<th>' + prestamo + '</th>'+
                        '<th></th>'+
                        '<th></th>'+
                    '</tr>');
            }else {
                let inter = prestamo * interes;
                let ca = r - inter;
                let n_prestamo = prestamo - ca;
                let iva = inter * 0.16;
                let total = iva + r;
                $('#table_body_capital').append('<tr>'+
                        '<th>'+ i +'</th>'+
                        '<th>'+ r.toFixed(2) +'</th>'+
                        '<th>'+ inter.toFixed(2) +'</th>'+
                        '<th>'+ ca.toFixed(2) +'</th>'+
                        '<th>' + n_prestamo.toFixed(2) + '</th>'+
                        '<th>'+ iva.toFixed(2) +'</th>'+
                        '<th>'+ total.toFixed(2)  +'</th>'+
                    '</tr>');
                prestamo = n_prestamo;
            }
        }

    });

});