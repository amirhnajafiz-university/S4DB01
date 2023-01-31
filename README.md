<h1 align="center">
    S4DB01
</h1>

<br />

My database final project at AUT.CEIT

## Project

The main idea was to create a strem website database, where we have some 
movies and users, and a single admin. Users can search movies, watch them, put comments for them and also list them.
Admin can add, remove or edit the movies.

Check the project <a href="./schema/README.md">Schema</a> for more information about how the project is implement.

## Execute

First install module <b>SQLite3</b> for python3:

```shell
pip install pysqlite3
```

The run the <i>createDB</i> file:

```shell
python createDB.py
```

After that run the application on main:

```shell
python main.py
```
