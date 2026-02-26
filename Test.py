
import http.server

PORT = 8888
server_address = ("", PORT)
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
print("Serveur actif sur le port :", PORT)

httpd = server(server_address, handler)
httpd.serve_forever()

from pathlib import Path

# Définit le dossier racine (ex: un niveau au-dessus du dossier 'scripts')
# Si le script est déjà à la racine, utilisez : root = Path(__file__).parent
root = Path(__file__).parent.parent 
filepath = root / "mon_fichier.txt"

# Enregistrement
with open(filepath, "w") as f:
    f.write(form = cgi.FieldStorage()
    print("Content-type: text/html; charset=utf-8\n")
    print(form.getvalue("name"))

    html = """<!DOCTYPE html>
    <head>  
    <body>
    <form action="/index.py" method="post">
    <input type="text" name="name" value="Votre nom" />
    <input type="submit" name="send" value="Envoyer information au serveur">
    </form>
    </body>
    </html>
    """
    ):

    print(html)