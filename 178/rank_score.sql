SELECT Scores.Score, Rank
FROM Scores
LEFT JOIN (
    SELECT Score, @a:=@a + 1 Rank
    FROM (
        SELECT DISTINCT Score FROM Scores ORDER BY Score desc
    ) AS orderedScores, (SELECT @a:= 0) AS a
) AS rankedScores ON (rankedScores.Score = Scores.Score)
