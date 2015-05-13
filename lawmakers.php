<?php
    $thisPage="Lawmakers"; 
    include 'top.php'; 
    require_once("lib/classes/dao.php"); ?>
    <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script> -->
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.9.1/jquery-ui.min.js"></script>
    <script src="js/shapeshift.min.js" type="text/javascript"></script>     
  
    <div class="maincontainer">
 
    <?php include 'dash.php'; ?>

    <div class="billmain">
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