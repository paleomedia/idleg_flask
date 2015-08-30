<?php


/* get list of lawmakers and insert into lawmakers table
read the json file contents */

require_once("lib/classes/dao.php");
 
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
    
    /* Save new bill information to bills table */
    
    /* read the json file contents */
 
    $jsondata = file_get_contents('http://openstates.org/api/v1/bills/?apikey=bcc2a830883c4f459dbffe94b2a3e90f&state=id&search_window=session'); 

//convert json object to php associative array
    $bills = json_decode($jsondata, true);
    
 //   echo "<pre>" . print_r($bills, 1) . "</pre>";

    $dao = new Dao();
    $connection = $dao->getConnection();
    $i = 1;
    foreach ($bills as $bill) {
        $bill_name = $bill['bill_id'];
        $year = $bill['session'];
        $title = $bill['title'];
        $bill_id = $bill['id'];
        
        echo "inserting record $i<br/>";
        $i++;
        
        $dao->saveBills($bill_id, $year, $title, $bill_name, $connection) or die(print_r($connection->errorInfo(), true));
        echo "$bill_name actually inserted</br>";
    } 
    
    
    ?>