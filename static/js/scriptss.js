function onReady5(){
    $('#gmenu a').each(function () {
        var location = window.location.href;
        var link = this.href;
        var result = location.match(link);
        if(result != null) {
            $(this).addClass('active');
        }
    });
}

function onReady3(){
    $('.calculator select').change(function(){
        $edition = $('select#edition').val();
        $size = $('select#size').val();
        $clothes = $('select#clothes').val();
        $size=$('select#size option:selected').attr('data-size');
        $price=$('select#clothes option:selected').attr('data-price');
        $finalPrice=$edition * $size *$price;
        $('span#finalPrice').text($finalPrice);
    })
}

$(document).ready(onReady5);
$(document).ready(onReady3);