      // we'll declare a JavaScript variable to track our clicks.
      var clicks = [0,0,0,0];
      var total = 0;

      function handleCowClick(cow) {
        total++;
        clicks[cow]++;
  
          // Now we will put it on the page.
        var score = document.getElementById('score');

        var a = document.getElementById('a');
        var b = document.getElementById('b');
        var c = document.getElementById('c');
        var d = document.getElementById('d');

        score.innerHTML = "TOTAL SCORE IS " + total;
        a.innerHTML = "ALBERT's click score is: " + clicks[0];
        b.innerHTML = "BOB's click score is: " + clicks[1];
        c.innerHTML = "CHRIS's click score is: " + clicks[2];
        d.innerHTML = "DAVE's click score is: " + clicks[3];
      }
    