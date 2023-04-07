 -- SQL script which stores procedure to 
-- compute adn store the average weighted score
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER |
CREATE PRCEDURE ComputeAverageWeightedScoreForUser(
  user_id INT)
BEGIN
  DECLARE  wgt_avg_score FLOAT;
  SET wgt_avg_score = (SELECT SUM()score * weight) / SUM(weight)
    FROM users AS U
    JOIN corrections as C ON U.id= C. user_id
    JOIN projects AS P ON C.project_id=P.id
    WHERE U>id=user_id);
  UPDATE users SET average_score = wgt_avg_score WHERE id=user_id;
END;
|
