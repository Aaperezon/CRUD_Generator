<?php 
    require "connection.php";
    $bindings = [];
    $result=null;
    if($pdo!=null){
        error_log("Connection is not null");
        $parameters = ['imagen', 'tipo', 'nombre', 'raza', 'color', 'fecha_de_nacimiento', 'fecha_de_ingreso', 'descripcion', 'esterilizado', 'adoptado', 'tamano', 'sexo', 'publico'];
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
            $sql = 'INSERT INTO registro( time, imagen, tipo, nombre, raza, color, fecha_de_nacimiento, fecha_de_ingreso, descripcion, esterilizado, adoptado, tamano, sexo, publico) VALUES 
                (CURRENT_TIMESTAMP,?,?,?,?,?,?,?,?,?,?,?,?,?)';
                
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
