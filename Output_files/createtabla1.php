<?php 
    require "Connection.php";
    $bindings = [];
    $result=null;
    if($pdo!=null){
        error_log("Connection is not null");

        $parameters = ['atributo1'];

        for($i = 0; $i < sizeof($parameters); $i++){
            if(!isset($_GET[$parameters[$i]])){
                $result = "Parameter ".$parameters[$i]." missing";
                break;
            }
            else{
                $bindings[] = $_GET[$parameters[$i]];
            }
        }
        if($result==null){
            $sql = 'INSERT INTO Tabla1( time, atributo1) VALUES 
                (CURRENT_TIMESTAMP,?)';
                
            $stmt = $pdo->prepare($sql);
            if($stmt->execute($bindings)){
                $result = "Insertion Success";
            }
            else{
                $result = "Insertion Error";
            }
        }
    }
    else{
        $result = "Connection Error";
    }
    echo json_encode($result);
?>
