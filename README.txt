//Comandos python

pip install -r requirements.txt instalar todas las dependendencias del proyecto


//Comandos Django

arrancar: python manage.py runserver
crear apps:  python manage.py startapp "profiles" "apps/profiles"         como se llamara y el directorio donde quedara
Migraciones:

python manage.py makemigrations "profiles"         eso es para crear migraciones, lo puedes hacer para toda la aplicacion o por modulo
python manage.py migrate       para aplicar la migracion 



//Comandos Git



//Comandos entorno virtual

crear: python -m venv .envs
activar: .\.envs\Scripts\activate
desactivar: deactivate