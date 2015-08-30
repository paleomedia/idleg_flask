<?php

if (!isset($_SESSION)) {
	session_start();
}

if (isset($_COOKIE["username"])) {
  $username = $_COOKIE["username"];
  $_SESSION["name"] = $username;
}
?>

<!DOCTYPE html>

<html>

<head>
  
  <link href='https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700' rel='stylesheet' type='text/css'>

  <title><?php if ($thisPage != "") {
    echo "$thisPage"; } ?> - Idaho Legislative Information Portal, Bills, Lawmakers & Data</title>
  <meta charset="utf-8" />
  <meta name="description" content="idleg: Idaho legislative bill information portal" />
  <meta name="keywords" content="Idaho, legislature, bills, laws, legislation" />
  <meta name="author" content="Nathaniel Hoffman" />  <!-- Note: Make dynamic based on page author -->
  <meta name="revised" content="<?php filemtime('index.php'); ?>" />  <!-- last mod of index.html -->
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link href="css/styles.css" type="text/scc" rel="stylesheet" />
  <link rel="shortcut icon" href="/images/favicon.ico" />

<!-- css fonts library -->
<link href="http://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet" />

<!-- jplist demo page styles -->
<link rel="stylesheet" href="normalize.css" type="text/css" />
<link rel="stylesheet" href="jplist-demo-pages.min.css" type="text/css" />

<!-- jQuery library -->		
<script src="../assets/js/vendor/jquery-1.10.0.min.js"></script>

<!-- jPList Core -->
<link href="jplist-core.min.css" rel="stylesheet" type="text/css" />
<script src="jplist-core.min.js"></script>

<!-- add here jPList controls and bundles -->
...

<!-- Example of jplist JavaScript options for PHP server side -->

<script>
$('document').ready(function(){
   $('#demo').jplist({
   
      itemsBox: '.list' 
      ,itemPath: '.list-item' 
      ,panelPath: '.jplist-panel'
      
      //data source
      ,dataSource: {
         
         type: 'server'
         ,server: {
         
            //jQuery ajax settings
            ajax:{
              url: 'server.php'
              ,dataType: 'html'
              ,type: 'POST'
            }

            ,serverOkCallback: function(serverData, statuses, ajax, response){
                //server callback in case of success 
            }

            ,serverErrorCallback: function(statuses){
                //server callback in case of fail 
            }
         }

         //render function for json + templates like handlebars, xml + xslt etc.
         ,render: null
       }

   });
});
</script> 


</head>

<header>
    <div class="tops">
      <div id="topline">
        <div class="socials">
          <ul>
            <li class="social">
              <a href="https://twitter.com/search?q=%23idleg&src=typd"><img src="images/twittericon.png" width="24px" height="24px">
              </a>
            </li>
            <li class="social">
              <a href="http://idleg.info/rss"><img src="images/RSS-Icon.png" width="24px" height="24px">
              </a>
            </li>
            <li class="social">
              <a href="https://github.com/paleomedia/idleg"><img src="images/Github-Icon.png" width="24px" height="24px">
              </a>
            </li>
            <li class="social">
              <a href="mailto:editor@idleg.info"><img src="images/Email-Icon.png" width="24px" height="24px">
              </a>
            </li>
            <li class="social">
              <a href="http://facebook.com"><img src="images/Facebook-Icon.png" width="24px" height="24px">
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div id="logoline">
        <div id="logo">
          <h1>#IDleg</h1>
        </div>
        <div id="slogan">
          <h2>An Idaho social-political network</h2>
        </div>
      </div>

<?php include('menu.php'); ?>

</header>

