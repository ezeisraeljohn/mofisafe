-- This prepares a mysql server for the project
-- creates a new database for this project

CREATE DATABASE IF NOT EXISTS mofisafe_dev_db;

CREATE USER IF NOT EXISTS 'mofisafe_dev'@'localhost' IDENTIFIED BY 'mofisafe_dev_pwd';

GRANT ALL PRIVILEGES ON mofisafe_dev_db.* TO 'mofisaf_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'mofisafe_dev'@'localhost';
