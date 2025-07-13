# MongoDB con Docker

Este proyecto contiene la configuración necesaria para desplegar un servicio de MongoDB utilizando Docker y Docker Compose.

## Requisitos del Sistema

- Docker Engine 20.10+
- Docker Compose 2.0+
- Ubuntu 20.04 (servidor)
- Servidor MongoDB desplegado en: `192.168.3.100`

## Estructura del Proyecto

```
mongo-server/
├── docker-compose.yml
├── init/
│   └── init-user.js
└── data/ (generado automáticamente)
```

## Información del Servidor

- **Sistema Operativo**: Ubuntu 20.04
- **Dirección IP**: `192.168.3.100`
- **Puerto MongoDB**: `27017`
- **Tipo de Despliegue**: Docker Compose

## Configuración e Instalación

### 1. Preparación del Entorno (En el Servidor Ubuntu 20.04)

```bash
mkdir -p mongo-server/init
cd mongo-server
```

### 2. Despliegue del Servicio (En el Servidor Ubuntu 20.04)

Ejecutar el siguiente comando para iniciar MongoDB en modo detached:

```bash
docker-compose up -d
```

### 3. Verificación del Servicio (En el Servidor Ubuntu 20.04)

Comprobar que el contenedor esté ejecutándose:

```bash
docker-compose ps
```

## Conexión a la Base de Datos

### Base de Datos Principal (Administración)

- **Host**: `192.168.3.100`
- **Puerto**: `27017`
- **Base de datos**: `admin`
- **Usuario**: `admin`
- **Contraseña**: `clave123`

**String de Conexión:**

```
mongodb://admin:clave123@192.168.3.100:27017/admin
```

### Base de Datos de Pruebas

- **Host**: `192.168.3.100`
- **Puerto**: `27017`
- **Base de datos**: `dbprueba`
- **Usuario**: `facci`
- **Contraseña**: `facci123`
- **Auth Source**: `dbprueba`

**String de Conexión:**

```
mongodb://facci:facci123@192.168.3.100:27017/dbprueba?authSource=dbprueba
```

## Conexión desde Cliente con MongoDB Compass

### Instalación de MongoDB Compass (En el Cliente)

1. Descargar MongoDB Compass desde: https://www.mongodb.com/products/compass
2. Instalar en el equipo cliente (Windows/Mac/Linux)

### Configuración de Conexiones en Compass

#### Conexión 1: Base de Datos Principal (Admin)

- Usar la configuración mostrada en `image.png`
- **URI de Conexión**: `mongodb://admin:clave123@192.168.3.100:27017/admin`

#### Conexión 2: Base de Datos de Pruebas

- Usar la configuración mostrada en `image-1.png`
- **URI de Conexión**: `mongodb://facci:facci123@192.168.3.100:27017/dbprueba?authSource=dbprueba`

### Pasos para Conectar desde Compass

1. Abrir MongoDB Compass en el equipo cliente
2. Hacer clic en "New Connection"
3. Pegar la URI de conexión correspondiente
4. Hacer clic en "Connect"
5. Navegar por las bases de datos y colecciones

## Comandos Útiles

### Gestión del Servicio (Ejecutar en el Servidor Ubuntu 20.04)

```bash
# Iniciar el servicio
docker-compose up -d

# Detener el servicio
docker-compose down

```

### Acceso a MongoDB Shell (Ejecutar en el Servidor Ubuntu 20.04)

```bash
# Conectar al shell de MongoDB (base de datos admin)
docker exec -it <container_name> mongosh -u admin -p clave123 --authenticationDatabase admin

# Conectar a la base de datos de pruebas
docker exec -it <container_name> mongosh -u facci -p facci123 --authenticationDatabase dbprueba

# Conectar sin autenticación (si está habilitado)
docker exec -it <container_name> mongosh
```

### Conexión desde Aplicaciones Cliente

#### Desde Python (Ejecutar en el Cliente)

```python
import pymongo

client_admin = pymongo.MongoClient("mongodb://admin:clave123@192.168.3.100:27017/admin")

client_pruebas = pymongo.MongoClient("mongodb://facci:facci123@192.168.3.100:27017/dbprueba?authSource=dbprueba")
```

#### Desde Node.js (Ejecutar en el Cliente)

```javascript
const { MongoClient } = require('mongodb');

const clientAdmin = new MongoClient(
  'mongodb://admin:clave123@192.168.3.100:27017/admin'
);

const clientPruebas = new MongoClient(
  'mongodb://facci:facci123@192.168.3.100:27017/dbprueba?authSource=dbprueba'
);
```

### Personalización

Para modificar la configuración inicial, edite el archivo `init/init-user.js` antes del primer despliegue.


### Actualización (Ejecutar en el Servidor Ubuntu 20.04)

Para actualizar MongoDB, modificar la versión en `docker-compose.yml` y ejecutar:

```bash
docker-compose pull
docker-compose up -d
```

## Capturas de Pantalla

### Conexión Admin en MongoDB Compass

![Configuración de conexión para base de datos admin](pruebas/image.png)

### Conexión de Pruebas en MongoDB Compass

![Configuración de conexión para base de datos de pruebas](pruebas/image-1.png)

## Resumen de Ubicaciones

| Acción                      | Ubicación de Ejecución                  |
| --------------------------- | --------------------------------------- |
| Despliegue de MongoDB       | Servidor Ubuntu 20.04 (`192.168.3.100`) |
| Gestión de contenedores     | Servidor Ubuntu 20.04                   |
| MongoDB Shell               | Servidor Ubuntu 20.04                   |
| MongoDB Compass             | Equipo Cliente                          |
| Aplicaciones Python/Node.js | Equipo Cliente                          |
| Respaldos y mantenimiento   | Servidor Ubuntu 20.04                   |
