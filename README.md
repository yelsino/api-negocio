# api-negocio

    paso 1 
      - DESCARGAR de la rama master

    paso 2
      crear, instalar y activar entorno virtual
      ojo, no es necesario que la api este dentro del entorno
      pueden estar "entorno y api" juntos en un mismo directorio
      ejemplo TIENDAAPI   -   ENTORNOVIRTUAL
    paso 3 
      instalar las dependencias del proyecto
      en la raiz de la api en un CMD
        - pip freeze > requirements.txt
        - pip install -r requirements.txt
     paso 4 
      ejecutar proyecto
      en la raiz del proyecto se debe ver el archivo manage.py, si se       estan en la raiz
        
        crear usuario en python version 2
       - python manage.py createsuperuser
       ejecutar en python version 2
        -python manage.py runserver
        
        crear usuario en python version 3
       - python3 manage.py createsuperuser
       ejecutar en python version 3
        -python3 manage.py runserver
       
   
