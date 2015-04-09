<div class="dashboard">
      <div class="dashhead" id="dashtop">
        Legislative Dash
      </div>
      <div id="search">
        <form>
          <input type="submit" value="Go">
          <div>
            <input type="search" name="search" placeholder="Search bills, legislators, etc...." autocomplete="on">
          </div>
        </form>
      </div>   

      <div class="dashhead" id="login">Login</div>

 	<?php if (isset($_SESSION["name"])) { ?>
 		 <div class="loginbox">
 		 <div class="dashitem">
 			<p>You are logged in as <?= $_SESSION["name"] ?>.</p>
 			<?php var_dump($_SESSION); ?>
 		</div>
 			<form id="logout" action="logout.php" method="post">
 				<input type="submit" value="Log out" />
 				<input type="hidden" name="logout" value="true" />
 			</form>
 		</div>
    
    <?php } elseif (isset($_SESSION["flash"])) {   #temp message across page redirects
	?>
		<div class="dashitem"><?= $_SESSION["flash"] ?> </div>
			<div class="loginbox">
        	<form action="login.php" method="POST">
          		<div class="loginbox">
            		<input type="text" name="username" id="username" placeholder="Username" />
          		</div>
          			<input type="submit" value="Go">
          		<div>
            		<input type="password" name="password" id="password" placeholder="Password">
          		</div>
        	</form>
        <p span id="newuser">or <a href="newaccount.php">create new account</a>
        </p>
        </span>
        </div>
	
	<?php
		unset($_SESSION["flash"]);
	}  else { ?>
        <div class="loginbox">
        	<form action="login.php" method="POST">
          		<div class="loginbox">
            		<input type="text" name="username" id="username" placeholder="Username" />
          		</div>
          			<input type="submit" value="Go">
          		<div>
            		<input type="password" name="password" id="password" placeholder="Password">
          		</div>
        	</form>
        <p span id="newuser">or <a href="newaccount.php">create new account</a>
        </p>
        </span>
        </div>
      <?php } ?>
      
      <div class="dashhead" id="bills">Bills</div>
      <div class="dashitem">LOGIN...to load your bills.</div>
      <div class="dashhead" id="testimony">Comments</div>
      <div class="dashitem">...to load your recent comments.</div>
      <div class="dashhead" id="lawmakers">Lawmakers</div>
      <div class="dashitem">...to load your legislators.</div>
      <div class="dashhead" id="topics">Topics</div>
      <div class="dashitem">...to load your topics.</div>

    </div>