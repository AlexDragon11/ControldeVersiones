import requests

# Reemplaza "TU_TOKEN_DE_ACCESO" con tu propio token de acceso personal
headers = {
    "Authorization": "Bearer TU_TOKEN_DE_ACCESO"
}

# URL para crear un repositorio en tu cuenta de GitHub
url = "https://api.github.com/user/repos"

# Datos para el nuevo repositorio
data = {
    "name": "nuevo-repositorio",
    "description": "Descripción del nuevo repositorio"
}

# Realiza la solicitud POST para crear el repositorio
response = requests.post(url, headers=headers, json=data)

# Verifica el código de respuesta
if response.status_code == 201:
    print("Repositorio creado exitosamente.")
else:
    print("Error al crear el repositorio:", response.text)
