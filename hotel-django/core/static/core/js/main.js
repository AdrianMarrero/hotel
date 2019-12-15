$(document).ready(function(){
    $('#datepicker').datepicker({
        uiLibrary: 'bootstrap4',
        format: 'dd/mm/yyyy',
        value: 'entrada',
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
        value: 'salida',
        disableDates:  function (date) {
            var d = new Date();
            if (d.getFullYear() === date.getFullYear()){
                return true;
            } else {
                return false;
            }
        }
    });



});

function buscar(){
    var $datetimepicker = $('#datepicker').datepicker();
    var $datetimepicker2 = $('#datepicker2').datepicker();
    var num_huspedes =  $('#FormControlSelect').val();
    console.log($datetimepicker.value());
    console.log($datetimepicker2.value());
    console.log(num_huspedes);
}