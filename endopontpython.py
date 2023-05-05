import requests

# Endpoint a verificar
url = "https://www.ejemplo.com/endpoint"

# Realizar una solicitud GET al endpoint
response = requests.get(url)

# Verificarificacion simple
if response.status_code == 200:
    print("El endpoint está activo.")
else:
    print("El endpoint no está activo.")

# JORGE LUIS MUÑIZ REPOMA