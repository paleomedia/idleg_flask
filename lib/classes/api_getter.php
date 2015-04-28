<?php
// api_getter.php
// class for saving and getting info to/from API
// not in use at the moment

class api_getter {

    private $api_key = "/?apikey=bcc2a830883c4f459dbffe94b2a3e90f";
    private $url_base = "http://openstates.org/api/v1/";

public function last_action($bill_id) {
    $url_base = $this->url_base
    $key = $this->api_key
    $url = $url_base . 'bills/' . $bill_id . $key;
    $bill_json = file_get_contents($url);
    $bill_detail = json_decode($bill_json, true);
    return $bill_detail[action_dates][last];
}

}
?>