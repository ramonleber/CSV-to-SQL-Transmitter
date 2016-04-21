# CSV-SQL-Transmitter 

This Python script parses and transfers .csv data into a MySQL database.
It contains a PyQT GUI to login to MySQL-database. All .csv files located in the user given systempath will be processed and transmitted to the database.
If the database with the user give name not yet exists, it will be created.
The user needs to declare keys that define at which line in the .csv files, the data and information are located.

If you have a .csv file with the following content...

tbl; Adresses
atr; COUNTRY; ZIP_CODE; STREET; STREET_NUMBER
frm; char[30]; numeric[5.0]; char[30]; numeric[5.0]
add;  "Germany";      75196; "Karlstrasse"; 76
add;  "Germany";      80809; "Marienplatz"; 43
add;  "Germany";      39683; "Ludwig-Weg"; 4

...then "tbl" is the key to parse for the table name,
"atr" is the key to parse for the attribute names,
"frm" is the key to parse for the attribute types,
"add" is the key to parse for the data.
