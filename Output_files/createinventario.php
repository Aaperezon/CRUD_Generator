<?php 
    require "connection.php";
    $bindings = [];
    $result=null;
    if($pdo!=null){
        error_log("Connection is not null");
        $parameters = ['id_area', 'id_categoria', 'id_color', 'nombre', 'FOREIGN KEY (id_area) REFERENCES area(id) ON DELETE CASCADE ON UPDATE CASCADE', 'FOREIGN KEY (id_categoria) REFERENCES categoria(id) ON DELETE CASCADE ON UPDATE CASCADE', 'FOREIGN KEY (id_color) REFERENCES color(id) ON DELETE CASCADE ON UPDATE CASCADE'];
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
            $sql = 'INSERT INTO inventario( time, id_area, id_categoria, id_color, nombre, FOREIGN KEY (id_area) REFERENCES area(id) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN KEY (id_categoria) REFERENCES categoria(id) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN KEY (id_color) REFERENCES color(id) ON DELETE CASCADE ON UPDATE CASCADE) VALUES 
                (CURRENT_TIMESTAMP,?,?,?,?,?,?,?)';
                
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
