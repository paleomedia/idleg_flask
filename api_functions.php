<?php

function last_action($bill_id) {

$api_key = "/?apikey=bcc2a830883c4f459dbffe94b2a3e90f";
$url_base = "http://openstates.org/api/v1/";
$url = $url_base . 'bills/' . $bill_id . $api_key;
$bill_json = file_get_contents($url);
$bill_detail = json_decode($bill_json, true);

return strtok($bill_detail[action_dates][last], " ") ;

}

?>