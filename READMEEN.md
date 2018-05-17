<h2 align="center">Ktools Linux</h2>
<h3 align="center">Version 0.2</h3><br>
<p align="justify">It's an application that collects all help information of tools included in the linux distribution for audits and penetration testing Kali Linux, giving users easy access to the help content without an internet connection. The official help content comes from website <a target="_blank" title="Penetration Testing Tools - Kali Linux" href="http://tools.kali.org">http://tools.kali.org</a> belonging to <a title="Offensive Security Training and Professional Services" href="https://www.offensive-security.com" target="_blank">offensive security</a>.</p>
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
<p align="center"><img title="Install Java 8" src="https://2.bp.blogspot.com/-etdCTHX4998/Wv34i-7u1kI/AAAAAAAAAp0/40oOlgvWyhojk7aE8pK7kisg0ToFXtj1wCLcBGAs/s1600/install.png"></p>
<p align="justify">If the Linux distribution does not have the repositories for openjdk-8-jre or openjfx, you can download the jre version of oracle in the following link <a href="" title="Java Jre 8">Java Jre 8</a>.</p>
<p align="center"><img title="Install Java 8 Oracle" src="https://3.bp.blogspot.com/-CeeKgqsCKBU/Wv4TVtNRL5I/AAAAAAAAAsA/Y3hGMtE6NEwluUJ1LKVVRANlKxlt5MTHwCLcBGAs/s1600/installjreen.png"></p>
<p align="justify">If you have jdk or jre installed in a version higher than 8, you must skip the steps that include the update-alternatives command, and extract the compressed file in the folder /usr/lib/jvm/ so the script will start ktools GUI with java version 8.</p>
<h4 align="left">Download</h4>
<p align="justify">Download ktools from github repository</p>
<p align="center"><img title="Download ktools from github repository" src="https://4.bp.blogspot.com/-0czqf_VQlAg/Ws_X-xd9eWI/AAAAAAAAAbs/zx7W_Y0UilIxyKIZdxf6Ta7yTOrvSeAvQCLcBGAs/s1600/install_2.png"></p>
<h4 align="left">Installation</h4>
<p align="justify">Once the script run the first time, a configuration file and menu entries will be create</p>
<p align="center"><img title="Ktools first run" src="https://4.bp.blogspot.com/-VuWXnb2Yeg8/Ws_X-6I7bgI/AAAAAAAAAbw/UmJ9Ags93SUTX1GqvIojlX-Q8pgxyVSqACLcBGAs/s1600/install_3.png">
</p>
<p align="center"><img title="Downloading and installing Ktools" src="https://2.bp.blogspot.com/-p9wPqAEBc_g/Ws_fvKXJmSI/AAAAAAAAAd4/7usLQVyUhIssDnbfaLVQEbG4_OJTqNd_QCLcBGAs/s1600/install_en.gif"></p>
<h4 align="left">Configuration</h4>
<p align="jsutify">Once the configuration file is created, the language is automatically detected and configured with the other options with the default values.</p>
<br>
<p align="justify">Options of the configuration file config.cfg of the script in python</p>
<p align="justify">
<pre>
[settings]
;language
lang = en
;create a symbolic link to execute the script and create the
;menu entries on the desktop and in the main menu
menu = 0
;database hash
dbhash = 40022da25ec234a94ced28da5a3208c0f0cea474f2424b193cdb606ea7189336
;it does a pause when tool information or tool list is showing,
;you must press enter to continue or q to exit
pausekey = 1
</pre>
</p>
<br>
<p align="center"><img title="Configuring menu option" src="https://4.bp.blogspot.com/-3BgHqO7RNY0/Ws_f3zLvf6I/AAAAAAAAAd8/YuZu_I_SODgkBdioH3oo64PpoJKaFwj3ACLcBGAs/s1600/config_en.gif"></p>
<br>
<p align="center"><img title="Configuring pausekey option" src="https://4.bp.blogspot.com/-Pmu_YP4VBOc/Ws_f_2r1KpI/AAAAAAAAAeA/uP5bYoK6AjUAGAzzqemkAM52LJLfLufBwCLcBGAs/s1600/config2_en.gif"></p>
<h4 align="left">Start</h4>
<p align="justify">Show help in the command line</p>
<p align="center">
<img title="Ktools" src="https://2.bp.blogspot.com/-hT8trSWtslc/Ws_X_RV97oI/AAAAAAAAAb0/3q9XDaBs4NARBKKptt4oisTKNaCezPzkACLcBGAs/s1600/install_4.png"></p>
<br>
<h3 align="center">Quick mode</h3><br>
<p align="justify">Shows information of categories and tools and then quit.</p>
<br>
<h4>Database update</h4>
<p align="justify">Verify if the database has been updated, and if any change is detected download and update the database file.</p>
<p align="center"><img title="update database" src="https://1.bp.blogspot.com/-k1InqIjxbQg/WtEa5oihlII/AAAAAAAAAj8/m0ooI_9NIbkZu-nD5cVkVP4Tdl94Qt53wCLcBGAs/s1600/quick_1.png" ></p>
<h4>Categories</h4>
<p align="justify">View tools in one or more categories by name.</p>
<p align="center"><img title="view categories by name" src="https://4.bp.blogspot.com/-H8ClVaBMPu4/WtEbjxx-7PI/AAAAAAAAAkE/NyEVGBWWU80zqYkwuEzDhKowevp1DjhZQCLcBGAs/s1600/quick_2.png" ></p>
<p align="justify">View tools in one or more categories by id.</p>
<p align="center"><img title="view a category by id" src="https://3.bp.blogspot.com/-qR6620J9WU8/WtEb4OigC2I/AAAAAAAAAkI/8ITYy05D53oQZ_KsJpny7GH7XRMV1yyBACLcBGAs/s1600/quick_3.png" ></p>
<h4>Tools</h4>
<p align="justify">View a tool by name.</p>
<p align="center"><img title="view a tool by name" src="https://3.bp.blogspot.com/-QT9d20WAzAs/WtEcpAgXfQI/AAAAAAAAAkU/-n4JsLX6vjA1r0ZY4ZTY692TD0yYNRE0wCLcBGAs/s1600/quick_4.png" ></p>
<p align="justify">View a tool by id.</p>
<p align="center"><img title="view a tool by id" src="https://1.bp.blogspot.com/-7glIWuB6Kdc/WtEczt5e7gI/AAAAAAAAAkY/piodKhVrzZIOesRxpham5Vq488n5Kt5MACLcBGAs/s1600/quick_5.png" ></p>
<h4>Lists</h4>
<p align="justify">View all categories.</p>
<p align="center"><img title="view all categories" src="https://1.bp.blogspot.com/-Dtl2j46rIL8/WuNYFa-MGaI/AAAAAAAAAoI/JYhucKhSC4MabJFIubDxe20zz1DSrTmWQCLcBGAs/s1600/quick_6.png" ></p>
<p align="justify">View all tools.</p>
<p align="center"><img title="view all tools" src="https://2.bp.blogspot.com/-2pJplDfJvTM/WuNYTIU5s0I/AAAAAAAAAoM/BnHKmX6fIGkSj_u4PD9_OULAJu8LCbk6ACLcBGAs/s1600/quick_7.png" ></p>
<h4>Search</h4>
<p align="justify">Search tools by name.</p>
<p align="center"><img title="search tools by name" src="https://2.bp.blogspot.com/-1CkZuDJ6Uk4/WtEe1VXEZYI/AAAAAAAAAk0/UO5tZQJ0h-sy86eRqaTGu6a757flLdcCgCLcBGAs/s1600/quick_8.png" ></p>
<p align="justify">Search tools by author.</p>
<p align="center"><img title="search tools by author" src="https://2.bp.blogspot.com/-3gy_V5U8sws/WuNYjPWoAsI/AAAAAAAAAoY/zfMYp9iBw0kLZhUjN_upyMgCqG1Rgl0cQCLcBGAs/s1600/quick_9.png" ></p>
<p align="justify">Search tools by content.</p>
<p align="center"><img title="search tools by content" src="https://4.bp.blogspot.com/-ix5rGOKuLpc/WuNYrqn8veI/AAAAAAAAAoc/vUV15GZ8WMwyhbNslVNBUWSzuI-Zr6VgwCLcBGAs/s1600/quick_10.png" ></p>
<br>
<h3 align="center">Shell mode</h3><br>
<p align="justify">It allows access to the different options of the tool through an interactive shell.</p>
<p>Start shell mode.</p>
<p align="center"><img title="ktools start shell mode" src="https://2.bp.blogspot.com/-PTDg2HhlxuA/WtEixhhavmI/AAAAAAAAAlo/jL7UmQfBD4A4onitgTqBYz_SWosPk5gbgCLcBGAs/s1600/shell_1.png" ></p>
<br>
<h4>Categories</h4>
<p align="justify">View tools in one or more categories by name.</p>
<p align="center"><img title="view categories by name" src="https://3.bp.blogspot.com/-SwFR2ga0hHw/WtEjkN8HCaI/AAAAAAAAAlw/AxzDgJHTl5o8hJ8MkBUAfXyFZMUlV-WiACLcBGAs/s1600/shell_2.png" ></p>
<p align="justify">View tools in one or more categories by id.</p>
<p align="center"><img title="view a category by id" src="https://1.bp.blogspot.com/-5NMKGN3BJcc/WtEjtT0GgRI/AAAAAAAAAl0/KhzuFDKmoBwD7o2k5wb-T6bNPAFnPM4YwCLcBGAs/s1600/shell_3.png" ></p>
<h4>Tools</h4>
<p align="justify">View a tool by name.</p>
<p align="center"><img title="view a tool by name" src="https://1.bp.blogspot.com/-6mrslcSacSk/WtEkM-6SrXI/AAAAAAAAAl8/CilGB0lXMEYj7QRn_ACkUxsfO9k1bbxMACLcBGAs/s1600/shell_4.png" ></p>
<p align="justify">View a tool by id.</p>
<p align="center"><img title="view a tool by id" src="https://1.bp.blogspot.com/-Gt_EvsGyY-I/WtEkX49HnjI/AAAAAAAAAmE/y3_cO-aNkuskTYvgz_uX_BOt59FcXQtpACLcBGAs/s1600/shell_5.png" ></p>
<h4>Show</h4>
<p align="justify">View all categories.</p>
<p align="center"><img title="view all categories" src="https://1.bp.blogspot.com/-_oACbz5NjMw/WtEkx7NGjOI/AAAAAAAAAmM/dQYSbLt132wBN6KuArKarYkSbETsMzXkQCLcBGAs/s1600/shell_6.png" ></p>
<p align="justify">View all tools.</p>
<p align="center"><img title="view all tools" src="https://2.bp.blogspot.com/-j357nPpzr2E/WtEk7c_JnRI/AAAAAAAAAmU/SyDNDEmgX-0xc7yVg2E1IRCWR293NREiwCLcBGAs/s1600/shell_7.png" ></p>
<h4>Search</h4>
<p align="justify">Search tools by name.</p>
<p align="center"><img title="search by name" src="https://2.bp.blogspot.com/-_PgqF-XQOpk/WtElYtRul5I/AAAAAAAAAmc/78Tu_dOoHA8vmL6J6TXasWiWcp2FasZigCLcBGAs/s1600/shell_8.png" ></p>
<p align="justify">Search tools by author.</p>
<p align="center"><img title="search by author" src="https://1.bp.blogspot.com/-sXwvM_OP2NA/WtElmYi33MI/AAAAAAAAAmk/hvAjSksv0Coy6knQP2EWkDuiijk7eX9ewCLcBGAs/s1600/shell_9.png" ></p>
<p align="justify">Search tools by content.</p>
<p align="center"><img title="search by content" src="https://3.bp.blogspot.com/-ARilG1Cjc7U/WtElwYJ3z-I/AAAAAAAAAmo/I_4V4OkrJwkI1Nt65LNTgURGq_2aXjbWgCLcBGAs/s1600/shell_10.png" ></p>
<br>
<h3 align="center">GUI</h3><br>
<p align="justify">The GUI in version 0.2 was written in Javafx, and allows access to help contents through a graphical interface, has new features such as saving the settings selected by the user in the graphical interface in the configuration file.</p>
<br>
<h4>Configuration</h4>
<p align="justify">Once the java application is executed for the first time, the configuration file is created which has options such as language, which is automatically detected along with the other options that take their default values.</p>
<p>Options of the configuration file ktoolsGui.properties of the graphical interface.</p>
<p align="justify">
<pre>
#ktoolGui settings
#database hash, is generated automatically
#when database changes
dbhash=6E49C321CF30D7D9E2855B921D7B4FD496F69363B5511AE4013649CF020BE7FB
#search on key pressed true or false
search=true
#check the author search option or name or content at the start
#of the application, 1=author 2=name 3=content
searchby=1
#Language spanish or english lang=es or en
lang=en
</pre>
</p>
<h4>Start</h4>
<p align="justify">Run ktools GUI.</p>
<p align="center"><img title="start ktools GUI" src="https://2.bp.blogspot.com/-oMlOSDjDEMg/WtEneuGFMxI/AAAAAAAAAnA/YXonAi6SCXQ3QEc1dtfjNb2_MT9xSdBTwCLcBGAs/s1600/GUI.png" ></p>
<p align="center"><img title="ktool GUI" src="https://2.bp.blogspot.com/-7auM9Q1r--E/Wv4Bjsp4lPI/AAAAAAAAAq8/FUmL4pSjYHMI9XRBTVsg1MsPEknEZUYegCLcBGAs/s1600/guien.png" ></p>
<h4>Ktools blog</h4>
<p align="justify"><a title="Ktools linux blog" href="https://ktools-linux-en.blogspot.com">https://ktools-linux-en.blogspot.com</a></p>
<h4>Youtube channel</h4>
<p align="justify"><a title="Ktools linux on youtube" href="https://www.youtube.com/channel/UCdx8zgVHSHCwsy5tRpYW8JA">https://www.youtube.com/channel/UCdx8zgVHSHCwsy5tRpYW8JA</a></p>

