[![CI](https://github.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_6/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_6/actions/workflows/cicd.yml)
# Eric Ortega Rodriguez Mini Project 6

# Complex SQL Query for MySQL Database - Using Avengers Data Set

<p align="center">
  <img src="image-5.png" alt="Avengers Data Set">
</p>

## Overview
This project implements a complex SQL query involving **joins**, **aggregation**, and **sorting** using an external database. The external database used in this project is [Databricks](https://databricks.com/), and the query fetches data from two related tables (`Avengers` and `Battles`) to calculate the total number of appearances and battles per Avenger. The I used can be found [here.](https://github.com/fivethirtyeight/data/tree/refs/heads/master/avengers)

## Requirements
1. **SQL Query**: Design and implement a complex SQL query that:
   - Joins data from multiple tables.
   - Aggregates data to compute totals.
   - Sorts the results based on specific criteria.

2. **Explanation**: Provide detailed documentation explaining what the query does and the expected results.

3. **CI/CD Pipeline**: Implement a basic Continuous Integration/Continuous Deployment (CI/CD) pipeline that automatically runs tests and ensures the query executes without errors.

4. **README**: This document explains the query, its purpose, and how to run it. It is also the one you are currently reading. 😄

---

## Query Explanation

The following SQL query was designed for a **MySQL-compatible** database (Databricks in this case). It retrieves information about Avengers and their battle history, joining two tables (`Avengers` and `Battles`) to calculate the total number of battles each Avenger has participated in, as well as their total appearances in comics. The results are sorted by the number of battles and the number of appearances.

### SQL Query:

```sql
SELECT 
    a.`Name/Alias`, 
    SUM(a.Appearances) AS total_appearances, 
    COUNT(b.battle_id) AS total_battles
FROM 
    Avengers a
JOIN 
    Battles b ON a.avenger_id = b.avenger_id
GROUP BY 
    a.`Name/Alias`
HAVING 
    SUM(a.Appearances) > 100  -- Only Avengers with more than 100 appearances
ORDER BY 
    total_battles DESC, total_appearances DESC;

```
## Deliverables 
### 1. SQL query
### 2. Written or video explanation of the query

# Written Explanation of the SQL Query

This query is designed to retrieve data about the Avengers and their participation in battles. The main purpose of the query is to calculate two key metrics for each Avenger:

1. **Total number of comic book appearances**.
2. **Total number of battles they have fought**.

Additionally, the query filters out any Avengers with fewer than 100 comic book appearances, and it sorts the results based on the total number of battles fought (from most to least) and, secondarily, by total appearances.

### Query Breakdown:

1. **FROM and JOIN Clauses**:
   - The query is pulling data from two tables: `Avengers` and `Battles`.
   - The `JOIN` clause is used to link the two tables using the `avenger_id` field, which exists in both tables. This allows the query to combine information about each Avenger from the `Avengers` table with information about their participation in battles from the `Battles` table.

2. **SELECT Clause**:
   - `a.Name/Alias`: Selects the name/alias of the Avenger from the `Avengers` table.
   - `SUM(a.Appearances) AS total_appearances`: This sums the number of comic book appearances for each Avenger. The `SUM()` function aggregates the values in the `Appearances` column for each Avenger.
   - `COUNT(b.battle_id) AS total_battles`: This counts the number of battles that each Avenger has participated in, based on the number of `battle_id` entries in the `Battles` table.

3. **GROUP BY Clause**:
   - The query groups the results by `a.Name/Alias`
4. **HAVING Clause**:
   - The `HAVING` clause filters out Avengers who have appeared in fewer than 100 comic books. The query only returns Avengers with 100 or more appearances (calculated by the `SUM(a.Appearances)`) are included in the results.

5. **ORDER BY Clause**:
   - The results are first sorted by `total_battles DESC`, meaning that Avengers with the highest number of battles appear on the list first

### For example:

The `Avengers` table contains the following data:

| avenger_id | Name/Alias      | Appearances |
|------------|-----------------|-------------|
| 1          | Iron Man        | 3000        |
| 2          | Captain America | 2800        |

Then the `Battles` table contains:

| battle_id | avenger_id |
|-----------|------------|
| 1         | 1          |
| 2         | 1          |
| 3         | 2          |
| 4         | 2          |
| 5         | 3          |

The query would do the following:
- Join the two tables based on `avenger_id`
- Calculate Iron Man has 3000 appearances and 2 battles, 
- Calculates that Captain America has 2800 appearances and 2 battles
- Return Iron Man and Captain America and would be sorted by their number of battles and appearances

### Expected Results:

| Name/Alias      | total_appearances | total_battles |
|-----------------|-------------------|---------------|
| Iron Man        | 3000              | 2             |
| Captain America | 2800              | 2             |


### In conclusion:

This query allows us to gain insight into the involvement of different Avengers and take a closer look at how much prevalence they had within the comic universe and battles.

