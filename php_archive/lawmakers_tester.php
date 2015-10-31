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
  
    <!-- jPList core -->		
  <link href="/css/jplist-core.min.css" rel="stylesheet" type="text/css" />
  <script src="/js/jplist/jplist-core.min.js"></script>	
  
  <!-- sort bundle -->
  <script src="/js/jplist/jplist.sort-bundle.min.js"></script>
  
  <!-- textbox filter control -->
  <script src="/js/jplist/jplist.textbox-control.min.js"></script>
  <link href="/css/jplist-textbox-control.min.css" rel="stylesheet" type="text/css" />
  
  <!-- jPList pagination bundle -->
  <script src="/content/js/jplist/jplist.pagination-bundle.min.js"></script>
  <link href="/content/css/jplist-pagination-bundle.min.css" rel="stylesheet" type="text/css" />		
  
  <!-- jPList history bundle -->
  <script src="/content/js/jplist/jplist.history-bundle.min.js"></script>
  <link href="/content/css/jplist-history-bundle.min.css" rel="stylesheet" type="text/css" />
  
  <!-- jPList toggle bundle -->
  <script src="/content/js/jplist/jplist.filter-toggle-bundle.min.js"></script>
  <link href="/content/css/jplist-filter-toggle-bundle.min.css" rel="stylesheet" type="text/css" />
  
  <!-- jPList views control -->
  <script src="/content/js/jplist/jplist.views-control.min.js"></script>
  <link href="/content/css/jplist-views-control.min.css" rel="stylesheet" type="text/css" />
  
  <!-- jPList preloader control -->
  <script src="/content/js/jplist/jplist.preloader-control.min.js"></script>
  <link href="/content/css/jplist-preloader-control.min.css" rel="stylesheet" type="text/css" />
  
  <!-- Handlebars Templates Library: http://handlebarsjs.com -->
  <script src="http://cdnjs.cloudflare.com/ajax/libs/handlebars.js/2.0.0-alpha.4/handlebars.min.js"></script>
  
  <!-- handlebars template -->
  <script id="jplist-template" type="text/x-handlebars-template">
   {{#each this}}
                  
      <div class="list-item box">	
         <div class="img left">
            <img src="{{image}}" alt="" title=""/>
         </div>
                        
         <div class="block right">
            <p class="title">{{title}}</p>
            <p class="desc">{{description}}</p>
            <p class="like">{{likes}} Likes</p>
            <p class="theme">{{keyword1}}, {{keyword2}}</p>
         </div>
      </div>
                     
   {{/each}}
  </script>	
  
  <script>
   $('document').ready(function () {

      var $list = $('#demo .list')
         ,template = Handlebars.compile($('#jplist-template').html());

      $('#demo').jplist({

         itemsBox: '.list'
         ,itemPath: '.list-item'
         ,panelPath: '.jplist-panel'

         //data source
         ,dataSource: {

            type: 'server'
            ,server: {

            //ajax settings
            ajax: {
               url: '/content/data-sources/php-mysql-demo/server-json.php'
               ,dataType: 'json'
               ,type: 'POST'
            }
         }

         //render function for json + templates like handlebars, xml + xslt etc.
         ,render: function (dataItem, statuses) {
            $list.html(template(dataItem.content));
         }
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

<?php
    $thisPage="Lawmakers"; 
   // include 'top.php'; 
    require_once("lib/classes/dao.php"); ?>
    <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script> -->
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.9.1/jquery-ui.min.js"></script>
    <!-- <script src="js/shapeshift.min.js" type="text/javascript"></script>     -->
  
    <div class="maincontainer">
 
    <?php include 'dash.php'; ?>

    <div class="billmain">
      
      <!-- demo -->
<div id="demo">
   
   <!-- panel -->
   <div class="jplist-panel">						
      
      <!-- reset button -->
      <button 
         type="button" 
         class="jplist-reset-btn"
         data-control-type="reset" 
         data-control-name="reset" 
         data-control-action="reset">
         Reset  <i class="fa fa-share"></i>
      </button>

      <!-- items per page dropdown -->
      <div
         class="jplist-drop-down"
         data-control-type="items-per-page-drop-down"
         data-control-name="paging"
         data-control-action="paging">

         <ul>
            <li><span data-number="3"> 3 per page </span></li>
            <li><span data-number="5"> 5 per page </span></li>
            <li><span data-number="10" data-default="true"> 10 per page </span></li>
            <li><span data-number="all"> View All </span></li>
         </ul>
      </div>

      <!-- sort dropdown -->
      <div
         class="jplist-drop-down"
         data-control-type="sort-drop-down"
         data-control-name="sort"
         data-control-action="sort">

         <ul>
            <li><span data-path="default">Sort by</span></li>
            <li><span data-path=".title" data-order="asc" data-type="text">Title A-Z</span></li>
            <li><span data-path=".title" data-order="desc" data-type="text">Title Z-A</span></li>
            <li><span data-path=".desc" data-order="asc" data-type="text">Description A-Z</span></li>
            <li><span data-path=".desc" data-order="desc" data-type="text">Description Z-A</span></li>
            <li><span data-path=".like" data-order="asc" data-type="number">Likes asc</span></li>
            <li><span data-path=".like" data-order="desc" data-type="number">Likes desc</span></li>
         </ul>
      </div>

      <!-- text filter by title -->
      <div class="text-filter-box">
                                             
         <!--[if lt IE 10]>
         <div class="jplist-label">Filter by Title:</div>
         <![endif]-->
                        
         <input 
            data-path=".title" 
            data-button="#title-search-button"
            type="text" 
            value="" 
            placeholder="Filter by Title" 
            data-control-type="textbox" 
            data-control-name="title-filter" 
            data-control-action="filter"
         />
                        
         <button 
            type="button" 
            id="title-search-button">
            <i class="fa fa-search"></i>
         </button>
      </div>
                     
      <!-- text filter by description -->
      <div class="text-filter-box">
                                                
         <!--[if lt IE 10]>
         <div class="jplist-label">Filter by Description:</div>
         <![endif]-->
                        
         <input 
            data-path=".desc" 
            data-button="#desc-search-button"
            type="text" 
            value="" 
            placeholder="Filter by Description" 
            data-control-type="textbox" 
            data-control-name="desc-filter" 
            data-control-action="filter"
         />	
                        
         <button 
            type="button" 
            id="desc-search-button">
            <i class="fa fa-search"></i>
         </button>
      </div>
                     
      <!-- checkbox filters -->
      <div
         class="jplist-group"
         data-control-type="checkbox-group-filter"
         data-control-action="filter"
         data-control-name="themes">

         <input
            data-path=".architecture"
            id="architecture"
            type="checkbox"
         />

         <label for="architecture">Architecture</label>

         <input
            data-path=".christmas"
            id="christmas"
            type="checkbox"
         />

         <label for="christmas">Christmas</label>

         <input
            data-path=".nature"
            id="nature"
            type="checkbox"
         />

         <label for="nature">Nature</label>

         <input
            data-path=".lifestyle"
            id="lifestyle"
            type="checkbox"
         />

         <label for="lifestyle">Lifestyle</label>
      </div>

      <div
         class="jplist-group"
         data-control-type="checkbox-group-filter"
         data-control-action="filter"
         data-control-name="colors">

         <input
            data-path=".red"
            id="red-color"
            type="checkbox"
         />

         <label for="red-color">Red</label>

         <input
            data-path=".green"
            id="green-color"
            type="checkbox"
         />

         <label for="green-color">Green</label>

         <input
            data-path=".blue"
            id="blue-color"
            type="checkbox"
         />

         <label for="blue-color">Blue</label>

         <input
            data-path=".brown"
            id="brown-color"
            type="checkbox"
         />

         <label for="brown-color">Brown</label>
                        
      </div>

      <!-- list / grid view -->
      <div 
         class="jplist-views" 
         data-control-type="views" 
         data-control-name="views" 
         data-control-action="views"
         data-default="jplist-list-view">
                        
         <button type="button" class="jplist-view jplist-list-view" data-type="jplist-list-view"></button>
         <button type="button" class="jplist-view jplist-grid-view" data-type="jplist-grid-view"></button>
      </div>
                     
      <!-- pagination results -->
      <div 
         class="jplist-label" 
         data-type="Page {current} of {pages}" 
         data-control-type="pagination-info" 
         data-control-name="paging" 
         data-control-action="paging">
      </div>
                        
      <!-- pagination -->
      <div 
         class="jplist-pagination" 
         data-control-type="pagination" 
         data-control-name="paging" 
         data-control-action="paging">
      </div>	

      <!-- preloader for data sources -->
      <div 
         class="jplist-hide-preloader jplist-preloader"
         data-control-type="preloader" 
         data-control-name="preloader" 
         data-control-action="preloader">
         <img src="/content/img/common/ajax-loader-line.gif" alt="Loading..." title="Loading..." />
      </div>		
      
   </div>				 
   
   <!-- HTML data -->   
   <div class="list">
      
      <!-- item 1 -->
      <div class="list-item">	
         ...
      </div>
      
      <!-- item 2 -->
      <div class="list-item">	
         ...
      </div>
      
      ...
      
   </div>
   
   <!-- no results found -->
   <div class="jplist-no-results">
      <p>No results found</p>
   </div>
               
</div>
      
      
        <div class="lawmaker">

            <?php $dao = new Dao();
            $legislators = $dao->getLegislators();
            foreach ($legislators as $legislator) { ?>
            
            <div>
                <div class="leg_img">
                    
                    <img src="<?php echo $legislator["photo_url"]; ?>" alt="<?php echo $legislator["last_name"]; ?>" />
                    <h2><span><?php echo $legislator["first_name"] . " " . $legislator["last_name"] . ", " . $legislator["party"] . " (". $legislator["district"] . ")"; ?></span></h2>
                </div>
        
            </div>        
            <?php } ?>
         </div>    

     <script type="text/javascript">
        $(document).ready(function(){
	$('.lawmaker').shapeshift(
	    {
    align:'left',
    minColumns:3
  });
  $(".ss-container").trigger("ss-shuffle")
});</script>

    </div>
    </div>
    
    
<?php include 'footer.php'; ?>