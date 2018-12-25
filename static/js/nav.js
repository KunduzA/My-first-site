function onReady4(){
    $(".clickMenu").hover(function(){
         $(".visibleMenu").toggle();
    })
    $(".visibleMenu").hover(function(){
         $(".visibleMenu").toggle();
    })
     $(".clickMenu-w").hover(function(){
         $(".visibleMenu-woman").toggle();
    })
     $(".visibleMenu-woman").hover(function(){
         $(".visibleMenu-woman").toggle();
    })
    $(".hidden-text").click(function(){
         $(".more-dropmenu").toggle();
    })
}

$(document).ready(onReady4);