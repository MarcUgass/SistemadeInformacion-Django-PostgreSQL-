# Frameworkweb-django
The `docker` command shall work as follows:

~~~{.diff}
$ docker run --hostname=e2e61a34c373 --env=POSTGRES_PASSWORD=1234 --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/16/bin --env=GOSU_VERSION=1.16 --env=LANG=en_US.utf8 --env=PG_MAJOR=16 --env=PG_VERSION=16.0-1.pgdg120+1 --env=PGDATA=/var/lib/postgresql/data --volume=/var/lib/postgresql/data -p 5432:5432 --runtime=runc -d postgres:latest

~~~
The `python debug` command shall work as follows:
~~~{.diff}
$ python manage.py runserver
~~~

Acceder a la aplicación web:
Genereación Base de Datos:
~~~{.diff}
127.0.0.1:8000/genBD
~~~
Registro:
~~~{.diff}
127.0.0.1:8000/registro
~~~
Administrador:
~~~{.diff}
127.0.0.1:8000/administrador
~~~
