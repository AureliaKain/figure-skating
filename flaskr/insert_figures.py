import sqlite3
from flaskr.db import get_db

get_db().execute('''
INSERT INTO figure (
id, 
title, 
videolink, 
category)
 
VALUES (
1, 
'Saut de valse',
'https://www.youtube.com/embed/eVP8r-ubbp8?list=PLHPS0ZfuDSceuVGrL4RV9KlXAZF7QMl9W',
 'Jump'
).fetchall()''')
