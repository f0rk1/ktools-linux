#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cmd, re
from traceback import print_exc

class mycmd(cmd.Cmd):

	prompt   = None
	instance = None
	use_raw_input = 1
		
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
	
		self.do_help("")
		
		
	def preloop(self):	
	
		print ( self.instance.locale["cmd"]["intro"].replace("[b]", self.instance.bold).replace("[/b]", self.instance.pEnd) )					
				
	
	def do_clear(self, opt):

	        self.instance.reset()	
	        self.instance.printHeader()

		
	def do_show(self, opt):

		self.instance.printHeader()

		if not opt == self.instance.locale["show"]["categories"] and not opt == self.instance.locale["show"]["tools"]:
			
			self.do_help("show")
			
		elif opt == self.instance.locale["show"]["categories"]:	
		
			self.instance.printCategories()
			
		elif opt == self.instance.locale["show"]["tools"]:		
		
			self.instance.printTools()
			

	def complete_show(self, text, line, begidx, endidx):
	
		c = [self.instance.locale["show"]["categories"], self.instance.locale["show"]["tools"] ]
		
		if text:

			return [a for a in c if a.startswith(text)]	
			
		else:
			
			return c
					

	def do_category(self, opt):

		self.instance.printHeader()

		opt = opt.replace("\\","").replace('"', "").replace('"', "")

		if re.match("^("+self.instance.locale["commandKeyword"]["id"]+"\:)+[\d]{1,}$", opt) or re.match("^[\d]{1,}$", opt):

			self.instance.printCategoryTools(opt)
			
		elif (re.match("^("+self.instance.locale["commandKeyword"]["name"]+"\:)+[\D\W\s]{2,100}$", opt) or re.match("^[\D\W\s]{2,100}$", opt)) and not str(self.instance.locale["commandKeyword"]["id"]+":") in opt and not opt ==  str(self.instance.locale["commandKeyword"]["name"]+":"):
				
			self.instance.printCategoryTools(opt)		
					
		else:
				
			self.do_help("category")
		
	
	def do_tool(self, opt):
	
		self.instance.printHeader()

		opt = opt.replace("\\","").replace('"', "").replace('"', "")
		
		if re.match("^("+self.instance.locale["commandKeyword"]["id"]+"\:)+[\d]{1,}$", opt) or re.match("^[\d]{1,}$", opt):
			
			self.instance.printToolHelp(opt)
			
		elif re.match("^("+self.instance.locale["commandKeyword"]["name"]+"\:)+[\w\-\s]{2,100}$", opt) or re.match("^[\w\-\s]{2,100}$", opt):
				
			self.instance.printToolHelp(opt)		
		
		else:
			
			self.do_help("tool")
		
			
	def do_search(self, opt):
	
		self.instance.printHeader()
		
		opt = opt.replace("\\","").replace('"', "").replace('"', "")
	
		if opt == None or opt == "":
			
			self.do_help("search")	
		
		else:	
			
			self.instance.search(opt)				
			
							
	def do_exit(self, opt):
	
		exit()

	def printHelp(self):
	        
		print ( self.instance.locale["cmd"]["category"].values()[0] )
		print ( self.instance.locale["cmd"]["clear"].values()[0] )
		print ( self.instance.locale["cmd"]["search"].values()[0] )
		print ( self.instance.locale["cmd"]["show"].values()[0] )
		print ( self.instance.locale["cmd"]["tool"].values()[0] )
		print ( self.instance.locale["cmd"]["help"].values()[0] )
		print ( self.instance.locale["cmd"]["exit"].values()[0] )

		
	def do_help(self, argv):
		
		self.instance.printHeader()
		headerBorder =  "\n\t========================================================\n" 
		print ( headerBorder + self.instance.locale["titles"]["cmd"] + headerBorder  )

			
		if argv == "" or not argv in ["show", "exit", "category", "category_id", "tool", "tool_id","search","clear"]:
			
			self.printHelp()
			
		else:	

			if argv == "show":
			
				print ( self.instance.locale["cmd"]["show"].values()[0] )
				
			elif argv == "category":
			
				print ( self.instance.locale["cmd"]["category"].values()[0] )
			
			elif argv == "tool":				
		
				print ( self.instance.locale["cmd"]["tool"].values()[0] )
			
			elif argv == "search":
		
				print ( self.instance.locale["cmd"]["search"].values()[0] )
			
			elif argv == "clear":
		
				print ( self.instance.locale["cmd"]["clear"].values()[0] )
		
			elif argv == "exit":
			
				print ( self.instance.locale["cmd"]["exit"].values()[0] )
