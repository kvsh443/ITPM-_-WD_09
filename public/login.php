<?php

$db =  pg_connect("dbname=dfkklebvpgkoue host=ec2-34-194-198-176.compute-1.amazonaws.com port=5432 user=hgzusbitssgbao password=0086bfa1dc7c81ee3b7ebace7abebc33ee405b195798cec088c716a1b3de36a0 sslmode=require");

  session_start();
   if($_SERVER["REQUEST_METHOD"] == "POST") {
      // username and password sent from form

      $error = "";
      $mypassword = pg_escape_string($_POST['password']);

      $sql = "SELECT id FROM sample WHERE password = '$mypassword'";
      $result = pg_query($db,$sql);
      $row = pg_fetch_assoc($result);


      $count = pg_num_rows($result);

      // If result matched $mypassword

      if($count) {

         $_SESSION["authenticated"] = 'true';
         header('Location: weighttables.php');

      }else {
         $error = "Your Password is invalid";
         header('Location: login.html');
      }
   }
?>
