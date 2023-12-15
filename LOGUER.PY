# Archivo: procesar_login.py
import cgi

# Obtiene los datos del formulario
form = cgi.FieldStorage()

# Obtiene el valor del campo de nombre de usuario y contraseña
username = form.getvalue('username')
password = form.getvalue('password')

# Verifica si las credenciales son correctas
if username == 'Contratacion1' and password == '123456':
    # Si son correctas, redirige a otro HTML
    print("Location: power_bi.html\n")  # Cambia "otro_html.html" al nombre de tu otro HTML
    print("Content-type: text/html\n")
    print()
else:
    # Si las credenciales son incorrectas, muestra un mensaje de error o redirige a otra página
    print("Content-type: text/html\n")
    print()
    print("<html><body><p>Credenciales incorrectas. Intenta de nuevo.</p></body></html>")

