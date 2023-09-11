
# Blog IA Pythoneers | Trabajo Final Etapa 2 Informatorio

 
## Setup:

**Clonar el repositorio**  

En una carpeta de su preferencia, mediante cmd u otra consola, clone el repositorio con el siguiente comando:

```
git clone #httpdelrepositorio
```  

**Para instalar el proyecto**  

Cree un entorno virtual y activelo:
```
crear entorno:  py -m venv venv   o   python -m venv venv
activar:        venv\Scripts\activate
```
**instalar las dependencias***
```
pip install -r requirements.txt 
```
**Crear la base de datos**

Como utilizamos MySql para la bd, hacer un archivo en la carpeta Settings llamado "local.py" y agregar lo que especificado en el archivo "base.py" respecto de la base de datos
-> líneas 76 a 92.

**Realizar las migraciones**
```
python manage.py makemigrations
python manage.py migrate
```
**Ejecutar el proyecto**
```
python manage.py runserver
```


```


