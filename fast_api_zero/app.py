from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Olá Mundo!"}


@app.get("/html")
def html():
    return "<h1>Olá mundo</h1>"


@app.get("/usuarios")
def listar_usuarios():
    return [
        {"id": 1, "nome": "Itallo"},
        {"id": 2, "nome": "Maria"},
        {"id": 3, "nome": "João"}
    ]


@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    return {
        "id": usuario_id,
        "nome": f"Usuário {usuario_id}"
    }