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

## Instalación de Docker en el Servidor Ubuntu 20.04

### 1. Actualizar el Sistema

```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Instalar Dependencias

```bash
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release -y
```

### 3. Agregar la Clave GPG de Docker

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

### 4. Agregar el Repositorio de Docker

```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### 5. Instalar Docker Engine

```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y
```

### 6. Instalar Docker Compose

```bash
# Descargar Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Dar permisos de ejecución
sudo chmod +x /usr/local/bin/docker-compose

# Crear enlace simbólico (opcional)
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

### 7. Configurar Docker para Usuario No Root (Opcional)

```bash
# Agregar usuario al grupo docker
sudo usermod -aG docker $USER

# Aplicar cambios (cerrar sesión y volver a iniciar)
newgrp docker
```

### 8. Verificar la Instalación

```bash
# Verificar Docker
docker --version
docker run hello-world

# Verificar Docker Compose
docker-compose --version
```

### 9. Habilitar Docker al Inicio del Sistema

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

## Configuración e Instalación del Proyecto MongoDB

### 1. Preparación del Entorno (En el Servidor Ubuntu 20.04)

```bash
mkdir -p mongo-server/init
cd mongo-server
```

### 2. Crear el archivo docker-compose.yml

Crear el archivo `docker-compose.yml` con el siguiente contenido:

```yaml
version: '3.3'

services:
  mongodb:
    image: mongo:4.4
    container_name: mongodb44
    restart: always
    ports:
      - '192.168.3.100:27017:27017'
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: clave123
    volumes:
      - ./data:/data/db
      - ./init:/docker-entrypoint-initdb.d
```

### 3. Crear el archivo de inicialización

Crear el archivo `init/init-user.js` con el script de inicialización de usuarios y bases de datos.

### 4. Despliegue del Servicio (En el Servidor Ubuntu 20.04)

Ejecutar el siguiente comando para iniciar MongoDB en modo detached:

```bash
docker-compose up -d
```

### 5. Verificación del Servicio (En el Servidor Ubuntu 20.04)

Comprobar que el contenedor esté ejecutándose:

```bash
docker-compose ps
```

## Explicación de la Configuración Docker Compose

### Parámetros del archivo docker-compose.yml

- **version: '3.3'**: Versión del formato de Docker Compose
- **image: mongo:4.4**: Imagen oficial de MongoDB versión 4.4
- **container_name: mongodb44**: Nombre del contenedor para fácil identificación
- **restart: always**: Reiniciar automáticamente el contenedor si se detiene
- **ports**: Mapeo de puertos desde la IP específica del servidor
  - `"192.168.3.100:27017:27017"`: Expone MongoDB solo en la IP del servidor
- **environment**: Variables de entorno para configuración inicial
  - `MONGO_INITDB_ROOT_USERNAME`: Usuario administrador root
  - `MONGO_INITDB_ROOT_PASSWORD`: Contraseña del administrador root
- **volumes**: Montaje de directorios
  - `./data:/data/db`: Persistencia de datos de MongoDB
  - `./init:/docker-entrypoint-initdb.d`: Scripts de inicialización

### Comandos de Gestión Adicionales

```bash
# Ver logs del contenedor en tiempo real
docker-compose logs -f mongodb

# Entrar al contenedor
docker exec -it mongodb44 bash

# Verificar estado del contenedor
docker ps

# Detener y eliminar contenedores y volúmenes
docker-compose down -v
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
docker exec -it mongodb44 mongosh -u admin -p clave123 --authenticationDatabase admin

# Conectar a la base de datos de pruebas
docker exec -it mongodb44 mongosh -u facci -p facci123 --authenticationDatabase dbprueba

# Conectar sin autenticación (si está habilitado)
docker exec -it mongodb44 mongosh
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


## Capturas de Pantalla

### Conexión facci en MongoDB Compass

![Configuración de conexión para base de datos admin](pruebas/image.png)

### Conexión de Pruebas en MongoDB Compass

![Configuración de conexión para base de datos de pruebas](pruebas/image-1.png)

## Resumen de Ubicaciones

| Acción                      | Ubicación de Ejecución                  |
| --------------------------- | --------------------------------------- |
| Instalación de Docker       | Servidor Ubuntu 20.04 (`192.168.3.100`) |
| Despliegue de MongoDB       | Servidor Ubuntu 20.04 (`192.168.3.100`) |
| Gestión de contenedores     | Servidor Ubuntu 20.04                   |
| MongoDB Shell               | Servidor Ubuntu 20.04                   |
| MongoDB Compass             | Equipo Cliente                          |
| Aplicaciones Python/Node.js | Equipo Cliente                          |
