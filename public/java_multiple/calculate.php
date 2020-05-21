<!DOCTYPE html>
<html lang="en">

<head>
    <title>Complexity Measuring Tool</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <style>
    pre {
        border: 0;
        padding: 0px;
        margin: 0px;
        background-color: transparent;
    }

    .table td,
    th {
        text-align: center;
    }

    .pre1 {
        border: 0;
        padding: 30px;
        margin: 0px;
        font-family: monospace;
        background-color: #F4F4F4;
    }
    </style>
</head>

<body>
    <div class="jumbotron">
        <div class="container">
            <h1>Complexity Measuring Tool</h1>
            <p>Web-based code complexity measuring tool</p>
            <span class="badge badge-danger">ITPM _ WD_09</span>
        </div>
    </div>

    <div class="container">
        <!-- Control the column width, and how they should appear on different devices -->
        <div class="row">
            <div class="col-sm-6" style="padding:20px;">
                View output in Slide show. Page by page output.
            </div>
            <div class="col-sm-3">
                <form action="./" method="POST">
                    <button style="margin-top:10px;" type="submit" class="btn btn-success btn-block btn-lg"
                        value="Upload Code"><span style="margin-right:10px;" class="glyphicon glyphicon-cloud-upload"
                            aria-hidden="true"></span>
                        Upload Code </button>
                </form>
            </div>
            <div class="col-sm-3">
                <form action="code.php" method="POST">
                    <!-- PHP CODE START -->

                    <?php

// get input code from client
$code = $_POST["code"];

echo '<button type="submit" style = "margin-top:10px;" class="btn btn-primary btn-block btn-lg" value="Slide Show"><span style="margin-right:10px;" class="glyphicon glyphicon-blackboard" aria-hidden="true"></span> Slide Show </button>';
echo "<textarea name ='code' style='visibility: hidden; height:0px; width:0px;' id = 'code' required>" . $code . "</textarea>";
echo "</form></div></div></div><div class='container'>";

// Show the code to the user
echo "<h1 style = 'margin-top:30px;'>Input Code</h1><br>";
echo "<p class='h3 text-right'>Total Complexity of the Submission : <span id='filevalue_' class='text-right btn btn-warning btn-lg btn-block;'> </span> </p> <br/>";
echo "<pre class='pre1' >" . $code . "</pre>";

// put the code in an array to post data as JSON
$data = array('code' => $code);
// REST API End point
$url = 'https://measurecomplexity.herokuapp.com/codecomplexity';
// Use CURL to communicate with the server through API
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, 1);
// Pass the data
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
// Store the response JSON
$response = curl_exec($ch);
curl_close($ch);

// Decode the JSON Object as array
$json = json_decode($response, true);

// varible to store the table number
$index = 1;

$tables = array();

foreach ($json as $value) {
    // function that returns the table name according to the table number
    setName($index);

    $table_value = "";

    // Table Start
    $table_value .= "<div class='table-responsive'> <table class='table'> ";
    // variable to identify the table headers. if count == 0, then it's a table header
    $count = 0;

    // Row
    foreach ($value as $tuple) {
        // header - make row blue
        if ($count == 0) {
            $table_value .= "<tr class='info'>";
        }
        // otherwise, it's a data row
        else {
            $table_value .= "<tr>";
        }

        // variable to identify code
        $is_code = 0;

        // Column
        foreach ($tuple as $col) {
            // header - make text bold
            if ($count == 0) {
                $table_value .= "<th>$col </th>";
            }
            // otherwise, it's data
            else {
                if ($is_code == 0) {
                    $table_value .= "<td style='text-align:left'><pre class='my'>" . $col . "</pre></td>";
                } else {
                    if (trim($col) != "0") {
                        if ((int) trim($col) >= 10) {
                            $table_value .= "<td style='background-color: #FF9494;'>" . trim($col) . "</td>";
                        } else if ((int) trim($col) >= 5) {
                            $table_value .= "<td style='background-color: #FDFF45;'>" . trim($col) . "</td>";
                        } else {
                            $table_value .= "<td>" . trim($col) . "</td>";
                        }
                    } else {
                        $table_value .= "<td></td>";
                    }
                }
            }
            $is_code++;
        }
        $count++;
        $table_value .= "</tr>";
    }
    $table_value .= "</table></div>";

    echo $table_value;

    $tables[$index] = $table_value;

    $index++;
}

// function that returns the table name according to the table number
function setName($index)
{
//don't change the order unless you change order accordingly in Helper.py
    switch ($index) {
        case 1:
            echo "<br><br><h1>Complexity of a program due to size</h1><br>";
            break;
        case 2:
            echo "<br><br><h1>Complexity of a program due to variables</h1><br>";
            break;
        case 3:
            echo "<br><br><h1>Complexity of a program due to methods </h1><br>";
            break;
        case 4:
            echo "<br><br><h1>Complexity of a program due to Coupling </h1><br>";
            break;
        case 5:
            echo "<br><br><h1>Complexity of a program due to control structures </h1><br>";
            break;
        case 6:
            echo "<br><br><h1>Complexity of a program due to inheritance </h1><br>";
            break;
        case 7:
            echo "<br><br><h1>Final Code Complexity </h1><br>";
            break;
    }
}

?>

                    <!-- PHP CODE END -->
                    <br><br><br>
            </div>
</body>
<script>

$(document).ready(function () {
    //Read Values From textarea
    var val = $("textarea").html().trim();
    if (val != "") {

      data_ = val;
  //prepating Ajax Request
    var settings = {
  "url": "https://measurecomplexity.herokuapp.com/codecomplexity/file",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "data": {
    "code": (data_)
  }
};

//When Request submitted
$.ajax(settings).done(function (response) {
  console.log(response);
  //displaying the response of Submission Complexity
  document.getElementById("filevalue_").innerHTML = response;

});

    }
});
</script>
</html>
