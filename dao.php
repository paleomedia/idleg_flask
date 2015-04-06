<?php
// Dao.php
// class for saving and getting info to/from MySQL

class Dao {

	private $host = "127.0.0.1";
    private $user = "root";
    private $dbpassword = "root";
    private $db = "idleg_test";
    private $dbport = 8889;  
  
  public function getConnection () {
    return
      new PDO("mysql:host={$this->host};dbname={$this->db};port={$this->dbport}", $this->user, $this->dbpassword);
  }

  public function saveComment ($comment) {
    $conn = $this->getConnection();
    $saveQuery =
        "INSERT INTO comments
        (comment)
        VALUES
        (:comment)";
    $q = $conn->prepare($saveQuery);
    $q->bindParam(":comment", $comment);
    $q->execute();
  }

  public function getComments () {
    $conn = $this->getConnection();
    return $conn->query("SELECT * FROM comments");
  }
  
  public function saveJson ($data) {
  	$conn = $this->getConnection();
  	foreach ($data as $item) {
  	$saveQuery = "INSERT INTO lawmakers
  	(first_name, last_name, middle_name, district, party, active, chamber, photo_url)
    VALUES(:item['first_name']."', '".$item['last_name']."', '".$item['middle_name']."', '".$item['district']."', '".$item['party']."', '".$item['active']."', '".$item['chamber']."', '".$item['photo_url']."');
    $q = $conn->prepare($saveQuery);
    $q->bindParam(":item", $item);
    $q->execute();
  }
  	
  
} // end Dao