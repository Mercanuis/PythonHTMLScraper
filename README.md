# PythonHTMLScraper
A small HTML Parser/Scraper for Python

Uses Python 2.7 because that was what I had on my dev laptop. With Python 3.0 I cannot verify nor know what might be different with regards to execution

Written in PyCharm, so forgive any weird any analysis rules it had with formatting. I am not sure if these follow Python 'Best Practices' when it comes to code organization

**How To Use**
There are 2 ways to use the scraper, you can call it via the command line with the following
```bash
python do_parse.py <URL> <target_word>
```

You should get something like this in the console:
```
python parse.py https://python.org the
No Value Can Be Found for https://python.org in DB, need to search
No Value Can Be Found for https://python.org in DB, need to search
Target = the, Count = 21
```
**Count is case insensitive:** 'The' and 'the' both count as a match for the inputed target

You can also create a HTTP listener for the reqeust. I used [SimpleHTTPServer](https://docs.python.org/2/library/basehttpserver.html) for this

```
python simpleserver.py 
Starting httpd...

```

Now you can send it something like the following:
```
curl http://localhost:8000/wordcount -X POST -H \
"Content-Type: application/json" \
-d '{"url":"https://www.python.org", "word":"python"}'
```

And should get something like this:
```
curl http://localhost:8000/wordcount -X POST -H \
"Content-Type: application/json" \
-d '{"url":"https://www.python.org", "word":"python"}'

{'status': 'ok', 'count': 46}HTTP/1.0 200 OK
Server: BaseHTTP/0.3 Python/2.7.15
Date: Thu, 14 Mar 2019 03:45:35 GMT
Content-type: application/json
```

The scraper is using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for the HTML parsing, and stripping of the words from the HTML into usable tokens. 

For the DB I'm using a technique shown in this [Medium Article](https://medium.freecodecamp.org/how-to-write-a-simple-toy-database-in-python-within-minutes-51ff49f47f1) that allows for a quick and dirty DB that can store previously found keys. The 'schema' is a `key: target/value` pairs where 'key' is the URL and 'target' is the word searched for. 
  
Caveats and Concerns
- Complexity is at worst **N^N** when you are looking for a new word, because then the scraper needs to fetch the HTML page, parse the tokens, and then collect the count. If there is a DB hit, then complexity is **N**
- Organization of the code is a mess. I wanted to learn more about proper module and class organization but I ran out of time
- `database` holds the db file upon initialization, the path is relative to where this is put and will likely need to be fixed if put in a different place
- `parse` is the name of the command-line script, but it holds a name close to the `parser.parse` function which is the main engine and service of the scraper, need to figure out a more clear name (Names are too hard! >:( )
- the HTTP response looks mangled and could probably be better recieved, need to learn how to set proper headers with the HTTP libraries
