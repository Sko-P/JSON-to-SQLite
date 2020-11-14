# JSON to SQLite database

## Description  

This tool takes a JSON file's data and puts it inside a SQLite Database.

It creates a database with a table named by you in the arguments when executing and adds columns to it based on the dictionnary's **keys** in the JSON file.

Exemple :

For a JSON file like the following : 

```json
[
{
    "id" : "lkqsq25454qsq",
    "name" : "Adelaïde",
    "age" : 20,
    "location" : "north",
    "division" : "b",
    "date" : "2004-01-02 18:44:43"
}
,
{
    "id" : "lkqsq27474qsq",
    "name" : "Adriane",
    "age" : 18,
    "location" : "west",
    "division" : "g",
    "date" : "2004-08-21 10:02:11"
}
]
```
You will have a database structured in this way : 

| id     | name | age | location | division | date |  
| ------ |----- |-----| -------- | -------- | ---- |
|lkqsq25454qsq|Adelaïde|20|north|b|2004-01-02 18:44:43|
|lkqsq27474qsq|Adriane|18|west|g|2004-08-21 10:02:11|

**NOTE :**  
* Make sure your dates inside the JSON file are written in the SQLite date format.
* This tool comes with a JSON file example named "dict.json"

## Installation  

* Clone this repository : 
```bash
git clone https://github.com/Sko-P/JSON-to-SQLite
```
## Usage
Put your .json file in the directory of the tool and use the following command :

```bash
python sql.py <json_file_name> <name_of_database> <name_of_table>
```
Replace the arguments by your own data

Exemple : 
```bash
python sql.py dict.json service.db equipement
```
In the above exemple :

* *dict.json* is the json file containing the data to put inside the database to be created
* *service.db* is the database that will be created to contain the JSON file's data
* *equipement* is the table that will be created inside your database (*service.db*) and will hold the JSON file's data.


## Contact

email : kmedelbachir@gmail.com
