<?php

if (isset($_POST['q'])) {
	$q = $_POST['q'];
	echo "Query: $q\n";
	route($q);
	// log_access($q, $_REQUEST[]);
} else {
	echo "No query";
	// log_access($_REQUEST[]);
}


function route($q) {
	if ($q == "toggle") {
		echo "Toggling lights";
		// Call the python script to toggle the lights
		$string = "python3 ".__DIR__."/scripts/toggleLights.py";
		shell_exec($string);
	}
}

function log_access($q=Null) {

	// Open the log file
	$logfile = __DIR__."/access.log";
	$fh = fopen($logfile, 'a') or die("Can't open file");

	// Write the query to the log file if it exists
	if(isset($q) || !empty($q) || $q != Null){
		$stringData = "Query: $q\n";
		fwrite($fh, $stringData);
	}
	
	// Always write the request to the log file	
	$stringData = "=============\n";
	fwrite($fh, $stringData);
	$stringData = $_SERVER['REQUEST_TIME_FLOAT']. " " .$_SERVER['REQUEST_METHOD']. " " .$_SERVER['REQUEST_URI']. " " .$_SERVER['QUERY_STRING']. " " .$_SERVER['HTTP_USER_AGENT']. " " .$_SERVER['REMOTE_ADDR']. " " .$_SERVER['HTTP_HOST']. " " .$_SERVER['SERVER_PROTOCOL']. " " .$_SERVER['SERVER_SOFTWARE']."\n";
	fwrite($fh, $stringData);

	echo "Logged access\n";

	// Close the log file
	fclose($fh);
}
