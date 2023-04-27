# IberiaJobs
Best Searcher for IT jobs in Spain.

# Integrantes
Javier Santos Sanz: Testing

Joaquín Sierra Granados: Backend

Álvaro Ruiz Roldán: Frontend

# Requisitos
Es necesario crear un archivo en la carpeta src llamado secrets.json con el siguiente formato, (en la entrega del campus se da un secrets.json para probarlo):
```
{
    "Jooble": "Tu clave",
    "EmpleatePage": 0 
}
```

Como el webscrapping ya fue ejecutado en su momento está toda la información guardada en el sql 
"iberiajobs_trabajos.sql" y "iberiajobs_stats", asi que no hace falta ejecutar de nuevo los archivos .py de la carpeta Webscrapping.

Será necesario tener un driver de firefox en la carpeta donde ejecutes el código de dataCollector_Empleate.py, sino lo puedes descargar aquí
# Docker
Ejecuta el comando "docker-compose up" sobre la carpeta raiz del proyecto, si sale un error de que el puerto 3306 está yá tomado, deberá borrar todos los procesos asociados al puerto 3306. Una vez terminada la instalación del proyecto en docker, solo habrá que abrir el index.html desde su navegador predeterminado.

Para ejecutar el WebScrapping mediante docker es necesario primero ejecutar "docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" -v ruta/absoluta/a/carpeta/pdf_files:/home/seluser/Downloads selenium/standalone-firefox:latest", pero antest iene que descargar la imagen de selenium/standalone-firefox:latest.

Esto creará una virtualización de firefox en el puerto 4444, que es el que se usa en el código para ejecutar el webscrapping, para consultar su funcionamiento tendrá poner esta dirección en su buscador: "http://localhost:7900/?autoconnect=1&resize=scale&password=secret".

Ejecuta el archivo data_Collector.py para que se ejecute el webscrapping.

# Backend y testing
Si se quiere realizar el testing o utilizar archivos de backend a excepción de empleate, cambie el contenido de database_config.json a:
```
{   
    "user": "root",
    "password": "root",
    "host": "localhost",
    "database": "iberiajobs"
}
```
Para el testing será necesario tener instalado pytest, se tendrá que ejecutar desde la carpeta donde tengas los webdrivers con el comando:
```python -m pytest``` o ```pytest``` si estás en unix.

Para testear los js, seguir las intrucciones en la carpeta js en test.
# Motivación

Poder ofrecer un entorno intuitivo para llevar a cabo búsquedas de trabajo para ingenieros tanto de España como fuera de ella, de esta forma facilitando la búsqueda y el tiempo de búsqueda de este tipo de trabajo.

# Objetivos 

El objetivo principal es crear una aplicación en este caso de tipo web donde poder consultar ofertas de trabajo de la especialidad de ingeniería, tanto en España como en Estados Unidos y compararlas.

# Subobjetivos

* Poder filtrar la oferta de trabajo que tu quieras en función de unos requisitos.  

* Consultar información referente a la base de datos de ofertas más buscadas, últimas búsquedas…

# Casos de uso

* Buscar ofertas de trabajo.

* Generar análisis de la base de datos.

* Poder filtrar el tipo de trabajo.

# TAM
Al tener cuatro tipos de clientes será el TAM todo el mercado que existe relacionado con estos:
* **Empresas IT en España:** Existiendo 72.857 empresas tecnológicas en 2020.
* **Fondos de inversión:** Decir el número de inversores no lo consideramos tan relevante como la masa monetaria invertida en el sector, que en la actualidad se trata de 50.000 millones de euros.
* **Profesionales:** Existiendo en la actualidad un total de 1.372.400 profesionales en este ámbito.
* **Academias:** Existen 35 centros de bootcamp en España.

# SAM
Estimamos que nuestro negocio podrá hacer negocio con los siguientes clientes:
* **Empresas IT:** Creemos que podemos brindar servicio a un 1% de las empresas tecnológicas, siendo en total 729 empresas.
* **Fondos de inversión:** Podemos servir a fondos cuyo monton combinado sea de un 0,5% de la inversión, siendo 250 millones de euros. Variando cuánto van a pagar dependiendo del dinero del fondo.
* **Profesionales:** Creemos que podremos dar servicio al menos a un 5% de todos los profesionales, siendo en total 68620 profesionales.
* **Academias**: Creemos que al ser tan dependientes del auge de tecnologías, podemos esperar realizar negocios con al menos 10 centros con bootcamps.

# Perfil Cliente
Podemos separar principalmente 3 categorías de clientes:
* **Empresas IT:** La información aportada será muy util para saber en qué tecnologías formar a sus empleados y en las que realizar sus proyectos.
* **Fondos de inversión:** La información generada por nuestro negocio le dará ventaja estratégica a los fondos de inversión, permitiendo predecir las tendencias de mercado comparando las actuales de España con las pasadas de USA.
* **Academias:** Les interesará conocer las siguientes tecnologías en boga para poder realizar bootcamps y clases sobre estas.
* **Especialistas:** Conocer las tecnologías que se harán famosas en el mercado laboral para poder adaptarse a este con tiempo, debido a que son novatos o quieren realizar un cambio en el trabajo.

# Business model canvas

![BMI•Business-model-canvas](https://user-images.githubusercontent.com/114731007/221013450-e6e27978-a2be-43aa-b30c-f0324d43e78a.png)


# Customer Journey
![Captura](https://user-images.githubusercontent.com/55651737/220865874-6dd84004-c59c-4525-8078-d5dbde5c08d8.PNG)

# KPIs

Los KPI’s pueden ser de mediadas objetivas de la empresa muy específicas y de otras más generales así que vamos a separarlos en diferentes categorías para que se diferencien bien:
* Comentarios:
  * % de comentarios positivos
  * Número de comentarios en general.
* Posicionamiento en la web:
  * Número de visitas a nuestra página.
  * % de empresas tecnologicas españolas que visitan nuestra página.
* Jobs:
  * Número de Jobs de nuestra página.
  * Número de visitas de cada categoría de jobs.
* Redes Sociales:
  * Número de visitas en nuestras redes sociales.
* Venta de información:
  * Cuantía fija de los ingresos en la venta de datos.

# OKR
* Tener más comentarios positivos que negativos en el 80% de nuestros Jobs.
* Tener al menos 10.000 comentarios sumando todos los Jobs.

* Tener 200.000 visitas en nuestra página web en un año.
* Tener al menos 1.000 empresas españolas que visitan nuestra página.

* Añadir 100 jobs nuevos en el periodo de un año.
* Tener al menos 10.000 visitas en cada categoría de Job.
* Mantener nuestro posicionamiento de nuestra página web siendo esta la primera en la página de Google durante los próximos 5 años.
* Tener al menos 500.000 de visitas en nuestras redes sociales.
* Ganar 200.000 euros en la venta de datos en un año.

# CONTRATO MERCANTIL
Contrato mercantil de desarrollo de servicios.
Está dividido en varias secciones:
*	Objeto: Se desarrollará una web la cual tiene diferentes servicios como el de saber cuales son las tecnologías más influyentes en las empresas actuales, búsquedas de empresas tanto en España como en Estados Unidos y obtener información de diferentes empresas.
*	Plazo: Duración del contrato desde el 30/01/2023 hasta el 05/05/2023 donde se finalizará con la presentación del proyecto.
*	Precio: Costo de los 3 desarrolladores más el coste de utilizar las API’s, coste de comprar el dominio y el coste de la compra del servidor y su mantenimiento.  
*	Obligaciones del contratista: El contratista, que en este caso son los tres desarrolladores, tiene la obligación de desarrollar los servicios acordados en el contrato en el plazo establecido y conforme a las especificaciones y estándares de calidad acordados.
*	Obligaciones del contratante: El contratante debe pagar al contratista el precio acordado en el contrato, debe proporcionar al contratista toda la información necesaria para que este último pueda crear y desarrollar el servicio acordado de manera efectiva y debe cumplir con los plazos y fechas establecidos en el contrato. Las demás obligaciones viene recabadas en los demás puntos del contrato mercantil.
*	Propiedad intelectual: El titular de los derechos de propiedad intelectual sobre los servicios desarrollados es el contratante de este contrato mercantil.
*	Confidencialidad: Se establece en este contrato que tanto los contratistas como el contratante deberán mantener todos los datos y servicios de este proyecto en confidencialidad.
*	Garantías: El contratista se compromete a que los servicios desarrollados cumplirán con los estándares de calidad acordados en el contrato, a entregar los servicios en el plazo acordado y conforme a las especificaciones del contrato, garantiza que los servicios desarrollados no infringen los derechos de propiedad intelectual de terceros, se compromete a brindar soporte y mantenimiento a los servicios desarrollados durante un período determinado después de su entrega y garantiza que toda la información confidencial del contratante será manejada de manera segura y confidencial ya definida en el anterior punto.

Requisitos definidos del servicio a desarrollar:
-	Base de datos amplia para una búsqueda amplia de las empresas de la aplicación.
-	El servicio debe permitir a los usuarios realizar búsquedas avanzadas y filtrar los resultados por ubicación, tecnologías usadas, etc.
-	El servicio debe ser accesible desde la web.
-	La información proporcionada por el servicio debe ser precisa y actualizada constantemente.
-	Se deben usar una API’s y webscraping para conseguir la información de los empleos tanto de estados Unidos como de España.
-	El servicio debe tener una seguridad mínima como por ejemplo que no se puedan introducir scripts a través de la barra de búsqueda ni en el login.

# Arquitectura global del proyecto
![Diagrama de arquitectura del sistema drawio (1)](https://user-images.githubusercontent.com/55651737/225561055-626dc162-820d-4496-8241-b63c88dfb1d5.png)


# TECNOLOGÍAS A USAR
Presentaremos las tecnologías que vamos a usar en el proyecto y que hemos pensado que son las más adecuadas:
## Frontend:
-	HTML5
-	CSS3
-	JAVASCRIPT
## Backend:
-	SQL
-	JAVASCRIPT
-	PYTHON
## Base de datos:
-	MySQL
## Estructuras de datos:
-	JSON
-	PDF

# Mockup de GUI y user experience

![Main](https://user-images.githubusercontent.com/55651737/225570447-336ead9d-9cd1-4b21-9ae5-15e0dd44f45c.png)

La página web presenta un diseño minimalista e intuitivo de fácil uso, la unica interacción del usuario es con el cuadro de busqueda. La información referente a las comparativas de trabajos se muestran haciendo "scroll" en la página.

