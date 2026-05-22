from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"mensagem": "API funcionando"}


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