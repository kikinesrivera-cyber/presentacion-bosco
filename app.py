from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="El jardín de las delicias | Exposición interactiva",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
STYLES_PATH = BASE_DIR / "styles.css"

IMAGES = {
    "triptico_completo": ASSETS_DIR / "triptico_completo.jpg",
    "triptico_cerrado": ASSETS_DIR / "triptico_cerrado.jpg",
    "panel_izquierdo": ASSETS_DIR / "panel_izquierdo.jpg",
    "panel_central": ASSETS_DIR / "panel_central.jpg",
    "panel_derecho": ASSETS_DIR / "panel_derecho.jpg",
}

SECTIONS = [
    "1) Portada cinematográfica",
    "2) ¿Quién fue El Bosco?",
    "3) ¿Qué es un tríptico?",
    "4) Lectura general de la obra",
    "5) Panel cerrado",
    "6) Panel izquierdo: el paraíso",
    "7) Panel central: el jardín de las delicias",
    "8) Panel derecho: el infierno",
    "9) ¿Qué significa la obra?",
    "10) ¿Qué transmite hoy?",
    "11) Reparto para 6 expositores",
    "12) Cierre memorable + quiz + créditos",
]


def load_css() -> None:
    if STYLES_PATH.exists():
        st.markdown(f"<style>{STYLES_PATH.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def image_or_placeholder(image_path: Path, caption: str = "") -> None:
    if image_path.exists():
        st.image(str(image_path), caption=caption, use_container_width=True)
    else:
        st.markdown(
            f"""
            <div class='missing-image-card'>
                <h4>🖼️ Imagen no encontrada</h4>
                <p>Falta el archivo: <code>{image_path.as_posix()}</code></p>
                <p>Colócalo dentro de <code>assets/</code> para activar esta vista.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def visual_header(kicker: str, title: str, subtitle: str = "") -> None:
    st.markdown(
        f"""
        <div class='hero-card'>
            <p class='kicker'>{kicker}</p>
            <h1>{title}</h1>
            <p class='hero-subtitle'>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def quote(text: str) -> None:
    st.markdown(f"<div class='quote-box'>“{text}”</div>", unsafe_allow_html=True)


def bullet_strip(items: list[str]) -> None:
    html = "".join([f"<span class='chip'>{item}</span>" for item in items])
    st.markdown(f"<div class='chip-row'>{html}</div>", unsafe_allow_html=True)


def nav_controls() -> None:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c1:
        if st.button("⬅️ Anterior", use_container_width=True):
            st.session_state.section_idx = max(0, st.session_state.section_idx - 1)
            st.rerun()
    with c3:
        if st.button("Siguiente ➡️", use_container_width=True):
            st.session_state.section_idx = min(len(SECTIONS) - 1, st.session_state.section_idx + 1)
            st.rerun()
    with c2:
        st.markdown(
            f"<div class='progress-chip'>Sección {st.session_state.section_idx + 1} de {len(SECTIONS)}</div>",
            unsafe_allow_html=True,
        )
        progress_pct = int(((st.session_state.section_idx + 1) / len(SECTIONS)) * 100)
        st.markdown(
            f"""
            <div class='progress-rail'>
                <div class='progress-fill' style='width:{progress_pct}%;'></div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def sidebar_index() -> None:
    st.sidebar.title("📚 Índice")
    selected = st.sidebar.radio("Navega por la exposición", SECTIONS, index=st.session_state.section_idx)
    new_idx = SECTIONS.index(selected)
    if new_idx != st.session_state.section_idx:
        st.session_state.section_idx = new_idx
        st.rerun()

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Modo exposición**")
    st.sidebar.caption("Usa el índice o Anterior/Siguiente para mantener ritmo visual.")


def cover_section() -> None:
    visual_header(
        "Presentación interactiva",
        "El jardín de las delicias: del paraíso al caos",
        "Una lectura visual y simbólica del tríptico de El Bosco",
    )
    image_or_placeholder(IMAGES["triptico_completo"], "Tríptico completo")
    quote("No es solo una pintura: es una advertencia pintada como un sueño.")


def who_is_bosch_section() -> None:
    visual_header("Contexto clave", "¿Quién fue El Bosco?", "Breve, claro y listo para explicar")
    bullet_strip(["Finales siglo XV", "Pintor neerlandés", "Símbolos + religión + fantasía"])

    c1, c2, c3 = st.columns(3)
    c1.markdown("<div class='info-card'><h4>👤 Quién fue</h4><p>Hieronymus Bosch (c.1450–1516), artista de imaginación inquietante.</p></div>", unsafe_allow_html=True)
    c2.markdown("<div class='info-card'><h4>🕰️ Época</h4><p>Europa religiosa, cambios sociales y temor al pecado.</p></div>", unsafe_allow_html=True)
    c3.markdown("<div class='info-card'><h4>⚡ Impacto</h4><p>Combina belleza y miedo para hacer pensar al espectador.</p></div>", unsafe_allow_html=True)

    st.markdown("<div class='special-card'><h4>Lo que hace único a El Bosco</h4><p>Transforma una obra religiosa en un espejo del comportamiento humano.</p></div>", unsafe_allow_html=True)


def triptych_section() -> None:
    visual_header("Idea visual", "¿Qué es un tríptico?", "Tres paneles que cuentan una historia")

    st.markdown(
        """
        <div class='triptych-diagram'>
            <div><h4>Izquierda</h4><p>Inicio</p></div>
            <div><h4>Centro</h4><p>Núcleo</p></div>
            <div><h4>Derecha</h4><p>Desenlace</p></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='special-card'><p><strong>Además:</strong> cerrado también narra una escena. En esta obra funciona como prólogo.</p></div>", unsafe_allow_html=True)


def general_reading_section() -> None:
    visual_header("Mapa narrativo", "Lectura general de la obra", "Recorrido rápido para explicarlo en clase")

    col_img, col_text = st.columns([2.1, 1])
    with col_img:
        image_or_placeholder(IMAGES["triptico_completo"], "Lectura completa")
    with col_text:
        st.markdown(
            """
            <div class='info-card compact'>
                <h4>Ruta de lectura</h4>
                <p>🌍 Cerrado = creación</p>
                <p>🌿 Izquierda = paraíso</p>
                <p>🍓 Centro = placer/exceso</p>
                <p>🔥 Derecha = castigo/infierno</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def closed_panel_section() -> None:
    visual_header("Panel 1", "Panel cerrado", "El prólogo en gris antes del estallido interior")

    col_img, col_text = st.columns([2.2, 1])
    with col_img:
        image_or_placeholder(IMAGES["triptico_cerrado"], "Tríptico cerrado")
    with col_text:
        st.markdown("<div class='info-card compact'><h4>Qué transmite</h4><p>Silencio, espera y comienzo de la historia.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='info-card compact'><h4>Por qué importa</h4><p>Prepara el contraste con el color y el caos interior.</p></div>", unsafe_allow_html=True)


def left_panel_section() -> None:
    visual_header("Panel 2", "Panel izquierdo: el paraíso", "Calma inicial con señales extrañas")

    col_img, col_text = st.columns([2.2, 1])
    with col_img:
        image_or_placeholder(IMAGES["panel_izquierdo"], "Panel izquierdo")
    with col_text:
        st.markdown("<div class='info-card compact'><h4>Qué vemos</h4><p>Dios, Adán, Eva y naturaleza armónica.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='info-card compact'><h4>Qué sugiere</h4><p>Orden, inocencia y tensión incipiente.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='tag'>calma extraña</div>", unsafe_allow_html=True)


def center_panel_section() -> None:
    visual_header("Panel 3 (principal)", "Panel central: el jardín de las delicias", "La parte más intensa y memorable")

    col_img, col_text = st.columns([2.4, 1])
    with col_img:
        image_or_placeholder(IMAGES["panel_central"], "Panel central")
    with col_text:
        st.markdown("<div class='info-card compact'><h4>Placer</h4><p>Atractivo visual inmediato.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='info-card compact'><h4>Exceso</h4><p>Acumulación sin límite.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='info-card compact'><h4>Fragilidad</h4><p>Lo bello parece breve.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='info-card compact'><h4>Desorden humano</h4><p>Confusión y pérdida de centro.</p></div>", unsafe_allow_html=True)

    quote("Lo atractivo también puede ser una trampa.")

    detail = st.selectbox(
        "🔎 Elige un detalle para comentar en exposición",
        ["Frutas gigantes", "Multitudes y repetición", "Animales extraños", "Ausencia de jerarquías claras"],
    )
    explain = {
        "Frutas gigantes": "Placer intenso pero breve: algo dulce que se agota rápido.",
        "Multitudes y repetición": "Muchas figuras repiten conductas y se pierde individualidad.",
        "Animales extraños": "Lo fantástico genera fascinación, pero también inestabilidad.",
        "Ausencia de jerarquías claras": "Todo parece simultáneo y confuso; no hay orden moral evidente.",
    }
    st.markdown(f"<div class='special-card'>{explain[detail]}</div>", unsafe_allow_html=True)


def right_panel_section() -> None:
    visual_header("Panel 4", "Panel derecho: el infierno", "La consecuencia del exceso")

    col_img, col_text = st.columns([2.2, 1])
    with col_img:
        image_or_placeholder(IMAGES["panel_derecho"], "Panel derecho")
    with col_text:
        st.markdown("<div class='special-card compact'><h4>Infierno musical</h4><p>Instrumentos convertidos en castigo.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='tag'>miedo</div>", unsafe_allow_html=True)
        st.markdown("<div class='tag'>castigo</div>", unsafe_allow_html=True)
        st.markdown("<div class='tag'>deshumanización</div>", unsafe_allow_html=True)

    quote("Lo que empezó como seducción termina como destrucción.")


def meaning_section() -> None:
    visual_header("Síntesis", "¿Qué significa la obra?", "Orden → deseo → consecuencias")
    st.markdown(
        "<div class='special-card'><p>Lectura simple: el ser humano nace en orden, se deja llevar por el exceso y termina enfrentando sus consecuencias.</p></div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div class='special-card'><p>No hay una única interpretación, pero muchos expertos la leen como advertencia, no como celebración del placer.</p></div>",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    c1.markdown("<div class='big-idea'>tentación</div>", unsafe_allow_html=True)
    c2.markdown("<div class='big-idea'>libertad mal usada</div>", unsafe_allow_html=True)
    c3.markdown("<div class='big-idea'>consecuencias</div>", unsafe_allow_html=True)


def today_section() -> None:
    visual_header("Vigencia", "¿Qué transmite hoy?", "Una advertencia que sigue actual")
    bullet_strip(["saturación", "placer inmediato", "pérdida de sentido"])

    c1, c2, c3 = st.columns(3)
    c1.markdown("<div class='info-card'><h4>Saturación</h4><p>Demasiados estímulos al mismo tiempo.</p></div>", unsafe_allow_html=True)
    c2.markdown("<div class='info-card'><h4>Placer inmediato</h4><p>Recompensa rápida sin reflexión.</p></div>", unsafe_allow_html=True)
    c3.markdown("<div class='info-card'><h4>Pérdida de sentido</h4><p>Cuando todo es urgente, nada es profundo.</p></div>", unsafe_allow_html=True)


def script_section() -> None:
    visual_header("Guion listo", "Reparto para 6 expositores", "10 minutos aproximados")

    scripts = {
        "Persona 1 · Apertura + El Bosco": [
            "Hoy veremos El jardín de las delicias como una historia sobre el ser humano.",
            "El Bosco fue un pintor neerlandés de finales del siglo XV con estilo único.",
            "Su obra mezcla religión, fantasía y advertencias sobre la conducta humana.",
        ],
        "Persona 2 · Tríptico + lectura general": [
            "Es un tríptico: tres paneles que se leen como una secuencia.",
            "Cuando está cerrado también cuenta algo: la creación.",
            "El recorrido va del orden al exceso y termina en consecuencias.",
        ],
        "Persona 3 · Panel cerrado + izquierdo": [
            "El panel cerrado es gris y funciona como prólogo.",
            "En el izquierdo aparece el paraíso con Adán, Eva y Dios.",
            "Hay armonía, pero ya se sienten señales de tensión.",
        ],
        "Persona 4 · Panel central": [
            "El panel central es el más llamativo y lleno de escenas.",
            "Se percibe placer, pero también exceso y confusión.",
            "Idea clave: lo atractivo también puede ser una trampa.",
        ],
        "Persona 5 · Panel derecho": [
            "En el panel derecho vemos castigo, oscuridad y caos.",
            "Lo que parecía diversión se convierte en consecuencia.",
            "Destaca el infierno musical, donde los instrumentos castigan.",
        ],
        "Persona 6 · Significado + actualidad + cierre": [
            "La obra habla de tentación, libertad mal usada y consecuencias.",
            "Sigue vigente porque hoy también vivimos saturación y exceso.",
            "Cierre: El Bosco pintó una advertencia sobre nosotros mismos.",
        ],
    }

    for speaker, lines in scripts.items():
        with st.expander(speaker):
            for line in lines:
                st.markdown(f"- {line}")


def final_section() -> None:
    visual_header("Cierre", "Pantalla final", "Impacto visual + interacción final")
    image_or_placeholder(IMAGES["triptico_completo"], "Cierre visual")
    quote("El Bosco no pintó solo un mundo extraño; pintó una advertencia sobre nosotros mismos.")

    with st.expander("🎯 Datos curiosos"):
        st.markdown("- El título *El jardín de las delicias* es moderno; no fue puesto por El Bosco.")
        st.markdown("- La obra está en el Museo del Prado (Madrid).")
        st.markdown("- El panel central sigue generando debate entre especialistas.")
        st.markdown("- El tríptico combina mensaje religioso e imaginación extrema.")

    st.subheader("🧠 Mini quiz")
    score = 0

    q1 = st.radio("1) ¿Qué representa el panel derecho?", ["Un nuevo paraíso", "Castigo y consecuencias", "Solo un paisaje"], key="q1")
    if q1 == "Castigo y consecuencias":
        score += 1

    q2 = st.radio("2) ¿Cómo se interpreta frecuentemente el panel central?", ["Equilibrio perfecto", "Advertencia sobre el exceso", "Escena histórica literal"], key="q2")
    if q2 == "Advertencia sobre el exceso":
        score += 1

    q3 = st.radio("3) ¿Para qué sirve ver el tríptico cerrado?", ["No aporta", "Da un prólogo visual", "Solo decorar"], key="q3")
    if q3 == "Da un prólogo visual":
        score += 1

    if st.button("Ver resultado"):
        st.success(f"Puntaje: {score}/3")
        if score == 3:
            st.balloons()

    st.subheader("📎 Créditos")
    st.markdown(
        """
        - Imágenes: reproducciones del tríptico y paneles de *El jardín de las delicias*.
        - Crédito recomendado: Museo del Prado (Hieronymus Bosch / El Bosco).
        - Fuentes sugeridas: ficha del Museo del Prado y materiales de historia del arte.
        - Esta app no descarga contenido automáticamente: usa imágenes locales en `assets/`.
        """
    )


load_css()

if "section_idx" not in st.session_state:
    st.session_state.section_idx = 0

sidebar_index()
nav_controls()
st.markdown("---")

section_renderers = [
    cover_section,
    who_is_bosch_section,
    triptych_section,
    general_reading_section,
    closed_panel_section,
    left_panel_section,
    center_panel_section,
    right_panel_section,
    meaning_section,
    today_section,
    script_section,
    final_section,
]

section_renderers[st.session_state.section_idx]()

st.markdown("---")
nav_controls()
