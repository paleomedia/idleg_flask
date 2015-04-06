<?php
$thisPage = 'Home'; 
require_once "Dao.php";
  $dao = new Dao();
include 'top.php'; ?>

  <body>

  <div class="maincontainer">
    
<?php include 'dash.php'; ?>
    
    <div class="billmain">
      <div class="active">
        <p>Most Active</p>
        <div class="billimage"><span>S 1081</span></div>
        <div class="lastaction">Passed Senate, 2/20/2015</div>
        <div class="billsummary">Summary: HEALTH CARE - Amends existing law to provide reserves and surplus requirements of public postsecondary educational institutions with a public postsecondary educational institution plan for health care benefits.</div>
        <div class="comments">
          <div class="commentbox">
            <form name="commentForm" action="handler.php" method="POST">
              <textarea name="comment" rows="4" placeholder="Write comments or testimony here, select pro, neutral or anti, and press Go."></textarea>
              <label>Yea or Nay?</label>
              <label>
                <input type="radio" name="vote" value="pro" /><img class="prolabel" src="images/thumbs_up.png" />
              </label>
              <label class="neutrallabel">
                <input type="radio" name="vote" value="neutral" />?</label>
              <label>
                <input type="radio" name="vote" value="anti" /><img class="antilabel" src="images/thumbs_down.png" />
              </label>
              <input type="submit" name="commentButton" value="Comment" />
              <input type="hidden" name="form" value="comment">
            </form>
          </div>
          <?php
    $comments = $dao->getComments();
    echo "<table>";
    foreach ($comments as $comment) {
      echo "<tr>";
      echo "<td>" . $comment["comment"] . "</td>";
 #    echo "<td>" . $comment["created"] . "</td>";
      echo "</tr>";
    }
    echo "</table>";
    ?>
          </div>
      </div>

<!--    <div class="active">
        <p>Also Active</p>
        <div class="billimage"><span>S 1082</span>
        </div>
        <div class="lastaction">Passed Senate, 2/20/2015</div>
        <div class="billsummary">Summary: HEALTH CARE - Amends existing law to provide reserves and surplus requirements of public postsecondary educational institutions with a public postsecondary educational institution plan for health care benefits.</div>
        <div class="comments">
          <div class="commentbox">
            <form>
              <textarea name="comment" rows="4" placeholder="Write comments or testimony here, select pro, neutral or anti, and press Go."></textarea>
              <label>Yea or Nay?</label>
              <label>
                <input type="radio" name="vote" value="pro" /><img class="prolabel" src="images/thumbs_up.png" />
              </label>
              <label class="neutrallabel">
                <input type="radio" name="vote" value="neutral" />?</label>
              <label>
                <input type="radio" name="vote" value="anti" /><img class="antilabel" src="images/thumbs_down.png" />
              </label>


              <input type="submit" value="Go" />
            </form>
          </div>
          <div class="pro">
            <span>Conrad says:</span> Best bill ever ... Lorem ipsum dolor sit amet, nobis suavitate iracundia ei his, ad nihil eirmod quo, viris temporibus qui eu. Et idque omnes instructior usu, qui ut posse everti lobortis, id his deserunt assentior.
            Quo oratio senserit te, verterem constituto usu ut. Te pro aeque equidem maluisset, ponderum consetetur sea no. At volutpat torquatos adipiscing est, tempor temporibus in cum.
          </div>
          <div class="neutral">
            <span>Sarah says:</span> Could go either way... Lorem ipsum dolor sit amet, nobis suavitate iracundia ei his, ad nihil eirmod quo, viris temporibus qui eu. Et idque omnes instructior usu, qui ut posse everti lobortis, id his deserunt assentior.
            Quo oratio senserit te, verterem constituto usu ut. Te pro aeque equidem maluisset, ponderum consetetur sea no. At volutpat torquatos adipiscing est, tempor temporibus in cum.
          </div>
          <div class="anti">
            <span>José says:</span> Impeach! Impeach! Lorem ipsum dolor sit amet, nobis suavitate iracundia ei his, ad nihil eirmod quo, viris temporibus qui eu. Et idque omnes instructior usu, qui ut posse everti lobortis, id his deserunt assentior.
            Quo oratio senserit te, verterem constituto usu ut. Te pro aeque equidem maluisset, ponderum consetetur sea no. At volutpat torquatos adipiscing est, tempor temporibus in cum.
          </div>
        </div>
      </div>

    </div> -->

  </div>

<?php include 'footer.php'; ?>  