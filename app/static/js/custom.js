
var options = {
  valueNames: [ 'billimage', 'lastaction', 'billsummary' ],
  page: 10,
  plugins: [
    ListPagination({
      innerWindow: 2,
      ourterWindow: 1
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

/*
$(function() {
  $('#submitcomment').click(function(e) {
    e.preventDefault();
    $.ajax({
      url: '/comment',
      data: $('form').serialize(),
      type: 'POST',
      success: function(response) {
        console.log(response.comment);
        var $newComment = $('<p>').text(response.comment);
        $('#comment').append($newComment);
      },
      error: function(error) {
        console.log(error);
        console.log("FAILURE");
      }
    });
  });
});
*/

(function () {

  'use strict';

  angular.module('newComment').
  component('newComment', {
    template:
      '<li>' +
        '<div class="commenterImage">
          <img src="" />
        </div>
        <div class="commenterName">
          <p>{{ comment.author }}</p>
        </div>
       <div class="commentText">
        <p>{{ comment.body }}</p> <span class="date sub-text">{{ comment.timestamp }}</span>
        </div>
      </li>
    
    
    
  })

  .controller('idLegController', ['$scope',
    function($scope) {
      
    $scope.getComment = function() {
      $log.log("test");
      
      //get comment
      var newComment = $scope.comment;
      
      // fire the API request
      $http.post('/comment', {"comment": newComment}).
        success(function(results) {
          $log.log(results);
        }).
        error(function(error) {
          $log.log(error);
        });
    };
    }
  ]);
})();

//can't figure out how to pass specific, dynamic id to this...

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