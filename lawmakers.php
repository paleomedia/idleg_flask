<?php
    $thisPage="Lawmakers"; 
    include 'top.php'; 
    require_once("dao.php"); ?>
  
    <div class="maincontainer">
   
<?php include 'dash.php'; 

/* read the json file contents */
 
    $jsondata = file_get_contents('http://openstates.org/api/v1/legislators/?apikey=bcc2a830883c4f459dbffe94b2a3e90f&state=id'); 

//convert json object to php associative array
    $legislators = json_decode($jsondata, true);
    
   // echo "<pre>" . print_r($legislators, 1) . "</pre>";

    $dao = new Dao();
    $connection = $dao->getConnection();
    $i = 1;
    foreach ($legislators as $legislator) {
     $sql = "INSERT INTO lawmakers(leg_id, last_name, first_name, middle_name, district, party, active, chamber, photo_url)
     VALUES('" . $legislator['leg_id'] . "', " .
           "'" . $legislator['last_name'] . "', " .
           "'" . $legislator['first_name'] . "', " .
           "'" . $legislator['middle_name'] . "', " .
                 $legislator['district'] . ", " .
           "'" . $legislator['party'] . "', " .
                 $legislator['active'] . ", " .
           "'" . $legislator['chamber'] . "', " .
           "'" . $legislator['photo_url'] . "')";
     echo "inserting record $i<br/>";
     $i++;
     
     $count = $connection->exec($sql) or die(print_r($connection->errorInfo(), true));
     echo "rows actually inserted $count </br>";
    }
      
    
    
 include 'footer.php'; ?>