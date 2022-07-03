<?php 
    require "connection.php";
    $bindings = [];
    $result=null;
    if($pdo!=null){
        error_log("Connection is not null");
        $parameters = ['id_registro', 'fecha', 'FOREIGN KEY (id_registro) REFERENCES registro(id) ON DELETE CASCADE ON UPDATE CASCADE'];
        $received = json_decode(file_get_contents('php://input'),true);
        foreach ($parameters as $parameter){
            if(!isset( $received[$parameter]) ){
                $result =  "Parameter '".$parameter."' missing";
                break;
            }else{
                $bindings[] = $received[$parameter];
            }
        }
        if($result==null){
            $sql = 'INSERT INTO vacuna( time, id_registro, fecha, FOREIGN KEY (id_registro) REFERENCES registro(id) ON DELETE CASCADE ON UPDATE CASCADE) VALUES 
                (CURRENT_TIMESTAMP,?,?,?)';
                
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
