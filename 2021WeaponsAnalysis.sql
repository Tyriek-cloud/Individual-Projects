/* I used a condensed version of the "NYPD Year to Date Arrests" shapefile (available here: https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc).
I then imported that data into Microsoft Access. The below is a series of multiple seperate queries to clean the data for analysis and for Tableau. 
Go here for the visualization: https://public.tableau.com/app/profile/tyriek.dashawn.warren/viz/2021AnalysisofWeaponsPossessioninthe73rdPrecinct/Story1 */

ALTER TABLE 2021_73rdArrests
DROP COLUMN ky_cd;

ALTER TABLE 2021_73rdArrests
DROP COLUMN law_cat_cd;

ALTER TABLE 2021_73rdArrests
DROP COLUMN pd_cd;

ALTER TABLE 2021_73rdArrests
DROP COLUMN time_arres;

SELECT *
FROM 2021_73rdArrests
WHERE pd_desc='WEAPONS POSSESSION 1 & 2';
