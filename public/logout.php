<?php
session_start();
unset($_SESSION["authenticated"]);
session_destroy();
header("Location: ./index.html");
?>
