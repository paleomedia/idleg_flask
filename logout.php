<?php
session_start();
session_destroy();
session_regenerate_id(TRUE);
setcookie("username", "", time() - 1);

header("Location:index.php");
?>