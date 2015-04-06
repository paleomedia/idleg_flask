<?php
if (!isset($_SESSION)) {
	session_start();
}
?>

<!DOCTYPE html>

<html>

<head>
  
  <link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700' rel='stylesheet' type='text/css'>

  <title><?php if ($thisPage != "") {
echo "$thisPage"; } ?> - Idaho Legislative Information Portal, Bills, Lawmakers & Data</title>
  <meta charset="utf-8" />
  <meta name="description" content="idleg: Idaho legislative bill information portal" />
  <meta name="keywords" content="Idaho, legislature, bills, laws, legislation" />
  <meta name="author" content="Nathaniel Hoffman" />  <!-- Note: Make dynamic based on page author -->
  <meta name="revised" content="<?php filemtime('index.php'); ?>" />  <!-- last mod of index.html -->
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link href="styles.css" type="text/scc" rel="stylesheet" />
  <link rel="shortcut icon" href="/images/favicon.ico" />

</head>

<header>
    <div class="tops">
      <div id="topline">
        <div class="socials">
          <ul>
            <li class="social">
              <a href="http://twitter.com/idleg"><img src="images/twittericon.png" width="24px" height="24px">
              </a>
            </li>
            <li class="social">
              <a href="http://idleg.com/rss"><img src="images/RSS-Icon.png" width="24px" height="24px">
              </a>
            </li>
            <li class="social">
              <a href="http://github.com"><img src="images/Github-Icon.png" width="24px" height="24px">
              </a>
            </li>
            <li class="social">
              <a href="mailto:editor@idleg.com"><img src="images/Email-Icon.png" width="24px" height="24px">
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

