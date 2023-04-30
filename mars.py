
from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


d = {
    "title": "Анкета",
    "surname": "",
    "name": "",
    "education": "",
    "profession": "",
    "sex": "",
    "motivation": "",
    "ready": ""
}


class LoginForm(FlaskForm):
    astronaut_id = IntegerField("Id астронавта", validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    capitan_id = IntegerField("Id капитана", validators=[DataRequired()])
    capitan_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route("/success")
def success():
    return "Всё ок"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/')
def start():
    return """<b><h1>Миссия Колонизация Марса</h1></b>"""


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    return render_template("base.html", title=title)


@app.route("/training/<prof>")
def proff(prof):
    return render_template("training.html", prof=prof.lower())


@app.route("/list_prof/<list_type>")
def list_proff(list_type):
    if list_type.lower() not in ("ol", "ul"):
        return "Некорректный параметр (Введите ol или ul)"
    arr = ["Программист", "Доктор", "Инженер", "Пилот", "Эколог"]
    return render_template("list_prof.html", prof_list=arr, list_type=list_type)


# данные, введённые в анкете(/astronaut_selection) сохраняются в словарь d
# в шаблон передаётся этот словарь
@app.route("/answer")
@app.route("/auto_answer")
def answer():
    print(d)
    return render_template("auto_answer.html", title=d["title"], d=d)


@app.route('/choice/<planet_name>')
def choice(planet_name):
    planet_name = planet_name.capitalize()
    d = {
        "Меркурий": {
            "number": 1,
            "color": "серого",
            "moons": 0
        },
        "Венера": {
            "number": 2,
            "color": "жёлтого",
            "moons": 0
        },
        "Земля": {
            "number": 3,
            "color": "синего",
            "moons": 1
        },
        "Марс": {
            "number": 4,
            "color": "красного",
            "moons": 2
        },
        "Юпитер": {
            "number": 5,
            "color": "оранжевого",
            "moons": 67
        },
        "Сатурн": {
            "number": 6,
            "color": "желтого",
            "moons": 63
        },
        "Уран": {
            "number": 7,
            "color": "голубого",
            "moons": 27
        },
        "Нептун": {
            "number": 8,
            "color": "синего",
            "moons": 14
        }
    }
    if planet_name not in d:
        return """<h1>Неизвестная планета</h1>"""
    return f"""
            <!doctype html>
            <html lang="en">
                <head>
                    <title>Варианты выбора</title>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="static\css\style.css">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                </head>
                <body>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
                    <div class="container mt-3">
                        <h1 class="text-primary text-center">Моё предложение: {planet_name}</h1>
                        <h3 class="text-white bg-primary">Эта планета {d[planet_name]['number']} по счёту от солнца.</h3>
                        <h3 class="text-white bg-success">Она {d[planet_name]['color']} цвета</h3>
                        <h3 class="text-white bg-info">У неё {d[planet_name]['moons']} спутников</h3>
                    </div>
                </body>
            </html>
           """


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f"""
            <!doctype html>
            <html lang="en">
                <head>
                    <title>Результаты</title>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="static\css\style.css">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                </head>
                <body>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
                    <div class="container mt-3">
                        <h1 class="text-dark text-center">Результаты отбора</h1>
                        <h2 class="text-dark text-center">Претендента на участие в миссии {nickname}:</h2>
                        <h3 class="text-white bg-primary">Поздравляем! Ваш рейстинг после прохождения {level} этапа отбора составляет {rating}!</h3>
                        <h3 class="text-white bg-success">Желаем удачи!</h3>
                    </div>
                </body>
            </html>
           """


@app.route("/promotion_image")
def promotion():
    # phrases = [
    #         "Человечество вырастает из детства.",
    #         "Человечеству мала одна планета.",
    #         "Мы сделаем обитаемыми безжизненные пока планеты.",
    #         "И начнем с Марса!",
    #         "Присоединяйся!"
    #     ]
    # return "<b><h2>" + "<br>".join(phrases) + "</h2></b>"
    return f"""
            <!doctype html>
            <html lang="en">
                <head>
                    <title>Привет, Марс!</title>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="static\css\style.css">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                </head>
                <body>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
                    <div class="base_container">
                        <h1><center>Жди нас, Марс!</center></h1>
                        <figure class="base_container">
                            <img src="static\img\mars.png" width=200>
                            <figcaption>Вот она какая, красная планета.</figcaption>
                        </figure>
                    </div>
                    <div class="container mt-3">
                        <p class="text-white-50 bg-success">Человечество вырастает из детства.</p>
                        <p class="text-white-50 bg-primary">Человечеству мала одна планета.</p>
                        <p class="text-white-50 bg-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                        <p class="text-danger bg-warning">И начнем с Марса!</p>
                        <p class="text-white-50 bg-dark">Присоединяйся!</p>
                    </div>
                </body>
            </html>
           """


@app.route("/carousel")
def mars_carousel():
    return f"""
            <!doctype html>
            <html lang="en">
                <head>
                    <title>Пейзажи Марса</title>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="static\css\style.css">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                </head>
                <body>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
                    <h1 class="text-dark text-center">Пейзажи Марса</h1>
                    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                        <div class="carousel-indicators">
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                        </div>
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                            <img src="static/img/1.jpg" class="d-block w-100" alt="...">
                            </div>
                            <div class="carousel-item">
                            <img src="static/img/2.jpg" class="d-block w-100" alt="...">
                            </div>
                            <div class="carousel-item">
                            <img src="static/img/3.png" class="d-block w-100" alt="...">
                            </div>
                        </div>
                        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Previous</span>
                        </button>
                        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Next</span>
                        </button>
                        </div>
                </body>
            </html>
           """


@app.route("/astronaut_selection", methods=["POST", "GET"])
def form():
    if request.method == "GET":
        return f"""
                <!DOCTYPE HTML>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                        <title>Отбор астронавтов</title>
                    </head>
                    <body>
                        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
                        <h1 class="text-primary text-center">Анкета претендента</h1>
                        <h2 class="text-secondary text-center">на участие в миссии</h2>
                        <div>
                            <form class="login_form" method="post">
                                <input type="text" class="form-control" placeholder="Введите фамилию" name="surname">
                                <input type="text" class="form-control" placeholder="Введите имя" name="name">
                                <input type="text" class="form-control" placeholder="Введите адрес почты" name="email">
                                <div>
                                    <label>Какое у Вас образование?</label>
                                    <select class="form-select" name="education">
                                        <option>Начальное</option>
                                        <option>Среднее</option>
                                        <option>Высшее</option>
                                    </select>
                                </div>
                                <div>
                                    <label>Ваши профессиии:</label>
                                    <div>
                                        <input type="checkbox" name="prof" value="programmer">
                                        <label>Программист</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" name="prof" value="ingeneer-researcher">
                                        <label>Инженер-исследователь</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" name="prof" value="meterolog">
                                        <label>Метеоролог</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" name="prof" value="pilot">
                                        <label>Пилот</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" name="prof" value="transform ingeneer">
                                        <label>Инженер по терраформированию</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" name="prof" value="doctor">
                                        <label>Доктор</label>
                                    </div>
                                </div>
                                <div>
                                    <label>Укажите пол: </label>
                                    <div>
                                        <input type="radio" name="sex" value="man" checked>
                                        <label>Мужской</label>
                                    </div>
                                    <div>
                                        <input type="radio" name="sex" value="woman">
                                        <label>Женский</label>
                                    </div>
                                </div>
                                <div>
                                    <label>Почему хоите принять участие в миссии?</label>
                                    <textarea rows="5" name="motivation"></textarea>
                                </div>
                                <div>
                                    <label>Приложите фотографию</label>
                                    <div>
                                        <input type="file" class="form-control" name="photo">
                                    </div>
                                </div>
                                <div>
                                    <input type="checkbox" name="stay" value="stay">
                                    <label>Готовы остаться на Марсе?</label>
                                </div>
                                <button class="btn btn-primary" type="submit">Отправить</button>
                            </form>
                        </div>
                    </body>
                </html>
        """
    elif request.method == "POST":
        print(request.form["surname"])
        d["surname"] = request.form["surname"]
        print(request.form["name"])
        d["name"] = request.form["name"]
        print(request.form["email"])
        print(request.form["education"])
        d["education"] = request.form["education"]
        arr = request.form.getlist("prof")
        print(*arr)
        d["profession"] = " ".join(arr)
        print(request.form["sex"])
        d["sex"] = request.form["sex"]
        print(request.form["motivation"])
        d["motivation"] = request.form["motivation"]
        print(request.form["photo"])
        if "stay" in request.form:
            d["ready"] = "True"
            print(request.form["stay"])
        else:
            d["ready"] = "False"
        # for el in request.form:
        #     print(el.split())
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")