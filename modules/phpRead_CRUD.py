import os

php = ""
def ReadMaker(tableName):
    global php
    php = (
'''<?php 
    require "Connection.php";
    $data = [];
    if($pdo!=null){
        error_log("Connection is not null");
        $sql = "SELECT * FROM '''+tableName+''' ORDER BY id DESC LIMIT 1";
        $stmt = $pdo->prepare($sql);
        $stmt->execute();
        while($row = $stmt->fetch(PDO::FETCH_NUM))
            $data[] = $row;
    }else{
        $data = "Connection error";
    }
    echo json_encode($data);
?>
'''
        )

def Run(tableName):
    pRead = './Output_files/Read'+tableName+'.php'

    if os.path.exists(pRead):
        os.remove(pRead)
        print ("Removed last file")
    ReadMaker(tableName);
    f = open(pRead, "a")
    f.write(php)
    f.close()
    print("New file created")
    print()