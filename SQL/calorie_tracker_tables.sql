-- Creating tables for Calorie Tracker App

USE Calorie_Tracker;

CREATE TABLE food_log(
	id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    meal_type VARCHAR(20) NOT NULL, -- breakfast, lunch, dinner, snack
    food_item VARCHAR(100) NOT NULL, -- any meal item
    calories FLOAT NOT NULL, -- kCal
    protein FLOAT NOT NULL, -- (g)
    fat FLOAT NOT NULL, -- (g)
    carbs FLOAT NOT NULL -- (g)
);
-- drop table food_log;

CREATE TABLE exercise_log(
	id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    exercise VARCHAR(50) NOT NULL, -- cardio, weightlifting
    duration FLOAT NOT NULL, -- in minutes
    calories_burned FLOAT NOT NULL
);

-- CREATE TABLE body_stats( -- This table does not need to be called everyday.
-- 	id INT AUTO_INCREMENT PRIMARY KEY,
--     date DATE NOT NULL,
--     weight FLOAT -- kg
-- );
-- drop table body_stats;  -- This is duplicated info from daily_summary

CREATE TABLE daily_summary (
    date DATE PRIMARY KEY,
    weight FLOAT NOT NULL, -- preferably measured at the beginning of the day
    total_calories FLOAT NOT NULL,
    notes VARCHAR(100)
);

-- ------------------------------------------------------------------------------------------------------------------------------------------
-- INSERT some values manually:
-- Jan 8th:
-- Food log
INSERT INTO food_log (date, meal_type, food_item, calories, protein, fat, carbs) VALUES
('2026-01-08', 'Breakfast', 'Oat pancakes + banana + honey', 520, 18, 12, 85),
('2026-01-08', 'Snack', 'Coffee + sugar + milk', 108, 0, 0, 27),
('2026-01-08', 'Lunch', 'Chicken, beans, cheese, veg, sweet potato', 635, 76, 19, 40),
('2026-01-08', 'Dinner', 'Oatmeal + apple juice', 425, 10, 5, 85),
('2026-01-08', 'Snack', 'Dalmata', 190, 2, 6.89, 30);

-- Exercise log
INSERT INTO exercise_log (date, exercise, duration, calories_burned) VALUES
('2026-01-08', 'Weights', 60, 250);

-- Daily summary
INSERT INTO daily_summary (date, weight, total_calories, notes) VALUES
('2026-01-08', 73.8, 1628, NULL);

-- ---------------------------------------------------------------------------------------------
-- Jan 9th:
-- Food log
INSERT INTO food_log (date, meal_type, food_item, calories, protein, fat, carbs) VALUES
('2026-01-09', 'Breakfast', 'French toast, 90g + honey', 238, 9, 8, 34),
('2026-01-09', 'Lunch', 'beans, ground beef,plantain, potato salad, cuajada,apple juice', 1093, 56, 46, 111);

-- Exercise log
-- No exercise yet

-- Daily summary
INSERT INTO daily_summary (date, weight, total_calories, notes) VALUES
('2026-01-09', 73.6, 1331, NULL);
















    