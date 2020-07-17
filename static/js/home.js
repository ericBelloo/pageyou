

$('document').ready(function(){
    $('#id_capital_prestado').on('click', function () {
        window.location = '/inversion-inicial/';
    });
    $('#id_tmar').on('click', function () {
        window.location = '/tmar/';
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

    /**
     *  Opciones para tmar
     */
    $(document).on('click', '#btn_tmar', function () {

        let aporacion_inv = parseFloat($('#id_apor_inver').val());
        let aportacion_otro = parseFloat($('#id_apor_otro').val());
        let aportacion_ins = parseFloat($('#id_apor_inst').val());

        let tmar_inv = parseFloat($('#id_tmar_inv').val());
        let tmar_otro = parseFloat($('#id_tmar_otro').val());
        let tmar_ins = parseFloat($('#id_tmar_inst').val());

        let aportacion_total = aporacion_inv + aportacion_otro + aportacion_ins;
        $('#r_aportacion').text(aportacion_total);

        aporacion_inv_por = (aporacion_inv * 1)/aportacion_total
        aportacion_otro_por = (aportacion_otro * 1)/aportacion_total;
        aportacion_ins_por = (aportacion_ins * 1)/aportacion_total;

        ponderacion_inv = (aporacion_inv_por * tmar_inv).toFixed(2);
        ponderacion_otro = (aportacion_otro_por * tmar_otro).toFixed(2)
        ponderacion_ins = (aportacion_ins_por * tmar_ins).toFixed(4);
        $('#r_tmar').text(parseFloat(ponderacion_inv) + parseFloat(ponderacion_otro) + parseFloat(ponderacion_ins));

        $('#table_body_tmar').children().remove();
        $('#table_body_tmar').append('<tr>' +
                '<th>Invercionista Privado</th>' +
                '<th>'+ aporacion_inv.toFixed(2) +'</th>' +
                '<th>'+ aporacion_inv_por.toFixed(2) +'</th>' +
                '<th>'+ tmar_inv.toFixed(2) +'</th>' +
                '<th>'+ ponderacion_inv +'</th>' +
            '</tr>'+
            '<tr>' +
                '<th>Otras Empresas</th>' +
                '<th>'+ aportacion_otro.toFixed(2) +'</th>' +
                '<th>'+ aportacion_otro_por.toFixed(2) +'</th>' +
                '<th>'+ tmar_otro.toFixed(2) +'</th>' +
                '<th>'+ ponderacion_otro +'</th>' +
            '</tr>'+
            '<tr>' +
                '<th>Institucion Financiera</th>' +
                '<th>'+ aportacion_ins.toFixed(2) +'</th>' +
                '<th>'+ aportacion_ins_por.toFixed(2) +'</th>' +
                '<th>'+ tmar_ins.toFixed(2) +'</th>' +
                '<th>'+ ponderacion_ins +'</th>' +
            '</tr>'
        );
    });

});