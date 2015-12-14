
var options = {
  valueNames: [ 'billimage', 'lastaction', 'billsummary' ],
  page: 10,
  plugins: [ ListPagination({}) ]
};

var billsList = new List('billsSort', options);

$('#filter-senate').click(function() {
  billsList.filter(function(item) {
    var html = item.values().billimage;
    var div = document.createElement("div");
    div.innerHTML = html;
    var billimage = div.textContent || div.innerText || "";
    if (billimage.substring(0,1) == "S") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-house').click(function() {
  billsList.filter(function(item) {
    var html = item.values().billimage;
    var div = document.createElement("div");
    div.innerHTML = html;
    var billimage = div.textContent || div.innerText || "";
    if (billimage.substring(0,1) == "H") {
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
  $('#submitcomment').click(function(e) {
    e.preventDefault();
    //var comment_id = '#comment-' + form.bill_num;
    //console.log(comment_id);
    console.log(bill.bill_id);
    $.ajax({
      url: '/comment',
      data: $('#comment_id').serialize(),
      type: 'POST',
      success: function(response) {
      /*$("sentiment h3").after("Your latest comment:")response.comment;
        $("#comment").val("");  */
      },
      error: function(error) {
        console.log(error);
        console.log("FAILURE");
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