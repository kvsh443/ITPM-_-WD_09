<?php
   require_once('login.php');
   if(empty($_SESSION["authenticated"]) || $_SESSION["authenticated"] != 'true') {
       header('Location: login.html');
   }

   $connect =  pg_connect("dbname=dfkklebvpgkoue host=ec2-34-194-198-176.compute-1.amazonaws.com port=5432 user=hgzusbitssgbao password=0086bfa1dc7c81ee3b7ebace7abebc33ee405b195798cec088c716a1b3de36a0 sslmode=require");
   $query_s = "SELECT * FROM sample ORDER BY id";
   $query_V = "SELECT * FROM variable_complexity ORDER BY id";
   $query_S = "SELECT * FROM size_complexity ORDER BY id";
   $query_M = "SELECT * FROM method_complexity ORDER BY id";
   $query_I = "SELECT * FROM inheritance_complexity ORDER BY id";
   $query_C = "SELECT * FROM coupling_complexity ORDER BY id";
   $query_T = "SELECT * FROM control_structure_complexity ORDER BY id";
   $result_s = pg_query($connect, $query_s);
   $result_S = pg_query($connect, $query_S);
   $result_V = pg_query($connect, $query_V);
   $result_M = pg_query($connect, $query_M);
   $result_I = pg_query($connect, $query_I);
   $result_C = pg_query($connect, $query_C);
   $result_T = pg_query($connect, $query_T);
    ?>
<!DOCTYPE html>
<html lang="en">
   <head>
      <title>Weight Tables</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" />
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/jquery-tabledit@1.0.0/jquery.tabledit.min.js" integrity="sha256-eQviKKzcfJX4mmVQzo/jhPQX0prZgVNmxW2/y2cs5wk=" crossorigin="anonymous"></script>
   </head>
   <body>
      <div class="container">
         <p class="h1" style="text-align: center;">Weight Tables</p>
         <div>
           <a href="logout.php" class="btn btn-info btn-lg pull-right">
             <span class="glyphicon glyphicon-log-out"></span> Log out
           </a>
         </div>
         <br />
         <br />
         <br />
         <div class="row">
            <div class="col-xs-4">
               <h2 class="sub-header">Size Table</h2>
               <br />
               <div class="table-responsive">
                  <table id="editable_tableS" class="table table-bordered table-striped">
                     <thead>
                        <tr>
                           <th>ID</th>
                           <th>Name</th>
                           <th>Value</th>
                        </tr>
                     </thead>
                     <tbody>
                        <?php
                           while($row = pg_fetch_assoc($result_S))
                           {
                            echo '
                            <tr>
                             <td>'.$row["id"].'</td>
                             <td>'.$row["real_name"].'</td>
                             <td>'.$row["value"].'</td>
                            </tr>
                            ';
                           }
                           ?>
                     </tbody>
                  </table>
               </div>
            </div>
            <div class="col-xs-4">
               <h2 class="sub-header">Variable Table</h2>
               <br />
               <div class="table-responsive">
                  <table id="editable_tableV" class="table table-bordered table-striped">
                     <thead>
                        <tr>
                           <th>ID</th>
                           <th>Name</th>
                           <th>Value</th>
                        </tr>
                     </thead>
                     <tbody>
                        <?php
                           while($row = pg_fetch_assoc($result_V))
                           {
                            echo '
                            <tr>
                             <td>'.$row["id"].'</td>
                             <td>'.$row["real_name"].'</td>
                             <td>'.$row["value"].'</td>
                            </tr>
                            ';
                           }
                           ?>
                     </tbody>
                  </table>
               </div>
            </div>
            <div class="col-xs-4">
               <h2 class="sub-header">Method Table</h2>
               <br />
               <div class="table-responsive">
                  <table id="editable_tableM" class="table table-bordered table-striped">
                     <thead>
                        <tr>
                           <th>ID</th>
                           <th>Name</th>
                           <th>Value</th>
                        </tr>
                     </thead>
                     <tbody>
                        <?php
                           while($row = pg_fetch_assoc($result_M))
                           {
                            echo '
                            <tr>
                             <td>'.$row["id"].'</td>
                             <td>'.$row["real_name"].'</td>
                             <td>'.$row["value"].'</td>
                            </tr>
                            ';
                           }
                           ?>
                     </tbody>
                  </table>
               </div>
            </div>
            <div class=row>
               <div class="col-xs-6">
                  <h2 class="sub-header">Inheritance Table</h2>
                  <br />
                  <div class="table-responsive">
                     <table id="editable_tableI" class="table table-bordered table-striped">
                        <thead>
                           <tr>
                              <th>ID</th>
                              <th>Name</th>
                              <th>Value</th>
                           </tr>
                        </thead>
                        <tbody>
                           <?php
                              while($row = pg_fetch_assoc($result_I))
                              {
                               echo '
                               <tr>
                                <td>'.$row["id"].'</td>
                                <td>'.$row["real_name"].'</td>
                                <td>'.$row["value"].'</td>
                               </tr>
                               ';
                              }
                              ?>
                        </tbody>
                     </table>
                  </div>
               </div>
               <div class="col-xs-6">
                  <h2 class="sub-header">Coupling Table</h2>
                  <br />
                  <div class="table-responsive">
                     <table id="editable_tableC" class="table table-bordered table-striped">
                        <thead>
                           <tr>
                              <th>ID</th>
                              <th>Name</th>
                              <th>Value</th>
                           </tr>
                        </thead>
                        <tbody>
                           <?php
                              while($row = pg_fetch_assoc($result_C))
                              {
                               echo '
                               <tr>
                                <td>'.$row["id"].'</td>
                                <td>'.$row["real_name"].'</td>
                                <td>'.$row["value"].'</td>
                               </tr>
                               ';
                              }
                              ?>
                        </tbody>
                     </table>
                  </div>
               </div>
            </div>
            <div class="row">
               <div class="col-xs-6 float-left">
                  <h2 class="sub-header">Control Structure Table</h2>
                  <br />
                  <div class="table-responsive">
                     <table id="editable_tableT" class="table table-bordered table-striped">
                        <thead>
                           <tr>
                              <th>ID</th>
                              <th>Name</th>
                              <th>Value</th>
                           </tr>
                        </thead>
                        <tbody>
                           <?php
                              while($row = pg_fetch_assoc($result_T))
                              {
                               echo '
                               <tr>
                                <td>'.$row["id"].'</td>
                                <td>'.$row["real_name"].'</td>
                                <td>'.$row["value"].'</td>
                               </tr>
                               ';
                              }
                              ?>
                        </tbody>
                     </table>
                  </div>
               </div>
            </div>
         </div>
         <br/>
         <br/>
         <br/>
         <div class="panel panel-default">
            <div class=row>
               <div class="col-xs-3">
               </div>
               <div class="col-xs-6">
                  <h2 class="sub-header">
                     Change Password
                  </h2>
                  <br />
                  <div class="panel-body">
                     <div class="table-responsive">
                        <table id="editable_tableL" class="table table-bordered table-striped">
                           <thead>
                              <tr>
                                 <th>ID</th>
                                 <th>Name</th>
                                 <th>PASSWORD</th>
                              </tr>
                           </thead>
                           <tbody>
                              <?php
                                 while($row = pg_fetch_assoc($result_s))
                                 {
                                  echo '
                                  <tr>
                                   <td>'.$row["id"].'</td>
                                   <td>'.$row["name"].'</td>
                                   <td>'.$row["password"].'</td>
                                  </tr>
                                  ';
                                 }
                                 ?>
                           </tbody>
                        </table>
                     </div>
                  </div>
                  <div class="col-xs-3">
                  </div>
               </div>
            </div>
         </div>
      </div>
   </body>
</html>
<script src="value.js"></script>
