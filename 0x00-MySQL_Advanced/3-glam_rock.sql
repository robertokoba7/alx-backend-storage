-- SQL script that lists all bands with Glam rock as their main style, 
-- ranked by their longevity
SELECT DISTINCT band_name,
	-- Compute the lifespan by subtracting the year formed from the split year
	IFNULL(split, 2020) - formed as lifespan
  FROM metal_bands 
  -- Only select bands with "Glam rock" as their main style  
  WHERE FIND_IN_SET('Glam rock', style)
  -- Order by lifespan, in descending order
  ORDER BY lifespan DESC;


