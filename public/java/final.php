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
    <!-- <div class="jumbotron">
        <div class="container">
            <h1>Complexity Measuring Tool</h1>
            <p>Web-based code complexity measuring tool</p>
        </div>
    </div> -->

    <div style="margin-top:20px; margin-right:20px; margin-left:20px;">
        <div class="row">
            <div class="col-sm-9">
                <h1>Complexity of a program due to Control all factors</h1>
            </div>
            <div class="col-sm-3">
                <ul class="pagination">
                    <li><a href="#">1</a></li>
                    <li><a href="#">2</a></li>
                    <li><a href="#">3</a></li>
                    <li><a href="#">4</a></li>
                    <li><a href="#">5</a></li>
                    <li><a href="#">6</a></li>
                    <li><a href="#">7</a></li>
                    <li class="active"><a href="#">8</a></li>
                </ul>
            </div>
        </div>

        <br>

        <?php

$code = $_POST["code"];

// put the code in an array to post data as JSON
$data = array('code' => $code);
// REST API End point
$url = 'http://measurecomplexity.herokuapp.com/codecomplexity/final';
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

$table_value = "";

// Table Start
$table_value .= "<div class='table-responsive'> <table class='table table-hover'> ";
// variable to identify the table headers. if count == 0, then it's a table header
$count = 0;

// Row
foreach ($json as $tuple) {
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
                $table_value .= "<td><pre class='my' style='text-align:left'>" . $col . "</pre></td>";
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

echo '<div class="container" style="margin-top:20px;">
    <div class="row">
        <div class="col-sm-6" style="padding:20px;">
        </div>
    <div class="col-sm-3">
                <form action="inheritancecomplexity.php" method="POST" class="float-right">
                    <input type="submit" class="btn btn-outline-dark btn-block btn-lg" value="Back">
                    <textarea name ="code" style="visibility: hidden; height:0px;" id = "code" required>' . $code . '</textarea>
                </form>
            </div>
    <div class="col-sm-3">
        <form action="index.html" method="POST" class="float-right">';

echo '<input type="submit" class="btn btn-primary btn-block btn-lg" value="Finish">';
echo "<textarea name ='code' style='visibility: hidden; height:5px;' id = 'code' required>" . $code . "</textarea>";
echo "</form>
        </div>
    </div>
<br><br>";

?>

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
  "url": "https://measurecomplexity.herokuapp.com/codecomplexity/All",
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
  console.log(response['Total'].length);
//displaying the response of Final Complexity Table
  for (var i = 0; i < response['Total'].length; i++) {
    console.log(response['Total'][i]);
  }


                var tr_str = "<tr class='active h4'>" +
                    "<td class='warning' align='center'>" + " <b>Total </b>"+ "</td>" +
                    "<td align='center'>" + response['Total'][0] + "</td>" +
                    "<td align='center'>" + response['Total'][1] + "</td>" +
                    "<td align='center'>" + response['Total'][2] + "</td>" +
                    "<td align='center'>" + response['Total'][3] + "</td>" +
                    "<td align='center'>" + response['Total'][4] + "</td>" +
                    "<td align='center'>" + response['Total'][5] + "</td>" +
                    "<td class='info' align='center'> <b>" + response['Total'][6]  + " </b> </td>" +
                    "</tr>";

                $("table tbody").append(tr_str);

});

    }
});
</script>
</html>
