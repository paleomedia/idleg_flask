<?php
// Dao.php
// class for saving and getting info to/from MySQL

class Dao {

    private $dbhost = "paleomedia-idleg-1299620";
    private $user = "paleomedia";
    private $password = "";
    private $database = "c9";
    private $dbport = 3306; 
   
  public function getConnection () {
    return
      new PDO("mysql:host={$this->dbhost};dbname={$this->database};port={$this->dbport}", $this->user, $this->password);
  }
  
  public function check_login($name, $password) {
    $conn = $this->getConnection();
    $name = $conn->quote($name);
    $rows = $conn->query("SELECT password FROM users WHERE username = $name");
    if ($rows) {
        foreach ($rows as $row) {             #only one row should match  
            if ($password === $row["password"]) {
                return TRUE;
            }
        }
    }
    return FALSE;    # user not found, or wrong password
  }

  public function ensure_logged_in() {
    if (!isset($_SESSION[$name])) {
    redirect("index.php", "You must login first");
    }
  }

  public function redirect($url, $flash_message = NULL) {
	  if ($flash_message) {
		$_SESSION["flash"] = $flash_message;
	  }
	  header("Location: $url");
	  die;
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
  
  public function newUser ($username, $password, $email) {
    $conn = $this->getConnection();
    
  }
  
  public function saveBills ($id, $session, $title, $bill_id, $connection) {
  
    $saveQuery =
          "INSERT INTO bills
          (bill_id, year, title, bill_name)
          VALUES
          (:id, :session, :title, :bill_id)";
      $q = $connection->prepare($saveQuery);
      $q->bindParam(":id", $id);
      $q->bindParam(":session", $session);
      $q->bindParam(":title", $title);
      $q->bindParam(":bill_id", $bill_id);
      $q->execute();
      return $bill_id;
  }
  
} // end Dao
?>