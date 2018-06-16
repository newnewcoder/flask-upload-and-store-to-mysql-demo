Simple Flask upload file and store to Mysql Demo

# How to run

## Setup Mysql

**step 1** install mysql
    
~~~bash
docker run --name upload_demo_db -e MYSQL_ROOT_PASSWORD=abc123 -p 3306:3306 -d mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
~~~

**step 2** setup database

~~~sql
CREATE DATABASE `mydb`;
USE `mydb`;
CREATE TABLE `upload_demo` (
`id` integer AUTO_INCREMENT PRIMARY KEY,
`file` LONGBLOB
) ENGINE=InnoDB
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
~~~

## Run Flask app

~~~bash
pip install -r requirements.txt
./run.sh
~~~

go [http://localhost:5000](http://localhost:5000)
