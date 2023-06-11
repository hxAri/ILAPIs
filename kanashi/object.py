#!/usr/bin/env python

#
# @author Ari Setiawan
# @create 23.05-2022
# @github https://github.com/hxAri/Kanashi
#
# Kanashī Copyright (c) 2022 - Ari Setiawan <hxari@proton.me>
# Kanashī Licence under GNU General Public Licence v3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Kanashī is not affiliated with or endorsed, endorsed at all by
# Instagram or any other party, if you use the main account to use this
# tool we as Coders and Developers are not responsible for anything that
# happens to that account, use it at your own risk, and this is Strictly
# not for SPAM.
#

from re import findall

from kanashi.utility.json import JSON
from kanashi.utility.json import JSONError

#[kanashi.Object]
class Object:
	
	#[Object( Dict data, Object parent )]: None
	def __init__( self, data, parent=None ):
		
		self.__parent__ = parent
		self.__method__ = {}
		self.__index__ = 0
		self.__data__ = {}
		
		# Inject data.
		self.set( data )
	
	#[Object.__getitem__( String key )]: Mixed
	def __getitem__( self, key ):
		return self.__dict__[key]
	
	#[Object.__setitem__( String key, Mixed value )]: None
	def __setitem__( self, key, value ):
		self.set({ key: value })
	
	#[Object.__iter__()]: Object
	def __iter__( self ):
		return self
	
	#[Object.__json( Dict | List data )]: Dict
	def __json( self, data=None ):
		if data == None:
			data = self.dict()
		match type( data ):
			case "dict":
				for key in data:
					match type( data[key] ).__name__:
						case "dict" | "list":
							data[key] = self.__json( data[key] )
						case _:
							if not JSON.isSerializable( data[key] ):
								data[key] = self.__str( data[key] )
			case "list":
				for idx in range( len( data ) ):
					match type( data[idx] ).__name__:
						case "dict" | "list":
							data[idx] = self.__json( data[idx] )
						case _:
							if not JSON.isSerializable( data[idx] ):
								data[idx] = self.__str( data[idx] )
		return data
	
	#[Object.__next__()]
	def __next__( self ):
		
		# Get current index iteration.
		index = self.__index__
		
		# Get object length.
		length = self.len()
		try:
			if index < length:
				self.__index__ += 1
				return self[self.keys( index )]
		except IndexError:
			pass
		raise StopIteration
	
	#[Object.__repr__()]: String
	def __repr__( self ):
		return "Object({}\x20{})".format( type( self ).__name__, self.json() )
	
	#[Object.__str__()]: String
	def __str__( self ):
		return self.json()
	
	#[Object.__str( Mixed data )]: String
	def __str( self, data ):
		text = f"{data}"
		text = text.replace( "'", "" )
		text = text.replace( ">", "/>" )
		return text
	
	#[Object.copy()]: Object
	def copy( self ):
		return Object( self.dict() )
	
	#[Object.dict()]: Dict
	def dict( self ):
		data = {}
		copy = self.__dict__
		for key in copy.keys():
			if key != "__data__" and key != "__index__" and key != "__method__" and key != "__parent__":
				if isinstance( copy[key], Object ):
					data[key] = copy[key].dict()
				elif isinstance( copy[key], list ):
					data[key] = []
					for item in copy[key]:
						if isinstance( item, Object ):
							data[key].append( item.dict() )
						else:
							data[key].append( item )
				else:
					data[key] = copy[key]
		return data
	
	#[Object.dump()]: String
	def dump( self ):
		return "{}".format( self.dict() )
	
	#[Object.json()]: String
	def json( self ):
		return JSON.encode( self.__json( self.dict() ) )
	
	#[Object.isset( String key )]: Bool
	def isset( self, key ):
		try:
			if self.__dict__[key]:
				pass
			return True
		except KeyError:
			return False
	
	#[Object.unset( String key )]: None
	def unset( self, key ):
		if key in self.__data__:
			del self.__data__[key]
		if key in self.__dict__:
			del self.__dict__[key]
	
	#[Object.idxs()]: List<Int>
	def idxs( self ):
		return([ idx for idx in range( len( self.__data__ ) ) ])
	
	#[Object.keys()]: List<String>
	def keys( self, index=None ):
		if isinstance( index, int ):
			 return self.keys()[index]
		return list( self.__data__.keys() )
	
	#[Object.get()]: Mixed
	def get( self, key ):
		return self.__dict__[key]
	
	#[Object.len()]: Int
	def len( self ):
		return len( self.__data__ )
	
	#[Object.__set( Dictionary data )]: None
	def set( self, data ):
		match type( data ).__name__:
			case "dict":
				for key in data.keys():
					self.__data__[key] = data[key]
					match type( data[key] ).__name__:
						case "dict":
							if key in self.__dict__ and isinstance( self.__dict__[key], Object ):
								self.__dict__[key].set( data[key] )
							else:
								self.__dict__[key] = Object( data[key] )
						case "list":
							self.__dict__[key] = []
							for item in data[key]:
								if type( item ).__name__ == "dict":
									self.__dict__[key].append( Object( item ) )
								else:
									self.__dict__[key].append( item )
						case _:
							self.__dict__[key] = data[key]
			case "str":
				try:
					self.set( JSON.decode( data ) )
				except JSONError as e:
					raise ValueError( "Invalid JSON String data parameter" )
			case _:
				raise ValueError( "Parameter data must be type Dictionary or JSON Strings, {} given".format( type( data ).__name__ ) )
		self.ref()
	
	#[Object.__ref()]: None
	def ref( self ):
		if self.__parent__ != None:
			for i, v in enumerate( self.__dict__ ):
				self.__parent__.__dict__[v] = self.__dict__[v]
		pass
	
