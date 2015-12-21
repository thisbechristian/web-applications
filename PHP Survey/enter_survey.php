<?php require "header.php"; 
session_start();

// if there is anything in the session field, we'll display it as an error.
if (array_key_exists('message_error', $_SESSION)) {
  if (!empty($_SESSION['message_error']) or strlen($_SESSION['message_error']) > 0) {
    echo $_SESSION['message_error'];
  }
}

// creates text and textarea html form input fields
function writeFormField($id, $label, $type) {
  echo "<label for=\"$id\">$label</label><br>";
  if ($type == 'text') {
    echo "<input type=\"text\" name=\"$id\" id=\"$id\" required=\"true\">";
  } else if ($type == 'textarea') {
    echo "<textarea id=\"$id\" name=\"$id\"></textarea>";
  }
  echo "<br><br><br>";
}

?>

<h1>Answer the survey please!</h1>

<form method="post" action="submit_survey.php">

	<?php writeFormField('name', 'Name?', 'text'); ?>
	<?php writeFormField('icecream', 'Favorite Flavor of Ice Cream?', 'text'); ?>
	<?php writeFormField('game', 'Favorite video game?', 'text'); ?>
	<input type="submit">
	
</form>
<br>

<h2><a href="show_survey.php">Survey Results !!!</a></h2>

<?php require "footer.php"; ?>
