
$(document).ready(function(){
  $('input').keyup(function(){
      let textsaisi = $(this).val();
      let attrName = $(this).attr('name');
      let validatorElement = ".div-error-"+attrName;
if(textsaisi===""){
   if(!$(this).hasClass('is-invalid')){
       $(this).addClass('is-invalid');
       $(validatorElement).show();
   }
}  else {
    $(this).removeClass('is-invalid');
     $(validatorElement).hide();
}

})
})
