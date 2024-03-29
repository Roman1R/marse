from flask import Flask, url_for

app = Flask(__name__)


@app.route('/promotion_image')
def promotion_image():
    return """<!doctype>
<html>
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
    <link rel="stylesheet" 
href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
crossorigin="anonymous">
    <title>Колонизация!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="/static/img/mars.png" alt="АХТУНГ!">
    <div class="alert alert-primary" role="alert">
    Человечество вырастает из детства.
    </div>
    <div class="alert alert-secondary" role="alert">
    Человечеству мала одна планета.
    </div>
    <div class="alert alert-success" role="alert">
    Мы сделаем обитаемыми безжизненные пока планеты.
    </div>
    <div class="alert alert-danger" role="alert">
    И начнем с Марса!
    </div>
    <div class="alert alert-warning" role="alert">
    Присоединяйся!
    </div>
</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
