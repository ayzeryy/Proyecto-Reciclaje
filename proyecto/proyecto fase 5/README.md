---

## 🔧 Requisitos

- Python 3.10 o superior
- MySQL Server
- Base de datos creada: `reciclaje_db`
- Paquetes necesarios:
  ```bash
  pip install mysql-connector-python pandas
  ```

---


```
proyecto/
├── main.py
├── db_conexion.py
├── usuarios.py
├── residuos.py
├── puntos.py
├── historial.py
└── datos/
    └── residuos.csv
```

---


### 1. Registro e inicio de sesión de usuarios
- Los usuarios pueden registrarse con correo y contraseña.
- Se almacena la fecha de registro.
- Se verifica si el usuario es administrador (`es_admin`).

### 2. Clasificación de residuos
- Permite buscar un residuo por nombre.
- Se muestra en qué tipo de bote debe depositarse.

### 3. Registro manual de residuos (admin)
- El administrador puede registrar residuos individualmente:
  ```python
  from residuos import agregar_residuo
  agregar_residuo()
  ```

### 4. Carga masiva de residuos desde CSV (admin)
- Permite cargar múltiples residuos a la vez desde un archivo `.csv`:
  ```python
  from residuos import cargar_residuos_csv
  cargar_residuos_csv("datos/residuos.csv")
  ```
- Verifica automáticamente si el residuo ya existe (por nombre) antes de insertarlo.
- Imprime advertencias si algún residuo se omite por duplicado.

#### ✅ Formato requerido del CSV:
```csv
nombre,descripcion,id_bote
papel,Papel reciclable,1
plastico,Envase PET,2
```

### 5. Sistema de puntos
- Cada vez que un usuario utiliza la app, se le otorgan puntos.
- Los puntos se guardan en la tabla `puntos` junto con la fecha.
- Los puntos se acumulan por mes y expiran automáticamente después de 30 días.

### 6. Historial de búsqueda
- Se registra cada búsqueda de residuos por usuario.
- Guarda la fecha, el residuo buscado y el ID del usuario.

### 7. Estadísticas y gráficos (pendiente de activar)
- El sistema podrá generar gráficas de barras por tipo de bote y gráficas de pastel por proporción de residuos usando `pandas`, `numpy` y `matplotlib`.

---

## 🛠️ Base de datos

La base de datos `reciclaje_db` contiene las siguientes tablas:

- `usuarios`: información de acceso, fecha de registro y tipo de usuario.
- `residuos`: nombre, descripción y relación con un `bote`.
- `botes`: tipos de contenedor y su color.
- `puntos`: historial de puntos por usuario y fecha.
- `historial_busqueda`: registro de búsquedas de residuos por usuario.

---

## ▶️ Ejecución

Inicia el programa principal desde terminal:

```bash
python main.py
```

---

## 📌 Notas

- Todos los residuos se almacenan en minúsculas para evitar duplicados por mayúsculas/minúsculas.
- Solo usuarios con `es_admin = TRUE` pueden cargar archivos CSV o agregar residuos manualmente.
- El sistema está preparado para escalar con futuras integraciones (API, interfaz web, etc.).

---
