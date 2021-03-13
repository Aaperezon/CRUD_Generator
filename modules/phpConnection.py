import os

php = ""
def ConnectionMaker(servername, username, password, dbname):
    global php
    php = (
'''<?php 
    $servername = "'''+servername+'''";
    $username = "'''+username+'''";
    $password = "'''+password+'''";
    $dbname = "'''+dbname+'''";

    try {
        $pdo = new PDO('mysql:host='.$servername.';dbname='.$dbname, $username, $password);

        // set the PDO error mode to exception
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    }
    catch(PDOException $e)
    {
        $pdo = null;
    }     
?>
'''
        )

def Run(servername, username, password, dbname):
    pConnection = './Output_files/connection.php'

    if (os.path.exists(pConnection)):
        os.remove(pConnection)
        print ("Removed last file")
    
    ConnectionMaker(servername, username, password, dbname);
    f = open(pConnection, "a")
    f.write(php)
    f.close()
    print("New file created")
    print()
