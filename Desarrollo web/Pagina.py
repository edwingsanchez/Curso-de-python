from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_page(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        error = "Nombre de usuario o contraseña incorrectos."

    return HttpResponse(
        f"""<!DOCTYPE html>
<html lang=\"es\">
<head>
    <meta charset=\"utf-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Iniciar sesión</title>
    <style>
        body {{ font-family: sans-serif; background: #f2f2f2; display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; }}
        .card {{ background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1); width: 100%; max-width: 360px; }}
        .card h1 {{ margin: 0 0 1rem; font-size: 1.5rem; }}
        .field {{ margin-bottom: 1rem; }}
        .field label {{ display: block; margin-bottom: 0.25rem; font-size: 0.9rem; }}
        .field input {{ width: 100%; padding: 0.75rem; border: 1px solid #ccc; border-radius: 5px; }}
        .button {{ width: 100%; padding: 0.9rem; border: none; border-radius: 6px; background: #1976d2; color: white; font-size: 1rem; cursor: pointer; }}
        .error {{ color: #c62828; margin-bottom: 1rem; }}
    </style>
</head>
<body>
    <div class=\"card\">
        <h1>Iniciar sesión</h1>
        {f'<div class="error">{error}</div>' if error else ''}
        <form method=\"post\">
            <div class=\"field\">
                <label for=\"username\">Usuario</label>
                <input id=\"username\" name=\"username\" type=\"text\" autocomplete=\"username\" required>
            </div>
            <div class=\"field\">
                <label for=\"password\">Contraseña</label>
                <input id=\"password\" name=\"password\" type=\"password\" autocomplete=\"current-password\" required>
            </div>
            <button class=\"button\" type=\"submit\">Entrar</button>
        </form>
    </div>
</body>
</html>"""
    )

urlpatterns = [
    path("login/", login_page, name="login"),
]
