

$('document').ready(function(){

    if(document.mozCancelFullScreen) {
        document.mozCancelFullScreen();
    }
  //Google Chrome
    else if(document.webkitCancelFullScreen) {
        document.webkitCancelFullScreen();
    }
  //Otro
     else if(document.cancelFullScreen) {
         document.cancelFullScreen();
     }

    $('#id_capital_prestado').on('click', function () {
        window.location = '/inversion-inicial/';
    });
    $('#id_tmar').on('click', function () {
        window.location = '/tmar/';
    });
    $('#id_fne').on('click', function () {
        window.location = '/fne/';
    })
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

    /**
     * Opciones para el Flujo Neto de efectivo
     */
    $(document).on('click', '#btn_fne', function () {
        let ingresos = parseFloat($('#id_ingresos').val());
        let gastos = parseFloat($('#id_gastos').val());
        let depresiacion = parseFloat($('#id_depresiacion').val());
        let financiamiento = 0.0;
        let inflacion = 0.0;
        let modena = 1;

        if($('#id_financiamiento_val').val() !== ''){
            financiamiento = parseFloat($('#id_financiamiento_val').val());
        }
        if($('#id_inflacion_val').val() !== ''){
            inflacion = parseFloat($('#id_inflacion_val').val());
        }

        if($('#id_moneda').val() !== ''){
            modena = parseFloat($('#id_moneda').val());
        }

        let utilidad = ingresos - gastos - depresiacion - financiamiento;
        let isr = utilidad * 0.30;
        let ptu = utilidad * 0.10;
        let utilidad_inpuestos = utilidad - isr - ptu;
        let fne = utilidad_inpuestos + depresiacion - inflacion;
        fne = fne * modena;
        $('#r_fne').text(fne.toFixed(4));
    });

    $('#id_financiamiento').change(function() {
        // this will contain a reference to the checkbox
        if (this.checked) {
            $('#id_financiamiento_val').removeClass('dn');
            $('#id_inflacion_val').removeClass('dn');
        } else {
            $('#id_financiamiento_val').addClass('dn');
            $('#id_financiamiento_val').val('');

            $('#id_inflacion_val').addClass('dn');
            $('#id_inflacion_val').val('');
        }
    });

    $('#id_inflacion').change(function() {
    // this will contain a reference to the checkbox
        if (this.checked) {
            $('#id_moneda').removeClass('dn')
        } else {
            $('#id_moneda').addClass('dn');
            $('#id_moneda').val('');
        }
    });


});