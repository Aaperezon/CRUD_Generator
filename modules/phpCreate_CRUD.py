import os

php = ""
def CreateMaker(tableName,parameters):
    global php
    parameters1 = ""
    interrogant = ""

    for a in parameters:
        if parameters.index(a) == 0:
            parameters1+=a
            interrogant+='?'
        else:
            parameters1+=", "+a
            interrogant+=',?'
    php = (
'''<?php 
    require "Connection.php";
    $bindings = [];
    $result=null;
    if($pdo!=null){
        error_log("Connection is not null");

        $parameters = '''+str(parameters)+''';

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
