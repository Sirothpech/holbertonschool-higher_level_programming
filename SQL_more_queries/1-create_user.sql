-- Script to create the MySQL server user user_0d_1 with all privileges.
-- Create user user_0d_1 if it does not exist and set the password to user_0d_1_pwd.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Set all privileges.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
