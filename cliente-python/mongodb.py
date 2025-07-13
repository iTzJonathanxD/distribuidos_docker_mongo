from pymongo import MongoClient

usuario = "facci"
clave = "facci123"
host = "192.168.3.100"
puerto = 27017
basedatos = "dbprueba"
coleccion = "clientes"

uri = f"mongodb://{usuario}:{clave}@{host}:{puerto}/{basedatos}?authSource={basedatos}"

try:
    cliente = MongoClient(uri)
    db = cliente[basedatos]
    colec = db[coleccion]

    print("=== Inserción de cliente ===")
    nombres = input("Nombres del cliente: ")
    direccion = input("Dirección: ")
    email = input("Email: ")
    saldo = float(input("Saldo: "))

    cliente_doc = {
        "nombres": nombres,
        "direccion": direccion,
        "email": email,
        "saldo": saldo
    }

    resultado = colec.insert_one(cliente_doc)
    print("✅ Cliente insertado con ID:", resultado.inserted_id)

except Exception as e:
    print("Error:", str(e))
