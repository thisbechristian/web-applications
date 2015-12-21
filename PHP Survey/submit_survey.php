<?php
session_start();

function log_error($message) {
  if (empty($_SESSION['message_error'])) {
    $_SESSION['message_error'] = '';
  }
  $_SESSION['message_error'] .= $message . "<br>";
}

# We'll clear the errors first.
$_SESSION['message_error'] = '';

# This will set the variables to the posted parameters from the form.
$name = $_POST['name'];
$icecream = $_POST['icecream'];
$game = $_POST['game'];
$time = time();

// we'll connect to the database here.
$conn = mysqli_connect("localhost", "root", "", "survey_db");

if ($conn->connect_error) {
  log_error("cannot connect to the db... sorry :(");
} 
else {

  // We're going to use a prepared statement, because it's a bit safer.
  // If there are no database errors, we'll create a prepared statement.
  $statement = $conn->prepare("INSERT INTO t_survey (c_name, c_icecream, c_game, c_time) VALUES (?,?,?,?)");
  if ($statement) {
  
    // we bind these parameters so that we can execute the statement.
    // the "sssi" identifies string, string, string, integer.
    $statement->bind_param("sssi", $a, $b, $c, $d);
  
    $a = $name;
    $b = $icecream;
    $c = $game;
    $d = $time;
  
    $statement->execute();
    
  } else {
    $error = $conn->errno . ' ' . $conn->error;
    echo $error;
    return;
  }
}

$conn->close();

// If there are no errors, we'll go back to the "show messages" screen.
if (!empty($_SESSION['message_error']) and strlen($_SESSION['message_error']) > 0) {
  header('location:enter_survey.php');
} else {
  header('location:show_survey.php');
}

