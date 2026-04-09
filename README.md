# FastAPI + Fuerza Bruta

## Cómo ejecutar la API

Primero abrimos la CMD y navegamos a la carpeta del proyecto:

```
cd C:\Users\Usuario\OneDrive\Escritorio\Garage_ideas\FastAPI
```

Luego levantamos el servidor con el siguiente comando:

```
python -m uvicorn main:app --reload
```

Abrimos el navegador en la siguiente URL para acceder a la documentación de FastAPI:

```
http://127.0.0.1:8000/docs
```

Ahí podremos aplicar los cambios según lo requieras. Por ejemplo:

- En el apartado **POST /login** se puede iniciar sesión con un usuario existente.
- En el apartado **PUT /users/{user_id}** se puede actualizar los datos de un usuario:
  - Usuario sin cambios: `{ "id": 1, "username": "admin", "password": "dog123", "email": "admin@mail.com", "is_active": true }`
  - Usuario cambiado: `{ "id": 1, "username": "admin", "password": "dog123", "email": "nuevo@gmail.com", "is_active": true }`

---

## Usuarios disponibles

| ID | Usuario | Contraseña |
|----|---------|------------|
| 1  | admin   | dog123     |
| 2  | user    | tiger456   |
| 3  | guest   | panther789 |

---

## Código de fuerza bruta

Con el servidor corriendo, abrimos **una segunda CMD** en la misma carpeta y ejecuta:

```
python fuerzabruta.py
```

El script intentará averiguar la contraseña del usuario objetivo probando todas las combinaciones posibles. Por ejemplo con `objetivo = "admin"`:

```
[1] Intento fallido: a
[2] Intento fallido: b
[3] Intento fallido: c
...
Usuario objetivo: admin
Contraseña encontrada: dog123
Total de intentos: ???
Tiempo total: ???s
```
