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
      <div class="loginbox">
<!--       	<?php
   		if (isset($_SESSION["status"])) {
      	echo "<div id=\"status\">" .  $_SESSION["status"] . "</div>";
      	unset($_SESSION["status"]);
   		}
   		?>   -->
        <form action="login.php" method="POST">
          <div class="loginbox">
            <input type="text" name="username" id="username" placeholder="User name" />
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
      <div class="dashhead" id="bills">Bills</div>
      <div class="dashitem">LOGIN...to load your bills.</div>
      <div class="dashhead" id="testimony">Comments</div>
      <div class="dashitem">...to load your recent comments.</div>
      <div class="dashhead" id="lawmakers">Lawmakers</div>
      <div class="dashitem">...to load your legislators.</div>
      <div class="dashhead" id="topics">Topics</div>
      <div class="dashitem">...to load your topics.</div>

    </div>