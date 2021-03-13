import os

php = ""
def DeleteMaker(tableName):
    global php
    php = (
'''<?php 
    require "Connection.php";
    $bindings = [];
    $result=null;
    if($pdo!=null){
        error_log("Connection is not null");
        $parameters = [];
        $auxParam = array_keys($_GET);
        foreach ($auxParam as $val){
            array_push($parameters,$val);
        }
        $parameters = implode(",", $parameters);
        foreach ($auxParam as $val){
            $bindings[] = $_GET[$val];
        }
        $bindings = implode(",", $bindings);
        $sql = "DELETE FROM '''+tableName+''' WHERE (" . $parameters . ") = (" . $bindings . ")";
        $stmt = $pdo->prepare($sql);
        if($stmt->execute()){
            $result = "Deletion Success";
        }
        else{
            $result = "Deletion Error";
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
    pDelete = './Output_files/delete'+tableName.lower()+'.php'

    if os.path.exists(pDelete):
        os.remove(pDelete)
        print ("Removed last file")
    DeleteMaker(tableName);
    f = open(pDelete, "a")
    f.write(php)
    f.close()
    print("New file created")
    print()