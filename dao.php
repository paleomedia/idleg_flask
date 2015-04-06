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
      new PDO("mysql:host={$this->host};dbname={$this->db};port={$this->dbport}", $this->user, $this->pass);
  }

  public function saveComment ($comment) {
    $conn = $this->getConnection();
    $saveQuery =
        "INSERT INTO comment
        (comment)
        VALUES
        (:comment)";
    $q = $conn->prepare($saveQuery);
    $q->bindParam(":comment", $comment);
    $q->execute();
  }

  public function getComments () {
    $conn = $this->getConnection();
    return $conn->query("SELECT * FROM comment");
  }
} // end Dao