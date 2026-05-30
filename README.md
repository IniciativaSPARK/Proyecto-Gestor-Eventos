
<div align="center">
  <img src="./public/spark-logo.png" alt="SPARK" width="140"/>

  <h1>Gestor Eventos</h1>

  <p><em>Visualiza y crea eventos para </em></p>
</div>

---

## 👋 Bienvenido al equipo

Primero, gracias por sumarte. Esto no es un tutorial ni un curso — es un proyecto **real**, que vamos a construir de principio a fin, y que va directo a tu portafolio profesional.

**Lo que importa no es que el producto salga perfecto. Lo que importa es que en unas semanas cada uno sea un mejor ingeniero del que empezó.**

---

# 🧠 ¿Qué estamos construyendo?

Una plataforma web dinámica para:

- Visualizar eventos en tiempo real
- Crear y configurar eventos
- Administrar aforos
- Gestionar horarios y detalles logísticos
- Eliminar o actualizar eventos
- Manejar contenido multimedia asociado a eventos
- Administrar permisos y operaciones seguras desde un panel administrativo

El sistema está diseñado bajo un enfoque de arquitectura moderna desacoplada:

- Frontend SSR optimizado para rendimiento y SEO
- Backend API REST de alto rendimiento
- Persistencia relacional robusta
- Infraestructura desplegada sobre AWS
- Contenerización completa mediante Docker

# 🛠 Stack Tecnológico

| Capa | Tecnología |
|---|---|
| Frontend | Angular v17+ con SSR |
| Backend | Python 3.10+ + FastAPI |
| Base de Datos | PostgreSQL |
| Almacenamiento Multimedia | AWS S3 (Si aplica) |
| Infraestructura | AWS EC2 |
| Proxy Inverso | Nginx |
| Contenerización | Docker + Docker Compose |
| ORM | SQLAlchemy |
| Gestión de Dependencias Frontend | pnpm |
| Control de Versiones | Git + GitHub |

---

## 🌿 Sobre este repositorio

Esta es la rama de **producción** (`main`). Todo lo que vive acá es el código que termina desplegado.

Vas a ser agregado como **colaborador** del repo en GitHub. Eso significa una cosa importante:

>  **No necesitas hacer fork.**
>  **Clonas el repo directamente y trabajas en tu propia rama.**

El fork solo aplica cuando alguien externo quiere contribuir. Como parte del equipo, trabajas directo sobre este repositorio.

---

## 🚀 Cómo empezar

### 1. Clona el repositorio

```bash
git clone https://github.com/IniciativaSPARK/Proyecto-Armario-Digital
cd Proyecto-Gestor-Eventos
```

### 2. Crea tu propia rama

**Nunca trabajes directo en `main`.** Crea una rama con tu nombre y lo que vas a hacer:

```bash
git checkout -b feature/[tu-nombre-funcionalidad]
```

Ejemplos:

```bash
git checkout -b feature/juan-auth
git checkout -b feature/maria-chat-engine
git checkout -b feature/carlos-dashboard
```

### 3. Trabaja, commitea y sube tu rama

# 🧾 Convención de Commits

Usaremos convención basada en Conventional Commits.

## Prefijos

| Prefijo   | Uso                                 |
| --------- | ----------------------------------- |
| feat:     | Nueva funcionalidad                 |
| fix:      | Corrección de errores               |
| refactor: | Refactor sin cambiar comportamiento |
| style:    | Cambios visuales o formato          |
| test:     | Pruebas                             |

Usa prefijos claros en tus commits:

```bash
git add .
git commit -m "feat: agregar login con JWT"
git push origin feature/tu-rama
```

### 4. Abre un Pull Request hacia `main`

Cuando termines una feature y quieras cargarlo al repositorio:

1. Abre un PR desde tu rama hacia `main`.
2. Describe qué hiciste y por qué.
3. Asigna al lider como reviewer.
4. Yo reviso, damos feedback, y hacemos merge juntos.

> ⚠️ **Todo PR se revisa antes del merge.**

---


## 💬 Comunicación

Cualquier **duda rápida, bloqueo o preguntas de implementación** puedes ir al grupo de WhatsApp del equipo

Por mínima que parezca la duda, escríbela en el WhatsApp. No tengas miedo de las "preguntas tontas", todos empezamos confundidos y es mejor preguntar que perder un día entero atorado.

---
# 💻 Levantar el proyecto en local

## Requisitos

Instalar previamente:

* Docker
* Docker Compose
* Node.js LTS
* Python 3.10+
* Git

# ⚙️ Configuración del Frontend

## 2. Instalar dependencias del frontend

```bash
cd apps/frontend
npm install
```

---

## 3. Ejecutar servidor Angular SSR en desarrollo

```bash
npm run dev
```

El frontend estará disponible en:

```text
http://localhost:4200
```

---

# ⚙️ Configuración del Backend

## 4. Entrar al backend

```bash
cd ../backend
```

---

## 5. Crear entorno virtual

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

---

## 6. Instalar dependencias Python

```bash
pip install -r requirements.txt
```

## 7. Iniciar servidor FastAPI

```bash
uvicorn app.main:app --reload
```

El backend estará disponible en:

```text
http://localhost:8000
```


---

# 🔒 Seguridad y Buenas Prácticas

## Nunca subir:

* `.env`
* credenciales AWS
* llaves privadas
* secretos JWT
* tokens
* certificados

---

## Siempre:

* usar variables de entorno
* validar inputs
* usar tipado
* revisar dependencias
* mantener commits claros
* documentar cambios importantes

---

<div align="center">
  <img src="./public/spark-logo.png" alt="SPARK" width="40"/>
  <br/>
  <sub>
    <strong>SPARK</strong> · Proyecto Gestión de Eventos
  </sub>
</div>
