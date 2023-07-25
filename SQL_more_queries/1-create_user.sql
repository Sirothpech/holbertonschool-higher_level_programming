-- Script to create the MySQL server user user_0d_1 with all privileges

-- Create user user_0d_1 if it does not exist and set the password to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1 on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to apply the changes immediately
FLUSH PRIVILEGES;