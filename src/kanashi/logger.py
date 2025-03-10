#!/usr/bin/env python3

#
# @author hxAri (hxari)
# @create 23-12-2024 17:30
# @github https://github.com/hxAri/Kanashi
#
# Kanashi is an Open-Source project for doing various
# things related to Instagram, e.g Login. Logout, Profile Info,
# Follow, Unfollow, Media downloader, etc.
#
# Kanashi Copyright (c) 2024 - hxAri <hxari@proton.me>
# Kanashi Licence under GNU General Public Licence v3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

from builtins import bool as Bool, int as Int, str as Str
from datetime import datetime
from enum import Enum
from inspect import getframeinfo, stack
from os import getpid, getuid, makedirs as mkdir
from os.path import isdir
from pwd import getpwuid
from pytz import timezone
from pytz.tzinfo import BaseTzInfo
from random import randint
from typing import (
	Any, 
	final, 
	Generic, 
	Tuple, 
	TypeVar as Var, 
	Union
)
from tzlocal import get_localzone_name as TzLocalzoneName

from kanashi import __program__ as program
from kanashi.common import colorize
from kanashi.constant import BasePath, BaseVenv


__all__ = [
	"disableStoreLog",
	"enableStoreLog",
	"Level",
	"Logger",
	"threshold"
]


_Context = Var( "_Context" )
""" Context Type """

_EnableStore:Bool = True
""" Logger enable save log """

_FDatetime:Str = "%Y-%m-%dT%H:%M:%S"
""" DateTime formatter """

_Formatter:Str = "{datetime}{utcoffset} {level} {username} P{pid}:T{thread} --- [{program}] {context} : {linenum} : {message}"
""" Logging formatter """

_Strftime = Var( "_Strftime", bytes, str )
""" DateTime String Formatted Type """

_Utcoffsets = Var( "_Utcoffsets", bytes, str )
""" DateTime String of Utcoffset Type """


def disableStoreLog() -> None:
	
	""" Enable store log into file """
	
	global _EnableStore
	_EnableStore = False

def enableStoreLog() -> None:
	
	""" Enable store log into file """
	
	global _EnableStore
	_EnableStore = True


class Level( Enum ):
	
	""" Application Logger Level """
	
	CRITICAL = 1
	""" Critical """
	
	DEBUG = 0
	""" Debug """
	
	DISABLE = randint( 8999, 9999 )
	""" Disable """
	
	ERROR = 2
	""" Error """
	
	INFO = 3
	""" Info """
	
	SUCCESS = 4
	""" Success """
	
	VERBOSE = -9999
	""" Verbose """
	
	WARNING = 5
	""" Warning """
	
	...


_Threshlod:Level = Level.INFO
""" Logger Threshold """


def threshold( level:Level ) -> None:
	
	""" Set logger threshold level """
	
	global _Threshlod
	_Threshlod = level


class Logger( Generic[_Context] ):
	
	"""
	Application Logger Implementation
	
	>>> logger = Logger( Class )
	>>> logger = Logger( Instance )
	>>> logger = Logger( "com.example.Main" )
	>>> logger.debug( "Hello World!", *args, **kwargs )
	"""
	
	__basepath:Str
	""" Basepath logging stored """
	
	__context:_Context
	""" Application context """
	
	__filename:Str
	""" Logging stored contents """
	
	__formatter:Str
	""" Logging message format """
	
	__timezone:BaseTzInfo
	""" Current Timezone """
	
	def __init__( self, context:_Context, formatter:Str=_Formatter ) -> None:
		
		"""
		Construct method of class Logger
		
		Parameters:
			context (_Context):
				Application context logger initial
			formatter (Str):
				Logger output format
		"""
		
		currtime = datetime.now()
		self.__basepath = f"{BasePath}/logging"
		if not isdir( self.basepath ):
			mkdir( self.basepath )
		self.__context = context
		self.__filename = currtime.strftime( f"{self.basepath}/{program.lower()}-%Y-%m-%d.log" )
		self.__formatter = formatter
		self.__timezone = timezone( TzLocalzoneName() )
	
	@final
	@property
	def basepath( self ) -> Str:
		
		""" Basepath logging stored """
		
		return self.__basepath
	
	@final
	@property
	def context( self ) -> Str:
		
		""" Logger context """
		
		context = self.__context
		if not isinstance( context, Str ):
			if not hasattr( context, "__qualname__" ):
				context = type( context )
			if hasattr( context, "__qualname__" ):
				return f"{context.__module__}.{context.__qualname__}"
			return f"{context.__module__}.{context.__name__}"
		return context
	
	def critical( self, message:Str, *args:Any, **kwargs:Any ) -> None:
		self.write( Level.CRITICAL, message, *args, **kwargs )
	
	def debug( self, message:Str, *args:Any, **kwargs:Any ) -> None:
		self.write( Level.DEBUG, message, *args, **kwargs )
	
	def error( self, message:Str, *args:Any, **kwargs:Any ) -> None:
		self.write( Level.ERROR, message, *args, **kwargs )
	
	@final
	@property
	def filename( self ) -> Str:
		
		""" Logger filename """
		
		return self.__filename
	
	@final
	@property
	def formatter( self ) -> Str:
		
		""" Logger fomatter """
		
		return self.__formatter
	
	def info( self, message:Str, *args:Any, **kwargs:Any ) -> None:
		self.write( Level.INFO, message, *args, **kwargs )
	
	def success( self, message:Str, *args:Any, **kwargs:Any ) -> None:
		self.write( Level.SUCCESS, message, *args, **kwargs )
	
	@final
	@property
	def timezone( self ) -> BaseTzInfo:
		
		""" Current timezone """
		
		return self.__timezone
	
	@final
	@property
	def username( self ) -> Str:
		
		""" Current os account username """
		
		return getpwuid( getuid() )[0]
	
	def utcoffset( self ) -> Tuple[_Strftime,_Utcoffsets]:
		
		""" Return formatted datetime and utcoffset """
		
		localtime = datetime.now( self.timezone )
		utfoffset = localtime.utcoffset()
		seconds = utfoffset.total_seconds()
		hours, remainder = divmod( seconds, 3600 )
		minutes = remainder // 60
		operator = "+" if seconds >= 0 else "-"
		offsets = f"{operator}{int(hours):02}:{int(minutes):02}"
		strftime = localtime.strftime( _FDatetime )
		return tuple([ strftime, offsets ])
	
	def warning( self, message:Str, *args:Any, **kwargs:Any ) -> None:
		self.write( Level.WARNING, message, *args, **kwargs )
	
	def write( self, level:Union[Int,Level,Str], message:Str, *args:Any, thread:Union[Int,Str]=0, **kwargs:Any ) -> None:
		
		"""
		Logger write
		
		Parameters:
			level (Int|Level|Str):
				Logger logging level
			message (Str):
				Logger message
			args (*Any):
				Logger argument message
			thread (Int|Str):
				Current thread position number
			kwargs (**Any):
				Logger key argument message
		"""
		
		stacks = stack()
		progpid = str( getpid() )
		inframe = getframeinfo( stacks[2][0] )
		linenum = str( inframe.lineno )
		context = f"{self.context}.{inframe.function}"
		context = context \
			.replace( "__main__", program.lower() ) \
			.replace( "<module>", "invoke" )
		strftime, offsets = self.utcoffset()
		levelname = level
		if isinstance( level, Int ):
			level = Level( value=0 )
		if isinstance( level, Level ):
			levelname = level.name
		thread = str( thread )
		username = self.username
		formatted = self.formatter.format(
			datetime=strftime,
			context=context[:38].ljust( 38 ),
			program=program[:16].ljust( 16 ),
			username=username[:6].center( 6 ),
			utcoffset=offsets[:6].ljust( 6 ),
			level=levelname[:8].center( 8 ),
			linenum=linenum[:4].ljust( 4 ),
			thread=thread[:4].ljust( 4 ),
			pid=progpid[:6].ljust( 6 ),
			message=message.format( *args, **kwargs )
		)
		if _EnableStore is True:
			with open( self.filename, "a", encoding="UTF-8" ) as fopen:
				fopen.write( formatted.replace( "\x0a", "\\n" ) )
				fopen.write( "\x0a" )
				fopen.close()
		if not isinstance( level, Str ) and level.value >= _Threshlod.value:
			print( f"\x0d{colorize( formatted )}" \
				.replace( BasePath, "{basepath}" ) \
				.replace( BaseVenv, "{virtual}" )
		 	)
		...
	
	...
