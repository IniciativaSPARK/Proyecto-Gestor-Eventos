from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
import os
import traceback

app = FastAPI(
    title="Proyecto Gestión de Eventos API - SPARK",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Usar IP local por defecto para evitar resolución IPv6 errónea de localhost
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://spark_admin:spark_secure_password@127.0.0.1:5433/spark_eventos"
)

# Imprime en la consola de Uvicorn la URL que Python está intentando consumir
print("\n" + "="*50)
print(f"DEBUG INFRAESTRUCTURA - DATABASE_URL USADA:\n{DATABASE_URL}")
print("="*50 + "\n")

@app.get("/", tags=["Health Check"])
def read_root():
    db_status = "untested"
    try:
        engine = create_engine(DATABASE_URL, connect_args={"connect_timeout": 3})
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        # Imprime el stack trace real en la terminal de Python de forma segura
        print("\n[ERROR DE CONEXIÓN A BASE DE DATOS]:")
        traceback.print_exc()
        db_status = "disconnected"

    return {
        "status": "online",
        "database": db_status,
        "framework": "FastAPI"
    }