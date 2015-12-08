
var options = {
  valueNames: [ 'billimage', 'lastaction', 'billsummary' ],
  page: 10,
  plugins: [ ListPagination({}) ]
};

var billsList = new List('billsSort', options);

$('#filter-senate').click(function() {
  billsList.filter(function(item) {
    if (item.values().billimage.substring(0,1) == "S") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-house').click(function() {
  billsList.filter(function(item) {
    if (item.values().billimage.substring(0,1) == "H") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-none').click(function() {
  billsList.filter();
  return false;
 });

$(function() {
  $('#submitcomment').click(function() {
    $.ajax({
      url: '/comment',
      data: $('form').serialize(),
      type: 'POST',
      success: function(response) {
        console.log(response);
        $("sentiment h3").after("Your latest comment:").comment();
        $("#comment").val("");
      },
      error: function(error) {
        console.log(error);
        alert("FAILURE");
      }
    });
  });
});


/*
Not sure what this function was for...

$(document).ready(function () {
  $('ul.nav > li').click(function (e) {
   e.preventDefault();
   $('ul.nav > li').removeClass('active');
   $(this).addClass('active');
  });
});

*/