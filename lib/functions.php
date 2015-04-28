<?php   // outputs e.g.  somefile.txt was last modified: December 29 2002 22:16:23.

$filename = 'index.html';
if (file_exists($filename)) {
    echo "$filename was last modified: " . date ("F d Y H:i:s.", filemtime($filename));
}



$db = new PDO("mysql:host=127.0.0.1;port=8889;dbname=idleg_test", "root", "root");
$query = $db->prepare('SELECT * from users where username = "paleomedia"');
$query->execute();
?>
<pre>
<?php
while($rows = $query->fetch(PDO::FETCH_ASSOC)){
     var_dump($rows); } ?>
     </pre>

<?php
    
 if ($db->connect_error) {
        die("Connection failed: " . $db->connect_error);
    } 
    echo "Connected successfully (".$db->host_info.")";


$db = new PDO("mysql:host=127.0.0.1;port=8889;dbname=idleg_test", "root", "root");
    var_dump($db);
    
 if ($db->connect_error) {
        die("Connection failed: " . $db->connect_error);
    } 
    echo "Connected successfully (".$db->host_info.")";

?>




/* read the json file contents */

<?php 
    $jsondata = file_get_contents('http://openstates.org/api/v1/legislators/?apikey=bcc2a830883c4f459dbffe94b2a3e90f&state=id');
    var_dump($jsondata);
    
//convert json object to php associative array
    $data = json_decode($jsondata, true);
    
    var_dump($data);
    
//get the legislator details
//    FIXXXXXX
// extra fields     $suffix = $data['personal']['address']['streetaddress'];
//                  $nickname = $data['personal']['address']['city'];
//                  $website = $data['personal']['address']['postalcode'];  

    $first_name = $data['first_name'];
    $last_name = $data['last_name'];
    $middle_name = $data['middle_name'];
    $district = $data['district'];
    $party = $data['party'];
    $active = $data['active'];
    $chamber = $data['chamber'];
    $photo_url = $data['photo_url'];
    
    
    $host = getenv('IP');
    $user = getenv('C9_USER');
    $password = "";
    $database = "c9";
    $dbport = 3306;

 try {
    $db = new PDO("mysql:dbname=$database; host=$host", $user, $password);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
} catch (PDOException $ex) {
    print "Error!: " . $ex->getMessage() . "<br/>";
    die();
}
    
//insert into mysql table
    mysql_select_db("lawmakers", $cxn);
    $sql = "INSERT INTO lawmakers(first_name, last_name, middle_name, district, party, active, chamber, photo_url)
    VALUES('$first_name', '$last_name', '$middle_name', '$district', '$party', '$active', '$chamber', '$photo_url')";
    if(!mysql_query($sql,$con))
    {
        die('Error : ' . mysql_error());
    }
    }

?>