-- Calculate the total number of fans for each country of origin
SELECT DISTINCT origin, SUM(fans) AS nb_fans FROM metal_bands
-- Group the bands by their country of origin
GROUP BY origin
-- Order the results by the total number of fans in descending order
ORDER BY nb_fans DESC;
