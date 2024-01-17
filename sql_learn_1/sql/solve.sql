-- Finding row number
WITH cte_row AS (
    SELECT
        your_column,
        ROW_NUMBER() OVER (order BY (SELECT NULL)) AS row

        FROM your_table
),
-- Finding group
cte_group AS (
    SELECT
        your_column, row,
        COUNT(your_column) OVER (order BY your_column) AS group

        FROM cte_row
)


-- Result
SELECT
    sum(your_column) OVER (PARTITION BY group) 

    FROM cte_group
    ORDER BY row