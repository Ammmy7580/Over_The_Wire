<?php

	$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
	$cookie = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=';

	function get_key($defaultdata, $cookie){
    	$key = '';
    	$defaultdata = json_encode($defaultdata);
    	$cookie = base64_decode($cookie);

    	// Iterate through each character
    	for($i=0;$i<strlen($cookie);$i++) {
    		$key .= $cookie[$i] ^ $defaultdata[$i];
    	}

    	return $key;
	}

	// echo get_key($defaultdata, $cookie);
	// key = "qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq" -> "qw8J"
	$newdata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

	function get_cookie($in){
    	$key = 'qw8J';
    	$text = json_encode($in);
    	$outText = '';

    	// Iterate through each character
    	for($i=0;$i<strlen($text);$i++) {
    		$outText .= $text[$i] ^ $key[$i % strlen($key)];
    	}

    	return base64_encode($outText);
	}

	echo get_cookie($newdata)
	// ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK

?>