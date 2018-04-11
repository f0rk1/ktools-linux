
<h2 align="center">Ktools Linux</h2>
<h3 align="center">Versión 0.2</h3><br>
<p align="justify">Es una aplicación que reúne toda la información de ayuda de las herramientas incluidas en la distribución de Linux para auditorias y test de penetración Kali Linux, brindando a los usuarios fácil acceso a los contenidos de ayuda sin conexión a Internet. Los contenidos oficiales de ayuda provienen de la web http://tools.kali.org perteneciente a offensive security. </p>
<br>
<h4 align="left">Características</h4>
<p align="justify">Ktools esta codificada en python y la interfaz gráfica en java, permitiendo visualizar los contenidos desde una terminal o desde una ventana. La herramienta clasifica los contenidos en categorías y herramientas como en Kali Linux, permitiendo al usuario acceder a la información buscando una categoría o buscando la herramienta directamente. Esta versión viene con nuevas características como la creación de accesos directos de la aplicación en el escritorio y en el menú principal, también tiene la opción de crear una pausa cuando se esta mostrando la información o la lista de herramientas. Ahora el script tiene la opción de actualizar la base de datos desde la línea de comandos.</p>
<p align="justify">La GUI fue creada con javafx que soporta contenidos html5, entonces incluye algunas animaciones y una nueva plantilla para mostrar la información de las herramientas.</p>
<br>
<h4 align="left">Requerimientos</h4>
<p align="justify">Python 2.7</p>
<p align="justify">Python sqlite3</p>
<p align="justify">Java 8 o OpenJdk 8</p>
<p align="justify">Javafx 8 o Openjfx 8</p>
<br>
<p>Instalar java 8 and openjfx 8</p>
<br>
<p align="center"><img title="Instalar Java 8" src="https://4.bp.blogspot.com/-uDinyAevxBQ/WszpuFKm-oI/AAAAAAAAAV8/xxHSUyYF8oAOV3LiSbal7T0Y_8rjxKcaQCLcBGAs/s1600/install%2B1.png"></p>
<br>
<h4 align="left">Descarga</h4>
<p align="center"><img title="Descargar ktools desde el repositorio en github" src="https://2.bp.blogspot.com/-k7vaLfJ3QtA/WszqujbYX4I/AAAAAAAAAWE/B71VmnFzsMUYKoFVaP73iDfcUDWLqV6_gCLcBGAs/s1600/install%2B2.png"></p>
<br>
<h4 align="left">Instalación</h4>
<p align="justify">Una vez se ejecuta el script por primera vez, se crea el archivo de configuración y luego creara los accesos directos de la aplicación</p>
<p align="center"><img title="Ktools primera ejecución" src="https://3.bp.blogspot.com/-_6KD-fjZSVk/Ws0OZ3LVKEI/AAAAAAAAAYw/1UpHvyxmak0CHl7xukzgmlTxSptEyyCbACLcBGAs/s1600/installes1.png">
</p>
<br>
<p align="center">
<img src="https://raw.githubusercontent.com/f0rk1/ktools-linux/master/img/es/install.gif">
</p>
<br>
<h4 align="left">Configuración</h4>
<p align="justify">Opciones script en Python</p>
<p align="justify">Archivo config.cfg</p>
<p align="justify">
<pre>
[settings]
;Idioma
lang = es
;crea un acceso directo para ejecutar el script y también crea los menús del programa en el escritorio y en el menú principal
menu = 0
;Hash de la base de datos
dbhash = 40022da25ec234a94ced28da5a3208c0f0cea474f2424b193cdb606ea7189336
;realiza una pausa cuando se muestra la información de la herramienta o cuando se listan todas las herramientas, debe presionar enter para continuar o q para salir
pausekey = 1
</pre>
</p>
<br>
<p align="center">
<img src="https://raw.githubusercontent.com/f0rk1/ktools-linux/master/img/es/config.gif">
</p>
<br>
<p align="center">
<img src="https://raw.githubusercontent.com/f0rk1/ktools-linux/master/img/es/config2.gif">
</p>
<br>
<p align="justify">Opciones GUI</p>
<p align="justify">Archivo ktoolsGui.properties</p>
<p align="justify">
<pre>
#ktoolGui settings
#hash de la base datos, es generado automáticamente cuando la base de datos cambia
dbhash=6E49C321CF30D7D9E2855B921D7B4FD496F69363B5511AE4013649CF020BE7FB
#buscar al teclear 
search=true
#marca la opción de búsqueda por autor, nombre o contenido al iniciar la aplicación, 1=autor 2=nombre 3=contenido
searchby=1
#idioma español o inglés lang=es o en
lang=es
</pre>
</p>
<br>
<h4 align="left">Iniciar Ktools</h4>
<p align="center">
<img title="Iniciar Ktools" src="https://3.bp.blogspot.com/-7TQQs6qoPwA/Ws0R6Tpr7II/AAAAAAAAAZM/llcTzPe-2KcIl-Jg6lG-jjyJ2j2ugE9cACLcBGAs/s1600/installes2.png"></p>
<br>
