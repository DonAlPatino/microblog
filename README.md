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

docker run --name elasticsearch -d --rm -p 9200:9200 --memory="2GB" -e discovery.type=single-node -e xpack.security.enabled=false  -t elasticsearch:8.11.1

get list indexes
curl http://localhost:9200/_aliases

app.elasticsearch.indices.delete(index='posts')

=============================
вы должны сгенерировать свой собственный секретный ключ (SECRET_KEY). Вы можете использовать следующую команду:
python3 -c "import uuid; print(uuid.uuid4().hex)"
====================================
windows:
waitress-serve --listen=localhost:8000 microblog:app

docker run --name mysql -d --rm -p 3306:3306 --env="MYSQL_ROOT_PASSWORD=password" -t mysql:8.4.1 
docker exec -it mysql bash
mysql -u root -p

mysql> create database microblog character set utf8 collate utf8_bin;
#   mysql> create user 'microblog'@'localhost' identified by 'dbpassword';
mysql> create user 'microblog'@'%' identified by 'dbpassword';
mysql> grant all privileges on microblog.* to 'microblog'@'localhost';
mysql> flush privileges;
mysql> quit;

========================
(venv) $ git pull                              # download the new version
(venv) $ sudo supervisorctl stop microblog     # stop the current server
(venv) $ flask db upgrade                      # upgrade the database
(venv) $ flask translate compile               # upgrade the translations
(venv) $ sudo supervisorctl start microblog    # start a new server
========================

docker build -t microblog:latest .
docker images
docker run --name microblog -d -p 8000:5000 --rm microblog:latest
docker stop microblog