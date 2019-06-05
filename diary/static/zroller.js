$( document ).ready(function() {
  console.log("ZROLLER.JS LOADED");

  //Script Variables
  var pages = [];
  var canSwitch = true;
  var SWITCHDELAY = 1200; // in ms
  var DEBUG = true;
  var ENABLE = true; // enable the zroll effect
  var MENU_ENABLE = true; // enables the menu indicating the visible page

  //Script
  if (ENABLE) {
    // gathering all pages into an array
    $('.zroller').each(function(i, obj) {
        pages.push($(this));
    });

    if (MENU_ENABLE) {
      //Injecting icons stylesheet for the menu
      $('head').append('<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous" />')
      // injecting styles for zr-menu
      $("<style>").prop("type", "text/css").html("\
      #zr-menu {\
          height : " + pages.length * 30 + "px;\
          display : table;\
          z-index : 100000;\
          position: absolute;\
          top: 50%;\
          -ms-transform: translateY(-50%);\
          transform: translateY(-50%);\
          margin-left : calc(100vw - 25px);\
      }\
      \
      .zr-menuItem {\
        display: table-row;\
        vertical-align: middle;\
        opacity : 0.5;\
      }\
      \
      .zroller {\
        position: absolute;\
        height : 100vh;\
        width : 100vw;\
        opacity: 0;\
        z-index: 0;\
      }").appendTo("head");

      // creating the menu
      var menuDiv = '<div id = "zr-menu">';
      for (i = 0 ; i < pages.length ; i++) {
        menuDiv += '<i id = "zr-i' + i  + '" class = "zr-menuItem fas fa-circle"></i>';
      }
      menuDiv += "</div>" ;
      var $menuDiv = $(menuDiv);
      $("body").append($menuDiv);
    }

    // fade first page into view
    fadePage(0, true);

    // NO Firefox Support Lmao!!!
    $(window).bind('mousewheel DOMMouseScroll', function(e){
          var target;
          if (canSwitch){
            for (i = 0 ; i < pages.length ; i ++) {
              if(pages[i].css("opacity") == 1) {
                fadePage(i, false); // fade visible page out of view

                if (e.originalEvent.wheelDelta / 100 > 0) { //Scrollng UP
                  if (i == 0) {
                    target = pages.length - 1;
                    if (DEBUG) console.log("Loading Page " + (pages.length));
                  } else {
                    target = i-1;
                    if (DEBUG) console.log("Loading Page " + (i));
                  }
                } else {
                  if (i == pages.length - 1) {
                    target = 0;
                    if (DEBUG) console.log("Loading Page " + 1);
                  } else {
                    target = i+1;
                    if (DEBUG) console.log("Loading Page " + (i+2));
                  }
                }

                fadePage(target, true); //fading target into view
              }
            }
            canSwitch = false;

            //Delay for next page switch
            setTimeout(function(){
                canSwitch = true;
              }, SWITCHDELAY
            );

          }
      });
  }

  function fadePage(pI, fadeIn) {
    // shows with index pI in the pages array
    var opacity;
    var mOpacity;
    if (fadeIn)  {
      opacity = 1;
      mOpacity = 1;
    }
    else {
      opacity = 0;
      mOpacity = 0.5;
    }

    pages[pI].fadeTo("fast", opacity);
    pages[pI].css("z-index", opacity);
    $("#zr-i" + pI).fadeTo("fast", mOpacity);
  }


});
