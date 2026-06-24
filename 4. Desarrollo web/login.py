from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "change_this_secret"

LOGIN_PAGE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Login</title>
    <style>
      body { font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 0; }
      .container { max-width: 400px; margin: 80px auto; padding: 20px; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
      .field { margin-bottom: 15px; }
      label { display: block; margin-bottom: 5px; }
      input[type=text], input[type=password] { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; }
      button { width: 100%; padding: 10px; background: #007bff; border: none; color: white; border-radius: 4px; cursor: pointer; }
      button:hover { background: #0056b3; }
      .error { color: red; margin-bottom: 15px; }
    </style>
  </head>
  <body>
    <div class="container">
      <h2>Iniciar sesión</h2>
      {% if error %}
      <div class="error">{{ error }}</div>
      {% endif %}
      <form method="post">
        <div class="field">
          <label for="username">Usuario</label>
          <input type="text" id="username" name="username" required>
        </div>
        <div class="field">
          <label for="password">Contraseña</label>
          <input type="password" id="password" name="password" required>
        </div>
        <button type="submit">Entrar</button>
      </form>
    </div>
  </body>
</html>
"""

HOME_PAGE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bienvenido</title>
    <style>
      body { font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 0; }
      .container { max-width: 500px; margin: 80px auto; padding: 20px; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
      a { color: #007bff; text-decoration: none; }
      a:hover { text-decoration: underline; }
    </style>
  </head>
  <body>
    <div class="container">
      <h2>Bienvenido, {{ username }}</h2>
      <p>Has iniciado sesión correctamente.</p>
      <p><a href="{{ url_for('logout') }}">Cerrar sesión</a></p>
    </div>
  </body>
</html>
"""

VALID_USERS = {
    "admin": "1234",
    "usuario": "clave"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if session.get("user"):
        return redirect(url_for("home"))

    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if VALID_USERS.get(username) == password:
            session["user"] = username
            return redirect(url_for("home"))

        error = "Usuario o contraseña incorrectos"

    return render_template_string(LOGIN_PAGE, error=error)

@app.route("/home")
def home():
    username = session.get("user")
    if not username:
        return redirect(url_for("login"))
    return render_template_string(HOME_PAGE, username=username)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
