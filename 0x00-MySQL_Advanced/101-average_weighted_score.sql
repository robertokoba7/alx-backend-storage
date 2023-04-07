-- SQL script which creates stored procedure and 
-- computes then store the average weighted score for all users.
DROP PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users AS U,
    (SELECT U.id, SUM(score * weight) / SUM(weight) AS wgt_avg
    FROM users AS U
    JOIN corrections as C ON U id=C.user_id
    JOIN projects P ON C.project_id=P.id
    GROUP BY U.id)
  AS WA
  SET U.average_score = WA.wgt_avg
  WHERE U.id=WA.id;
END;
|
