$(document).ready(function(){
  $('.delete-entry').on('click', function(e){
    $target = $(e.target);
    const id = $target.attr('data-id');
    $.ajax({
      type:'DELETE',
      url:'/entries/'+id,
      success:function(response){
        alert('Deleting Article');
        window.location.href='/';
      },
      error:function(err){
        console.log(err);
      }
    });
  });
});
