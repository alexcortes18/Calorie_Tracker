use Calorie_Tracker;

WITH RECURSIVE my_dates(date)	AS		(SELECT '2026-01-11'
										UNION ALL
										SELECT date + INTERVAL 1 DAY
										FROM my_dates
										WHERE date <= CURRENT_DATE),
				averages	 	AS		(SELECT date,
                                                NULLIF(weight,0) AS weight,
												COALESCE(total_calories,(SELECT	AVG(total_calories) FROM daily_summary)) AS total_calories
										FROM 	daily_summary),
				final 			AS		(SELECT	md.date, 
												a.weight, 
												a.total_calories,
												a.weight - LAG(a.weight) OVER (ORDER BY a.date ASC)AS daily_weight_difference
								FROM 	my_dates md LEFT JOIN averages a ON md.date = a.date)
-- SELECT AVG(daily_weight_difference) -- * 2.205 as lbs_lost_per_day
-- FROM(
	SELECT	date, weight, total_calories, daily_weight_difference
	FROM	final;
--    ) as avg_daily_weight_difference;