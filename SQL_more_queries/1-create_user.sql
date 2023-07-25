-- Script to create the MySQL server user user_0d_1 with all privileges
-- Create user user_0d_1 if it does not exist and Grant all privileges to user_0d_1 on all databases
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
