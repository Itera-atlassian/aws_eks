from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn
import logging
import time

# Configura el sistema de registro
console_formatter = uvicorn.logging.ColourizedFormatter(
    "{asctime} {levelprefix}  {message}",
    style="{",
    use_colors=True
)
logger = logging.getLogger("uvicorn.ALL")
handler = logging.StreamHandler()  # Utiliza StreamHandler para enviar los registros a la consola
handler.setFormatter(console_formatter)
logger.addHandler(handler)
logger.propagate = False


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


@app.get("/sumatoria/{number}")
async def calculate_factorial(number: int):
    start_time = time.time()
    logger.info("---------- Iniciando transacción: sumatoria ----------")
    logger.info(f"/sumatoria/{number}")
    
    if number < 0:
        return {"error": "El número debe ser no negativo"}
    elif number == 0:
        return {"factorial": 1}
    else:
        
        result = 1
        for i in range(1, number + 1):
            result += i
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Response: {result}, Time: {execution_time:.3f}s")
        logger.info("---------- Finalizando transacción: sumatoria ----------")
        return {"sumatoria": result, "time": execution_time}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, access_log=False)