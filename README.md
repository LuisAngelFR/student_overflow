# Student Overflow

Este es un proyecto de ejemplo utilizando Flask y SQLAlchemy para crear una aplicación de preguntas y respuestas desarrollada como proyecto escolar.

## Requisitos

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Instalación

1. Clona el repositorio:
  ```bash
  git clone https://github.com/LuisAngelFR/student_overflow.git
  cd student_overflow
  ```

2. Crea un entorno virtual y actívalo:
  ```bash
  python -m virtualenv venv
  source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
  ```

3. Instala las dependencias:
  ```bash
  pip install -r requirements.txt
  ```

## Uso

1. Inicia la aplicación:
  ```bash
  python app.py
  ```

2. Abre tu navegador y ve a `http://127.0.0.1:5000/` o `http://localhost:5000/` para ver la aplicación en funcionamiento.

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación.
- `templates/`: Carpeta que contiene las plantillas HTML.
  - `index.html`: Página principal que muestra todas las preguntas.
  - `question.html`: Página que muestra una pregunta y sus respuestas.
  - `ask_question.html`: Página para hacer una nueva pregunta.

## Descripción del Código

- `Question`: Modelo que representa una pregunta.
- `Answer`: Modelo que representa una respuesta.
- Rutas:
  - `/`: Muestra todas las preguntas.
  - `/question/<int:id>`: Muestra una pregunta específica y sus respuestas.
  - `/ask`: Permite hacer una nueva pregunta.
