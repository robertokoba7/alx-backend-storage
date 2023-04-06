-- Calculate the total number of fans for each country of origin
SELECT origin, SUM(nb_fans) AS total_fans 
FROM metal_bands
-- Group the bands by their country of origin
GROUP BY origin
-- Order the results by the total number of fans in descending order
ORDER BY total_fans DESC;
