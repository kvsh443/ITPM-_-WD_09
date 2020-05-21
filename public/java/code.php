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
                <h1>Input Code</h1>
            </div>
            <div class="col-sm-3">
                <ul class="pagination">
                    <li class="active"><a href="#">1</a></li>
                    <li><a href="#">2</a></li>
                    <li><a href="#">3</a></li>
                    <li><a href="#">4</a></li>
                    <li><a href="#">5</a></li>
                    <li><a href="#">6</a></li>
                    <li><a href="#">7</a></li>
                    <li><a href="#">8</a></li>
                </ul>
            </div>
        </div>

        <br>

        <?php

$code = $_POST["code"];

// Show the code to the user
echo "<pre class='pre1' >" . $code . "</pre>";

echo '<div class="container" style="margin-top:20px;">
    <div class="row">
        <div class="col-sm-6" style="padding:20px;">
        </div>
        <div class="col-sm-3">
                <form action="calculate.php" method="POST" class="float-right">
                    <input type="submit" class="btn btn-outline-dark btn-block btn-lg" value="Back">
                    <textarea name ="code" style="visibility: hidden; height:0px;" id = "code" required>' . $code . '</textarea>
                </form>
            </div>
    <div class="col-sm-3">
        <form action="sizecomplexity.php" method="POST" class="float-right">';

echo '<input type="submit" class="btn btn-primary btn-block btn-lg" value="Next">';
echo "<textarea name ='code' style='visibility: hidden; height:5px;' id = 'code' required>" . $code . "</textarea>";
echo "</form>
        </div>
    </div>
<br><br>";

?>

    </div>
</body>

</html>
