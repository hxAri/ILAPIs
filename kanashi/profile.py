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

from kanashi.config import Config
from kanashi.decorator import avoidForMySelf
from kanashi.error import BestieError, BlockError, FavoriteError, FollowError, ProfileError, RestrictError, UserError, UserNotFoundError
from kanashi.object import Object
from kanashi.readonly import Readonly
from kanashi.request import RequestRequired
from kanashi.utility import File, String, tree, typedef, typeof
	

#[kanashi.profile.ProfilePriperties]
class ProfileProperties:
	
	@property
	def bestie( self ):
		return self.isBestie
	
	@property
	def biography( self ):
		return self.__profile__.biography
	
	@property
	def biographyFormat( self ):
		return "\x20\x20{}".format( self.biographyRawText.replace( "\n", "\x0a\x20\x20\x20\x20\x20\x20" ) )
	
	@property
	def biographyEntities( self ):
		return self.__profile__.biography_with_entities.entities
	
	@property
	def biographyEntityUsers( self ):
		users = []
		entities = self.biographyEntities
		for entity in entities:
			if  not entity.isset( "user" ): continue
			if  user := entity.user:
				users.append( user.username )
		return users
	
	@property
	def biographyEntityUsersFormat( self ):
		return "-\x20@{}".format( "\x0a\x20\x20\x20\x20-\x20@".join( self.biographyEntityUsers ) )
	
	@property
	def biographyEntityHashtags( self ):
		hashtags = []
		entities = self.biographyEntities
		for entity in entities:
			if  not entity.isset( "hashtag" ): continue
			if  hashtag := entity.hashtag:
				hashtags.append( hashtag.name )
		return hashtags
	
	@property
	def biographyEntityHashtagsFormat( self ):
		return "-\x20#{}".format( "\x0a\x20\x20\x20\x20-\x20#".join( self.biographyEntityHashtags ) )
	
	@property
	def biographyRawText( self ):
		if  self.__profile__.biography_with_entities.raw_text == None:
			self.__profile__.biography_with_entities.raw_text = ""
		return self.__profile__.biography_with_entities.raw_text
	
	@property
	def blockedByViewer( self ):
		return self.__profile__.blocked_by_viewer
	
	@property
	def categoryName( self ):
		return self.__profile__.category_name
	
	@property
	def countEdgeFelixVideoTimeline( self ):
		return self.__profile__.edge_felix_video_timeline.count
	
	@property
	def countEdgeFollow( self ):
		return self.__profile__.edge_follow.count
	
	@property
	def countEdgeFollowedBy( self ):
		return self.__profile__.edge_followed_by.count
	
	@property
	def countEdgeMediaCollections( self ):
		return self.__profile__.edge_media_collections.count
	
	@property
	def countEdgeMutualFollowedBy( self ):
		return self.__profile__.edge_mutual_followed_by.count
	
	@property
	def countEdgeOwnerToTimelineMedia( self ):
		return self.__profile__.edge_owner_to_timeline_media.count
	
	@property
	def countEdgeSavedMedia( self ):
		return self.__profile__.edge_saved_media.count
	
	@property
	def edgeFelixVideoTimeline( self ):
		return self.__profile__.edge_felix_video_timeline.edges
	
	@property
	def edgeFollow( self ):
		return self.__profile__.edge_follow.edges
	
	@property
	def edgeFollowedBy( self ):
		return self.__profile__.edge_followed_by.edges
	
	@property
	def edgeMediaCollections( self ):
		return self.__profile__.edge_media_collections.edges
	
	@property
	def edgeMutualFollowedBy( self ):
		return self.__profile__.edge_mutual_followed_by.edges
	
	@property
	def edgeOwnerToTimelineMedia( self ):
		return self.__profile__.edge_owner_to_timeline_media.edges
	
	@property
	def edgeSavedMedia( self ):
		return self.__profile__.edge_saved_media.edges

	@property
	def eimuid( self ):
		return self.__profile__.eimu_id
	
	@property
	def fbid( self ):
		return self.__profile__.fbid
	
	@property
	def followedByViewer( self ):
		return self.__profile__.followed_by_viewer
	
	@property
	def followsViewer( self ):
		return self.__profile__.follows_viewer
	
	@property
	def fullname( self ):
		return self.__profile__.full_name
	
	@property
	def fullnameFormat( self ):
		name = []
		if  self.fullname:
			name.append( self.fullname )
		else:
			pass
		name.append( f"({self.username})" )
		if  self.isVerified:
			name.append( "\x1b[1;36m√\x1b[0m" )
		return "\x20".join( name )
	
	@property
	def hasBlockedViewer( self ):
		return self.__profile__.has_blocked_viewer
	
	@property
	def id( self ):
		return self.__profile__.id
	
	@property
	def isBestie( self ):
		return self.__profile__.is_bestie
	
	@property
	def isBlockingReel( self ):
		return self.__profile__.is_blocking_reel
	
	@property
	def isBusinessAccount( self ):
		return self.__profile__.is_business_account
	
	@property
	def isEligibleToSubscribe( self ):
		return self.__profile__.is_eligible_to_subscribe
	
	@property
	def isEmbedsDisabled( self ):
		return self.__profile__.is_embeds_disabled
	
	@property
	def isFeedFavorite( self ):
		return self.__profile__.is_feed_favorite
	
	@property
	def isGuardianOfViewer( self ):
		return self.__profile__.is_guardian_of_viewer

	@property
	def isInCanada( self ):
		return self.__profile__.is_in_canada
	
	@property
	def isSupervisedByViewer( self ):
		return self.__profile__.is_supervised_by_viewer
	
	@property
	def isJoinedRecently( self ):
		return self.__profile__.is_joined_recently
	
	@property
	def isMutingNotes( self ):
		return self.__profile__.is_muting_notes
	
	@property
	def isMutingReel( self ):
		return self.__profile__.is_muting_reel
	
	@property
	def isMySelf( self ):
		return self.__profile__.id == self.__viewer__.id
	
	@property
	def isNotMySelf( self ):
		return self.__profile__.id != self.__viewer__.id
	
	@property
	def isPrivateAccount( self ):
		return self.__profile__.is_private
	
	@property
	def isProfessionalAccount( self ):
		return self.__profile__.is_professional_account
	
	@property
	def isSupervisedUser( self ):
		return self.__profile__.is_supervised_user
	
	@property
	def isVerified( self ):
		return self.__profile__.is_verified
	
	@property
	def muting( self ):
		return self.__profile__.muting
	
	#[Profile.prints]: List
	@property
	def prints( self ):
		
		"""
		This is only usage for Actions|Main class from
		kanashi.main.Actions and kanashi.main.Main
		"""
		
		display = [ "", {} ]
		
		# General information to be displayed.
		prints = [
			"id",
			"self",
			"account",
			"username",
			"fullname",
			"pronouns",
			"category",
			"websites",
			"statuses",
			"entities",
			"contexts"
		]
		
		for line in prints:
			match line:
				case "id":
					value = self.id
				case "self":
					value = self.isMySelf
				case "account":
					account = []
					if  self.isPrivateAccount:
						account.append( "Private" )
					else:
						account.append( "Public" )
						if  self.isBusinessAccount:
							account.append( "Business" )
						if  self.isProfessionalAccount:
							account.append( "Professional" )
					value = "/".join( account )
				case "username":
					value = "\x1b[1;38;5;189m\x7b\x7d\x1b[0m".format( self.username )
				case "fullname":
					value = "\x1b[1;37m\x7b\x7d\x1b[0m".format( self.fullname )
					if  self.isVerified:
						value += "\x20\x1b[1;38;5;195m\u221a\x1b[0m"
				case "pronouns":
					value = self.pronounsFormat if self.pronounsFormat else None
				case "category":
					if  self.isProfessionalAccount:
						value = self.categoryName
				case "websites":
					if  self['bio_links']:
						link = {}
						if  "title" in self['bio_links'][0]:
							link['Title'] = self['bio_links']['title']
						link['Type'] = self['bio_links'][0]['link_type'].capitalize()
						link['Url'] = "\x1b[1;38;5;81m{}\x1b[0m".format( self['bio_links'][0]['url'] )
						value = link
				case "statuses":
					if  self.isNotMySelf:
						value = {
							"Block": {
								"Blocked by owner": self.hasBlockedViewer,
								"Blocked by viewer": self.blockedByViewer
							},
							"Follow": {
								"Followed by owner": self.followsViewer,
								"Requested by owner": self.requestedFollow,
								"Followed by viewer": self.followedByViewer,
								"Requested by viewer": self.requestedByViewer
							},
							"Muting": {
								"Notes": self.isMutingNotes,
								"Reel": self.isMutingReel,
							},
							"Bestie": self.isBestie,
							"Favorite": self.isFeedFavorite,
							"Restrict": self.restrictedByViewer
						}
					else:
						value = "Unavailable"
				case "entities":
					value = {
						"Users": {
							"Count": len( self.biographyEntityUsers ),
							"List": [ "@{}".format( user ) for user in self.biographyEntityUsers ]
						},
						"Hashtags": {
							"Count": len( self.biographyEntityHashtags ),
							"List": [ "#{}".format( hashtag ) for hashtag in self.biographyEntityHashtags ]
						}
					}
				case "contexts":
					if  self.isNotMySelf:
						value = {
							"Linkeds": [ "@{}".format( user.username ) for user in self['profile_context_links_with_user_ids'] ],
							"Facepiles": [ "@{}".format( user.username ) for user in self['profile_context_facepile_users'] ]
						}
				case _:
					value = "Unavailable"
			try:
				display[1][line.capitalize()] = value
				del value
			except NameError:
				continue
		
		biography = []
		for i in range( 0, len( self.biography if self.biography else "" ), 36 ):
			biography.append( "\x20\x20{}".format( self.biography[i:i+36].replace( "\n", "\x0a\x20\x20\x20\x20\x20\x20" ) ) )
		if  len( biography ) == 0:
			biography = [ "None" ]
		display.append( "\x0a\x20\x20\x20\x20".join([
			"----------------------------------------",
			"- Biography",
			"----------------------------------------",
			*biography,
			"----------------------------------------"
		]))
		
		edges = "\x0a\x20\x20\x20\x20".join([
			"",
			"┌───────┬───────┬────────┬─────────────┐",
			"│ Posts │ Felix │ Saveds │ Collections │",
			"├───────┼───────┼────────┼─────────────┤",
			"│ {} │ {} │ {} │ {} │",
			"└───────┴───────┴────────┴─────────────┘",
			"----------------------------------------",
			"┌─────────────┬─────────────┬──────────┐",
			"│  Followers  │  Following  │  Mutual  │",
			"├─────────────┼─────────────┼──────────┤",
			"│ {} │ {} │ {} │",
			"└─────────────┴─────────────┴──────────┘",
			""
		])
		display.append( edges.format(*[
			f"{self.countEdgeOwnerToTimelineMedia}".center( 5 ),
			f"{self.countEdgeFelixVideoTimeline}".center( 5 ),
			f"{self.countEdgeSavedMedia}".center( 6 ),
			f"{self.countEdgeMediaCollections}".center( 11 ),
			f"{self.countEdgeFollowedBy}".center( 11 ),
			f"{self.countEdgeFollow}".center( 11 ),
			f"{self.countEdgeMutualFollowedBy}".center( 8 ),
		]))
		
		# Create Tree Structure
		# For Human readabled profile info.
		display[1] = tree( data=display[1], indent=4 )
		
		return display
	
	#[Profile.prints]: List
	@property
	def printsV2( self ):
		
		"""
		This is only usage for Actions|Main class from
		kanashi.main.Actions and kanashi.main.Main
		"""
		
		# General information to be displayed.
		# The empty string will be used for the new line.
		prints = [
			"│",
			"id",
			"username",
			"fullname",
			"│",
			"pronouns",
			"│",
			"category",
			"│",
			"account",
			"│",
			"website",
			"│",
			"follow",
			"│",
			"block",
			"│",
			"restrict",
			"muting",
			"│",
			"bestie",
			"favorite",
			"",
			"biography",
			"",
			"edges",
			""
		]
		
		for i in range( len( prints ), 0, -1 ):
			idx = i -1
			val = prints[idx]
			match val:
				case "id":
					prints[idx] = f"├── ID|PK {self.id}"
				case "fullname":
					prints[idx] = f"├── Fullname \x1b[1;37m{self.fullname}\x1b[0m"
				case "username":
					prints[idx] = f"├── Username \x1b[1;38;5;189m{self.username}\x1b[0m"
					if  self.isVerified:
						prints[idx] += "\x20\x1b[1;36m√\x1b[0m"
				case "pronouns":
					prints[idx] = "\x0a\x20\x20\x20\x20│\x20\x20\x20└──\x20".join([ "├── Pronouns", self.pronounsFormat if self.pronounsFormat else "None" ])
				case "category":
					if  self.isProfessionalAccount:
						prints[idx] = "\x0a\x20\x20\x20\x20│\x20\x20\x20└──\x20".join([ "├── Category", self.categoryName if self.categoryName else "None" ])
					else:
						prints[idx] = "\x0a\x20\x20\x20\x20│\x20\x20\x20└──\x20".join([ "├── Category", "Not a Professional Account" ])
				case "account":
					account = []
					if  self.isPrivateAccount:
						account.append( "Private" )
					else:
						account.append( "Public" )
						if  self.isBusinessAccount:
							account.append( "Business" )
						if  self.isProfessionalAccount:
							account.append( "\x20Professional" )
					prints[idx] = "\x0a\x20\x20\x20\x20│\x20\x20\x20└──\x20".join([ "├── Account", "/".join( account ) ])
				case "website":
					prints[idx] = [ "├── Website" ]
					if  self['bio_links']:
						if  "title" in self['bio_links'][0]:
							prints[idx].append( "Title {}".format( self['bio_links']['title'] ) )
						prints[idx].append( self['bio_links'][0]['link_type'].capitalize() )
						prints[idx].append( "\x1b[1;38;5;81m{}\x1b[0m".format( self['bio_links'][0]['url'] ) )
					else:
						prints[idx].append( "None" )
					prints[idx] = "\x0a\x20\x20\x20\x20│\x20\x20\x20└──\x20".join( prints[idx] )
				case "biography":
					if  self.biography:
						prints[idx] = "\x0a\x20\x20\x20\x20".join([
							"----------------------------------------",
							"- Biography",
							"----------------------------------------",
							"{}".format( self.biographyFormat ),
							"----------------------------------------",
							"- Biography Entities",
							"----------------------------------------",
							"- Biography Entitity Users",
							"----------------------------------------",
							"{}".format( self.biographyEntityUsersFormat if self.biographyEntityUsers else "- None" ),
							"----------------------------------------",
							"- Biography Entitity Hashtags",
							"----------------------------------------",
							"{}".format( self.biographyEntityHashtagsFormat if self.biographyEntityHashtags else "- None" ),
							"----------------------------------------"
						])
					else:
						del prints[idx]
				case "block":
					if  self.isMySelf:
						prints[idx] = "├── Block is not available for own profile"
					else:
						block = []
						if  self.hasBlockedViewer:
							block.append( "├── This user has blocked your account" )
						else:
							block.append( "├── This user did not block your account" )
						if  self.blockedByViewer:
							block.append( "├── You have blocked this user" )
						else:
							block.append( "├── You did not block this user" )
						prints[idx] = "\x0a\x20\x20\x20\x20".join( block )
				case "muting":
					if  self.isNotMySelf:
						if  self.muting:
							prints[idx] = "├── You have mute this user"
						else:
							prints[idx] = "├── You did not mute this user"
					else:
						prints[idx] = "├── Mute is not available for own profile"
				case "restrict":
					if  self.isNotMySelf:
						if  self.restrictedByViewer:
							prints[idx] = "├── You have restrict this user"
						else:
							prints[idx] = "├── You did not restrict this user"
					else:
						prints[idx] = "├── Restrict is not available for own profile"
				case "bestie":
					if  self.isNotMySelf:
						if  self.isBestie:
							prints[idx] = "├── This user is your bestie"
						else:
							prints[idx] = "├── This user is not your bestie"
					else:
						prints[idx] = "├── Bestie is not available for own profile"
				case "favorite":
					if  self.isNotMySelf:
						if  self.isFeedFavorite:
							prints[idx] = "├── This user feed is your favourite"
						else:
							prints[idx] = "├── This user feed is not your favourite"
					else:
						prints[idx] = "├── Favorite is not available for own profile"
				case "follow":
					if  self.isMySelf:
						prints[idx] = "├── Follow is not available for own profile"
					else:
						follow = []
						if  self.followsViewer:
							follow.append( "├── This user is following your account" )
						elif self.requestedFollow:
							follow.append( "├── This user is requested follow your account" )
						else:
							follow.append( "├── This user is not following your account" )
						if  self.followedByViewer:
							follow.append( "├── You have followed this user" )
						elif self.requestedByViewer:
							follow.append( "├── Your follow request has not been approved" )
						else:
							follow.append( "├── You are not following this user" )
						prints[idx] = "\x0a\x20\x20\x20\x20".join( follow )
				case "edges":
					prints[idx] = "\x0a\x20\x20\x20\x20".join([
						"----------------------------------------",
						"┌───────┬───────┬────────┬─────────────┐",
						"│ Posts │ Felix │ Saveds │ Collections │",
						"├───────┼───────┼────────┼─────────────┤",
						"│ {} │ {} │ {} │ {} │",
						"└───────┴───────┴────────┴─────────────┘",
						"----------------------------------------",
						"┌─────────────┬─────────────┬──────────┐",
						"│  Followers  │  Following  │  Mutual  │",
						"├─────────────┼─────────────┼──────────┤",
						"│ {} │ {} │ {} │",
						"└─────────────┴─────────────┴──────────┘",
						"----------------------------------------"
					])
					prints[idx] = prints[idx].format(*[
						f"{self.countEdgeOwnerToTimelineMedia}".center( 5 ),
						f"{self.countEdgeFelixVideoTimeline}".center( 5 ),
						f"{self.countEdgeSavedMedia}".center( 6 ),
						f"{self.countEdgeMediaCollections}".center( 11 ),
						f"{self.countEdgeFollowedBy}".center( 11 ),
						f"{self.countEdgeFollow}".center( 11 ),
						f"{self.countEdgeMutualFollowedBy}".center( 8 ),
					])
				case _:
					pass
			pass
		return prints
	
	@property
	def profile( self ):
		return self.__profile__
	
	@property
	def profilePicture( self ):
		return self.__profile__.rofile_pic_url
	
	@property
	def profilePictureHD( self ):
		if  self.__profile__.isset( "hd_profile_pic_url_info" ):
			return self.__profile__.hd_profile_pic_url_info.url
		elif  self.__profile__.isset( "hd_profile_pic_versions" ):
			return self.__profile__.hd_profile_pic_versions[-1].url
		return self.__profile__.profile_pic_url_hd
	
	@property
	def profilePictureHDResolution( self ):
		if  self.__profile__.isset( "hd_profile_pic_url_info" ):
			return "{}x{}".format(
				self.__profile__.hd_profile_pic_url_info.width,
				self.__profile__.hd_profile_pic_url_info.height
			)
		elif  self.__profile__.isset( "hd_profile_pic_versions" ):
			return "{}x{}".format(
				self.__profile__.hd_profile_pic_versions[-1].width,
				self.__profile__.hd_profile_pic_versions[-1].height
			)
		return "320x320"
	
	@property
	def pronouns( self ):
		return self.__profile__.pronouns
	
	@property
	def pronounsFormat( self ):
		if  self.pronouns:
			return "/".join( self.pronouns )
		return ""
	
	@property
	def requestedFollow( self ):
		return self.__profile__.incoming_request
	
	@property
	def requestedByViewer( self ):
		return self.__profile__.requested_by_viewer
	
	@property
	def restrictedByViewer( self ):
		return self.__profile__.restricted_by_viewer
	
	@property
	def subscribed( self ):
		return self.__profile__.subscribed
	
	@property
	def username( self ):
		return self.__profile__.username
	
	@property
	def viewer( self ):
		return self.__viewer__.copy()
	

#[kanashi.profile.Profile]
class Profile( ProfileProperties, Readonly, RequestRequired ):
	
	#[Profile.ATTRIBUTES]
	ATTRIBUTES = [
	]
	
	#[Profile( Object viewer, Request request, Dict profile, Mixed **kwargs )]: None
	def __init__( self, viewer, request, profile, **kwargs ):
		
		"""
		Construct method of class Profile.
		
		:params Object viewer
			Object represent user active
		:params Request request
			Object instance of request
		:params Dict profile
			User profile
		
		:return None
		"""
		
		# Viewer login information.
		self.__viewer__ = viewer
		
		# Instance of class Parent.
		self.__parent__ = super()
		self.__parent__.__init__( request )
		
		# Save profile user info.
		self.__profile__ = Object( profile )
		
		# Inherited methods from clients if available.
		self.__methods__ = kwargs.pop( "methods", {} )
	
	#[Profile.__getitem__( String key )]: Mixed
	def __getitem__( self, key ):
		return self.__profile__[key]
	
	#[Profile.__setitem__( String key, Mixed value )]: Mixed
	def __setitem__( self, key, value ):
		return self.__profile__.set({ key: value })
	
	#[Profile.approve( Bool approve )]:
	@avoidForMySelf
	def approve( self, approve=True ):
		
		"""
		Approve or ignore request follow from user.
		
		:params Bool approve
			Approve action
		
		:return Object
			Approve or ignore result represent
		:raises ValueError
			When the approve parameter is invalid
		:raises ProfileError
			When the user does not request follow your account
			When you will approve yourself
		:raises TypeError
			When the approve does not passed when new Profile instance crated
		"""
		
		if  typedef( approve, bool, False ):
			raise ValueError( "Invalid approve parameter, value must be type bool, {} passed", typeof( approve ) )
		elif not self.requestedFollow:
			raise ProfileError( "This user does not sent request to follow your account" )
		elif self.isMySelf:
			raise ProfileError( "Unable to aprove or ignore request follow for yourself" )
		else:
			if  "approve" not in self.__methods__:
				raise TypeError( "This profile instance can't usage for approve or ignore request follow" )
			result = self.__methods__['approve']( id=self.id, approve=approve )
			self.__profile__.incoming_request = False
			return result
	
	#[Profile.bestie()]: Object
	@avoidForMySelf
	def bestie( self ):
		
		"""
		Make bestie or unbestie user.
		
		THIS FUNCTION|METHOD UNDER DEVELOPMENT
		THERE ARE UNRESOLVED BUG IN THIS FUNCTIONALITY
		
		:return Object
			Bestie result represent
		:raises BestieError
			When you trying to make yourself as bestie
			When you are not following the user
			When something wrong, please to check the request response history
		"""
		
		if  self.isMySelf:
			raise BestieError( "Unable to set yourself as a bestie" )
		if  self.followedByViewer:
			self.headers.update({
				"Accept-Encoding": "gzip, deflate, br",
				"Content-Type": "application/json",
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/{}/".format( self.username )
			})
			data = {
				"add": [],
				"remove": [],
				"source": "profile"
			}
			if  self.isBestie:
				action = "Remove Bestie"
				data['remove'].append( self.id )
			else:
				action = "Adding Bestie"
				data['add'].append( self.id )
			request = self.request.post( "https://www.instagram.com/api/v1/friendships/set_besties/", json=data )
			status = request.status_code
			if  status == 200:
				response = request.json()
				if  "friendship_statuses" in response:
					self.__profile__.is_bestie = False if self.isBestie else True
					return Object( response['friendship_statuses'] )
				else:
					raise BestieError( response['message'] if "message" in response and response['message'] else f"Something wrong when {action} the {self.username}" )
			else:
				self.throws( action, status )
		else:
			raise BestieError( "Can't set user as bestie before following" )
	
	#[Profile.block()]: Object
	@avoidForMySelf
	def block( self ):
		
		"""
		Block or unblock user.
		
		:return Object
			Block result represent
		:raises BlockError
			When you trying to block yourself
			When something wrong, please to check the request response history
		"""
		
		if  self.isMySelf:
			raise BlockError( "Unable to block or unblock yourself" )
		self.headers.update({
			"Accept-Encoding": "gzip, deflate, br",
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/{}/".format( self.username )
		})
		if  self.blockedByViewer:
			target = "https://www.instagram.com/api/v1/web/friendships/{}/unblock/"
			action = "Unblock"
		else:
			target = "https://www.instagram.com/api/v1/web/friendships/{}/block/"
			action = "Blocking"
		request = self.request.post( target.format( self.id ) )
		status = request.status_code
		if  status == 200:
			response = request.json()
			if  "status" in response and response['status'] == "ok":
				self.__profile__.blocked_by_viewer = False if self.blockedByViewer else True
				return Object({
					"id": self.id,
					"username": self.username,
					"blocking": self.blockedByViewer
				})
			else:
				raise BlockError( response['message'] if "message" in response and response['message'] else f"Something wrong when {action} the {self.username}" )
		else:
			self.throws( action, status )
	
	#[Profile.export( String fname )]: None
	def export( self, fname=None ):
		
		"""
		Export profile info.
		
		:params String fname
			File name to save
			By default, Kanashī will save it in
			the ~/onsaved/exports/profile/ folder. To change
			it, please add a slash (/) before the filename,
			e.g /sdcard/path/filename without the file extension .json
		
		:return None
		:raise ProfileError
			When failed export profile info
		"""
		
		if  not isinstance( fname, str ):
			fname = self.username
		fdata = self.__profile__.json()
		if  fname[0] != "/":
			fname = Config.ONSAVED.export.profile.format( fname )
		else:
			fname = "{}.json".format( fname )
		try:
			File.write( fname, fdata )
		except Exception as e:
			raise ProfileError( "Failed to export profile info", prev=e )
	
	#[Profile.favorite()]: Object
	@avoidForMySelf
	def favorite( self ):
		
		"""
		Make favorite or unfavorit user.
		
		:return Object
			Favorite result represent
		:raises FavoriteError
			When you trying to make yourself as favorite for yourself, this is ambigue bro!
			When you are not following the user
			When something wrong, please to check the request response history
		"""
		
		if  self.isMySelf:
			raise FavoriteError( "Unable to set yourself as a favourite" )
		if  self.followedByViewer:
			self.headers.update({
				"Accept-Encoding": "gzip, deflate, br",
				"Content-Type": "application/x-www-form-urlencoded",
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/{}/".format( self.username )
			})
			data = { "source": "profile" }
			if  self.isFeedFavorite:
				action = "Remove favorite"
				data['remove'] = [ self.id ]
			else:
				action = "Make favorite"
				data['add'] = [ self.id ]
			request = self.request.post( "https://www.instagram.com/api/v1/friendships/update_feed_favorites/", data=data )
			status = request.status_code
			if  status == 200:
				response = request.json()
				if  "status" in response and response['status'] == "ok":
					self.__profile__.is_feed_favorire = False if self.isFeedFavorite else True
					return Object({
						"id": self.id,
						"username": self.username,
						"favorite": self.isFeedFavorite
					})
				else:
					raise FavoriteError( response['message'] if "message" in response and response['message'] else f"Something wrong when {action} the {self.username}" )
			else:
				self.throws( action, status )
		else:
			raise FavoriteError( "Can't set user as favorite before following" )
	
	#[Profile.follow()]: Object
	@avoidForMySelf
	def follow( self ):
		
		"""
		Follow or follow user.
		
		:return Object
			Follow result represent
		:raises FollowError
			When you trying to follow yourself, this is ambigue bro!
			When something wrong, please to check the request response history
		"""
		
		if  self.isMySelf:
			raise FollowError( "Unable to follow or unfollow yourself" )
		self.headers.update({
			"Accept-Encoding": "gzip, deflate, br",
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/{}/".format( self.username )
		})
		data = {
			"container_module": "\x70\x72\x6f\x66\x69\x6c\x65",
			"nav_chain": "\x50\x6f\x6c\x61\x72\x69\x73\x50\x72\x6f\x66\x69\x6c\x65\x52\x6f\x6f\x74\x3a\x70\x72\x6f\x66\x69\x6c\x65\x50\x61\x67\x65\x3a\x31\x3a\x76\x69\x61\x5f\x63\x6f\x6c\x64\x5f\x73\x74\x61\x72\x74",
			"user_id": self.id
		}
		if  self.followedByViewer:
			target = f"https://www.instagram.com/api/v1/friendships/destroy/{self.id}/"
			action = "Unfollow"
		elif self.requestedByViewer:
			target = f"https://www.instagram.com/api/v1/friendships/destroy/{self.id}/"
			action = "Cancel request follow"
		else:
			target = f"https://www.instagram.com/api/v1/friendships/create/{self.id}/"
			action = "Following"
		request = self.request.post( target, data=data )
		status = request.status_code
		if  status == 200:
			response = request.json()
			if  "friendship_status" in response:
				follow = response['friendship_status']
				self.__profile__.requested_by_viewer = follow['outgoing_request']
				self.__profile__.outgoing_request = follow['outgoing_request']
				self.__profile__.incoming_request = follow['incoming_request']
				self.__profile__.followed_by_viewer = follow['following']
				self.__profile__.is_private = follow['is_private']
				return Object({
					"id": self.id,
					"private": self.isPrivateAccount,
					"username": self.username,
					"following": self.followedByViewer,
					"requested": self.requestedByViewer
				})
			else:
				raise FollowError( response['message'] if "message" in response and response['message'] else f"Something wrong when {action} the {self.username}" )
		else:
			self.throws( action, status )
	
	#[Profile.profilePictureSave( String name, Bool random )]: Object
	def profilePictureSave( self, name=None, random=False ):
		
		"""
		Download profile picture user.
		
		:return Object
			Download result represent
		:raise ProfileError
			When the user has no profile picture
		"""
		
		if  self['has_anonymous_profile_picture']:
			raise ProfileError( "User has no profile picture" )
		if  not isinstance( name, str ):
			if  random:
				name = String.random( 32 )
				name += "-{}".format( self.profilePictureHDResolution )
			else:
				name = "{} ({}) {}".format( self.fullname, self.username, self.profilePictureHDResolution )
		if  name[0] != "/":
			fname = Config.ONSAVED.media.profile.format( name )
		else:
			fname = "{}.json".format( name )
		self.request.save( url := self.profilePictureHD, fname, fmode="wb" )
		return Object({
			"url": url,
			"fmode": "wb",
			"fname": name,
			"saved": fname
		})
	
	#[Profile.remove()]: Object
	@avoidForMySelf
	def remove( self ):
		
		"""
		Remove user from followers.
		
		:return Object
			Remove result represent
		:raises ProfileError
			When you trying to remove yourself from follower lists, this is ambigue bro!
			When the user does not following your account
			When something wrong, please to check the request response history
		"""
		
		if  not self.followsViewer:
			raise ProfileError( "This user does not following your account" )
		elif self.isMySelf:
			raise ProfileError( "Unable to remove yourself from follower" )
		else:
			self.headers.update({
				"Content-Type": "application/x-www-form-urlencoded",
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/{}/followers/".format( self.viewer.username )
			})
			request = self.request.post( "https://www.instagram.com/api/v1/web/friendships/{}/remove_follower/".format( self.id ), data={} )
			status = request.status_code
			if  status == 200:
				response = request.json()
				if  "status" in response and response['status'] == "ok":
					self.__profile__.follows_viewer = False
					return Object({
						"id": self.id,
						"username": self.username,
						"followed": False
					})
				else:
					raise FollowError( response['message'] if "message" in response and response['message'] else f"Something wrong when remove {self.username} from follower" )
			else:
				self.throws( "Remove follower", status )
	
	#[Profile.report( Dict|Object options )]: Object
	@avoidForMySelf
	def report( self, options ):
		
		"""
		Report user account.
		
		THIS FUNCTIONALITY CURRENTLY IS DEPRECATED
		THIS JUST WASTE MY TIME BROOOO!
		
		:return Object
			Report result represent
		:raises ReportError
			Report result representation
		"""
	
	#[Profile.restrict()]: Object
	@avoidForMySelf
	def restrict( self ):
		
		"""
		Restrict or unrestrict user.
		
		:return Object
			Restrict result represent
		:raises RestrictError
			When you trying to restrict yourself
			When something wrong, please to check the request response history
		"""
		
		if  self.isMySelf:
			raise RestrictError( "Unable to restrict or unrestrict yourself" )
		self.headers.update({
			"Accept-Encoding": "gzip, deflate, br",
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/{}/".format( self.username )
		})
		if  self.restrictedByViewer:
			action = "Restrict"
			target = "https://www.instagram.com/api/v1/web/restrict_action/restrict/"
		else:
			action = "Unrestrict"
			target = "https://www.instagram.com/api/v1/web/restrict_action/unrestrict/"
		data = { "target_user_id": self.id }
		request = self.request.post( target, data=data )
		status = request.status_code
		if  status == 200:
			response = request.json()
			if  "status" in response and response['status'] == "ok":
				self.__profile__.restricted_by_viewer = False if self.restrictedByViewer else True
				return Object({
					"id": self.id,
					"username": self.username,
					"restrict": self.restrictedByViewer
				})
			else:
				raise RestrictError( response['message'] if "message" in response and response['message'] else f"Something wrong when {action} the {self.username}" )
		else:
			self.throws( action, status )
		pass
	
	#[Profile.throws( String action, int status )]: None
	def throws( self, action, status ):
		
		"""
		Raises common errors in when request.
		
		:params String action
			Request action
		:params Int status
			Request response satus code
		
		:return None
		:raises UserNotFoundError
			When the user does not found
			This usually happens because of a typo error in the url
		:raises UserError
			When something wrong on request action, please to check the request response history
		"""
		
		match status:
			case 404:
				raise UserNotFoundError( f"Target \"{self.username}\" user not found" )
			case _:
				raise UserError( f"An error occurred while {action} the user [{status}]" )
	