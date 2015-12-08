// ajax.js file
$(function() {
$("#form").submit(function(){
    var values = $("form").serialize();
    var comment = $("#comment").val();
    var sentiment = "." . $("input:radio[name=vote]:checked").val();
    
    console.log(values);
    $.ajax({
      type: "POST",
      url: "../lib/handler.php",
      data: values,
      success: function() {
        $("sentiment h3").after("Your latest comment:").comment);
        $("#comment").val("");
      },
      error: function () {
        alert("FAILURE");
      }
    });
    return false;
  });

});