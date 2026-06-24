from flask import Flask, render_template_string

app = Flask(__name__)

HTML = '''
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Página con Flask</title>
    <style>
      body{font-family: Arial, sans-serif; margin:2rem; background-color:black}
      header{border-bottom:1px solid #ddd; margin-bottom:1rem}
      p{color: white}
    </style>
  </head>
  <body>
    <header>
      <h1>Barbería</h1>
    </header>
    <main>
      <p>Bienvenido a la experiencia de tu vida.</p>
    </main>
  </body>
</html>
'''


@app.route('/')
def index():
    return render_template_string(HTML, path='/')


if __name__ == '__main__':
    # Ejecuta la app en modo debug en el puerto 5000
    app.run(debug=True)
