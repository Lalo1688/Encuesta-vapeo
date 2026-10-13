import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Encuesta Anónima: Consumo de Vapeadores", page_icon="📊", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stStatusWidget"] {visibility: hidden;}
    .viewerBadge_container__1QSob {display: none !important;}
    </style>
""", unsafe_allow_html=True)

st.title("Encuesta Anónima sobre el Consumo y los Factores Asociados al Vapeo")

st.divider()

CSV_FILE = "respuestas_vapeo.csv"

def guardar_respuesta(datos):
    df_nuevo = pd.DataFrame([datos])
    if not os.path.exists(CSV_FILE):
        df_nuevo.to_csv(CSV_FILE, index=False, encoding='utf-8-sig')
    else:
        df_nuevo.to_csv(CSV_FILE, mode='a', header=False, index=False, encoding='utf-8-sig')

with st.form("formulario_encuesta"):
    
    st.header("Sección 1. Datos generales y contexto personal")
    p1 = st.radio("1. ¿En qué grado estás matriculado actualmente?", ["9A", "9B", "9C", "10B", "10C", "11A", "11B", "11C"], key="p1")
    p2 = st.radio("2. ¿Qué edad tienes actualmente?", ["13 años", "14 años", "15 años", "16 años", "17 años", "18 años o más", "Prefiero no responder"], key="p2")
    p3 = st.radio("3. ¿Con qué género te identificas?", ["Femenino", "Masculino", "No binario", "Otra identidad de género", "Prefiero no responder"], key="p3")
    p4 = st.radio("4. ¿Con qué frecuencia conversas en casa sobre temas como salud, estrés, amistades o decisiones personales?", ["Muy frecuentemente", "Frecuentemente", "A veces", "Casi nunca", "Nunca", "Prefiero no responder"], key="p4")
    p5 = st.radio("5. ¿Sientes que cuentas con una persona adulta de confianza a quien acudir si tienes un problema?", ["Sí", "A veces", "No", "No estoy seguro/a", "Prefiero no responder"], key="p5")

    st.header("Sección 2. Experiencia con el vapeo")
    p6 = st.radio("6. ¿Alguna vez has probado un vaper (cigarrillo electrónico)?", ["Sí", "No", "No estoy seguro/a de si lo que probé era un vapeador", "Prefiero no responder"], key="p6")
    p7 = st.radio("7. ¿Con qué frecuencia usas o has usado vaper?", ["Diario", "De 1 a 3 veces por semana", "Ocasionalmente (solo en fiestas o reuniones)", "Solo lo probé una vez", "Nunca lo he probado", "Prefiero no responder"], key="p7")
    p8 = st.radio("8. Si has probado o usas vaper, ¿a qué edad tuviste tu primer contacto con él?", ["Antes de los 13 años", "13 años", "14 años", "15 años", "16 años", "17 años", "18 años o más", "No he probado un vaper / No aplica", "Prefiero no responder"], key="p8")
    p9 = st.radio("9. Si has probado un vaper, ¿en qué contexto ocurrió la primera vez?", ["En una reunión o fiesta", "En el colegio o cerca de él", "En casa propia o de otra persona", "En un parque o espacio público", "En una salida con amigos", "En otro lugar o contexto", "No he probado un vaper / No aplica", "Prefiero no responder"], key="p9")
    p10 = st.radio("10. ¿Quién fue la primera persona que te ofreció, prestó o acercó un vaper? Marca la opción que más se aproxime.", ["Madre, padre, madrastra o padrastro", "Hermana/o, prima/o u otro familiar", "Amiga/o o compañera/o de clase", "Pareja o persona con la que salía", "Otra persona conocida", "Persona desconocida", "Lo tomé sin que me lo ofrecieran", "Nadie me lo ofreció / lo conseguí de otra forma", "No he probado un vaper / No aplica", "Prefiero no responder"], key="p10")

    st.header("Sección 3. Motivos e influencias relacionadas con el consumo")
    p11 = st.radio("11. ¿Cuál fue el motivo principal por el que probaste un vaper por primera vez, si lo has probado?", ["Curiosidad", "Quería probar el sabor o la sensación", "Mis amistades lo usaban", "Presión para encajar o no quedar por fuera", "Me lo ofrecieron y acepté", "Quería manejar estrés, tristeza, ansiedad o aburrimiento", "Lo vi en redes sociales o contenido digital", "Lo vi en familiares o personas cercanas", "Quería parecer mayor o seguir una moda", "Otro motivo", "No he probado un vaper / No aplica", "Prefiero no responder"], key="p11")
    p12 = st.radio("12. Antes de probarlo, ¿qué tanto sabías sobre los posibles efectos del vapeo en la salud?", ["Sabía mucho", "Sabía algo", "Sabía muy poco", "No sabía nada", "No he probado un vaper / No aplica", "Prefiero no responder"], key="p12")
    p13 = st.radio("13. ¿Qué tan importante fue la curiosidad en tu decisión de probarlo, si lo has probado?", ["Nada importante", "Poco importante", "Moderadamente importante", "Muy importante", "Fue el motivo principal", "No he probado un vaper / No aplica", "Prefiero no responder"], key="p13")
    p14 = st.radio("14. ¿Influyó el deseo de encajar con un grupo o evitar burlas en tu decisión de probarlo?", ["Sí, mucho", "Sí, algo", "Muy poco", "No influyó", "No he probado un vaper / No aplica", "Prefiero no responder"], key="p14")
    p15 = st.radio("15. ¿Influyó el estrés, la ansiedad, la tristeza, el enojo o el aburrimiento en tu decisión de probarlo?", ["Sí, mucho", "Sí, algo", "Muy poco", "No influyó", "No he probado un vaper / No aplica", "Prefiero no responder"], key="p15")
    p16 = st.radio("16. ¿Influyeron los sabores, olores o diseños de los vapeadores en tu interés por probarlos?", ["Sí, mucho", "Sí, algo", "Muy poco", "No influyeron", "No he probado un vaper / No aplica", "Prefiero no responder"], key="p16")
    p17 = st.radio("17. ¿Influyeron videos, publicaciones o creadores de contenido en redes sociales en tu interés por vapear?", ["Sí, mucho", "Sí, algo", "Muy poco", "No influyeron", "No uso o casi no uso redes sociales", "No he probado un vaper / No aplica", "Prefiero no responder"], key="p17")
    p18 = st.radio("18. ¿Influyeron familiares adultos que vapean o hablan del vapeo como algo normal?", ["Sí, mucho", "Sí, algo", "Muy poco", "No influyeron", "No conozco familiares que vapeen", "No he probado un vaper / No aplica", "Prefiero no responder"], key="p18")
    p19 = st.radio("19. ¿Influyeron compañeros o amistades que vapean?", ["Sí, mucho", "Sí, algo", "Muy poco", "No influyeron", "No conozco compañeros o amistades que vapeen", "No he probado un vaper / No aplica", "Prefiero no responder"], key="p19")
    p20 = st.radio("20. ¿Influyó tener problemas personales, familiares, académicos o con amistades?", ["Sí, mucho", "Sí, algo", "Muy poco", "No influyó", "No deseo responder sobre este tema", "No he probado un vaper / No aplica"], key="p20")
    p21 = st.radio("21. ¿Influyó pensar que vapear era menos perjudicial que fumar cigarrillo tradicional?", ["Sí, mucho", "Sí, algo", "Muy poco", "No influyó", "No sabía comparar los riesgos", "No he probado un vaper / No aplica", "Prefiero no responder"], key="p21")
    p22 = st.radio("22. ¿Qué tan fácil crees que sería para ti decir «no» si alguien te ofrece un vaper?", ["Muy fácil", "Algo fácil", "Algo difícil", "Muy difícil", "No estoy seguro/a", "Prefiero no responder"], key="p22")
    p23 = st.radio("23. ¿Has sentido que alguien insiste, se burla o te excluye por no querer vapear?", ["Sí, varias veces", "Sí, una vez", "No", "No estoy seguro/a", "Prefiero no responder"], key="p23")

    st.header("Sección 4. Entorno escolar, acceso e información")
    
    st.write("24. ¿En qué lugares del colegio o sus alrededores has visto u oído que se usan vapers? (Puedes marcar varias opciones)")
    p24_ops = [
        "En los baños", "En las canchas", "En zonas de descanso durante el recreo", 
        "En pasillos o escaleras", "En salones vacíos", "En la cafetería o sus alrededores", 
        "En zonas apartadas del patio", "En los alrededores de la entrada o a la salida", 
        "No he visto ni oído que se usen", "No lo sé", "Prefiero no responder"
    ]
    p24 = [op for op in p24_ops if st.checkbox(op, key=f"p24_{op}")]

    p25 = st.radio("25. ¿Qué tan fácil resulta para un menor de edad conseguir o comprar un vaper?", ["Muy fácil", "Moderadamente fácil", "Difícil", "Muy difícil", "No lo sé", "Prefiero no responder"], key="p25")
    p26 = st.radio("26. ¿Consideras que vapear es menos perjudicial que fumar cigarrillo tradicional?", ["Sí, es menos dañino", "No, puede causar daños importantes", "No tengo información suficiente sobre el tema", "No lo sé", "Prefiero no responder"], key="p26")
    p27 = st.radio("27. ¿Tus padres o acudientes han hablado contigo acerca de los riesgos del uso de vapers?", ["Sí, hemos hablado del tema", "No, nunca se ha mencionado en casa", "No recuerdo", "No aplica a mi situación familiar", "Prefiero no responder"], key="p27")
    p28 = st.radio("28. ¿El colegio ha realizado charlas, talleres o actividades sobre la prevención del uso de vapers?", ["Sí, frecuentemente", "Muy pocas veces", "Nunca", "No recuerdo", "Prefiero no responder"], key="p28")

    st.header("Sección 5. Prevención y posibles cambios")
    p29 = st.radio("29. ¿Qué tipo de actividad preventiva te parecería más útil?", ["Charlas con profesionales de la salud", "Talleres participativos", "Información anónima y clara", "Actividades sobre manejo del estrés y emociones", "Orientación para resistir la presión de grupo", "Material informativo para familias", "Campañas creadas por estudiantes", "Otra", "Ninguna", "Prefiero no responder"], key="p29")
    p30 = st.radio("30. Si has vapeado, ¿has pensado en reducir o dejar el consumo?", ["Sí", "No", "No estoy seguro/a", "No he vapeado / No aplica", "Prefiero no responder"], key="p30")
    
    enviado = st.form_submit_button("Enviar Encuesta de Forma Anónima")

    if enviado:
        respuesta_data = {
            "Fecha_Hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Grado": p1, "Edad": p2, "Genero": p3, "ConversasCasa": p4, "AdultoConfianza": p5,
            "ProbadoVaper": p6, "Frecuencia": p7, "EdadPrimerContacto": p8, "ContextoPrimeraVez": p9,
            "QuienOfrecio": p10, "MotivoPrincipal": p11, "SabiaEfectos": p12, "Curiosidad": p13,
            "Encajar": p14, "EstresEmociones": p15, "SaboresDisenos": p16, "RedesSociales": p17,
            "FamiliaresVapean": p18, "AmigosVapean": p19, "ProblemasPersonales": p20, "MenosPerjudicial": p21,
            "FacilidadDecirNo": p22, "InsistenciaBurlas": p23, "LugaresColegio": ", ".join(p24),
            "FacilidadConseguir": p25, "MenosPerjudicialCigarrillo": p26, "PadresHablado": p27,
            "ColegioCharlas": p28, "ActividadUtil": p29, "PensadoReducir": p30
        }
        
        guardar_respuesta(respuesta_data)
        st.success("¡Muchas gracias! Tus respuestas han sido registradas de forma segura y anónima.")

st.divider()
st.subheader("Acceso Administrador")
pin = st.text_input("Ingresa el PIN para descargar los datos:", type="password")

if pin == "ilovelinux":
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "rb") as f:
            st.download_button(
                label="Descargar Respuestas",
                data=f,
                file_name="respuestas_encuesta_vapeo.csv",
                mime="text/csv"
            )
    else:
        st.info("Aún no hay respuestas registradas en el sistema.")
elif pin != "":
    st.error("Incorrecto, ¿para qué quieres descargar las respuestas?.")
