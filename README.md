"# microblog" 

python tests.py

https://habr.com/ru/articles/804245/

flask db init
flask db migrate -m "users table" - генерация миграций
flask db upgrade - применение миграций


flask shell - сразу проваливаемся в контекст
users = db.session.scalars(sa.select(User)).all()

u = User(username='susan', email='susan@example.com')
u.set_password('cat')
db.session.add(u)
db.session.commit()


aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:8025

export MAIL_SERVER=localhost
export MAIL_PORT=8025

====================
[extractors]
jinja2 = jinja2.ext:babel_extract
====================
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel init -i messages.pot -d app/translations -l ru

#При каждом изменении интерфеса
pybabel compile -d app/translations