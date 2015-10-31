<?php 
$thisPage="New_Account"; 
include 'top.php'; ?>

<div class="maincontainer">
   
<div class="dashboard">
      <div class="dashhead" id="dashtop">
        Legislative Dash
      </div>
      
	<div class="dashhead" id="login">Create new account</div>    
		<div class="loginbox">
        	<form action="lib/newuser.php" method="POST">
          		<div class="loginbox">
            		<input type="text" name="username" id="username" placeholder="Username" /> 
            		<input type="email" name="email" id="email" placeholder="Email" />      			
            		<input type="password" name="password" id="password" placeholder="Password">
            		<input type="password" name="passconfirm" id="passwordconfirm" placeholder="Confirm password">
            		</div>
            		<label for="rememberme">Remember me:</label> 
            		<input type="checkbox" name="rememberme" value="1">
          			<input type="submit" value="Go">
        	</form>      
		</div>
	</div>
    
 <div class="billmain">
      <div class="active">
        <p>Most Active</p>
        <div class="billimage"><span>S 1081</span></div>
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
    </div>  
</div>
    
<?php include 'footer.php'; ?>