#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sqlite3, sys, logging, re, json, cmd, traceback, hashlib, binascii, ConfigParser, importlib, subprocess, pwd, urllib2
from datetime import datetime
from stat import *
from traceback import print_exc

class ktools:

	path_	 = os.path.abspath( sys.argv[0] )
	dbFile   = "tools.db"
	logFile  = "ktools.log"
	confFile = "config.cfg"
	version  = 0.2
	lang     = None
	locale   = None
	paintc	 = "\x1b["
	pEnd	 = "\x1b[0m"
	bold	 = paintc+"1m"
	logger   = None
	ln       = "/usr/local/bin/ktools"
	propmt   = None	
	id_lang  = None
	isCmd    = False
	data     = None
	dbHash   = ""
	menu     = None
	desktop  = None
	pausekey = None
	linesPr  = 0
	content  = None
			
	def __init__( self ):

		try:
		
			self.path_    = "/"+self.path_[1:-len( "ktools.py" )]
			self.dbFile   = self.path_ + self.dbFile
			self.logFile  = self.path_ + self.logFile
			self.confFile = self.path_ + self.confFile
			self.lang     = "es" if "es" in os.getenv( "LANG" ) else "en"

			logging.basicConfig( filename=self.logFile, level=logging.ERROR )
			self.logger = logging.getLogger( "ktools" )
			
			if not os.path.exists( self.dbFile ):
				
				self.loadLang()
				ask = raw_input( self.locale["asks"]["adb"] )
				
				if ask == self.locale["asks"]["yes"]:
					
					self.downloadDb()
					self.logger.error( str( datetime.now() ) + ":" + self.locale["titles"]["dbdnw"] )
					self.initConfiguration()
				
				else:
				
					exit()	
			
			else:
				
				self.initConfiguration()

		except Exception as ex:

			self.printException( ex )
			
	def initConfiguration( self ):
		
		self.verifyConfigFile()	
		self.loadLang()
		self.getData()
				
		if self.menu == "1":
				
			self.createSymlinkMenu()

		else:
				
			self.deleteSymlinkMenu()
						
		self.initArgs()
			
	def downloadDb( self ):
	
		dbnew = urllib2.urlopen( "https://github.com/f0rk1/ktools-linux/blob/master/tools.db?raw=true" )
		data = dbnew.read()
					
		if data != None:		
		
			db = open( self.dbFile, "w" )
			db.write( data )	
			db.close()
			
		else:
			
			raise Exception( self.locale["updatedb"][3] )	
			
			
	def loadLang( self ):
	
		if self.lang == "es":

			if os.path.exists( self.path_+"locale/es.json" ):

				self.locale  = json.load( open( self.path_+"locale/es.json", "r" ) )
				self.id_lang = 2

			else:

				raise Exception( "Json file not found" )

		else:

			if os.path.exists( self.path_+"locale/en.json" ):

				self.locale  = json.load( open( self.path_+"locale/en.json","r" ) )
				self.id_lang = 1

			else:

				raise Exception( "Json file not found" )
			
	def verifyConfigFile( self ):
	
		self.loadLang()
		
		if not os.path.exists( self.confFile ):
			
			self.createConfigFile()
			self.logger.error( str( datetime.now() ) + ":" + self.locale["conffile"][0] )
				
		Config = ConfigParser.ConfigParser()
		Config.read( self.confFile )				

		if Config.has_section( "settings" ):

			if len( Config.options( "settings" ) ) == 0 or len( Config.options( "settings" ) ) < 4:
								
				self.createConfigFile()
				self.logger.error( str( datetime.now() ) + ":" + self.locale["conffile"][1] )
				self.verifyConfigFile()
				return False
					
			fields = {}
	
			if Config.has_option( "settings", "lang" ):
					
				opt = Config.get( "settings", "lang" )
						
				if not opt == "":

					if re.match( "^(es|en)$", opt ):

						self.lang = opt
									
					else:
									
						fields["lang"] = self.lang										
				
				else:
					
					fields["lang"] = self.lang
			
			else:
				
				fields["lang"] = self.lang

				
			if Config.has_option( "settings", "dbhash" ):

				hashDb = Config.get( "settings", "dbhash" )
						
				if not hashDb == "":
						
					h = hashlib.sha256( open( self.dbFile, 'rb' ).read() ).hexdigest()
					
					if hashDb == h:
							
						self.dbHash = hashDb
					
					else:	
							
						self.dbHash = h	
						fields["dbhash"] = self.dbHash
						self.logger.error( str(datetime.now() ) + ":" + self.locale["conffile"][2] )
						
				else:
						
					self.dbHash = hashlib.sha256( open( self.dbFile, 'rb' ).read() ).hexdigest()
					fields["dbhash"] = self.dbHash
					
			else:
				
				self.dbHash = hashlib.sha256( open( self.dbFile, 'rb' ).read() ).hexdigest()
				fields["dbhash"] = self.dbHash

			if Config.has_option( "settings", "menu" ):

				menu = Config.get( "settings", "menu" )
							
				if re.match( "^[0-1]$", menu ) == None:

					fields["menu"] = 1
					self.menu = 1		

				else:

					self.menu = menu		
							
			else:	

				fields["menu"] = 1
				self.menu = 1
				
			if Config.has_option( "settings", "pausekey" ):

				pausekey = Config.get( "settings", "pausekey" )
							
				if re.match( "^[0-1]$", pausekey ) == None:

					fields["pausekey"] = 1
					self.pausekey = 1

				else:

					self.pausekey = int( pausekey )		
							
			else:	

				fields["pausekey"] = 1	
				self.pausekey = 1							
						
			if len( fields ) > 0:

				for f in fields:
									
					Config.set( "settings", f, fields[f] )											
						
				Config.write( open( self.confFile, "w" ) )
				self.logger.error( str( datetime.now() ) + ":" + self.locale["conffile"][1] )	
			
		else:

			self.createConfigFile()
			self.logger.error( str( datetime.now() ) + ":" + self.locale["conffile"][1] )
			self.verifyConfigFile()
				
	def createConfigFile( self ):
	
		Config  = ConfigParser.ConfigParser( allow_no_value = True )
		self.dbHash = hashlib.sha256( open( self.dbFile, 'rb' ).read() ).hexdigest()
				
		Config.add_section( "settings" )
		
		Config.set( "settings", self.locale["conffile"][3]["lang"] )
		Config.set( "settings", "lang", self.lang )			
		Config.set( "settings", self.locale["conffile"][3]["menu"].encode( "utf-8" ) )
		Config.set( "settings", "menu", 1 )
		Config.set( "settings", self.locale["conffile"][3]["dbhash"].encode( "utf-8" ) )
		Config.set( "settings", "dbhash", self.dbHash )
		Config.set( "settings", self.locale["conffile"][3]["pausekey"].encode( "utf-8" ) )
		Config.set( "settings", "pausekey", 1 )			
		Config.write( open( self.confFile, "w" ) )							

	def initArgs( self ):
	
		try:
		
			self.printHeader()

			if len( sys.argv ) == 1:
			
				kcmd = None

				if os.path.exists( self.path_ + "libs/" + self.lang.lower() + ".py" ):

					kcmd = importlib.import_module( "libs." + self.lang.lower() )

				else:
				
					raise Exception( "Missing module" )
					
				if "module" in str( type( kcmd ) ):
				
					self.isCmd  = True		
					self.prompt = kcmd.mycmd()
					self.prompt.set_instance( self ) 
					self.prompt.prompt = self.paintc + "2m ktools> " + self.pEnd
					self.prompt.cmdloop()		
			
			else:
			
				for a in range( 1, len( sys.argv ) ):

					if re.search( "[\=\/\%\;\']", sys.argv[a] ) != None:
					
						self.printHelp()
						return False		

				if sys.argv[1] == self.locale["args"]["help"][0] or sys.argv[1] == self.locale["args"]["help"][1]:
				
					self.printHelp()
			
				elif sys.argv[1] == self.locale["args"]["category"][0] or sys.argv[1] == self.locale["args"]["category"][1]:
				
					if len( sys.argv ) == 3:
					
						self.printCategoryTools( str( sys.argv[2] ) )

					else:	
				
						self.printHelp()
					
				elif sys.argv[1] == self.locale["args"]["search"][0] or sys.argv[1] == self.locale["args"]["search"][1]:
			
					if len( sys.argv ) == 3:
				
						self.search( str( sys.argv[2] ) )					
					
					else:
				
						self.printHelp()
		
				elif sys.argv[1] == self.locale["args"]["tool"][0] or sys.argv[1] == self.locale["args"]["tool"][1]:					
				
					if len(sys.argv) == 3:
						
						self.printToolHelp( str( sys.argv[2] ).lower() )
					
					else:
				
						self.printHelp()		
					
				elif sys.argv[1] == self.locale["args"]["listc"][0] or sys.argv[1] == self.locale["args"]["listc"][1]:
			
					self.printCategories()			
			
				elif sys.argv[1] == self.locale["args"]["listt"][0] or sys.argv[1] == self.locale["args"]["listt"][1]:
			
					self.printTools()

				elif sys.argv[1] == self.locale["args"]["gui"][0] or sys.argv[1] == self.locale["args"]["gui"][1]:
	
					jarPath = self.path_+"ktools.jar"

					if os.path.exists(jarPath):
				
						os.system( "java -jar " + jarPath )
					
					else:
					
						raise Exception ( jarPath + " not found" )
						
				elif sys.argv[1] == self.locale["args"]["uptdb"][0] or sys.argv[1] == self.locale["args"]["uptdb"][1]:
				
					self.updateDb()

				else:

					self.printHelp()
					
		except Exception as ex:	
		
			self.printException( ex )
			exit()
			
	def createSymlinkMenu( self ):

		logo      = "/usr/share/icons/gnome/256x256/apps/ktools.png"		
		menuname  = "ktools.desktop"
		menunameg = "ktools GUI.desktop"
		menudesk  = pwd.getpwnam( os.getlogin() )[5] + "/"
		menuitem  = '#!usr/bin/env xdg-open\n[Desktop Entry]\nType=Application\nTerminal=true\nExec=ktools\nName=Ktools\nComment[es]=Colección contenidos de ayuda herramientas Kali Linux\nComment[en]=Collection of help content of Kali Linux tools\nIcon=' + logo + '\nCategories=Ktools'
		menuitemg = '#!usr/bin/env xdg-open\n[Desktop Entry]\nType=Application\nTerminal=true\nExec=ktools -g\nName=Ktools GUI\nComment[es]=Ktools GUI\nComment[en]=Ktools GUI\nIcon=' + logo + '\nCategories=Ktools'
		menupath  = ""
		newm      = {}
		modifym   = {}

		if os.path.exists( menudesk+ "/.local/share/applications/" ):
			
			menupath = menudesk + "/.local/share/applications/"

		elif os.path.exists( "/usr/local/share/applications/" ):
			
			menupath = "/usr/local/share/applications/"

		elif os.path.exists( "/usr/share/applications/" ):
			
			menupath = "/usr/share/applications/"

		menufile  = menupath + menuname
		menufileg = menupath + menunameg
		
		for f in self.locale["titles"]["desktop"]:
												
			if os.path.exists( menudesk + f ):
					
				menudesk = menudesk + f + "/"
				
		menud = menudesk + menuname
		menudg = menudesk + menunameg

		self.createSymlink()		
		
		if not os.path.exists( menufile ):
		
			newm["menu"] = { "path": menufile, "name": menuname, "content": menuitem, "type": "menu" }
			
		else:
		
			if open( menufile, "r" ).read() != menuitem:
			
				modifym["menu"] = { "path": menufile, "name": menuname, "content": menuitem, "type": "menu" }
					
		if not os.path.exists( menud ):
		
			newm["menud"] = { "path": menud, "name": menuname, "content": menuitem.replace( "Categories=Applications","" ), "type": "desktop" }	
			
		else:
		
			if open( menud ,"r" ).read() != menuitem.replace( "Categories=Applications","" ):
				
				modifym["menud"] = { "path": menud, "name": menuname, "content": menuitem.replace( "Categories=Applications","" ), "type": "desktop" }	
					
		
		if not os.path.exists( menufileg ):
		
			newm["menug"] = { "path": menufileg, "name": menunameg, "content": menuitemg, "type": "menu" }
		
		else:
		
			if open( menufileg, "r" ).read() != menuitemg:
			
				modifym["menug"] = { "path": menufileg, "name": menunameg, "content": menuitemg, "type": "menu" }
				
		if not os.path.exists( menudg ):
		
			newm["menudg"] = { "path": menudg, "name": menunameg, "content": menuitemg.replace( "Categories=Applications","" ), "type": "desktop" }	
			
		else:
		
			if open( menudg ,"r" ).read() != menuitemg.replace( "Categories=Applications","" ):
				
				modifym["menudg"] = { "path": menudg, "name": menunameg, "content": menuitemg.replace( "Categories=Applications","" ), "type": "desktop" }			
		
		if len(newm) > 0:
		
		
			ask = raw_input( unicode( self.locale["asks"]["amenu"] ).encode( "utf-8" ) )
				
			if ask.lower() == unicode( self.locale["asks"]["yes"] ).encode( "utf-8" ):
			
				if self.isRoot():
				
					self.checkLogo()

					for a in newm:

						open( newm[a]["path"], "w" ).write( newm[a]["content"] ) 
						
						if newm[a]["type"] == "desktop":
						
							os.chown( newm[a]["path"], pwd.getpwnam(os.getlogin())[2], pwd.getpwnam(os.getlogin())[3] )
		
		if len(modifym) > 0:
		
		
			ask = raw_input( unicode( self.locale["asks"]["amenur"] ).encode( "utf-8" ) )
				
			if ask.lower() == unicode( self.locale["asks"]["yes"] ).encode( "utf-8" ):

				if self.isRoot():
				
					self.checkLogo()

					for a in modifym:
				
						os.remove( modifym[a]["path"] ) 					
						open( modifym[a]["path"], "w" ).write( modifym[a]["content"] )
						
						if modifym[a]["type"] == "desktop":
							
							os.chown( modifym[a]["path"], pwd.getpwnam( os.getlogin() )[2], pwd.getpwnam( os.getlogin() )[3] )
		
	def createSymlink( self ):
	
		s     = os.path.abspath( __file__ ).replace( " ", "\\ " )
		fcnt  = '#!/bin/bash\n\nif [ $# -eq 0 ]; then\n\tpython ' + s + '\nelse\n\tpython ' + s + ' "$@"\nfi\nexit'
		
		if not os.path.exists( self.ln ):
		
			ask = raw_input( unicode( self.locale["asks"]["asym"] ).encode( "utf-8" ) )
				
			if ask.lower() == unicode( self.locale["asks"]["yes"] ).encode( "utf-8" ):
			
				if self.isRoot():
						
					open( self.ln,"w" ).write( fcnt )
			
					os.chmod( self.ln, 0o755 )
					os.chown( self.ln, pwd.getpwnam( 'root' )[2], pwd.getpwnam( 'root' )[3] )
	
		else:

			if open( self.ln , "r" ).read() != fcnt:
				
				ask = raw_input( unicode( self.locale["asks"]["asymr"] ).encode( "utf-8" ) )
				
				if ask.lower() == unicode( self.locale["asks"]["yes"] ).encode( "utf-8" ):
			
					if self.isRoot():
			
						os.remove( self.ln )
						open( self.ln,"w" ).write( fcnt )
			
						os.chmod( self.ln, 0o755 )
						os.chown( self.ln, pwd.getpwnam( 'root' )[2], pwd.getpwnam( 'root' )[3] )
		
	def checkLogo( self ):			
		
		lpath = "/usr/share/icons/gnome/256x256/apps/ktools.png"
		kpath = self.path_ + "img/ktools.png"
		
		if not os.path.exists( lpath ):

			if not os.path.exists( kpath ):
			
				raise Exception( "Image not found" )
				
			else:
				
				with open( kpath, "r" ) as src, open( lpath, "w" ) as dst: dst.write( src.read() )
				
		else:
			

			if open( lpath, "r" ).read() != open( kpath, "r" ).read():
				
				os.remove( lpath )				
				with open( kpath, "r" ) as src, open( lpath, "w" ) as dst: dst.write( src.read() )

	def deleteSymlinkMenu( self ):
		
		logo      = "/usr/share/icons/gnome/256x256/apps/ktools.png"		
		menuname  = "ktools.desktop"
		menunameg = "ktools GUI.desktop"
		menudesk  = pwd.getpwnam( os.getlogin() )[5] + "/"
		menupath  = ""


		if os.path.exists( menudesk+ "/.local/share/applications/" ):
			
			menupath = menudesk + "/.local/share/applications/"

		elif os.path.exists( "/usr/local/share/applications/" ):
			
			menupath = "/usr/local/share/applications/"

		elif os.path.exists( "/usr/share/applications/" ):
			
			menupath = "/usr/share/applications/"

		menufile  = menupath + menuname
		menufileg = menupath + menunameg
		
		for f in self.locale["titles"]["desktop"]:
												
			if os.path.exists( menudesk + f ):
					
				menudesk = menudesk + f + "/"
				
		menud = menudesk + menuname
		menudg = menudesk + menunameg
			
		if os.path.exists( menufile ) or os.path.exists( menufileg ) or os.path.exists( menud ) or os.path.exists( menudg ):
			
			ask = raw_input( unicode( self.locale["asks"]["asymd"] ).encode( "utf-8" ) )
				
			if ask.lower() == unicode( self.locale["asks"]["yes"] ).encode( "utf-8" ):
			
				if self.isRoot():
				
					if os.path.exists( menufile ):
			
						os.remove( menufile )
					
					if os.path.exists( menufileg ):
			
						os.remove( menufileg )
				
					if os.path.exists( menud ):
			
						os.remove( menud )
				
					if os.path.exists( menudg ):
			
						os.remove( menudg )				

	def isRoot( self ):

		if os.getuid() != 0:
			
			raise Exception( self.locale["rootaccess"] ) 

		else:
		
			return True		
	
	def getData( self ):
		
		self.data  = {}
		categories = self.query( "SELECT id_category,name FROM category_lang WHERE id_lang=:a;", { 'a':self.id_lang }, True )
		
		for row in categories:
                        
                                tools = self.query( "SELECT tool.id_tool,tool.name FROM tool_reference INNER JOIN tool ON tool_reference.id_tool=tool.id_tool WHERE tool_reference.id_category=:b ORDER BY tool.name ASC;", { 'b':row[0] }, True )
                                d = {}   
                                   
                                for t in tools:
                                
                                        d[str( t[0] )] = t[1]
     
                                c={}
                                c[row[1]]=d
                                self.data[row[0]] = c
 			
	def printException( self, ex ):

		if not self.locale == None:
		
			print ( self.locale["exception"] ) 

		print ( str( ex ) )
				
		if not self.logger == None:
				
			self.logger.error( str( datetime.now() ) + ":" + str( ex ) )

		print_exc()

	def reset( self ):
		
		os.system( "clear" )
				
	def printHeader( self ):
		
		self.reset()
		version = "v " + str( self.version )
		author  = self.locale["authorby"] + self.locale["author"]
		
		color = self.paintc+"96m"

		print ( "\t"+color+"******************************************"+self.pEnd )
		print ( "\t"+color+"*   _   __                               *"+self.pEnd )
		print ( "\t"+color+"*  | | / /   _                 _         *"+self.pEnd )
		print ( "\t"+color+"*  | |/ /  _| |_   _      _   | | ____   *"+self.pEnd )
		print ( "\t"+color+"*  |  _ \ (_   _)/ _ \  / _ \ | |/  __)  *"+self.pEnd )
		print ( "\t"+color+"*  | | \ \  | | ( (_) )( (_) )| |\___ \  *"+self.pEnd )    
		print ( "\t"+color+"*  |_|  \_\ |_|  \ _ /  \ _ / |_|(____/  *"+self.pEnd )
		print ( "\t"+color+"*                                        *"+self.pEnd )
		print ( "\t"+color+"******************************************"+self.pEnd )
		print ( "\t"+color+"*  "+author+"                "+version+"  *"+self.pEnd )
		print ( "\t"+color+"******************************************"+self.pEnd )
	
	def printHelp( self ):
	
		for a in self.locale["usage"]:
		
			print ( a.replace( "[b]", self.bold ).replace( "[/b]", self.pEnd ) ) 
			
	def dbConnect( self ):
	
		dbConn = sqlite3.connect( self.dbFile )
		dbConn.text_factory = str
		return dbConn
		
	def query( self, statement, value, showMsg ):
		
		try:
	
			dbConn = self.dbConnect()	
			dbConn.text_factory = str
			c = dbConn.cursor()
			
			rows = ""
		
			if len( statement ) > 0:

				if value != None:
				
					c.execute( statement, value )
					
				else:
				
					c.execute( statement )	
				
				Rows = c.fetchall()

				if len( Rows ) > 0:
					
					rows = Rows
					
				else:
				
					if showMsg:
						
						print ( "\n" + self.bold + self.locale["notFound"] + self.pEnd + "\n" )
						
					rows = False
				
			else:
			
				rows = False
			
			dbConn.close()
			
			del dbConn, c
			
			return rows	
				
		except Exception as ex:
		
			self.printException( ex )
			
	def updateDb( self ):
	
		try:
		
			dbver  = urllib2.urlopen( "https://raw.githubusercontent.com/f0rk1/ktools-linux/master/ver/test" )
			dbgith = dbver.read()
			dbgith = dbgith[:-1] if dbgith.endswith( "" ) else dbgith
			dbhash = self.dbHash
			dbver.close()

			if re.match( "[a-zA-Z0-9]", dbgith ) != None:

				if dbhash != dbgith:
				
					dbnew = urllib2.urlopen( "https://github.com/f0rk1/ktools-linux/blob/master/tools.db?raw=true" )
					data = dbnew.read()
					
					if data != None:
					
						index = 0
					
						for a,b,c in os.walk( self.path_ ):

							if "tools.db.old." in "".join( [z for z in c] ):

								for d in c:
								
									if "tools.db.old." in d:
											
										tmp =  d.replace( "tools.db.old.", "" ) 

										if re.match( "[0-9]", tmp ):

											index =  int( tmp ) + 1
										
						dbn = open( "temp.db", "w" )
						dbn.write( data )
						dbn.close()
						dbnew.close()
						
						os.rename( self.dbFile, self.dbFile + ".old." + str( index ) )
						os.rename( "temp.db", self.dbFile )
						print ( self.locale["updatedb"][0] )
						self.logger.error( str( datetime.now() ) + ":" + self.locale["updatedb"][0][1:] )
						
						self.dbHash = hashlib.sha256( open( self.dbFile, 'rb' ).read() ).hexdigest()
						
						Config = ConfigParser.ConfigParser()
						Config.read( self.confFile )		
						Config.set( "settings", "dbhash", self.dbHash )											
						Config.write( open( self.confFile, "w" ) )
						

				else:
				
					print ( self.locale["updatedb"][1] )
					
			else:
				
				print ( self.locale["updatedb"][2] )
				
		except Exception as ex:
								
			self.printException( ex )
			exit()
	
	def printLists( self, lists ):
	
		maxLen = 5
		lines, cols = subprocess.check_output( ["stty", "size"] ).decode().split()
		cols  = int( cols )
		lines = int( lines )
		n     = 1
				
		if cols <= 100:
                        
                	n = 2
                                
		elif cols > 100 and cols <= 150:                             
                        
                	n = 3
                                
		else:     

			n = 4   

		if 'list' in str( type( lists ) ):
		
			if 'int' in str( type( n ) ):
					
				if n <= maxLen:
			
					l = len( lists )
					
					if l >= n:
					
						m = l%n
						j = l-m
						line = ''
						
						for v in range( 0, j, n ):
							
							k = v + n
							
							for a in range( v, k ):
																
								line += '{:<35}'.format( str( lists[a][0].title() ).title() )

							print ( "\t\x1b[m" + line + self.pEnd )
							line = ''
							self.linesPr += 1

						if m > 0:

							for i in range( j, l ):

								if i == j:

									line += '\t{:<35}'.format( str(lists[i][0]).title() )

								else:

									line += '{:<35}'.format( str( lists[i][0] ).title() )

							print ( line )
							line = ''
							self.linesPr += 1

					elif l < n:

						for a in range( 0, l ):
        
							print ( '\t{:<35}'.format( str( lists[a][0]).title() ) )
							self.linesPr += 1

					elif l == 1:
						
						print ( '\t{:<35}'.format( str( lists[0][0] ).title() ) + "\n\n" )
						self.linesPr += 1
							
				else:
						
					raise Exception( "max columns 5" )
						
		print ( "\n\n" 	)

	def search( self, argv ):
	
		arg        = str( argv.lower() )
		searchType = 0
		rows       = False

		print ( self.bold + self.locale["titles"]["tool"] + self.pEnd )

		if re.match( "^(" + self.locale["commandKeyword"]["author"] + "\:)+[\w\-]{2,80}$", argv ):

			arg =  arg.replace( str( self.locale["commandKeyword"]["author"] + ":" ), "" )
			rows = self.query( "SELECT (id_tool||'. '||name)as n FROM tool WHERE author LIKE :a ORDER BY name ASC", { 'a':'%'+arg+'%' }, False )
			print ( self.locale["search"]["author"] + arg + "'\n\n" )
			
		elif re.match( "^(" + self.locale["commandKeyword"]["name"] + "\:)+[\w\-]{2,80}$", argv ) or re.match( "^[\w\-]{2,80}$", argv ):

			arg = arg.replace( str( self.locale["commandKeyword"]["name"] + ":" ), "" )
			rows = self.query( "SELECT DISTINCT (id_tool||'. '||name)as n FROM tool WHERE name LIKE :a ORDER BY name ASC", { 'a':'%'+arg+'%' }, False )
			searchType = 2
			print ( self.locale["search"]["name"] + arg + "'\n\n" )
			
		elif re.match( "^(" + self.locale["commandKeyword"]["content"] + "\:)+[\w\-]{2,80}$", argv ):

			arg = arg.replace( str( self.locale["commandKeyword"]["content"] + ":" ), "" )
			self.content = arg
			rows = self.query( "SELECT DISTINCT (tool.id_tool||'. '||tool.name)as n FROM tool INNER JOIN tool_lang ON tool.id_tool=tool_lang.id_tool WHERE tool_lang.description LIKE :a OR tool_lang.usage LIKE :a AND tool_lang.id_lang=:l ORDER BY tool.name ASC", { 'a':'%'+arg+'%', 'l':self.id_lang }, False )
			print ( self.locale["search"]["content"] + arg + "'\n\n" )
				
		if rows != False:
		
			ids = []
			index  = 0

			for a in rows:
				ids.insert( index, a[0].split(". ")[0] )
				index += 1
		
			del arg	
			self.printLists( rows )
			
			id_ = raw_input( unicode( self.locale["asks"]["atool"] ).encode( "utf-8" ) )
			
			if id_.isdigit():
			
				if id_ in ids:
				
					self.printHeader()
					self.printToolHelp( "id:" + id_ )
					
				else:
				
					if id_ != "0":
				
						ans = raw_input( self.locale[ "asks" ][ "asearch" ].encode( "utf-8" ) )

						if ans == self.locale[ "asks" ][ "yes" ]:
					
							self.printHeader()
							self.printToolHelp( "id:" + id_ )												
		        
			else:

				print ( self.locale["nEx"] )                

		elif os.path.exists( "/usr/bin/" + arg ) or os.path.exists( "/usr/sbin/" + arg ) or os.path.exists( "/sbin/" + arg ) or os.path.exists( "/bin/" + arg ) and searchType == 2:

			print ( self.locale["asks"]["ahelpman"] )
				
			see = raw_input( unicode( self.locale["asks"]["ahelp"] ).encode( "utf-8" ) )
				
			if see == unicode( self.locale["asks"]["yes"] ).encode( "utf-8" ):
				
				os.system( "man " + arg )

		else:
			
			print ( self.bold + self.locale["notFound"] + self.pEnd + "\n" )
		
	def printCategories( self ):
	
		if self.data == None:
		
			self.getData()
			
	
		if len(self.data) > 0:
	        
			print ( self.bold + self.locale["titles"]["categories"] + self.pEnd )

			for a in self.data.keys():
	                
				print ( "\t   |__ " + str(a)+ ". " + self.data[a].keys()[0].capitalize() )
	                        
			print ( "\n" )
	
			id_ = raw_input( unicode( self.locale["asks"]["acategory"] ).encode( "utf-8" ) )		
			
			if id_.isdigit():
			
				if id_ != "0":	
				
				        self.printHeader()
				        self.printCategoryTools( "id:" + str( id_ ) )
					
			else:
				
				print ( self.locale["nEx"] )	     
				
		else:
                        
			print ( "\n" + self.bold + self.locale["notFound"] + self.pEnd + "\n" )
				
	def printCategoryTools( self, pattern ):
        
		rows    = False
		printBy = 0
		val     = None
		isFound = False
		
		if self.data == None:
		
			self.getData()
			
		if re.match( "^(" + self.locale["commandKeyword"]["name"] + "\:)+[\D\W\s]{2,100}$", pattern ) or re.match( "^[\D\W\s]{2,100}$", pattern ):
		
			printBy = 1
			val = str( pattern.replace( str( self.locale["commandKeyword"]["name"] + ":" ), "" ) )
		
		elif re.match( "^(" + self.locale["commandKeyword"]["id"] + "\:)+[0-9]{1,}$", pattern ) or re.match( "^[0-9]{1,}$", pattern ):
		
			printBy = 2
			val = int( pattern.replace( str( self.locale["commandKeyword"]["id"] + ":" ), "" ) )

		else:
		
			if not self.isCmd:
			
				self.printHelp()
				return False

		if printBy == 1 :
			
			for a in self.data.keys():
				
				if val in self.data[a].keys()[0]:

					print ( "\n" + self.bold + "\t" + str(a) + ". "+ str(self.data[a].keys()[0]).capitalize() + self.pEnd + "\n\n" )
					
					d = self.data[a].values()
					toolsSorted = sorted( d[0].values() )
					rows= ([])
			
					for t in toolsSorted:
				
						for b in d[0].keys(): 
						
							if t == d[0][b] :
				
								rows.append( ( str( b ) + ". " + d[0][b], ) )

					self.printLists( rows )
			
		if printBy == 2 :
			
			for a in self.data.keys():
				
				if a == val:
				
					print ( "\n" + self.bold + "\t" + str(a) + ". " + str(self.data[a].keys()[0]).capitalize() + self.pEnd + "\n\n" )
					
					d = self.data[a].values()
					toolsSorted = sorted( d[0].values() )
					rows= ([])
			
					for t in toolsSorted:
				
						for b in d[0].keys(): 
						
							if t == d[0][b] :
				
								rows.append( ( str( b ) + ". " + d[0][b], ) )

					self.printLists( rows )
			        		
		if rows !=  False:
		
			ids = []
			index = 0
			
			for a in rows:
			
				ids.insert( index, a[0].split( ". " )[0] )
				index += 1
				
			id_ = raw_input( unicode( self.locale["asks"]["atool"] ).encode( "utf-8" ) )

			if id_.isdigit():
			
				if id_ in ids:
				
					self.printHeader()
					self.printToolHelp( "id:" + id_ )
					
				else:	
				
					if id_ != "0":
				
						ans = raw_input( self.locale[ "asks" ][ "asearch" ].encode( "utf-8" ) )
					
						if ans == self.locale[ "asks" ][ "yes" ]:
					
							self.printHeader()
							self.printToolHelp( "id:" + id_ )
				
			else:
				
				print ( self.locale["nEx"] )					
				    
		else:
		
			print ( "\n" + self.bold + self.locale["notFound"] + self.pEnd + "\n" )
				    
	def printTools( self ):
	
		if self.data == None:
		
			self.getData()

		print ( "\n" + self.bold + self.locale["titles"]["tool"] + self.pEnd + "\n" )
                
		for a in self.data.keys():

			print ( self.bold + "\t" + str( a ) + ". " + self.data[a].keys()[0].capitalize() + self.pEnd + "\n" )

			d = self.data[a].values()
			toolsSorted = sorted( d[0].values() )
			rows= ([])

			for t in toolsSorted:

				for b in d[0].keys(): 

					if t == d[0][b] :

						rows.append( ( str( b ) + ". " + d[0][b], ) )

			self.printLists( rows )     
			
			if self.pausekey == 1:
			
				res = raw_input( "" )
				
				if res == "q" or res == "Q":
					
					return
		        
		id_ = raw_input( unicode( self.locale["asks"]["atool"] ).encode( "utf-8" ) )
		
		if id_.isdigit():
			
			if id_ != "0":
				
				self.printHeader()
				self.printToolHelp( "id:" + id_ )				
				
		else:
			
			print ( self.locale["nEx"] )

	def printToolHelp( self, pattern ):			

		rowsC = False
		row   = False
		name  = None
		id    = None
		self.linesPr = 0

		if re.match( "^(" + self.locale["commandKeyword"]["id"] + "\:)+[\d]{1,}$", pattern ) or re.match( "^[\d]{1,}$", pattern ):

			id = pattern.replace( self.locale["commandKeyword"]["id"] + ":", "" )
			
			rowsC = self.query( "SELECT category.id_category,category_lang.name FROM category_lang INNER JOIN(category INNER JOIN(tool_reference INNER JOIN tool ON tool_reference.id_tool=tool.id_tool) ON category.id_category= tool_reference.id_category)ON category_lang.id_category=category.id_category WHERE tool.id_tool=:id AND category_lang.id_lang=:lang", { 'id':id, 'lang':self.id_lang }, True )
		
			if rowsC != False:		
	
				row = self.query( "SELECT tool.link, tool.name, tool.source, tool.homePage, tool.kaliRepo, tool.author, tool.license, tool_lang.description, tool_lang.usage FROM tool INNER JOIN tool_lang ON tool.id_tool=tool_lang.id_tool WHERE tool.id_tool=:id AND tool_lang.id_lang=:lang", { 'id':id, 'lang':self.id_lang }, True )	
				
				
		elif re.match( "^(" + self.locale["commandKeyword"]["name"] + "\:)+[\w\-\s]{2,100}$", pattern ) or re.match( "^[\w\-\s]{2,100}$", pattern ):
		
			name = str( pattern.replace( self.locale["commandKeyword"]["name"] + ":", "" ) )
			
			rowsC = self.query( "SELECT category.id_category,category_lang.name FROM category_lang INNER JOIN(category INNER JOIN(tool_reference INNER JOIN tool ON tool_reference.id_tool=tool.id_tool) ON category.id_category= tool_reference.id_category)ON category_lang.id_category=category.id_category WHERE tool.name=:t AND category_lang.id_lang=:lang ", { "t":name.lower(), "lang":self.id_lang }, True )
				
			if rowsC != False:	
				
				row = self.query( "SELECT tool.link, tool.name, tool.source, tool.homePage, tool.kaliRepo, tool.author, tool.license, tool_lang.description, tool_lang.usage FROM tool INNER JOIN tool_lang ON tool.id_tool=tool_lang.id_tool WHERE tool.name=:tname AND tool_lang.id_lang=:lang", { 'tname':name.lower(), 'lang':self.id_lang }, True )					
				
		else:
			
			if not self.isCmd:
				self.printHelp()		
		
		if rowsC != False and row != False:

			print ( "\n\n\t" + self.bold+row[0][1].encode( "utf-8" ).capitalize() )
				
			print ( self.bold + self.locale["titles"]["category"] + self.pEnd )

			for c in rowsC:

				print ( "\t" + str( c[0] ) + ". " + c[1].capitalize() + "\n" )
				self.linesPr += 1
                                       
			print ( "\n" + self.bold + self.locale["titles"]["link"].encode( "utf-8" ) + self.pEnd + row[0][0] )

			description = row[0][7].replace( "[shell]", "" ).replace( "[/shell]", "" )
			source = row[0][2]
			homepage = row[0][3]
			kalirepo = row[0][4]
			author = row[0][5]
			license = row[0][6] 
	
			if source != "":

					source = "\n[b]" + self.locale["titles"]["source"].encode( "utf-8" ) + "[/b]" + source.encode( "utf-8" ) + "\n"
        
			if homepage != "":        				
        
				homepage = "[b]" + self.locale["titles"]["web"].encode( "utf-8" ) + "[/b]" + homepage.encode( "utf-8" ) + "\n"

			if kalirepo != "":

				kalirepo = "[b]"+self.locale["titles"]["repo"].replace( "[t]", row[0][1] ).title().encode( "utf-8" ) + "[/b]" + kalirepo.encode( "utf-8" ) + "\n"

			author = "\n[b]" + self.locale["titles"]["author"].encode( "utf-8" ) + "[/b]" + author.encode( "utf-8" ) + "\n"
			license = "[b]" + self.locale["titles"]["license"].encode( "utf-8" ) + "[/b]" + license.encode( "utf-8" )
			data = source + homepage + kalirepo + author + license
		
			self.printFormatted(data)
				
			print ( "\n" + self.bold + self.locale["titles"]["description"].encode( "utf-8" ) + self.pEnd + "\n\n" )
			self.linesPr += 30
			
			temp = ""
				
			for p in description.splitlines():
				
				if p != "" :
				
					if self.locale["titles"]["tincludes"].encode( "utf-8" ) in p:
						
					        temp = temp + "\n[b]" + p + "[/b]\n\n\n"
						        
					else:
						
	      			               	if self.content != None:
	      			                
		      			                p = p.replace( self.content, "[b]" + self.content + "[/b]" ).replace( self.content.upper(), "[b]" + self.content.upper() + "[/b]" )
		      			                
		      			       	temp = temp + p + "\n"
		      			       	
			temp = temp.replace( "root@kali:~#", self.paintc +"31mkalit@root" + self.paintc + "0m:" + self.paintc + "34m~" + self.paintc +"0m#" + self.pEnd ) 
			
			if row[0][8] != "":
			
				usage = row[0][8].replace( "[shell]\n", "" ).replace( "[/shell]\n", "" ).replace( "[/shell]", "" ).replace( "root@kali:~#", self.paintc + "31mkalit@root" + self.paintc + "0m:"  + self.paintc + "34m~" + self.paintc +"0m#" + self.pEnd )
				
				if self.content != None:
	      			                
      			                usage = usage.replace( self.content, "[b]" + self.content + "[/b]" ).replace( self.content.upper(), "[b]" + self.content.upper() + "[/b]" )
      			                
				temp = temp + "\n\n[b]" + self.locale["titles"]["usage"].encode( "utf-8" ) + "[/b]\n\n\n" + usage + "\n"				

			self.content = None				
			self.printFormatted( temp )	
				
	def printFormatted( self, text ):

		lines,cols = subprocess.check_output( ["stty", "size"] ).decode().split()
		cols = int( cols )
		lines = int( lines )
		text = text.replace( "[b]", self.bold ).replace( "[/b]", self.pEnd )
		
		r = ""
		n = 60
		
		if cols <= 100:
		
		        n=60
		        
		elif cols > 100 and cols < 200:
		
		        n=90
		        
		else:
		        
		        n=130                
                
		for t in text.splitlines():
		
			if self.linesPr >= lines and self.pausekey == 1:
			
				res = raw_input( "" )
				self.linesPr = 5
				
				if res == "q" or res == "Q":
					
					return
			
			if len( t ) < n:
			
				print ( "\t" + str( t ) )
				self.linesPr +=1

			else:
			
				l = len( t )
				m = l%n
				j = l - m
				u = 0
				v = n
				
				for g in range( l/n ):		
                                                
					print ( "\t" + t[u:v] )
					self.linesPr +=1
					u = v
					v += n
					
				if m > 0:

					if l:

						line = ""

						if t[u:v].endswith( "." ):
                                                
							line= "\n"

						print ( "\t" + t[(v-n):l] + "\n" + line )
						self.linesPr +=1						
		
kt = ktools()
