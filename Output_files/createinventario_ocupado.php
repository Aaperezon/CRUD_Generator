<?php 
    require "connection.php";
    $bindings = [];
    $result=null;
    if($pdo!=null){
        error_log("Connection is not null");
        $parameters = ['id_inventario', 'id_usuario', 'FOREIGN KEY (id_inventario) REFERENCES inventario(id) ON DELETE CASCADE ON UPDATE CASCADE', 'FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE ON UPDATE CASCADE'];
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
            $sql = 'INSERT INTO inventario_ocupado( time, id_inventario, id_usuario, FOREIGN KEY (id_inventario) REFERENCES inventario(id) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE ON UPDATE CASCADE) VALUES 
                (CURRENT_TIMESTAMP,?,?,?,?)';
                
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
