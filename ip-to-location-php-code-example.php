<?php
// Set IP address and API access key
$ip = '67.250.186.196';
$access_key = 'YOUR_ACCESS_KEY';

// Initialize CURL
$ch = curl_init('https://apiip.net/api/check?ip='.$ip.'&accessKey='.$access_key.'');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Store the data
$json_res = curl_exec($ch);
curl_close($ch);

// Decode JSON response
$api_result = json_decode($json_res, true);

// Output the "code" value inside "currency" object
echo $api_result['currency']['code'];

?>