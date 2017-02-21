-- List the number of occurances of each score
-- Select occurances grouped by score
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score DESC
