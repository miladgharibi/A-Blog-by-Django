let menuToggle = document.querySelector('.menuBtn');
menuToggle.onclick = (event) => {
    document.querySelector('.navbar ul').classList.toggle('active');
    document.querySelector('.menuBtn').classList.toggle('active');    
}

let title_input = document.querySelector('#id_title');

if (title_input){
  $("#id_title").keyup(function() {
    var Text = $(this).val();
    Text = Text.toLowerCase();
    Text = Text.replace(/[^a-zA-Z0-9]+/g,'-');
    $("#id_slug").val(Text);        
  });
}


function scroll_to_about(event){
  var pageId = $('.about');
  if (window.location.pathname != '/'){
    window.location.pathname = '/';
    $("html, body").animate({ scrollTop: pageId.offset().top }, 10);
  
  } else {
    $("html, body").animate({ scrollTop: pageId.offset().top }, 10);
  };
}

function scroll_to_contact(event){
  var pageId = $('.contact');
  if (window.location.pathname != '/'){
    window.location.pathname = '/';
    $("html, body").animate({ scrollTop: pageId.offset().top }, 10);
  
  } else {
    $("html, body").animate({ scrollTop: pageId.offset().top }, 10);
  };
}