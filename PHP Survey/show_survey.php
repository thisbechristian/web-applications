<?php require "header.php"; 

// let's establish a connection.
$conn = new mysqli("localhost", "root", "", "survey_db");
if ($conn->connect_error) {
  echo "cannot connect to the db... sorry :(";
} else {

  // once connected get survey data from the db.
  $sql = "SELECT c_name, c_icecream, c_game, c_time FROM t_survey";
  $result = $conn->query($sql);
  if ($result) {
  
  	echo "<h1>Survey results!!!</h1>";
  
    // the num_rows property identifies how many records were returned by the query.
    if ($result->num_rows > 0) {
  
      // when there are no more records, this will return null.
      while ($row = $result->fetch_assoc()) {
    
    	echo "<h4>";
        // build HTML survey out of the record.
        echo "Name: " . $row['c_name'] . "<br>";
        echo "Favorite Ice Cream: " . $row['c_icecream'] . "<br>";
        echo "Favorite Video Game: " . $row['c_game'] . "<br>";
      
        // format the time.
        $mytime = date('Y-m-d G:m', $row['c_time']);
        echo "Time Posted: $mytime<br>";
		echo "</h4>";
        echo "<br>";
      }
    }
    else {
      echo "There are no surveys!<br>";
    }
  }
  //log the error
  else {
    $error = $conn->errno . ' ' . $conn->error;
    echo "Error: " + $error;
  }
}

$conn->close();

?>
<h2><a href="enter_survey.php">Fill Out Survey !!!</a></h2>
<?php require "footer.php"; ?>