function onReady2(){
    $(document).on("click",".before", function(){
        var form=$("form[name='form']");
        form.css("display", "block");
        $(".before").replaceWith(form);
    });

    $(document).on("click", "input[name='submit']", function(){
        var name = $("input[name='text']").val();
        $('#form').hide();
        $('div.before').show();
         alert("Уважаемый(ая) "+name+" ,ваше сообщение принято");
    });
}

$(document).ready(onReady2);
