"""CSS-STYLES:
h1 {
   color: #d22e3a
}

h2 {
   color: #ff01ff
}
"""

from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/image_mars')
def sample():
    lst = """Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!""".split('\n')
    return f"""<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars.png')}" 
           alt="АХТУНГ!">
    
</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
