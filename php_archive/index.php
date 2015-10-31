<?php
$thisPage = 'Home'; 
require_once "lib/classes/dao.php";
include 'lib/api_functions.php';

  $dao = new Dao();
  
include 'top.php'; ?>

  <body>

  <div class="maincontainer">
    
<?php include 'dash.php'; ?>

<div class="billmain">
  
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
  <script src="js/ajax.js" type="text/javascript"></script>
  
  Filter bills:
  <ul>
    <li>Most comments</li>
    <li>Recent bills</li>
    <li>Signed</li>
  </ul>
  
  <?php
  
    $bill_list = $dao->getBills();

    foreach ($bill_list as $bill) { 
      $action_date = last_action($bill["bill_id"]) ?>
      <div class="active">
        <p>Active Bills</p>
      <div class="billimage"><span><?php echo $bill["bill_name"]; ?></span></div>
      <div class="lastaction">Last Action: <?php echo $action_date; ?> </div>
      <div class="billsummary"><?php echo $bill["title"]; ?></div>
      
      <div class="comments">
          <div class="commentbox">
            <form name="commentForm" action="lib/handler.php" method="POST">
              <textarea name="comment" rows="4" id="comment" placeholder="Write comments or testimony here, select pro, neutral or anti, and press Submit."></textarea>
              <label>Yea, Nay or Neutral?</label>
              <label>
                <input type="radio" name="vote" value="pro" id="pro" /><img class="prolabel" src="images/thumbs_up.png" />
              </label>
              <label>
                <input type="radio" name="vote" value="anti" id="anti" /><img class="antilabel" src="images/thumbs_down.png" />
              </label>
              <label class="neutrallabel">
                <input type="radio" name="vote" value="neutral" id="neutral" checked="checked" />?</label>
              <input type="submit" name="commentButton" value="Submit" />
              <input type="hidden" name="form" value="comment" />
              <input type="hidden" name="bill" value="<?php echo $bill["bill_id"]; ?>" />
            </form>
          </div>
          
            <div class="pro"><h3>Yea</h3>
              <?php $comments = $dao->getComments($bill["bill_id"], "pro");
              foreach ($comments as $comment) { 
              ?>
              <span><?php echo $comment["username"]; ?> says:</span> <?php echo $comment["comment"] . "<br />";
              echo "DATE:" . $comment["date"] . "<br />"; ?> 
              <?php } ?>
            </div> 
            
            <div class="neutral"><h3>Neutral</h3>
              <?php $comments = $dao->getComments($bill["bill_id"], "neutral");
              foreach ($comments as $comment) {  ?>
              <span><?php echo $comment["username"]; ?> says:</span> <?php echo $comment["comment"] . "<br />";
              echo "DATE:" . $comment["date"] . "<br />"; ?>
              <?php } ?>
            </div>

            <div class="anti"><h3>Nay</h3>
              <?php $comments = $dao->getComments($bill["bill_id"], "anti");
              foreach ($comments as $comment) {  ?>
              <span><?php echo $comment["username"]; ?> says:</span> <?php echo $comment["comment"] . "<br />";
              echo "DATE:" . $comment["date"] . "<br />";  ?>
              <?php } ?>
            </div>
      </div>
    </div>
      
    <?php } ?>

  </div>
</div>

  

<?php include 'footer.php'; ?>  