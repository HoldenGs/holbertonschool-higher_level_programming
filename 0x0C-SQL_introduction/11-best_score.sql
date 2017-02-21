-- List all rows with scores higher than 9, ordered by score
-- List rows
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
