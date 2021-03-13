import os

php = ""
def UpdateMaker(tableName):
    global php
    php = (
'''<?php 
    require "Connection.php";
    $result=null;
    if($pdo!=null){
        error_log("Connection is not null");
        $parameters = [];
        $auxParam = array_keys($_GET);
        $idVal = -1;
        for($i = 0; $i < sizeof($auxParam); $i++){
            if($auxParam[$i] != 'id'){
                $temp = $auxParam[$i]."=".$_GET[$auxParam[$i]];
                array_push($parameters,$temp);
            }else{
                $idVal = $_GET[$auxParam[$i]];
            }
        }
        $parameters = implode(",", $parameters);
        $sql = "UPDATE '''+tableName+''' SET ". $parameters . " WHERE id=". $idVal;
        $stmt = $pdo->prepare($sql);
        if($stmt->execute()){
            $result = "Update Success";
        }
        else{
            $result = "Update Error";
        }
    }
    else{
        $result = "Connection Error";
    }
    echo json_encode($result);
?>
'''
    )

def Run(tableName):
    pUpdate = './Output_files/update'+tableName.lower()+'.php'

    if os.path.exists(pUpdate):
        os.remove(pUpdate)
        print ("Removed last file")
    UpdateMaker(tableName);
    f = open(pUpdate, "a")
    f.write(php)
    f.close()
    print("New file created")
    print()