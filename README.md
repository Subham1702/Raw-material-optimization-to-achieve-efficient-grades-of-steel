# Raw-material-optimization-to-achieve-efficient-grades-of-steel
## Project Description:
### Business Problem:
The steel manufacturing industry faces significant challenges in identifying optimal combination of raw materials and energy inputs necessary to produce high-quality steel efficiently.
### Business Objective: 
Maximize steel quality, Minimize costs.
### Business Constraint: 
Minimize energy use.
### Business Success Criteria: 
Reduce the processing time by 50%.
### Economic Success Criteria: 
Achieve a cost saving of at least $1M.

## Data Understanding:
Data Dimension = 311 records, 27 attributes.
Data Dictionary:
![image](https://github.com/user-attachments/assets/c5a7007a-0b9b-4842-a70e-10f8565ce404)

## Exploratory Data Analysis(EDA) & Data Preprocessing:
<details>
  <summary>EDA using MySQL</summary>
	
  ```SQL
create database if not exists Steel_db;
USE Steel_db;
#drop table if exists steel_prod;
#truncate table steel_prod;

create table if not exists steel_prod (
steel_grade VARCHAR(20) NOT NULL,
auto_app VARCHAR(100) NOT NULL,
scrap_steel VARCHAR(10) NOT NULL,
pig_iron VARCHAR(10) NOT NULL,
iron_ore VARCHAR(10) NOT NULL,
phosphorus VARCHAR(10) NOT NULL,
carbon VARCHAR(10) NOT NULL,
melting_time_EAF VARCHAR(10) NOT NULL,
prod_vol VARCHAR(20) NOT NULL,
Yield VARCHAR(10) NOT NULL,
BF_SCT VARCHAR(10) NOT NULL,
EAF_SCT VARCHAR(10) NOT NULL,
LRF_SCT VARCHAR(10) NOT NULL,
Total_CT VARCHAR(10) NOT NULL,
BF_El VARCHAR(10) NOT NULL,
EAF_El VARCHAR(10) NOT NULL,
LRF_El VARCHAR(10) NOT NULL,
Total_El_Con VARCHAR(10) NOT NULL,
OriginalCost_Ton VARCHAR(10) NOT NULL,
new_scrap_steel VARCHAR(10) NOT NULL,
new_pig_iron VARCHAR(10) NOT NULL,
new_iron_ore VARCHAR(10) NOT NULL,
new_el_con VARCHAR(10) NOT NULL,
BF_El_new VARCHAR(10) NOT NULL,
EAF_El_new VARCHAR(10) NOT NULL,
LRF_El_new VARCHAR(10) NOT NULL,
Estimated_cost_per_ton VARCHAR(10) NOT NULL
);

set sql_safe_updates = 0;
DELETE FROM steel_prod WHERE new_scrap_steel = '#VALUE!';
select * from steel_prod;

											## Exploratory Data Analysis ##
# 1st moment business decision: -
## Mean:                                            
select avg(scrap_steel) from steel_prod;
select avg(pig_iron) from steel_prod;
select avg(iron_ore) from steel_prod;
select avg(phosphorus) from steel_prod;
select avg(carbon) from steel_prod;
select avg(melting_time_EAF) from steel_prod;
select avg(prod_vol) from steel_prod;
select avg(yield) from steel_prod;
select avg(BF_SCT) from steel_prod;
select avg(EAF_SCT) from steel_prod;
select avg(LRF_SCT) from steel_prod;
select avg(Total_CT) from steel_prod;
select avg(BF_El) from steel_prod;
select avg(EAF_El) from steel_prod;
select avg(LRF_El) from steel_prod;
select avg(Total_El_Con) from steel_prod;
select avg(OriginalCost_Ton) from steel_prod;
select avg(new_scrap_steel) from steel_prod;
select avg(new_pig_iron) from steel_prod;
select avg(new_iron_ore) from steel_prod;
select avg(new_el_con) from steel_prod;
select avg(BF_El_new) from steel_prod;
select avg(EAF_El_new) from steel_prod;
select avg(LRF_El_new) from steel_prod;
select avg(Estimated_cost_per_ton) from steel_prod;

## Median:
WITH cte AS (
    SELECT scrap_steel,
           ROW_NUMBER() OVER (ORDER BY scrap_steel) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(scrap_steel) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT pig_iron,
           ROW_NUMBER() OVER (ORDER BY pig_iron) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(pig_iron) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT iron_ore,
           ROW_NUMBER() OVER (ORDER BY iron_ore) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(iron_ore) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT carbon,
           ROW_NUMBER() OVER (ORDER BY carbon) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(carbon) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT phosphorus,
           ROW_NUMBER() OVER (ORDER BY phosphorus) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(phosphorus) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT melting_time_EAF,
           ROW_NUMBER() OVER (ORDER BY melting_time_EAF) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(melting_time_EAF) AS median_duration
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT prod_vol,
           ROW_NUMBER() OVER (ORDER BY prod_vol) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(prod_vol) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT yield,
           ROW_NUMBER() OVER (ORDER BY yield) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(yield) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT BF_SCT,
           ROW_NUMBER() OVER (ORDER BY BF_SCT) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(BF_SCT) AS median
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT EAF_SCT,
           ROW_NUMBER() OVER (ORDER BY EAF_SCT) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(EAF_SCT) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT LRF_SCT,
           ROW_NUMBER() OVER (ORDER BY LRF_SCT) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(LRF_SCT) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT total_CT,
           ROW_NUMBER() OVER (ORDER BY total_CT) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(total_CT) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT BF_El,
           ROW_NUMBER() OVER (ORDER BY BF_El) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(BF_El) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT EAF_El,
           ROW_NUMBER() OVER (ORDER BY EAF_El) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(EAF_El) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT LRF_El,
           ROW_NUMBER() OVER (ORDER BY LRF_El) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(LRF_El) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT Total_El_Con,
           ROW_NUMBER() OVER (ORDER BY Total_El_Con) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(Total_El_Con) AS median
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT OriginalCost_Ton,
           ROW_NUMBER() OVER (ORDER BY OriginalCost_Ton) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(OriginalCost_Ton) AS median
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT new_scrap_steel,
           ROW_NUMBER() OVER (ORDER BY new_scrap_steel) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(new_scrap_steel) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT new_pig_iron,
           ROW_NUMBER() OVER (ORDER BY new_pig_iron) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(new_pig_iron) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT new_iron_ore,
           ROW_NUMBER() OVER (ORDER BY new_iron_ore) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(new_iron_ore) AS median_val
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT Estimated_cost_per_ton,
           ROW_NUMBER() OVER (ORDER BY Estimated_cost_per_ton) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(Estimated_cost_per_ton) AS median
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT new_el_con,
           ROW_NUMBER() OVER (ORDER BY new_el_con) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(new_el_con) AS median
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT BF_El_new,
           ROW_NUMBER() OVER (ORDER BY BF_El_new) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(BF_El_new) AS median
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));

WITH cte AS (
    SELECT Estimated_cost_per_ton,
           ROW_NUMBER() OVER (ORDER BY Estimated_cost_per_ton) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM steel_prod
)
SELECT AVG(Estimated_cost_per_ton) AS median
FROM cte
WHERE row_num IN (FLOOR((total_count + 1) / 2), CEIL((total_count + 1) / 2));



## Mode:
SELECT steel_grade AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY steel_grade ORDER BY frequency DESC LIMIT 1; 
SELECT auto_app AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY auto_app ORDER BY frequency DESC LIMIT 1;
SELECT scrap_steel AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY scrap_steel ORDER BY frequency DESC LIMIT 1;
SELECT pig_iron AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY pig_iron ORDER BY frequency DESC LIMIT 1;
SELECT iron_ore AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY iron_ore ORDER BY frequency DESC LIMIT 1;
SELECT phosphorus AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY phosphorus ORDER BY frequency DESC LIMIT 1;
SELECT carbon AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY carbon ORDER BY frequency DESC LIMIT 1;
SELECT melting_time_EAF AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY melting_time_EAF ORDER BY frequency DESC LIMIT 1;
SELECT prod_vol AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY prod_vol ORDER BY frequency DESC LIMIT 1;
SELECT yield AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY yield ORDER BY frequency DESC LIMIT 1;
SELECT BF_SCT AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY BF_SCT ORDER BY frequency DESC LIMIT 1;
SELECT EAF_SCT AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY EAF_SCT ORDER BY frequency DESC LIMIT 1;
SELECT LRF_SCT AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY LRF_SCT ORDER BY frequency DESC LIMIT 1;
SELECT Total_CT AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY Total_CT ORDER BY frequency DESC LIMIT 1;
SELECT BF_El AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY BF_El ORDER BY frequency DESC LIMIT 1;
SELECT EAF_El AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY EAF_El ORDER BY frequency DESC LIMIT 1;
SELECT LRF_El AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY LRF_El ORDER BY frequency DESC LIMIT 1;
SELECT Total_El_Con AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY Total_El_Con ORDER BY frequency DESC LIMIT 1;
SELECT OriginalCost_Ton AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY OriginalCost_Ton ORDER BY frequency DESC LIMIT 1;
SELECT new_scrap_steel AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY new_scrap_steel ORDER BY frequency DESC LIMIT 1;
SELECT new_pig_iron AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY new_pig_iron ORDER BY frequency DESC LIMIT 1;
SELECT new_iron_ore AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY new_iron_ore ORDER BY frequency DESC LIMIT 1;
SELECT new_el_con AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY new_el_con ORDER BY frequency DESC LIMIT 1;
SELECT BF_El_new AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY BF_El_new ORDER BY frequency DESC LIMIT 1;
SELECT EAF_El_new AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY EAF_El_new ORDER BY frequency DESC LIMIT 1;
SELECT LRF_El_new AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY LRF_El_new ORDER BY frequency DESC LIMIT 1;
SELECT Estimated_cost_per_ton AS mode_value, COUNT(*) AS frequency FROM steel_prod GROUP BY Estimated_cost_per_ton ORDER BY frequency DESC LIMIT 1;

# 2nd moment business decision
## Range:
select round(MAX(Total_El_Con) - MIN(Total_El_Con), 4) as range_1 FROM steel_prod;
select round(MAX(OriginalCost_Ton) - MIN(OriginalCost_Ton), 4) as range_2 FROM steel_prod;
select round(MAX(new_el_con) - MIN(new_el_con), 4) as range_3 FROM steel_prod;
select round(MAX(Estimated_cost_per_ton) - MIN(Estimated_cost_per_ton), 4) as range_4 FROM steel_prod;
select round(MAX(scrap_steel) - MIN(scrap_steel), 4) as range_1 FROM steel_prod;
select round(MAX(pig_iron) - MIN(pig_iron), 4) as range_1 FROM steel_prod;
select round(MAX(phosphorus) - MIN(phosphorus), 4) as range_1 FROM steel_prod;
select round(MAX(iron_ore) - MIN(iron_ore), 4) as range_1 FROM steel_prod;
select round(MAX(carbon) - MIN(carbon), 4) as range_1 FROM steel_prod;
select round(MAX(melting_time_EAF) - MIN(melting_time_EAF), 4) as range_1 FROM steel_prod;
select round(MAX(prod_vol) - MIN(prod_vol), 4) as range_1 FROM steel_prod;
select round(MAX(yield) - MIN(yield), 4) as range_1 FROM steel_prod;
select round(MAX(BF_SCT) - MIN(BF_SCT), 4) as range_1 FROM steel_prod;
select round(MAX(EAF_SCT) - MIN(EAF_SCT), 4) as range_1 FROM steel_prod;
select round(MAX(LRF_SCT) - MIN(LRF_SCT), 4) as range_1 FROM steel_prod;
select round(MAX(Total_CT) - MIN(Total_CT), 4) as range_1 FROM steel_prod;
select round(MAX(BF_El) - MIN(BF_El), 4) as range_1 FROM steel_prod;
select round(MAX(LRF_El) - MIN(LRF_El), 4) as range_1 FROM steel_prod;
select round(MAX(Total_El_Con) - MIN(Total_El_Con), 4) as range_1 FROM steel_prod;
select round(MAX(OriginalCost_Ton) - MIN(OriginalCost_Ton), 4) as range_1 FROM steel_prod;
select round(MAX(new_scrap_steel) - MIN(new_scrap_steel), 4) as range_1 FROM steel_prod;
select round(MAX(new_pig_iron) - MIN(new_pig_iron), 4) as range_1 FROM steel_prod;
select round(MAX(new_iron_ore) - MIN(new_iron_ore), 4) as range_1 FROM steel_prod;

## Variance:
select ROUND((variance(Total_El_Con)), 4) as variance_1 from steel_prod;
select ROUND((variance(OriginalCost_Ton)), 4) as variance_2 from steel_prod;
select ROUND((variance(new_el_con)), 4) as variance_3 from steel_prod;
select ROUND((variance(Estimated_cost_per_ton)), 4) as variance_4 from steel_prod;

## Standard Deviation:
select round((stddev(Total_El_Con)), 4) FROM steel_prod;
select round((stddev(OriginalCost_Ton)), 4) FROM steel_prod;
select round((stddev(new_el_con)), 4) FROM steel_prod;
select round((stddev(scrap_steel)), 4) FROM steel_prod;
select round((stddev(pig_iron)), 4) FROM steel_prod;
select round((stddev(iron_ore)), 4) FROM steel_prod;
select round((stddev(carbon)), 4) FROM steel_prod;
select round((stddev(phosphorus)), 4) FROM steel_prod;
select round((stddev(melting_time_EAF)), 4) FROM steel_prod;
select round((stddev(prod_vol)), 4) FROM steel_prod;
select round((stddev(yield)), 4) FROM steel_prod;
select round((stddev(BF_SCT)), 4) FROM steel_prod;
select round((stddev(EAF_SCT)), 4) FROM steel_prod;
select round((stddev(LRF_SCT)), 4) FROM steel_prod;
select round((stddev(prod_vol)), 4) FROM steel_prod;
select round((stddev(yield)), 4) FROM steel_prod;
select round((stddev(Total_CT)), 4) FROM steel_prod;
select round((stddev(BF_El)), 4) FROM steel_prod;
select round((stddev(EAF_El)), 4) FROM steel_prod;
select round((stddev(LRF_El)), 4) FROM steel_prod;
select round((stddev(Total_El_Con)), 4) FROM steel_prod;
select round((stddev(OriginalCost_Ton)), 4) FROM steel_prod;
select round((stddev(new_scrap_steel)), 4) FROM steel_prod;
select round((stddev(new_pig_iron)), 4) FROM steel_prod;
select round((stddev(new_iron_ore)), 4) FROM steel_prod;
select round((stddev(new_el_con)), 4) FROM steel_prod;
select round((stddev(BF_El_new)), 4) FROM steel_prod;
select round((stddev(EAF_El_new)), 4) FROM steel_prod;
select round((stddev(LRF_El_new)), 4) FROM steel_prod;
select round((stddev(Estimated_cost_per_ton)), 4) FROM steel_prod;



# 3rd Moment Business Decision
## Skewness:
SELECT
(
SUM(POWER(Total_El_Con- (SELECT AVG(Total_El_Con) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Total_El_Con) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(OriginalCost_Ton- (SELECT AVG(OriginalCost_Ton) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(OriginalCost_Ton) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(new_el_con- (SELECT AVG(new_el_con) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(new_el_con) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(Estimated_cost_per_ton- (SELECT AVG(Estimated_cost_per_ton) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Estimated_cost_per_ton) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(scrap_steel- (SELECT AVG(scrap_steel) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(scrap_steel) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(pig_iron- (SELECT AVG(pig_iron) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(pig_iron) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(iron_ore- (SELECT AVG(iron_ore) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(iron_ore) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(phosphorus- (SELECT AVG(phosphorus) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(phosphorus) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(carbon- (SELECT AVG(carbon) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(carbon) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(melting_time_EAF- (SELECT AVG(melting_time_EAF) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(melting_time_EAF) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(prod_vol- (SELECT AVG(prod_vol) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(prod_vol) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(yield- (SELECT AVG(yield) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(yield) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(BF_SCT- (SELECT AVG(BF_SCT) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(BF_SCT) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(EAF_SCT- (SELECT AVG(EAF_SCT) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(EAF_SCT) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(LRF_SCT- (SELECT AVG(LRF_SCT) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(LRF_SCT) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(Total_CT- (SELECT AVG(Total_CT) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Total_CT) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(BF_El- (SELECT AVG(BF_El) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(BF_El) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(EAF_El- (SELECT AVG(EAF_El) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(EAF_El) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(LRF_El- (SELECT AVG(LRF_El) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(LRF_El) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(Total_El_Con- (SELECT AVG(Total_El_Con) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Total_El_Con) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(OriginalCost_Ton- (SELECT AVG(OriginalCost_Ton) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(OriginalCost_Ton) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(new_scrap_steel- (SELECT AVG(new_scrap_steel) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(new_scrap_steel) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(new_pig_iron- (SELECT AVG(new_pig_iron) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(new_pig_iron) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(new_iron_ore- (SELECT AVG(new_iron_ore) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(new_iron_ore) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(BF_El_new - (SELECT AVG(BF_El_new) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(BF_El_new) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(EAF_El_new- (SELECT AVG(EAF_El_new) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(EAF_El_new) FROM steel_prod), 3))
) AS skewness FROM steel_prod;

SELECT
(
SUM(POWER(LRF_El_new- (SELECT AVG(LRF_El_new) FROM steel_prod), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(LRF_El_new) FROM steel_prod), 3))
) AS skewness FROM steel_prod;



# 4th moment of business decision
## Kurtosis:
SELECT
(
(SUM(POWER(Total_El_Con- (SELECT AVG(Total_El_Con) FROM steel_prod), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Total_El_Con) FROM steel_prod), 4))) - 3
) AS kurtosis FROM steel_prod;

SELECT
(
(SUM(POWER(OriginalCost_Ton- (SELECT AVG(OriginalCost_Ton) FROM steel_prod), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(OriginalCost_Ton) FROM steel_prod), 4))) - 3
) AS kurtosis FROM steel_prod;

SELECT
(
(SUM(POWER(new_el_con- (SELECT AVG(new_el_con) FROM steel_prod), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(new_el_con) FROM steel_prod), 4))) - 3
) AS kurtosis FROM steel_prod;

SELECT
(
(SUM(POWER(Estimated_cost_per_ton- (SELECT AVG(Estimated_cost_per_ton) FROM steel_prod), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Estimated_cost_per_ton) FROM steel_prod), 4))) - 3
) AS kurtosis FROM steel_prod;


													### Querying the data ###
select * from steel_prod;
select count(distinct(steel_grade)) from steel_prod;         #204
select steel_grade, count(*) as frequency from steel_prod GROUP BY steel_grade ORDER BY frequency DESC LIMIT 1;   # AISI 5120                                                
select steel_grade, count(*) as frequency from steel_prod GROUP BY steel_grade ORDER BY frequency LIMIT 1;  # AISI 1010
select auto_app from steel_prod WHERE steel_grade = 'AISI 5120';   # gears, structural comp, axles
select auto_app from steel_prod WHERE steel_grade = 'AISI 1010';   # body panels, brackets

select count(distinct(auto_app)) from steel_prod;   #108
select auto_app, count(*) as frequency from steel_prod GROUP BY auto_app ORDER BY frequency DESC LIMIT 1;   #structural parts requiring high strength
select auto_app, count(*) as frequency from steel_prod GROUP BY auto_app ORDER BY frequency LIMIT 1;   #body panels, brackets


select avg(pig_iron) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(pig_iron) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(iron_ore) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(pig_iron) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(phosphorus) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(phosphorus) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(scrap_steel) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(scrap_steel) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(carbon) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(carbon) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(melting_time_EAF) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(melting_time_EAF) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(prod_vol) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(prod_vol) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(yield) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(yield) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(BF_SCT) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(BF_SCT) from steel_prod WHERE steel_grade = 'AISI 5120';
select AVG(EAF_SCT) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(EAF_SCT) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(LRF_SCT) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(LRF_SCT) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(Total_CT) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(Total_CT) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(BF_El) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(BF_El) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(EAF_El) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(EAF_El) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(LRF_El) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(LRF_El) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(Total_El_con) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(Total_El_con) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(OriginalCost_Ton) from steel_prod WHERE steel_grade = 'AISI 5120';

select avg(new_scrap_steel) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(new_scrap_steel) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(new_pig_iron) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(new_pig_iron) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(new_iron_ore) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(new_iron_ore) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(new_el_con) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(new_el_con) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(BF_El_new) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(BF_El_new) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(EAF_El_new) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(EAF_El_new) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(LRF_El_new) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(LRF_El_new) from steel_prod WHERE steel_grade = 'AISI 5120';
select avg(Estimated_cost_per_ton) from steel_prod WHERE steel_grade = 'AISI 5120';
select max(Estimated_cost_per_ton) from steel_prod WHERE steel_grade = 'AISI 5120';



													### Data Preprocessing ###
#A) Handling duplicates:
SELECT steel_grade, auto_app, COUNT(*)
FROM steel_prod
GROUP BY steel_grade, auto_app
HAVING COUNT(*) > 1;

WITH DuplicateRecords AS (
    SELECT steel_grade, auto_app, COUNT(*)
    FROM steel_prod
    GROUP BY steel_grade, auto_app
    HAVING COUNT(*) > 1
)
SELECT sg.*
FROM steel_prod sg
JOIN DuplicateRecords dr
ON sg.steel_grade = dr.steel_grade AND sg.auto_app = dr.auto_app;


		# Outlier Analysis #
#A) Identification:
WITH orderedList AS (
    SELECT scrap_steel, ROW_NUMBER() OVER (ORDER BY scrap_steel) AS row_n
    FROM steel_prod
),
iqr AS (
    SELECT
        scrap_steel,
        q3_value AS q_three,
        q1_value AS q_one,
        q3_value - q1_value AS outlier_range
    FROM orderedList
    JOIN (SELECT scrap_steel AS q3_value FROM orderedList WHERE row_n = FLOOR((SELECT COUNT(*) FROM steel_prod) * 0.75)) q3 ON 1=1
    JOIN (SELECT scrap_steel AS q1_value FROM orderedList WHERE row_n = FLOOR((SELECT COUNT(*) FROM steel_prod) * 0.25)) q1 ON 1=1
)
SELECT count(scrap_steel) AS outlier_value
FROM iqr
WHERE scrap_steel >= q_three + outlier_range
   OR scrap_steel <= q_one - outlier_range;          # 19

WITH orderedList AS (
    SELECT pig_iron, ROW_NUMBER() OVER (ORDER BY pig_iron) AS row_n
    FROM steel_prod
),
iqr AS (
    SELECT
        pig_iron,
        q3_value AS q_three,
        q1_value AS q_one,
        q3_value - q1_value AS outlier_range
    FROM orderedList
    JOIN (SELECT pig_iron AS q3_value FROM orderedList WHERE row_n = FLOOR((SELECT COUNT(*) FROM steel_prod) * 0.75)) q3 ON 1=1
    JOIN (SELECT pig_iron AS q1_value FROM orderedList WHERE row_n = FLOOR((SELECT COUNT(*) FROM steel_prod) * 0.25)) q1 ON 1=1
)
SELECT pig_iron AS outlier_value
FROM iqr
WHERE pig_iron >= q_three + outlier_range
   OR pig_iron <= q_one - outlier_range;     # 0
   
WITH orderedList AS (
    SELECT phosphorus, ROW_NUMBER() OVER (ORDER BY phosphorus) AS row_n
    FROM steel_prod
),
iqr AS (
    SELECT
        phosphorus,
        q3_value AS q_three,
        q1_value AS q_one,
        q3_value - q1_value AS outlier_range
    FROM orderedList
    JOIN (SELECT phosphorus AS q3_value FROM orderedList WHERE row_n = FLOOR((SELECT COUNT(*) FROM steel_prod) * 0.75)) q3 ON 1=1
    JOIN (SELECT phosphorus AS q1_value FROM orderedList WHERE row_n = FLOOR((SELECT COUNT(*) FROM steel_prod) * 0.25)) q1 ON 1=1
)
SELECT distinct(count(phosphorus)) AS outlier_value
FROM iqr
WHERE phosphorus >= q_three + outlier_range
   OR phosphorus <= q_one - outlier_range;        # 77
   
WITH orderedList AS (
    SELECT yield, ROW_NUMBER() OVER (ORDER BY yield) AS row_n
    FROM steel_prod
),
iqr AS (
    SELECT
        yield,
        q3_value AS q_three,
        q1_value AS q_one,
        q3_value - q1_value AS outlier_range
    FROM orderedList
    JOIN (SELECT yield AS q3_value FROM orderedList WHERE row_n = FLOOR((SELECT COUNT(*) FROM steel_prod) * 0.75)) q3 ON 1=1
    JOIN (SELECT yield AS q1_value FROM orderedList WHERE row_n = FLOOR((SELECT COUNT(*) FROM steel_prod) * 0.25)) q1 ON 1=1
)
SELECT yield AS outlier_value
FROM iqr
WHERE yield >= q_three + outlier_range
   OR yield <= q_one - outlier_range;      #51
   
WITH orderedList AS (
    SELECT OriginalCost_Ton, ROW_NUMBER() OVER (ORDER BY OriginalCost_Ton) AS row_n
    FROM steel_prod
),
iqr AS (
    SELECT
        OriginalCost_Ton,
        q3_value AS q_three,
        q1_value AS q_one,
        q3_value - q1_value AS outlier_range
    FROM orderedList
    JOIN (SELECT OriginalCost_Ton AS q3_value FROM orderedList WHERE row_n = FLOOR((SELECT COUNT(*) FROM steel_prod) * 0.75)) q3 ON 1=1
    JOIN (SELECT OriginalCost_Ton AS q1_value FROM orderedList WHERE row_n = FLOOR((SELECT COUNT(*) FROM steel_prod) * 0.25)) q1 ON 1=1
)
SELECT count(OriginalCost_Ton) AS outlier_value
FROM iqr
WHERE OriginalCost_Ton >= q_three + outlier_range
   OR OriginalCost_Ton <= q_one - outlier_range;        # 312
   
#B) Removal of outlier values:


   
# Zero and near-zero variance:
select variance(scrap_steel) as V1 from steel_prod;
select variance(pig_iron) as V2 from steel_prod;
select variance(iron_ore) as V3 from steel_prod;
select variance(phosphorus) as V4 from steel_prod;
select variance(carbon) as V5 from steel_prod;
select variance(melting_time_EAF) as V6 from steel_prod;
select variance(prod_vol) as V7 from steel_prod;
select variance(yield) as V8 from steel_prod;
select variance(BF_SCT) as V9 from steel_prod;
select variance(EAF_SCT) as V10 from steel_prod;
select variance(LRF_SCT) as V11 from steel_prod;
select variance(Total_CT) as V12 from steel_prod;
select variance(BF_El) as V13 from steel_prod;
select variance(LRF_El) as V14 from steel_prod;



									# Normalization (min-max scaling)
select * from steel_prod;
CREATE TABLE Steel_scaled AS
SELECT
steel_grade,
auto_app,
scrap_steel,
pig_iron,
phosphorus,
carbon,
melting_time_EAF,
(prod_vol - min_prod_vol) / (max_prod_vol - min_prod_vol) AS scaled_vol,
BF_El,
EAF_El,
LRF_El
(Total_El_Con - min_Total_El_Con) / (max_Total_El_Con - min_Total_El_Con) AS scaled_total_con,
OriginalCost_Ton,
new_scrap_steel,
new_pig_iron,
new_iron_ore,
(new_el_con - min_new_el_con) / (max_new_el_con - min_new_el_con) AS scaled_new_el_con,
BF_El_new,
EAF_El_new,
LRF_El_new,
Estimated_cost_per_ton
FROM (
SELECT
steel_grade,
auto_app,
scrap_steel,
pig_iron,
phosphorus,
carbon,
melting_time_EAF,
(SELECT MIN(prod_vol) FROM steel_prod) AS min_prod_vol,
(SELECT MAX(prod_vol) FROM steel_prod) AS max_prod_vol,
BF_El,
EAF_El,
LRF_El,
(select MAX(Total_El_Con) FROM steel_prod) AS max_Total_El_Con,
(select MIN(Total_El_Con) from steel_prod) AS min_Total_El_Con,
OriginalCost_Ton,
new_scrap_steel,
new_pig_iron,
new_iron_ore,
(select max(new_el_con) from steel_prod) AS max_new_el_con,
(select min(new_el_con) from steel_prod) AS min_new_el_con,
BF_El_new,
EAF_El_new,
LRF_El_new,
Estimated_cost_per_ton
FROM steel_prod
) AS scaled_data;
```
</details>

## Dashboard 1: KPI.
![alt text](https://github.com/Subham1702/Raw-material-optimization-to-achieve-efficient-grades-of-steel/blob/main/Screenshot%20(368).png)

## Dashboard 2: Detailed Report.
![alt text](https://github.com/Subham1702/Raw-material-optimization-to-achieve-efficient-grades-of-steel/blob/main/Screenshot%20(367).png)

## Insights from the Data Analysis:
1. Correlation Matrix:
![alt text](https://github.com/Subham1702/Raw-material-optimization-to-achieve-efficient-grades-of-steel/blob/main/Correlation%20Matrix.png)
- Scrap steel usage is positively correlated with yield increasing scrap steel leads to better production efficiency.
- Higher scrap steel usage shows a slight reduction in energy consumption making it more energy-efficient.
- Increasing the proportion of scrap steel can help optimize both yield and energy use
- Pig iron usage negatively correlates with yield meaning higher use reduces production efficiency.
- Increased pig iron usage slightly raises energy consumption driving up energy requirements.
- Total energy consumption strongly correlates with production costs, indicating that higher energy use leads to increased costs per ton.
2. Scatter Plot:
  ![alt text](https://github.com/Subham1702/Raw-material-optimization-to-achieve-efficient-grades-of-steel/blob/main/Scatter_1.png)
   (a). Scrap Steel (%) vs. Total Energy Consumption (Kwh): As the percentage of scrap steel increases, total energy consumption tends to decrease or remain stable. This suggests that increasing scrap steel usage could lead to more energy-efficient production, supporting the goal of minimizing energy consumption.

  
  ![alt text](https://github.com/Subham1702/Raw-material-optimization-to-achieve-efficient-grades-of-steel/blob/main/Scatter_2.png)
   (b). Pig Iron (%) vs. Estimated Cost per Ton ($): Higher percentages of pig iron result in higher estimated costs per ton. The plot shows a clear upward trend, meaning that reducing pig iron usage can help achieve cost savings, aligning with the business objective of reducing costs.

### Statistical Insights:
1. Correlation Analysis:
   - Scrap Steel (%) is positively correlated with Yield (%) and negatively correlated with Total Energy Consumption, meaning increased scrap steel usage improves yield and reduces energy consumption.
   - Pig Iron (%) is negatively correlated with Yield (%) and positively correlated with Estimated Cost per Ton. Higher pig iron usage increases production costs and lowers yield.
   - Total Energy Consumption is highly correlated with Cost per Ton, indicating that reducing energy consumption will directly reduce production costs.

2. Scatter Plots Analysis:
   - Increasing Scrap Steel usage leads to lower energy consumption, while higher Pig Iron usage increases costs.
   - Cost savings can be improved by optimizing the balance between scrap steel and pig iron.
  
### Business Insights:
1. Increase Scrap Steel Usage: This will help reduce energy consumption and increase yield, leading to cost savings.
2. Reduce Pig Iron Usage: Decreasing pig iron will lower production costs and increase efficiency.
3. Focus on Reducing Energy Consumption: Reducing energy usage, especially in energy-intensive stages, will help achieve the $1M cost-saving target.

## Recommendations:
- Optimize material composition to maximize yield and minimize costs.
- Focus on improving energy efficiency in the Electric Arc Furnace (EAF) and Ladle Refining Furnace (LRF) stages.




