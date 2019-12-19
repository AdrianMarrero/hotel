$(document).ready(function(){
    $('#msj_error').hide();

    $('#datepicker').datepicker({
        uiLibrary: 'bootstrap4',
        format: 'dd/mm/yyyy',
        disableDates:  function (date) {
            var d = new Date();
            if (d.getFullYear() === date.getFullYear()){
                return true;
            } else {
                return false;
            }
        }
    });
    $('#datepicker2').datepicker({
        uiLibrary: 'bootstrap4',
        format: 'dd/mm/yyyy',
        disableDates:  function (date) {
            var d = new Date();
            if (d.getFullYear() === date.getFullYear()){
                return true;
            } else {
                return false;
            }
        }
    });

    $("#form1").submit(function(e){
        $('#msj_error').hide();
        $('#msj_error').text('');
        var date_start_comp;
        var date_end_comp;
        var $datetimepicker = $('#datepicker').datepicker();
        var $datetimepicker2 = $('#datepicker2').datepicker();
        var date_start = $datetimepicker.value();
        if(date_start === ''){
            $('#msj_error').text('Introduce fecha de entrada');
            $('#msj_error').show();
            return false;
        }
        var date_end = $datetimepicker2.value();
        if(date_end === ''){
            $('#msj_error').text("Introduce fecha de salida");
            $('#msj_error').show();
            return false;
        }
        var formatted_date_start = date_start.split("/");
        var formatted_date_end = date_end.split("/");
        formatted_date_start = formatted_date_start[1] + "/" + formatted_date_start[0] + "/" + formatted_date_start[2];
        formatted_date_end = formatted_date_end[1] + "/" + formatted_date_end[0] + "/" + formatted_date_end[2];
        date_start_comp =  new Date(formatted_date_start).getTime();
        date_end_comp =  new Date(formatted_date_end).getTime();
        if(date_start_comp > date_end_comp){
            $('#msj_error').text("fecha de entrada es mayor a la de salida");
            $('#msj_error').show();
            return false;
        }else if(date_start_comp === date_end_comp){
                $('#msj_error').text("La fecha de entrada no puede ser igual a la de salida");
                $('#msj_error').show();
                return false;
        }else if(date_start_comp > date_end_comp){
            $('#msj_error').hide();
            $('#msj_error').text('');
            return true;
        }
    }); 



});

function hide(){
    $('#msj_error').hide();
}

function buscar(){
    var $datetimepicker = $('#datepicker').datepicker();
    var $datetimepicker2 = $('#datepicker2').datepicker();
    var dias = restaFechas($datetimepicker.value(),$datetimepicker2.value());
    console.log(dias)
    var num_huspedes = $('#FormControlSelect').val();
    console.log($datetimepicker.value());
    console.log($datetimepicker2.value());
    console.log(num_huspedes);
}



restaFechas = function(f1,f2){
    var aFecha1 = f1.split('/');
    var aFecha2 = f2.split('/');
    var fFecha1 = Date.UTC(aFecha1[2],aFecha1[1]-1,aFecha1[0]);
    var fFecha2 = Date.UTC(aFecha2[2],aFecha2[1]-1,aFecha2[0]);
    var dif = fFecha2 - fFecha1;
    var dias = Math.floor(dif / (1000 * 60 * 60 * 24));
    return dias;
 }
