-- Create a second table in hbtn_0c_0 database and insert some data into it
-- Create a table
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- Insert John into the second_table
INSERT INTO second_table (`id`, `name`, `score`) VALUES (1, 'John', 10);
-- Insert Alex into the second_table
INSERT INTO second_table (`id`, `name`, `score`) VALUES (1, 'Alex', 3);
-- Insert Bob into the second_table
INSERT INTO second_table (`id`, `name`, `score`) VALUES (1, 'Bob', 14);
-- Insert George into the second_table
INSERT INTO second_table (`id`, `name`, `score`) VALUES (1, 'George', 8);
