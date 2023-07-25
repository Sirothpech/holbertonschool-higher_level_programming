-- Script to create the MySQL database hbtn_0d_2 and user user_0d_2 with SELECT privilege only.
-- Create database hbtn_0d_2 if it does not exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user user_0d_2 if it does not exist and set the password to user_0d_2_pwd.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant SELECT privilege to user_0d_2 on the database hbtn_0d_2.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
