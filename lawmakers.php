<?php
$thisPage="Lawmakers"; 
include 'top.php'; 
require_once "Dao.php"; ?>
  
<div class="maincontainer">
   
<?php include 'dash.php'; 

/* read the json file contents */
 
    $jsondata = file_get_contents('http://openstates.org/api/v1/legislators/?apikey=bcc2a830883c4f459dbffe94b2a3e90f&state=id'); 

//convert json object to php associative array
    $data = json_decode($jsondata, true);
    
/* get the legislator details
// FIXXXXXX extra fields
     $suffix = $data['personal']['address']['streetaddress'];
     $nickname = $data['personal']['address']['city'];
     $website = $data['personal']['address']['postalcode'];  
     
    $first_name = $data['first_name'];
    $last_name = $data['last_name'];
    $middle_name = $data['middle_name'];
    $district = $data['district'];
    $party = $data['party'];
    $active = $data['active'];
    $chamber = $data['chamber'];
    $photo_url = $data['photo_url'];  
    
    
    $sql = "INSERT INTO lawmakers(first_name, last_name, middle_name, district, party, active, chamber, photo_url)
    VALUES('$first_name', '$last_name', '$middle_name', '$district', '$party', '$active', '$chamber', '$photo_url')";
    if(!mysql_query($sql,$con))
    {
        die('Error inserting data: ' . mysql_error());
    }
    }
    
    VALUES('".$item['first_name']."', '".$item['last_name']."', '".$item['middle_name']."', '".$item['district']."', '".$item['party']."', '".$item['active']."', '".$item['chamber']."', '".$item['photo_url']."');
*/

    try {
      $dao = new Dao();
    } catch (Exception $e) {
      var_dump($e);
      die;
    }   
    
//insert into mysql table
   	saveJson($data);

    
    
 include 'footer.php'; ?>