import requests
from base64 import b64decode

# Reemplaza estos valores con el propietario del repositorio, el nombre del repositorio y la ruta del archivo
owner = "ciscored3507"
repo = "bd"
path = "path/to/your/file.bdf"

# Construye la URL para la API de GitHub
url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

# Realiza la solicitud GET a la API de GitHub
response = requests.get(url)
data = response.json()

# Decodifica el contenido del archivo
file_content = b64decode(data['content']).decode('utf-8')

# Imprime el contenido del archivo
print(file_content)
