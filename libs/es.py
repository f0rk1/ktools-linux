#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cmd, re
from traceback import print_exc

class mycmd(cmd.Cmd):

	prompt   = None
	instance = None
	use_raw_input = 0
		
	def set_instance(self, instance = None):

		try:

			if not instance == None:
		
				self.instance = instance
				
			else:

				raise Exception("Ktools instance error")	
				
				
		except Exception as ex:	
				
			print_exc()			
				
	
	'''def do_EOF(self, line):	
	
		return True'''
	
		
	def postcmd(self, stop, line):
		
		if line != "":
		
			print ("")
			
	
	def precmd(self, line):
		
		if line != "":
		
			print ("")
			
		return cmd.Cmd.precmd(self, line)
		
	
	def default(self, line):
	
		self.do_ayuda("")
		
		
	def preloop(self):	
	
		print ( self.instance.locale["cmd"]["intro"].replace("[b]", self.instance.bold).replace("[/b]", self.instance.pEnd) )
		
	
	def do_limpiar(self, opt):

	        self.instance.printHeader()

		
	def do_mostrar(self, opt):

		self.instance.printHeader()

		if not opt == self.instance.locale["show"]["categories"] and not opt == self.instance.locale["show"]["tools"]:
			
			self.do_ayuda("mostrar")
			
		elif opt == self.instance.locale["show"]["categories"]:	
		
			self.instance.printCategories()
			
		elif opt == self.instance.locale["show"]["tools"]:		
		
			self.instance.printTools()

	
	def complete_mostrar(self, text, line, begidx, endidx):

		c = [self.instance.locale["show"]["categories"], self.instance.locale["show"]["tools"] ]
		
		if text:

			return [a for a in c if a.startswith(text)]	
			
		else:
			
			return c
		

	def do_categoria(self, opt):

		self.instance.printHeader()

		opt = opt.replace("\\","").replace('"', "").replace('"', "")
			
		if re.match("^("+self.instance.locale["commandKeyword"]["id"]+"\:)+[\d]{1,}$", opt) or re.match("^[\d]{1,}$", opt):

			self.instance.printCategoryTools(opt)			
			
		elif (re.match("^("+self.instance.locale["commandKeyword"]["name"]+"\:)+[\D\W\s]{2,100}$", opt) or re.match("^[\D\W\s]{2,100}$", opt) ) and not str(self.instance.locale["commandKeyword"]["id"]+":") in opt and not opt ==  str(self.instance.locale["commandKeyword"]["name"]+":"):
				
			self.instance.printCategoryTools(opt)					
		
		else:
				
			self.do_ayuda("categoria") 
		
				
							
	def do_herramienta(self, opt):
	
		self.instance.printHeader()

		opt = opt.replace("\\","").replace('"', "").replace('"', "")

		if re.match("^("+self.instance.locale["commandKeyword"]["id"]+"\:)+[\d]{1,}$", opt) or re.match("^[\d]{1,}$", opt):

			self.instance.printToolHelp(opt)
			
		elif re.match("^("+self.instance.locale["commandKeyword"]["name"]+"\:)+[\w\-\s]{2,100}$", opt) or re.match("^[\w\-\s]{2,100}$", opt):  
				
			self.instance.printToolHelp(opt)		

		else:
		
			self.do_ayuda("herramienta")


			
	def do_buscar(self, opt):
	
		self.instance.printHeader()
	
		if opt == "":
			
			self.do_ayuda("buscar")	
		
		else:	

			self.instance.search(str(opt))				
			
							
	def do_salir(self, opt):
	
		exit()

		
	def printHelp(self):
	        
		print ( self.instance.locale["cmd"]["search"].values()[0] )
		print ( self.instance.locale["cmd"]["category"].values()[0] )
		print ( self.instance.locale["cmd"]["tool"].values()[0] )
		print ( self.instance.locale["cmd"]["clear"].values()[0] )
		print ( self.instance.locale["cmd"]["show"].values()[0] )
		print ( self.instance.locale["cmd"]["help"].values()[0] )
		print ( self.instance.locale["cmd"]["exit"].values()[0] )
		
	
	def do_help(self, argv):

		self.do_ayuda(argv)

	
	def do_ayuda(self, argv):
		
		self.instance.printHeader()
		headerBorder =  "\n\t========================================================\n"		
		print ( headerBorder + self.instance.locale["titles"]["cmd"] + headerBorder  )
		
		if argv == "" or not argv in ["mostrar", "salir", "categoria", "herramienta", "buscar", "limpiar"]:
			
			self.printHelp()
			
		else:	

			if argv == "mostrar":
			
				print ( self.instance.locale["cmd"]["show"].values()[0] )
				
			elif argv == "categoria":
			
				print ( self.instance.locale["cmd"]["category"].values()[0] )
			
			elif argv == "herramienta":				
		
				print ( self.instance.locale["cmd"]["tool"].values()[0] )
			
			elif argv == "buscar":
		
				print ( self.instance.locale["cmd"]["search"].values()[0] )
			
			elif argv == "limpiar":
		
				print ( self.instance.locale["cmd"]["clear"].values()[0] )
		
			elif argv == "salir":
			
				print ( self.instance.locale["cmd"]["exit"].values()[0] )
				
				
	def complete_ayuda(self, text, line, begidx, endidx):	
	
		return [str(self.instance.locale["cmd"][a].keys()[0]) for a in self.instance.locale["cmd"].keys() if re.match("^"+text, self.instance.locale["cmd"][a].keys()[0])]
