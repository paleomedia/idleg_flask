
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


//Start Angular functions
var app = angular.module('newComment', []);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('//');
    $interpolateProvider.endSymbol('//');
});

  app.controller('newCommentController', ['$scope', '$log', '$http',
    function($scope, $log, $http) {

    $scope.getComment = function(comment) {
      $scope.master = angular.copy(comment);
        $log.log("test");
        console.log("controller");
        cosole.dir($scope);
      //get new comment
      var newComment = $scope.comment.text;
      //var csrfToken = document.getElementsByName('csrf_token')[0].value
      var csrfToken = $scope.comment.csrf;
      var billNum = $scope.comment.bill;
      var position = $scope.comment.position;
      $log.log(newComment);
      $log.log(billNum);

      //add comment to database
      $http({
        method: 'POST',
        url: '/comment',
        data: $.param({"comment": newComment, "csrfToken": csrfToken, "billNum": billNum, "position": position}),
        headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
      }).
        
        success(function(comment) {
          $log.log(comment);
        }).
        error(function(error) {
          $log.log(error);
        });
    };
    }
  ]);




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
      $("sentiment h3").after("Your latest comment:")response.comment;
        $("#comment").val("");
      },
      error: function(error) {
        console.log(error);
        console.log("FAILURE");
      }
    });
  });
});

*/