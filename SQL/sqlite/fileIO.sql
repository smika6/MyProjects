/* fileIO.sql */
/* SQLite file IO example */
.mode csv
.separator ,
--output output.csv

CREATE TABLE test(a INTEGER, b INTEGER);
.import input.csv testTable

SELECT * FROM testTable;
