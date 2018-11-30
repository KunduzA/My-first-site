function onReady(){
    var $top=$(".top");
    $(window).on("scroll", function(){
        if($(window).scrollTop()>=100){
            $top.fadeIn();
        }else{
            $top.fadeOut();
        }
    });

$top.on("click", function(){
    $("html,body").animate({scrollTop:0},900)
    });
}

$(document).ready(onReady);