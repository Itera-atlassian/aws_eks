from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn

app = FastAPI()
app.title = "HelloWorld with FastAPI"
app.version = "1.0.0"

@app.get('/', tags=["home"])
def message():
    with open('template.html', 'r') as file:
        html_template = file.read()
    return HTMLResponse(content=html_template)

@app.get('/registro', tags=["home"])
def message():
    with open('template.html', 'r') as file:
        html_template = file.read()
    return "registro exitoso"

@app.get('/health', tags=["system"])
def verificar_salud():
    return JSONResponse(content={"status": "OK"})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)