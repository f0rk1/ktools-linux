<h2 align="center">Ktools Linux</h2>
<h3 align="center">Version 0.2</h3><br>
<p align="justify">It's an application that collects all help information of tools included in the linux distribution for audits and penetration testing Kali Linux, giving users easy access to the help content without an internet connection. The official help content comes from website http://tools.kali.org belonging to offensive security.</p>
<br>
<h4 align="left">Features</h4>
<p align="justify">Ktools was coded in python and the graphical interface in java, allowing to visualize the information from a terminal or from a window.The tool classifies the contents in categories and tools as in Kali Linux, allowing the user to access the information searching for a category or searching the tool directly. This version comes with new features like creation of menu entries on desktop and main menu and it does a pause when the tool information or tool list is showing. Now has the ability to update the database from the command line </p>
<p align="justify">The GUI is now coded with javafx that supports html5 contents, therefore it includes some animations and a new css template to show the tools information.</p>
<br>
<h4 align="left">Requirements</h4>
<p align="justify">Python 2.7</p>
<p align="justify">Python sqlite3</p>
<p align="justify">Java 8 or OpenJdk 8</p>
<p align="justify">Javafx 8 or Openjfx 8</p>
<br>
<p>Install java 8 and openjfx 8</p>
<br>
<p align="center"><img title="Install Java 8" src="https://4.bp.blogspot.com/-uDinyAevxBQ/WszpuFKm-oI/AAAAAAAAAV8/xxHSUyYF8oAOV3LiSbal7T0Y_8rjxKcaQCLcBGAs/s1600/install%2B1.png"></p>
<br>
<h4 align="left">Download</h4>
<p align="justify">Download ktools from github repository</p>
<br>
<p align="center"><img title="Download ktools from github repository" src="https://2.bp.blogspot.com/-k7vaLfJ3QtA/WszqujbYX4I/AAAAAAAAAWE/B71VmnFzsMUYKoFVaP73iDfcUDWLqV6_gCLcBGAs/s1600/install%2B2.png"></p>
<br>
<h4 align="left">Installation</h4>
<p align="justify">Once the script run the first time, a configuration file and menu entries will be create</p>
<p align="center"><img title="Ktools first run" src="https://1.bp.blogspot.com/-sh8F-4QEQlY/Ws0YwTjRwEI/AAAAAAAAAZo/JutkdmMSZQYeHYteHJxWnrABjQH9Z_AzwCLcBGAs/s1600/install%2B3.png">
</p>
<br>
<p align="center"><img title="Downloading and installing Ktools" src="https://github.com/f0rk1/ktools-linux/blob/master/img/en/install.gif"></p>
<br>
<h4 align="left">Configuration</h4>
<p align="jsutify">Once the configuration file is created, the language is automatically detected and configured with the other options with the default values.</p>
<br>
<p align="justify">Options of the configuration file config.cfg of the script in python</p>
<p align="justify">
<pre>
[settings]
;language
lang = es
;create a symbolic link to execute the script and create the menu entries on the desktop and in the main menu
menu = 0
;database hash
dbhash = 40022da25ec234a94ced28da5a3208c0f0cea474f2424b193cdb606ea7189336
;it does a pause when tool information or tool list is showing, you must press enter to continue or q to exit
pausekey = 1
</pre>
</p>
<br>
<p align="center"><img title="Configuring menu option" src="https://github.com/f0rk1/ktools-linux/blob/master/img/en/config.gif"></p>
<br>
<p align="center"><img title="Configuring pausekey option" src="https://github.com/f0rk1/ktools-linux/blob/master/img/en/config2.gif"></p>
<br>
<p align="justify">Options of the configuration file ktoolsGui.properties of the graphical interface</p>
<br>
<p align="justify">
<pre>
#ktoolGui settings
#database hash, is generated automatically when database changes
dbhash=6E49C321CF30D7D9E2855B921D7B4FD496F69363B5511AE4013649CF020BE7FB
#search on key pressed true or false
search=true
#check the author search option or name or content at the start of the application, 1=author 2=name 3=content
searchby=1
#Language spanish or english lang=es or en
lang=es
</pre>
</p>
<br>
<h4 align="left">Start</h4>
<p align="justify">Show help in the command line</p>
<p align="center">
<img title="Ktools" src="https://3.bp.blogspot.com/-b3CmJfO3-GI/Wsz2MLhAZvI/AAAAAAAAAW4/wvb4AQoVUoYD7QsJjl90d-PJtk3ehMcPQCLcBGAs/s1600/install%2B4.png"></p>
