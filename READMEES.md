
<h2 align="center">Ktools Linux</h2>
<h3 align="center">Versión 0.2</h3><br>
<p align="justify">Es una aplicación que reúne toda la información de ayuda de las herramientas incluidas en la distribución de Linux para auditorias y test de penetración Kali Linux, brindando a los usuarios fácil acceso a los contenidos de ayuda sin conexión a Internet. Los contenidos oficiales de ayuda provienen de la web <a target="_blank" title="Penetration Testing Tools - Kali Linux" href="http://tools.kali.org">http://tools.kali.org</a> perteneciente a <a title="Offensive Security Training and Professional Services" href="https://www.offensive-security.com" target="_blank">offensive security</a>. </p>
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
<p align="center"><img title="Instalar Java 8" src="https://2.bp.blogspot.com/-gdcl9kDVD48/Ws_U56OtrPI/AAAAAAAAAaw/gMABbMXdsTY2qYoaYeksYUck6Vna6-qWwCLcBGAs/s1600/installes_1.png"></p>
<h4 align="left">Descarga</h4>
<p align="justify">Descargar ktools desde el repositorio en github</p>
<p align="center"><img title="Descargar ktools desde el repositorio en github" src="https://1.bp.blogspot.com/-OOzE-z6Q848/Ws_UF3DSVoI/AAAAAAAAAak/gthJ5AZRZQAYuTqscQJSZePZPkJI3DXTwCLcBGAs/s1600/installes_2.png"></p>
<h4 align="left">Instalación</h4>
<p align="justify">Una vez se ejecuta el script por primera vez, se crea el archivo de configuración y luego creara los accesos directos de la aplicación</p>
<p align="center"><img title="Ktools primera ejecución" src="https://3.bp.blogspot.com/-EIe-IemG6Qc/Ws_VrY1kfyI/AAAAAAAAAa4/xf5hY6VoAxgOwyZPDk3GvrnQ0IFHWkL2gCLcBGAs/s1600/installes_3.png">
</p>
<p align="center">
<img title="Configurando e instalando Ktools" src="https://3.bp.blogspot.com/-c4I47yZvqzc/Ws_eCbuxwXI/AAAAAAAAAdg/H1ooupowlHMffActbuUJVbRw97Da3CGiQCLcBGAs/s1600/install_es.gif">
<br>
<h4 align="left">Configuración</h4>
<p align="justify">Una vez el archivo de configuración es creado, se configura el idioma que es detectado automáticamente junto con las otras opciones que toman sus valores predeterminados.</p>
<br>
<p align="justify">Opciones del archivo de configuración config.cfg del script en python</p>
<br>
<p align="justify">
<pre>
[settings]
;Idioma
lang = es
;crea un acceso directo para ejecutar el script y también crea los
;menús del programa en el escritorio y en el menú principal
menu = 0
;Hash de la base de datos
dbhash = 40022da25ec234a94ced28da5a3208c0f0cea474f2424b193cdb606ea7189336
;realiza una pausa cuando se muestra la información de la herramienta o 
;cuando se listan todas las herramientas, debe presionar enter para continuar o q para salir
pausekey = 1
</pre>
</p>
<br>
<p align="center">
<img title="Configurando la opción de menu" src="https://1.bp.blogspot.com/-87Ulfgxnsz8/Ws_ecoqnsUI/AAAAAAAAAdk/PEAW6lESTxodb33Z68wFt0Xgc4Mzboi4wCLcBGAs/s1600/config_es.gif">
</p>
<p align="center">
<img title="Configurando la opción pausekey" src="https://4.bp.blogspot.com/-Ap4K_NMq7FI/Ws_etFWsD4I/AAAAAAAAAdo/Wv05eOFK2PoNAV7TugXNm0C3Esvg1tRdwCLcBGAs/s1600/config2_es.gif">
</p>
<h4 align="left">Iniciar Ktools</h4>
<p align="justify">Ver la ayuda en la línea de comandos</p>
<p align="center">
<img title="Iniciar Ktools" src="https://4.bp.blogspot.com/-nsFpt-00E_I/Ws_WPIHyVoI/AAAAAAAAAbQ/gRKn9OhmmO0sRLPRyU4TviweDuK_T-uBgCLcBGAs/s1600/installes_4.png"></p>
<br>
<h3 align="center">Modo rápido</h3>
<br>
<p align="justify">Muestra la información de las categorías y herramientas y luego termina la ejecución del script.</p>
<br>
<h4 align="left">Actualizar Base de datos</h4>
<p align="justify">Verifica si la base de datos ha sido actualizada, y si algún cambio es detectado descarga y actualiza el archivo de la base de datos.</p>
<p align="center"><img title="actualizar base de datos" src="https://2.bp.blogspot.com/-hO_gFC-nRiU/WtC3IOREF-I/AAAAAAAAAes/_BuMUG4JR-Q88s6nROe3JFsmSYjmh1nqwCLcBGAs/s1600/rapido_1.png"></p>
<h4 align="left">Categorías</h4>
<p align="justify">Ver las herramientas en una o varias categorías por nombre.</p>
<p align="center"><img title="ver categorías por nombre" src="https://2.bp.blogspot.com/-M_q1ZbSY5_M/WtC33GIzpTI/AAAAAAAAAe0/FhEgIh8mPycWVvDH4k9Sb1Jw8WfW7aHywCLcBGAs/s1600/rapido_2.png"></p>
<p align="justify">Ver las herramientas en una o varias categorías por id.</p>
<p align="center"><img title="ver una categoría por id" src="https://3.bp.blogspot.com/-82FQJg5KYCM/WtC4OcDH-_I/AAAAAAAAAe4/Bg-3QnKbc5kZj24lQ2P26Uqx_GAiMOpxgCLcBGAs/s1600/rapido_3.png"></p>
<h4 align="left">Herramientas</h4>
<p align="justify">Ver una herramienta por nombre.</p>
<p align="center"><img title="ver una herramienta por nombre" src="https://3.bp.blogspot.com/-EGTNOZBR0j4/WtC48tWvXiI/AAAAAAAAAfE/TmnNyNQUKEgnnEA93sxCJGrrKzYDCEE7QCLcBGAs/s1600/rapido_4.png"></p>
<p align="justify">Ver una herramienta por id.</p>
<p align="center"><img title="ver una herramienta por id" src="https://4.bp.blogspot.com/-i4NfKlACck0/WtC6fTa1niI/AAAAAAAAAfQ/jXC0YhxOanENvBQkNTjAuJf2fGP0BNFDgCLcBGAs/s1600/rapido_5.png"></p>
<h4 align="left">Listas</h4>
<p align="justify">Ver todas las categorías.</p>
<p align="center"><img title="ver todas las categorías" src="https://2.bp.blogspot.com/-RkK2YhSihL4/WtC69ZuU2VI/AAAAAAAAAfg/NBHYWKzNjfoSI75e86A0PjGUqgs0ygD-ACLcBGAs/s1600/rapido_6.png"></p>
<p align="justify">Ver todas las herramientas.</p>
<p align="center"><img title="ver todas las herramientas" src="https://3.bp.blogspot.com/-Q31fzSOX_jk/WtC7YX4ruVI/AAAAAAAAAfo/svzqecW2NQgdwnASs6EeTj5rsnyGGZASQCLcBGAs/s1600/rapido_7.png"></p>
<h4 align="left">Buscar</h4>
<p align="justify">Buscar herramientas por nombre.</p>
<p align="center"><img title="buscar herramientas por nombre" src="https://1.bp.blogspot.com/-clwc7L98P4I/WtC9SCGUyfI/AAAAAAAAAgE/msmaq3tN158J92yi8-0szg6Xp3nI6vVLwCLcBGAs/s1600/rapido_8.png"></p>
<p align="justify">Buscar herramientas por autor.</p>
<p align="center"><img title="buscar herramientas por autor" src="https://1.bp.blogspot.com/-lc0BJXjFUgc/WtC9kRRxP9I/AAAAAAAAAgI/kH7Aexvlcxokt07Lhf_RE5mTtI6j7NTzgCLcBGAs/s1600/rapido_9.png"></p>
<p align="justify">Buscar herramientas por contenido.</p>
<p align="center"><img title="buscar herramientas por contenido" src="https://2.bp.blogspot.com/-ZF3SgKqOw_M/WtC90dBda9I/AAAAAAAAAgQ/Znj0IQKorakkHuQ3buJPSPoXuRie4UitwCLcBGAs/s1600/rapido_10.png"></p>
<br>
<h3 align="center">Modo shell</h3>
<br>
<p align="justify">Permite acceder a las diferentes opciones de la herramienta mediante una shell interactiva.</p>
<p align="justify">Acceder a la herramienta en modo shell.</p>
<p align="center"><img title="ktools iniciar modo shell" src="https://1.bp.blogspot.com/-VMXzLPZxqHg/WtC-rZ974TI/AAAAAAAAAgg/W3t71Ytm0BEaI3EbAM7ynk8yHEqOGZhEgCLcBGAs/s1600/shell_1.png"></p>
<br>
<h4 align="left">Categorías</h4>
<p align="justify">Ver las herramientas en una o varias categorías por nombre.</p>
<p align="center"><img title="ver categorías por nombre" src="https://2.bp.blogspot.com/-DXKi4TF2cwY/WtC_P6vsXyI/AAAAAAAAAgo/eA6k07RmDFwn0WwW19iUnVyS0ROe3KFyQCLcBGAs/s1600/shell_2.png"></p>
<p align="justify">Ver las herramientas en una o varias categorías por id.</p>
<p align="center"><img title="ver una categoría por id" src="https://4.bp.blogspot.com/-mH-nCw9MVbw/WtC_fvpAqPI/AAAAAAAAAgs/lWorSehoAogTPjrWybJGobluG81-wNk1QCLcBGAs/s1600/shell_3.png"></p>
<h4 align="left">Herramientas</h4>
<p align="justify">Ver una herramienta por nombre.</p>
<p align="center"><img title="ver herramienta por nombre" src="https://1.bp.blogspot.com/-N4JkOWSq15I/WtDABiLenUI/AAAAAAAAAg8/25akWkbuVCw4RomgceQRgRP5Opdr5xYfACLcBGAs/s1600/shell_4.png"></p>
<p align="justify">Ver una herramienta por id.</p>
<p align="center"><img title="ver herramienta por id" src="https://4.bp.blogspot.com/-JjeDKy8PNgA/WtDAQFsU77I/AAAAAAAAAhM/oUUmYH1hlfYPdttQIrI36IACdQq9eqdYQCLcBGAs/s1600/shell_5.png"></p>

<h4 align="left">Mostrar</h4>
<p align="justify">Ver todas las categorías.</p>
<p align="center"><img title="ver todas las categorías" src="https://4.bp.blogspot.com/-2f9V_oNWTEo/WtDApB9_kDI/AAAAAAAAAhU/AIkjWJee4bkZljQDnPPE1_1idbWvIfPewCLcBGAs/s1600/shell_6.png"></p>
<p align="justify">Ver todas las herramientas.</p>
<p align="center"><img title="ver todas la herramientas" src="https://3.bp.blogspot.com/-hDt6yxznIDQ/WtDA4dy1EkI/AAAAAAAAAhc/24PUaM5xOSYiwFZqZcsh9nZc5HZOc1WewCLcBGAs/s1600/shell_7.png"></p>
<h4 align="left">Buscar</h4>
<p align="justify">Buscar herramientas por nombre.</p>
<p align="center"><img title="buscar herramientas por nombre" src="https://2.bp.blogspot.com/-fvHxqvwahG0/WtDBMb31TkI/AAAAAAAAAho/3TkkrY69bwkEDON7YU0CHtxeIKx-nYSmgCLcBGAs/s1600/shell_8.png"></p>
<p align="justify">Buscar herramientas por autor.</p>
<p align="center"><img title="buscar herramientas por autor" src="https://4.bp.blogspot.com/-I-TiR_rwBvI/WtDBdWJvYUI/AAAAAAAAAhw/aXhCQnO4rE8ssHQeI32s6bhvNmFElfwUwCLcBGAs/s1600/shell_9.png"></p>
<p align="justify">Buscar herramientas por contenido.</p>
<p align="center"><img title="buscar herramientas por contenido" src="https://3.bp.blogspot.com/-NRT7I6CuVn4/WtDBqu27uoI/AAAAAAAAAh0/WEMEe2sPyQs8e-I_T7OptstT8xdhQk_UQCLcBGAs/s1600/shell_10.png"></p>
<br>
<h3 align="center">GUI</h3>
<br>
<p align="justify">la GUI en su versión 0.2 fue escrita en Javafx, y permite acceder a los contenidos de ayuda mediante una interfaz gráfica, tiene nuevas características como el guardado de las configuraciones seleccionadas por el usuario en la interfaz gráfica en el archivo de configuración.</p>
<br>
<h4 align="left">Configuración</h4>
<p align="justify">Una vez la aplicación de java es ejecutada por primera vez, se crea el archivo de configuración el cual tiene opciones como el idioma, el cual es detectado automáticamente junto con las otras opciones que toman sus valores predeterminados.</p>
<p>Opciones del archivo de configuración ktoolsGui.properties de la interfaz gráfica.</p>
<p align="justify">
<pre>
#ktoolGui settings
#hash de la base datos, es generado automáticamente
#cuando la base de datos cambia
dbhash=6E49C321CF30D7D9E2855B921D7B4FD496F69363B5511AE4013649CF020BE7FB
#buscar al teclear 
search=true
#marca la opción de búsqueda por autor, nombre o contenido al 
#iniciar la aplicación, 1=autor 2=nombre 3=contenido
searchby=1
#idioma español o inglés lang=es o en
lang=es
</pre>
</p>
<br>
<h4 align="left">Ejecución</h4>
<p align="justify">Inciar ktools GUI.</p>
<p align="center"><img title="iniciar ktools GUI" src="https://3.bp.blogspot.com/-fJjUJPn0ngc/WtDEVMtYo-I/AAAAAAAAAiU/E5LaOdfQRwIRHEuyWqKKBZxoMpSJ1x-CwCLcBGAs/s1600/GUI.png"></p>
<p align="center"><img title="ktools GUI" src="https://4.bp.blogspot.com/-Z6p0KUPpJdY/WtDRzhqtApI/AAAAAAAAAjg/DTWmw6qTyoUjurBev_HfdnIz3nWkk8rxwCLcBGAs/s1600/GUI2.png"></p>
<h4>Blog ktools</h4>
<p><a title="Ktools linux blog" target="_blank" href="https://ktools-linux.blogspot.com">https://ktools-linux.blogspot.com</a></p>
