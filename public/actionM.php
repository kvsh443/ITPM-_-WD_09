<?php
//action?.php for Method
$connect =  pg_connect("dbname=dfkklebvpgkoue host=ec2-34-194-198-176.compute-1.amazonaws.com port=5432 user=hgzusbitssgbao password=0086bfa1dc7c81ee3b7ebace7abebc33ee405b195798cec088c716a1b3de36a0 sslmode=require");

$input = filter_input_array(INPUT_POST);

$value = pg_escape_string($input["value"]);


if($input["action"] === 'edit')
{
 $query = "
 UPDATE method_complexity
 SET value = '".$value."'
 WHERE id = '".$input["id"]."'
 ";

 pg_query($query);

}

echo json_encode($input);

?>
