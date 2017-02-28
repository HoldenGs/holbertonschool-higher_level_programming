-- Create a new user named 'user_0d_1' with password 'user_0d_1_pwd'
-- Creates a new user if none exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
