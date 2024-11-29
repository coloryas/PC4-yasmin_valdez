# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.

# Primero, debes abrir el folder donde se encuentra tu archivo de Python en la terminal de tu computadora.
# Para hacerlo, debes escribir el siguiente comando en la terminal de tu computadora
# cd ruta_de_tu_carpeta
# o desde Visual Studio Code, seleccionas Open Folder y seleccionas la carpeta 
# donde se encuentra tu archivo de Python

# Segundo, debes instalar un entorno virtual en tu computadora.
# python -m venv .venv
# Este comando crea un entorno virtual en la carpeta actual con el nombre .venv.

# Para activar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# .venv\Scripts\activate
# Para desactivar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# deactivate

# Tercero, debes instalar Streamlit en tu entorno virtual.
# pip install Streamlit 

# Cuarto, puedes abrir el tutorial de Streamlit en tu navegador.
# streamlit hello o python -m streamlit hello

# Quinto, debes abrir el archivo de Python en la terminal de tu computadora.
# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py o python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>Hey its Yas</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("photo_p.jpg", caption='YO', width=300)

# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

texto = """
Hola! Soy Yasmin, una persona resiliente y creativa, quien se enfoca en alcanzar mis metas y objetivos. Mi signo es Capricornio y nací en Lima. Actualmente, estudio Publicidad porque me fascina explotar mi creatividad y las estrategías de comunicación, además de las oportunidades que ofrece para entender e influir en las emociones y decisiones de las personas. Lo que más me gusta de mi carrera es la posibilidad de conocer e indagar sobre las diversas perspectivas que existen en el mundo, de manera que me sirve como herramienta fundamental para innovar en cada proyecto. En el futuro, me gustaría dedicarme a ser Fashion styling en pasarelas de moda o diseñadora de vestuario en películas, donde pueda seguir desarrollándome de manera creativa. En mi tiempo libre, disfruto de tomar fotos, ver películas, leer poemas, comprar ropa, escuchar música y de pasar tiempo con mis mascotas, ya que me permite relajarme y desconectar del mundo caótico en el que vivimos hoy en día.

"""

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 14px;'>{texto}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 14px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.

# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.

# Agregar un  texto para la respuesta
texto_2 = """
Al principio, saber que iba a aprender a programar fue emocionante para mí, pero luego resultó algo abrumador. Me atrae la idea de crear cosas desde cero y entender cómo funciona la tecnología hoy en día, sobre todo las herramientas digitales que son parte de esta era digital; sin embargo, he encontrado muchos desafíos en el camino. Mientras avanzaban las semanas, me sentía confundida con la gran cantidad de información; a veces me perdía con cada subtema, por lo que perdía el hilo.
La programación me ha enseñado a trabajar en paciente y saber gestionar mis emociones cuando cometo errores, es decir, como una oportunidad de aprendizaje, aunque todavía me cuesta mantener la atención y no frustrarme. Me gusta que haya un orden detrás de cada línea de código, pero aún así me siento perdida en los detalles.
En el futuro, me gustaría mucho seguir mejorando para poder aplicar la programación en los proyectos que se presenten en la facultad. Lo ideal sería que pueda disfrutar del proceso sin sentirme tan abrumada y utilizar estos conocimientos para aportar valor en mi carrera profesional. 
"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 14px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Ahora agregamos un video a mi blog donde explico algún tema de las clases
# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Explicación de un tema de las clases 📚</h2>", unsafe_allow_html=True)
# <h2 style='text-align: center;'>Explicación de un tema de las clases 📚</h2>: Esta es una cadena de código HTML
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Explicación de un tema de las clases 📚") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.

# Agregamos un video a la aplicación web ( menor a 20 MB)
#st.video("ppc-2024-1.mp4")
# st.video("ppc-2024-1.mp4"): Esta línea está agregando un video a la aplicación web.

# Agregamos un enlace a la página web donde está el video.
enlace = f'<a href="https://www.youtube.com/watch?v=uArFYpxDOoU" target="_blank"><button>TAP TAP A LA PANTALLA</button></a>'
st.markdown(enlace, unsafe_allow_html=True)
# f'<a href="URL" target="_blank"><button>Nombre</button></a>':
# La etiqueta <a> se utiliza para crear un enlace en HTML.
# El atributo href se utiliza para especificar la URL de destino del enlace.
# El atributo target="_blank" se utiliza para abrir el enlace en una nueva pestaña del navegador.
# La etiqueta <button> se utiliza para crear un botón en HTML.
# El texto dentro de las etiquetas <button> ("Nombre creativo para el botón") es el contenido del botón.
# La variable enlace contiene la cadena de código HTML para el enlace y el botón

# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>Mis gráficos elaborados</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Los análisis de Ellie</h1>: Esta es una cadena de código HTML.
# La etiqueta <h1> se utiliza para el encabezado principal de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h1> ("Los análisis de Ellie") es el contenido del encabezado.

# Creamos una lista de gráficos
graficos = ['Frecuencia de goleadas', 'Mapa de películas', 'Mapa de ubicación']

# Creamos un cuadro de selección en la barra lateral
grafico_seleccionado = sidebar.selectbox('Selecciona un gráfico', graficos)
# El cuadro de selección se crea con la función selectbox.
# El primer argumento es el texto que se muestra en el cuadro de selección.
# El segundo argumento es una lista de opciones que se pueden seleccionar.
# En este caso, las opciones son los elementos de la lista graficos.
# La opción seleccionada se asigna a la variable grafico_seleccionado.
# La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
# La función selectbox se utiliza para crear un cuadro de selección en la barra lateral.

# Mostramos el gráfico seleccionado
if grafico_seleccionado == 'Frecuencia de goleadas':
    sidebar.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de barras muestra la frecuencia de goleadas del equipo Fiorentina, comparando los goles anotados por los locales vs. los visitantes. Se importó la biblioteca Matplotlib.pyplot y a través del Plt.bar() para crear un gráfico de barras. Inicialmente, se definió una lista llamada Goles que contiene las cantidades de goles marcados por la Fiorentina como equipo local (g_local) y como visitante (g_visitante). Además, se añadieron las etiquetas LOCAL y VISITANTE. Para el tamaño del gráfico, se usó plt.figure(figsize=(10, 6)). Para los colores personalizados de las barras, se usó los códigos #c39bd3 (lila oscuro) y #e8daef (lila claro) para diferenciarlos. También se añadió un título principal plt.title(), un nombre para el eje X plt.xlabel() y un nombre para el eje Y plt.ylabel(). Finalmente, el plt.show() para mostrar el gráfico.</div>", unsafe_allow_html=True)
    sidebar.image("Grafico_1.PNG", caption='Frecuencia de goleadas', width=500)
    pass
elif grafico_seleccionado == 'Mapa de películas':
    sidebar.markdown("<div style='text-align: justify'>El gráfico 2 muestra un mapa interactivo donde se utilizó el folium.Map(). Se creó un mapa base con las coordenadas [40.00, -100.0], lo que ubica el mapa de los Estados Unidos. El mapa tiene un zoom de 4 y utiliza el OpenStreetMap para mostrar el fondo cartográfico. Se añadieron marcadores a través de un bucle que itera sobre un DataFrame llamado dataframe_Películas, en el cual cada fila representa una película. Los marcadores ubican la latitud y longitud que fueron extraídas del DataFrame, y cada uno contiene columnas (Popup) para mostrar el nombre de la película y (Tooltip) para señalar el país relacionado con dicha película. Como resultado, el mapa interactivo muestra los marcadores en Los Ángeles y Nueva York, identificando los lugares donde se grabaron ciertas películas representadas en el DataFrame. .</div>", unsafe_allow_html=True)
    sidebar.image("Grafico_2.PNG", caption='Mapa de películas', width=500)
    pass
elif grafico_seleccionado == 'Mapa de ubicación':
    sidebar.markdown("<div style='text-align: justify'>El gráfico 2.1 muestra un mapa interactivo donde se utilizó el folium.Map() para generar un mapa interactivo con las coordenadas geográficas [-18.00, -60.0], con un zoom de 4 y utilizando el OpenStreetMap. Luego, para añadir marcadores al mapa, se empleó un bucle que itera sobre un DataFrame llamado Páezz, el cual contiene columnas como Latitude, Longitude, Language y Glottocode. Cada marcador tiene dos elementos: un Popup para el nombre del lenguaje asociado y un Tooltip que despliega el código ISO. Como resultado, el mapa interactivo muestra los marcadores que indican la posición geográfica de lenguajes o dialectos..</div>", unsafe_allow_html=True)
    sidebar.image("Grafico_21.PNG", caption='Mapa de ubicación', width=500)
    pass

# if grafico_seleccionado == 'Gráfico de Macroareas': Esta línea verifica si la opción seleccionada es 'Gráfico de Macroareas'.
# Si es así, se ejecuta el código dentro del bloque if.
# En este caso, se muestra un texto y una imagen correspondientes al gráfico de Macroareas.
# El texto y la imagen se muestran en la barra lateral.
# La función markdown se utiliza para mostrar el texto en la barra lateral.
# La función image se utiliza para mostrar la imagen en la barra lateral.
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen.
# El argumento width se utiliza para especificar el ancho de la imagen.
# La palabra clave pass se utiliza para indicar que no se debe hacer nada en caso de que la opción seleccionada no sea 'Gráfico de Macroareas'.
