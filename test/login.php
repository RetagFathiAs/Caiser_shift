<?php
session_start();

include "db.php";
$email = $_POST["em"];
$pass = $_POST["pass"];
$sql = "SELECT * FROM users WHERE username='$email' AND password ='$pass'";
$result = mysqli_query($conn, $sql);

$num = mysqli_num_rows($result);
if ($num == 1){
    header("Location: dash.php");
}
else {
    echo "NOT_CORRECT";
}
?>


