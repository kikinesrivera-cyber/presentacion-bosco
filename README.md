# Presentación interactiva: *El jardín de las delicias* (El Bosco)

Proyecto en **Python + Streamlit** para una exposición escolar/universitaria de ~10 minutos, diseñado para 6 integrantes.

## 1) Requisitos

- Windows 10/11 (también funciona en Linux/macOS)
- Python 3.10 o superior
- VS Code

## 2) Estructura esperada

```bash
presentacion-bosco/
├─ app.py
├─ styles.css
├─ requirements.txt
├─ README.md
└─ assets/
   ├─ triptico_completo.jpg
   ├─ triptico_cerrado.jpg
   ├─ panel_izquierdo.jpg
   ├─ panel_central.jpg
   └─ panel_derecho.jpg
```

> Si faltan imágenes, la app **no se rompe**: muestra placeholders elegantes indicando qué archivo falta.

## 3) Instalación (Windows en VS Code)

Abre la carpeta del proyecto en VS Code y en la terminal ejecuta:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## 4) Ejecución

Con el entorno activo:

```powershell
streamlit run app.py
```

Luego abre la URL local que muestre la terminal (normalmente `http://localhost:8501`).

## 5) Dónde colocar imágenes

Pon los archivos dentro de la carpeta `assets/` con estos nombres exactos:

- `assets/triptico_completo.jpg`
- `assets/triptico_cerrado.jpg`
- `assets/panel_izquierdo.jpg`
- `assets/panel_central.jpg`
- `assets/panel_derecho.jpg`

## 6) Contenido incluido en la app

- 12 secciones con navegación **Anterior / Siguiente** y sidebar con índice.
- Estilo oscuro elegante (negro, sepia, dorado oscuro, rojo profundo).
- Lectura narrativa completa del tríptico.
- Guion final para 6 expositores (frases listas para decir).
- Sección colapsable de datos curiosos.
- Mini quiz interactivo de 3 preguntas.
- Créditos de imágenes y fuentes al final.

## 7) Personalización rápida

- Edita textos en `app.py`.
- Ajusta colores/estética en `styles.css`.
- Cambia imágenes reemplazando archivos en `assets/`.

## 8) Solución de problemas comunes

- **No abre Streamlit**: verifica que activaste `.venv` y ejecutaste `pip install -r requirements.txt`.
- **Faltan imágenes**: revisa nombres exactos y extensión `.jpg`.
- **Puerto ocupado**: prueba `streamlit run app.py --server.port 8502`.
