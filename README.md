# api-two-calidad

Este microservicio es el encargado de realizar la busqueda del encryptedToken para un internalId dado.

### Autor

[Andres Camilo Silva Morales](https://github.com/acsm2411)

### Prerrequisitos

1. Contar con [Python 3](https://www.python.org/downloads/) instalado en la computadora donde se ejecutara la API.
2. Descargar las dependencias del proyecto utilizando el siguiente comando (estando ubicado en la carpeta del proyecto):

```bash
pip3 install -r requirements.txt
```

3. [Postman](https://www.postman.com/downloads/) en caso de que se quieran realizar pruebas utilizando este software (opcional).

### ¿Como ejecutar la app local?

Ejecutar el siguiente comando:

```bash
uvicorn main:app --reload --port=<puerto>
```

Donde `<puerto>` debe ser reemplazado por un numero de puerto (Debe ser diferente para cada API para evitar colisiones).

### ¿Como probar la app localmente?

Tenemos dos posibilidades para realizar pruebas con nuestra app:

1. Utilizando Swagger

Para esto, simplemente debemos acceder a la ruta /docs de nuestra API en ejecucion y se nos mostrara la pagina de swagger con todos los endpoints listos para probar.

![image](https://user-images.githubusercontent.com/30994170/185979083-05e094c0-be74-499f-80fd-bde84adb4724.png)

2. Accediendo a los endpoints directamente

Podemos acceder directamente al endpoint correspondiende de nuestra API y escribir valores en la URL para hacer nuestras pruebas.

![image](https://user-images.githubusercontent.com/30994170/185979356-d55299eb-8c8d-411a-8b95-ebc8f6bc7ab3.png)

3. Con Postman

Para esto, debemos agregar la request con la ruta de nuestra API y enviarle el valor de path necesario:

![image](https://user-images.githubusercontent.com/30994170/185979567-ff679f51-bdcf-4985-befc-0ea5470a57aa.png)

Algunos valores de prueba:

* 51332
* 35319
* 60105
* 4130
* 51908

### ¿Como abrir la app cuando está en ejecución?

Para abrir la app luego de su ejecución, accedemos a la siguiente ruta en el navegador de preferencia:

`http://localhost:<puerto>`

Donde `<puerto>` debe ser reemplazado por el numero de puerto escogido durante el comando de ejecución o 8000 por defecto.
