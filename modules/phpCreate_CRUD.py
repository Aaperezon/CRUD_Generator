import os

php = ""
def CreateMaker(tableName,parameters):
    global php
    parameters1 = ""
    interrogant = ""
    parameters_not_empty_values = []
    for a in parameters:
        if a != "":
            if parameters.index(a) == 0:
                parameters1+=a
                interrogant+='?'
            else:
                parameters1+=", "+a
                interrogant+=',?'
            parameters_not_empty_values.append(a)
    parameters = parameters_not_empty_values
    php = (
'''<?php 
    require "connection.php";
    $bindings = [];
    $result=null;
    if($pdo!=null){
        error_log("Connection is not null");
        $parameters = '''+str(parameters)+''';
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
            $sql = 'INSERT INTO '''+tableName+'''( time, '''+parameters1+''') VALUES 
                (CURRENT_TIMESTAMP,'''+interrogant+''')';
                
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
'''
        )

def Run(tableName,parameters):
    pCreate = './Output_files/create'+tableName.lower()+'.php'
    if os.path.exists(pCreate):
        os.remove(pCreate)
        print ("Removed last file")
    CreateMaker(tableName,parameters);
    f = open(pCreate, "a")
    f.write(php)
    f.close()
    print("New file created")
    print()
