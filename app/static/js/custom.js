/*var options = {
  valueNames: [ 'billimage', 'lastaction', 'billsummary' ],
  page: 10,
  plugins: [
    ListPagination({
      innerWindow: 2,
      outerWindow: 1
    })
  ]
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
 */
 
$("#submitcomment").click(function (event) {
  if (!$("input:radio[name='position']:checked").val()>0) {
    alert('Please select your position on the bill before submitting comment.');
    event.preventDefault();
  } });

$(function() {
  $('.commentForm').submit(function(e) {
    e.preventDefault();
    var parent = $(this).parent().parent();
    var position = "." + $(this).find("input[type=radio]:checked").val();
    var commentBox = parent.find(position);
    
    $.ajax({
      url: '/comment',
      data: $(this).serialize(),
      type: 'POST',
      success: function(response) {
        var newComment = response.comment;
        commentBox.append('<li><span class="commentText"><p>' + newComment + '</p></span><span class="commenterName"><p>You</p></span><span class="date sub-text">Just now</span></li>');
        $('input[type=text], textarea').val('');
      },
      error: function(error) {
        console.log(error);
        console.log("FAILURE");
      }
    });
  });
});


/*
$('#filter-year').change( function() {
  var billyear = $(this).val();
  var csrftoken = $('meta[name=csrf-token]').attr('content')
  })
  
  
})
*/
/*
$(function() {
  $('#filter-year').change(function(e) {
    // e.preventDefault();
    var billyear = $(this).val();
    var csrftoken = $('meta[name=csrf-token]').attr('content')
    console.log(billyear);
    
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken)
            }
        }
    })
    
    $.ajax({
      url: '/loadBills',
      data: {'billyear':billyear},
      type: 'POST',
      success: function(response) {
        console.log(moreBills);
      },
      error: function(error) {
        console.log(error);
        console.log("FAILURE");
      }
      });
    });
  });
*/


/*
$(function() {
  $('#submitcomment').click(function(e) {
    e.preventDefault();
    $.ajax({
      url: '/comment',
      data: $("#"+(e.toElement.form.id)).serialize(),
      type: 'POST',
      success: function(response) {
      console.log(response.comment);
      /*$("sentiment h3").after("Your latest comment:")response.comment;
        $("#comment").val("");  */
/*      },
      error: function(error) {
        console.log(error);
        console.log("FAILURE");
      }
    });
  });
});

*/


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