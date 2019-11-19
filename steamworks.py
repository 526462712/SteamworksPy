#================================================
# Steamworks For Python
#================================================
from ctypes import *
import sys, os
#------------------------------------------------
# User Status
#------------------------------------------------
FriendFlags = {  # regular friend
	'None': 0x00,
	'Blocked': 0x01,
	'FriendshipRequested': 0x02,
	'Immediate': 0x04,
	'ClanMember': 0x08,
	'OnGameServer': 0x10,
	'RequestingFriendship': 0x80,
	'RequestingInfo': 0x100,
	'Ignored': 0x200,
	'IgnoredFriend': 0x400,
	'Suggested': 0x800,
	'All': 0xFFFF,
	}
#------------------------------------------------
# Main Steam Class, obviously
#------------------------------------------------
class Steam:
	# Set some basic variables for the Steam class
	cdll = None
	warn = False
	loaded = False
	# Initialize Steam
	@staticmethod
	def Init():
		os.environ['LD_LIBRARY_PATH'] = os.getcwd()
		# Check system architecture
		# This may need refined, might not work so well in Windows
		if (sys.maxsize > 2**32) is False:
			OS_BIT = '32bits'
		else:
			OS_BIT = '64bits'
		# Loading SteamworksPy API for Linux
		if sys.platform == 'linux' or sys.platform == 'linux2':
			Steam.cdll = CDLL(os.path.join(os.getcwd(), "SteamworksPy.so"))
			print("INFO: SteamworksPy loaded for Linux")
			Steam.loaded = True
		# Loading SteamworksPy API for Mac
		elif sys.platform == 'darwin':
			Steam.cdll = CDLL(os.path.join(os.getcwd(), "SteamworksPy.dylib" ))
			print("INFO: SteamworksPy loaded for Mac")
			Steam.loaded = True
		# Loading SteamworksPy API for Windows
		elif sys.platform == 'win32':
			# Check Windows architecture
			if OS_BIT == '32bits':
				Steam.cdll = CDLL(os.path.join(os.getcwd(), "SteamworksPy.dll"))
			else:
				Steam.cdll = CDLL(os.path.join(os.getcwd(), "SteamworksPy64.dll"))
			print("INFO: SteamworksPy loaded for Windows")
			Steam.loaded = True
		# Unrecognized platform, warn user, do not load Steam API
		else:
			print("ERROR: SteamworksPy failed to load (unsupported platform!)")
			Steam.warn = True
			return
		# Set restype for initialization
		Steam.cdll.IsSteamRunning.restype = c_bool
		# Check that Steam is running
		if Steam.cdll.IsSteamRunning():
			print("INFO: Steam is running")
		else:
			print("ERROR: Steam is not running")
		# Boot up the Steam API 
		if Steam.cdll.SteamInit() == 0:
			print("INFO: Steamworks initialized!")
		else:
			print("ERROR: Steamworks failed to initialize!")
		#----------------------------------------
		# Restypes and Argtypes
		#----------------------------------------
		#
		# Set restype for Apps functions
		Steam.cdll.IsSubscribed.restype = bool
		Steam.cdll.IsLowViolence.restype = bool
		Steam.cdll.IsCybercafe.restype = bool
		Steam.cdll.IsVACBanned.restype = bool
		Steam.cdll.IsAppInstalled.restype = bool
		Steam.cdll.GetCurrentGameLanguage.restype = c_char_p
		Steam.cdll.GetAvailableGameLanguages.restype = c_char_p
		Steam.cdll.IsSubscribedApp.restype = bool
		Steam.cdll.IsDLCInstalled.restype = bool
		Steam.cdll.GetEarliestPurchaseUnixTime.restype = int
		Steam.cdll.IsSubscribedFromFreeWeekend.restype = bool
		Steam.cdll.GetDLCCount.restype = int
		Steam.cdll.InstallDLC.restype = None
		Steam.cdll.UninstallDLC.restype = None
		Steam.cdll.MarkContentCorrupt.restype = bool
		Steam.cdll.GetAppInstallDir.restype = c_char_p
		Steam.cdll.IsAppInstalled.restype = bool
		Steam.cdll.GetAppOwner.restype = int
		Steam.cdll.GetLaunchQueryParam.restype = c_char_p
		Steam.cdll.GetAppBuildId.restype = int
		Steam.cdll.GetFileDetails.restype = None
		# Set restype for Controller functions
		Steam.cdll.ActivateActionSet.restype = None
		Steam.cdll.GetActionSetHandle.restype = c_uint64
#		Steam.cdll.GetAnalogActionData.restype = dictionary?
		Steam.cdll.GetAnalogActionHandle.restype = c_uint64
#		Steam.cdll.GetAnalogActionOrigins.restype = array?
#		Steam.cdll.GetConnectedControllers.restype = array?
		Steam.cdll.GetControllerForGamepadIndex.restype = c_uint64
		Steam.cdll.GetCurrentActionSet.restype = c_uint64
		Steam.cdll.GetInputTypeForHandle.restype = c_uint64
#		Steam.cdll.GetDigitalActionData.restype = dictionary?
		Steam.cdll.GetDigitalActionHandle.restype = c_uint64
#		Steam.cdll.GetDigitalActionOrigins.restype = array?
		Steam.cdll.GetGamepadIndexForController.restype = int
#		Steam.cdll.GetMotionData.restype = dictionary?
		Steam.cdll.ControllerInit.restype = bool
		Steam.cdll.RunFrame.restype = None
		Steam.cdll.ShowBindingPanel.restype = bool
		Steam.cdll.ControllerShutdown.restype = bool
		Steam.cdll.TriggerVibration.restype = None
		# Set restype for Music functions
		Steam.cdll.MusicIsEnabled.restype = None
		Steam.cdll.MusicIsPlaying.restype = None
		Steam.cdll.MusicGetVolume.restype = c_float
		Steam.cdll.MusicPause.restype = None
		Steam.cdll.MusicPlay.restype = None
		Steam.cdll.MusicPlayNext.restype = None
		Steam.cdll.MusicPlayPrev.restype = None
		Steam.cdll.MusicSetVolume.restype = None
		# Set restype for Screenshot functions
		Steam.cdll.AddScreenshotToLibrary.restype = c_uint32
		Steam.cdll.HookScreenshots.restype = None
		Steam.cdll.IsScreenshotsHooked.restype = bool
		Steam.cdll.SetLocation.restype = bool
		Steam.cdll.TriggerScreenshot.restype = None
		# Set restype for UGC functions
		Steam.cdll.DownloadItem.restype = bool
		Steam.cdll.SuspendDownloads.restype = None
		Steam.cdll.StartItemUpdate.restype = c_uint64
		Steam.cdll.GetItemState.restype = int
		Steam.cdll.CreateItem.restype = None
		Steam.cdll.SetItemTitle.restype = bool
		Steam.cdll.SetItemDescription.restype = bool
		Steam.cdll.SetItemUpdateLanguage.restype = bool
		Steam.cdll.SetItemUpdateLanguage.restype = bool
		Steam.cdll.SetItemMetadata.restype = bool
		Steam.cdll.SetItemMetadata.restype = bool
		Steam.cdll.SetItemVisibility.restype = bool
		Steam.cdll.SetItemContent.restype = bool
		Steam.cdll.SetItemPreview.restype = bool
		Steam.cdll.SubmitItemUpdate.restype = None
		# Set restype for User functions
		Steam.cdll.GetSteamID.restype = c_uint64
		Steam.cdll.LoggedOn.restype = bool
		Steam.cdll.GetPlayerSteamLevel.restype = int
		Steam.cdll.GetUserDataFolder.restype = c_char_p
		Steam.cdll.GetGameBadgeLevel.restype = int
		# Set restype for Utils functions
		Steam.cdll.OverlayNeedsPresent.restype = bool
		Steam.cdll.GetAppID.restype = int
		Steam.cdll.GetCurrentBatteryPower.restype = int
		Steam.cdll.GetIPCCallCount.restype = c_uint32
		Steam.cdll.GetIPCountry.restype = c_char_p
		Steam.cdll.GetSecondsSinceAppActive.restype = int
		Steam.cdll.GetSecondsSinceComputerActive.restype = int
		Steam.cdll.GetServerRealTime.restype = int
		Steam.cdll.GetSteamUILanguage.restype = c_char_p
		Steam.cdll.IsOverlayEnabled.restype = bool
		Steam.cdll.IsSteamInBigPictureMode.restype = bool
		Steam.cdll.IsSteamRunningInVR.restype = bool
		Steam.cdll.IsVRHeadsetStreamingEnabled.restype = bool
		Steam.cdll.SetOverlayNotificationInset.restype = None
		Steam.cdll.SetOverlayNotificationPosition.restype = None
		Steam.cdll.SetVRHeadsetStreamingEnabled.restype = None
		Steam.cdll.ShowGamepadTextInput.restype = bool
		Steam.cdll.StartVRDashboard.restype = None
		
	# Is Steam loaded
	@staticmethod
	def IsSteamLoaded():
		if not Steam.cdll and not Steam.warn:
			print("Steam is not loaded")
			Steam.warn = True
			return False
		else:
			return True
	# Yeah
	@staticmethod
	def Call(method):
		if Steam.IsSteamLoaded():
			return method()
		else:
			return False
	# Running callbacks
	@staticmethod
	def RunCallbacks():
		if Steam.IsSteamLoaded():
			Steam.cdll.RunCallbacks()
			return True
		else:
			return False

#------------------------------------------------
# Class for Steam Apps
#------------------------------------------------
class SteamApps:
	# Checks if the active user is subscribed to the current App ID.
	@staticmethod
	def IsSubscribed():
		if Steam.IsSteamLoaded():
			return Steam.cdll.IsSubscribed()
		else:
			return False
	# Checks if the license owned by the user provides low violence depots.
	@staticmethod
	def IsLowViolence():
		if Steam.IsSteamLoaded():
			return Steam.cdll.IsLowViolence()
		else:
			return False
	# Checks whether the current App ID is for Cyber Cafes.
	@staticmethod
	def IsCybercafe():
		if Steam.IsSteamLoaded():
			return Steam.cdll.IsCybercafe()
		else:
			return False
	# Checks if the user has a VAC ban on their account.
	@staticmethod
	def IsVACBanned():
		if Steam.IsSteamLoaded():
			return Steam.cdll.IsVACBanned()
		else:
			return "None"
	# Gets the current language that the user has set.
	@staticmethod
	def GetCurrentGameLanguage():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetCurrentGameLanguage()
		else:
			return "None"
	# Gets a comma separated list of the languages the current app supports.
	@staticmethod
	def GetAvailableGameLanguages():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetAvailableGameLanguages()
		else:
			return "None"
	# Checks if the active user is subscribed to a specified AppId.
	@staticmethod
	def IsSubscribedApp(appID):
		if Steam.IsSteamLoaded():
			return Steam.cdll.IsSubscribedApp(appID)
		else:
			return False
	# Checks if the user owns a specific DLC and if the DLC is installed.
	@staticmethod
	def IsDLCInstalled(dlcID):
		if Steam.IsSteamLoaded():
			return Steam.cdll.IsDLCInstalled(dlcID)
		else:
			return False
	# Gets the time of purchase of the specified app in Unix epoch format (time since Jan 1st, 1970).
	@staticmethod
	def GetEarliestPurchaseUnixTime(appID):
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetEarliestPurchaseUnixTime(appID)
		else:
			return 0
	# Checks if the user is subscribed to the current app through a free weekend.
	# This function will return false for users who have a retail or other type of license.
	# Suggested you contact Valve on how to package and secure your free weekend properly.
	@staticmethod
	def IsSubscribedFromFreeWeekend():
		if Steam.IsSteamLoaded():
			return Steam.cdll.IsSubscribedFromFreeWeekend()
		else:
			return False
	# Get the number of DLC the user owns for a parent application/game.
	@staticmethod
	def GetDLCCount():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetDLCCount()
		else:
			return 0
	# Allows you to install an optional DLC.
	@staticmethod
	def InstallDLC(dlcID):
		if Steam.IsSteamLoaded():
			return Steam.cdll.InstallDLC(dlcID)
		else:
			return
	# Allows you to uninstall an optional DLC.
	@staticmethod
	def UninstallDLC(dlcID):
		if Steam.IsSteamLoaded():
			return Steam.cdll.UninstallDLC(dlcID)
		else:
			return
	# Allows you to force verify game content on next launch.
	@staticmethod
	def MarkContentCorrupt(missingFilesOnly):
		if Steam.IsSteamLoaded():
			return Steam.cdll.MarkContentCorrupt(missingFilesOnly)
		else:
			return False
	# Gets the install folder for a specific AppID.
	@staticmethod
	def GetAppInstallDir(appID):
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetAppInstallDir(appID)
		else:
			return ""
	# Check if given application/game is installed, not necessarily owned.
	@staticmethod
	def IsAppInstalled(appID):
		if Steam.IsSteamLoaded():
			return Steam.cdll.IsAppInstalled(appID)
		else:
			return False
	# Gets the Steam ID of the original owner of the current app. If it's different from the current user then it is borrowed.
	@staticmethod
	def GetAppOwner():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetAppOwner()
		else:
			return 0
	# Gets the associated launch parameter if the game is run via steam://run/<appid>/?param1=value1;param2=value2;param3=value3 etc.
	@staticmethod
	def GetLaunchQueryParam(key):
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetLaunchQueryParam(key)
		else:
			return ""
	# Return the build ID for this app; will change based on backend updates.
	@staticmethod
	def GetAppBuildId():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetAppBuildId()
		else:
			return 0
	# Asynchronously retrieves metadata details about a specific file in the depot manifest.
	@staticmethod
	def GetFileDetails(filename):
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetFileDetails(filename)
		else:
			return

#------------------------------------------------
# Class for Steam Controller
#------------------------------------------------
class SteamController:
	# Reconfigure the controller to use the specified action set.
	@staticmethod
	def ActivateActionSet(controllerHandle, actionSetHandle):
		if Steam.IsSteamLoaded():
			return Steam.cdll.ActivateActionSet()
		else:
			return
	# Lookup the handle for an Action Set.
	@staticmethod
	def GetActionSetHandle(actionSetName):
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetActionSetHandle(actionSetName)
		else:
			return 0
	# Returns the current state of the supplied analog game action.
#	@staticmethod
#	def GetAnalogActionData(controllerHandle, analogActionHandle):
#		if Steam.IsSteamLoaded():
#			return Steam.cdll.GetAnalogActionData(controllerHandle, analogActionHandle)
#		else:
#			return ""
	# Get the handle of the specified Analog action.
	@staticmethod
	def GetAnalogActionHandle(actionName):
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetAnalogActionHandle(actionName)
		else:
			return 0
	# Get the origin(s) for an analog action within an action.
#	@staticmethod
#	def GetAnalogActionOrigins(controllerHandle, actionSetHandle, analogActionHandle):
#		if Steam.IsSteamLoaded():
#			return Steam.cdll.GetAnalogActionOrigins(controllerHandle, actionSetHandle, analogActionHandle)
#		else:
#			return []
	# Get current controllers handles.
#	@staticmethod
#	def GetConnectedControllers():
#		if Steam.IsSteamLoaded():
#			return Steam.cdll.GetConnectedControllers()
#		else:
#			return []
	# Returns the associated controller handle for the specified emulated gamepad.
	@staticmethod
	def GetControllerForGamepadIndex(index):
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetControllerForGamepadIndex(index)
		else:
			return 0
	# Get the currently active action set for the specified controller.
	@staticmethod
	def GetCurrentActionSet(controllerHandle):
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetCurrentActionSet(controllerHandle)
		else:
			return 0
	# Get the input type (device model) for the specified controller. 
	@staticmethod
	def GetInputTypeForHandle(controllerHandle):
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetInputTypeForHandle(controllerHandle)
		else:
			return 0
	# Returns the current state of the supplied digital game action.
#	@staticmethod
#	def GetDigitalActionData(controllerHandle, digitalActionHandle):
#		if Steam.IsSteamLoaded():
#			return Steam.cdll.GetDigitalActionData(controllerHandle, digitalActionHandle)
#		else:
#			return {}
	# Get the handle of the specified digital action. 
	@staticmethod
	def GetDigitalActionHandle(actionName):
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetDigitalActionHandle(actionName)
		else:
			return 0
	# Get the origin(s) for an analog action within an action.
#	@staticmethod
#	def GetDigitalActionOrigins(controllerHandle, actionSetHandle, digitalActionHandle):
#		if Steam.IsSteamLoaded():
#			return Steam.cdll.GetDigitalActionOrigins(controllerHandle, actionSetHandle, digitalActionHandle)
#		else:
#			return []
	# Returns the associated gamepad index for the specified controller.
	@staticmethod
	def GetGamepadIndexForController(controllerHandle):
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetGamepadIndexForController(controllerHandle)
		else:
			return 0
	# Returns raw motion data for the specified controller.
#	@staticmethod
#	def GetMotionData(controllerHandle):
#		if Steam.IsSteamLoaded():
#			return Steam.cdll.GetMotionData(controllerHandle)
#		else:
#			return {}
	# Start SteamControllers interface.
	@staticmethod
	def ControllerInit():
		if Steam.IsSteamLoaded():
			return Steam.cdll.ControllerInit()
		else:
			return False
	# Syncronize controllers.
	@staticmethod
	def RunFrame():
		if Steam.IsSteamLoaded():
			return Steam.cdll.RunFrame()
		else:
			return
	# Invokes the Steam overlay and brings up the binding screen.
	@staticmethod
	def ShowBindingPanel(controllerHandle):
		if Steam.IsSteamLoaded():
			return Steam.cdll.ShowBindingPanel(controllerHandle)
		else:
			return False
	# Stop SteamControllers interface.
	@staticmethod
	def ControllerShutdown():
		if Steam.IsSteamLoaded():
			return Steam.cdll.ControllerShutdown()
		else:
			return False
	# Trigger a vibration event on supported controllers.
	@staticmethod
	def TriggerVibration(controllerHandle):
		if Steam.IsSteamLoaded():
			return Steam.cdll.TriggerVibration(controllerHandle, leftSpeed, rightSpeed)
		else:
			return

#------------------------------------------------
# Class for Steam Music
#------------------------------------------------
class SteamMusic:
	# Is Steam music enabled.
	@staticmethod
	def MusicIsEnabled():
		if Steam.IsSteamLoaded():
			return Steam.cdll.MusicIsEnabled()
		else:
			return False
	# Is Steam music playing something.
	@staticmethod
	def MusicIsPlaying():
		if Steam.IsSteamLoaded():
			return Steam.cdll.MusicIsPlaying()
		else:
			return False
	# Get the volume level of the music.
	@staticmethod
	def MusicGetVolume():
		if Steam.IsSteamLoaded():
			return Steam.cdll.MusicGetVolume()
		else:
			return 0
	# Pause whatever Steam music is playing.
	@staticmethod
	def MusicPause():
		if Steam.IsSteamLoaded():
			return Steam.cdll.MusicPause()
		else:
			return
	# Play current track/album.
	@staticmethod
	def MusicPlay():
		if Steam.IsSteamLoaded():
			return Steam.cdll.MusicPlay()
		else:
			return
	# Play next track/album.
	@staticmethod
	def MusicPlayNext():
		if Steam.IsSteamLoaded():
			return Steam.cdll.MusicPlayNext()
		else:
			return
	# Play previous track/album.
	@staticmethod
	def MusicPlayPrev():
		if Steam.IsSteamLoaded():
			return Steam.cdll.MusicPlayPrev()
		else:
			return
	# Set the volume of Steam music.
	@staticmethod
	def MusicSetVolume(volume):
		if Steam.IsSteamLoaded():
			return Steam.cdll.MusicSetVolume(volume)
		else:
			return

#------------------------------------------------
# Class for Steam Screenshots
#------------------------------------------------
class SteamScreenshots:
	# Adds a screenshot to the user's Steam screenshot library from disk.
	@staticmethod
	def AddScreenshotToLibrary(filename, thumbnailFilename, width, height):
		if Steam.IsSteamLoaded():
			return Steam.cdll.AddScreenshotToLibrary(filename, thumbnailFilename, width, height)
		else:
			return 0
	# Toggles whether the overlay handles screenshots.
	@staticmethod
	def HookScreenshots(hook):
		if Steam.IsSteamLoaded():
			return Steam.cdll.HookScreenshots(hook)
		else:
			return
	# Checks if the app is hooking screenshots.
	@staticmethod
	def IsScreenshotsHooked():
		if Steam.IsSteamLoaded():
			return Steam.cdll.IsScreenshotsHooked()
		else:
			return False
	# Sets optional metadata about a screenshot's location.
	@staticmethod
	def SetLocation(screenshot, location):
		if Steam.IsSteamLoaded():
			return Steam.cdll.SetLocation(screenshot, location)
		else:
			return False
	# Causes Steam overlay to take a screenshot.
	@staticmethod
	def TriggerScreenshot():
		if Steam.IsSteamLoaded():
			return Steam.cdll.TriggerScreenshot()
		else:
			return

#------------------------------------------------
# Class for Steam UGC / Workshop
#------------------------------------------------
class SteamUGC:
	# Download new or update already installed item. If returns true, wait for DownloadItemResult_t. If item is already installed, then files on disk should not be used until callback received.
	# If item is not subscribed to, it will be cached for some time. If bHighPriority is set, any other item download will be suspended and this item downloaded ASAP.
	@staticmethod
	def DownloadItem(publishedFileID, highPriority):
		if Steam.IsSteamLoaded():
			return Steam.cdll.DownloadItem(publishedFileID, highPriority)
		else:
			return False
	# SuspendDownloads( true ) will suspend all workshop downloads until SuspendDownloads( false ) is called or the game ends.
	@staticmethod
	def SuspendDownloads(suspend):
		if Steam.IsSteamLoaded():
			return Steam.cdll.SuspendDownloads(suspend)
		else:
			return
	# Starts the item update process.
	@staticmethod
	def StartItemUpdate(appID, publishedFileID):
		if Steam.IsSteamLoaded():
			return Steam.cdll.StartItemUpdate(appID, publishedFileID)
		else:
			return 0
	# Gets the current state of a workshop item on this client.
	@staticmethod
	def GetItemState(publishedFileID):
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetItemState(publishedFileID)
		else:
			return 0
	# Creating a workshop item.
	@staticmethod
	def CreateItem(appID, fileType):
		if Steam.IsSteamLoaded():
			return Steam.cdll.CreateItem(appID, fileType)
		else:
			return
	# Sets a new title for an item.
	@staticmethod
	def SetItemTitle(updateHandle, title):
		if Steam.IsSteamLoaded():
			return Steam.cdll.SetItemTitle(updateHandle, title)
		else:
			return False
	# Sets a new description for an item.
	@staticmethod
	def SetItemDescription(updateHandle, description):
		if Steam.IsSteamLoaded():
			return Steam.cdll.SetItemDescription(updateHandle, description)
		else:
			return False
	# Sets the language of the title and description that will be set in this item update.
	@staticmethod
	def SetItemUpdateLanguage(updateHandle, language):
		if Steam.IsSteamLoaded():
			return Steam.cdll.SetItemUpdateLanguage(updateHandle, language)
		else:
			return False

	# Sets arbitrary metadata for an item. This metadata can be returned from queries without having to download and install the actual content.
	@staticmethod
	def SetItemMetadata(updateHandle, metadata):
		if Steam.IsSteamLoaded():
			return Steam.cdll.SetItemMetadata(updateHandle, metadata)
		else:
			return False
	# Sets the visibility of an item.
	@staticmethod
	def SetItemVisibility(updateHandle, visibility):
		if Steam.IsSteamLoaded():
			return Steam.cdll.SetItemVisibility(updateHandle, visibility)
		else:
			return False
	# Sets the folder that will be stored as the content for an item.
	@staticmethod
	def SetItemContent(updateHandle, contentFolder):
		if Steam.IsSteamLoaded():
			return Steam.cdll.SetItemContent(updateHandle, contentFolder)
		else:
			return False
	# Sets the primary preview image for the item.
	@staticmethod
	def SetItemPreview(updateHandle, previewFile):
		if Steam.IsSteamLoaded():
			return Steam.cdll.SetItemPreview(updateHandle, previewFile)
		else:
			return False
	# Uploads the changes made to an item to the Steam Workshop; to be called after setting your changes.
	@staticmethod
	def SubmitItemUpdate(updateHandle, changeNote):
		if Steam.IsSteamLoaded():
			return Steam.cdll.SubmitItemUpdate(updateHandle, changeNote)
		else:
			return
#------------------------------------------------
# Class for Steam Users
#------------------------------------------------
class SteamUsers:
	# Get user's Steam ID.
	@staticmethod
	def GetSteamID():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetSteamID()
		else:
			return 0
	# Check, true/false, if user is logged into Steam currently.
	@staticmethod
	def LoggedOn():
		if Steam.IsSteamLoaded():
			return Steam.cdll.LoggedOn()
		else:
			return False
	# Get the user's Steam level.
	@staticmethod
	def GetPlayerSteamLevel():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetPlayerSteamLevel()
		else:
			return 0
	# Get the user's Steam installation path (this function is depreciated).
	@staticmethod
	def GetUserDataFolder():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetUserDataFolder()
		else:
			return ""
	# Trading Card badges data access, if you only have one set of cards, the series will be 1.
	# The user has can have two different badges for a series; the regular (max level 5) and the foil (max level 1).
	@staticmethod
	def GetGameBadgeLevel(series, foil):
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetGameBadgeLevel(series, foil)
		else:
			return 0

#------------------------------------------------
# Class for Steam Utils
#------------------------------------------------
class SteamUtils:
	# Checks if the Overlay needs a present. Only required if using event driven render updates.
	@staticmethod
	def OverlayNeedsPresent():
		if Steam.IsSteamLoaded():
			return Steam.cdll.OverlayNeedsPresent()
		else:
			return False
	# Get the Steam ID of the running application/game.
	@staticmethod
	def GetAppID():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetAppID()
		else:
			return 0
	# Get the amount of battery power, clearly for laptops.
	@staticmethod
	def GetCurrentBatteryPower():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetCurrentBatteryPower()
		else:
			return 0
	# Returns the number of IPC calls made since the last time this function was called.
	@staticmethod
	def GetIPCCallCount():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetIPCCallCount()
		else:
			return 0
	# Get the user's country by IP.
	@staticmethod
	def GetIPCountry():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetIPCountry()
		else:
			return ""
	# Return amount of time, in seconds, user has spent in this session.
	@staticmethod
	def GetSecondsSinceAppActive():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetSecondsSinceAppActive()
		else:
			return 0
	# Returns the number of seconds since the user last moved the mouse.
	@staticmethod
	def GetSecondsSinceComputerActive():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetSecondsSinceComputerActive()
		else:
			return 0
	# Get the actual time.
	@staticmethod
	def GetServerRealTime():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetServerRealTime()
		else:
			return 0
	# Get the Steam user interface language.
	@staticmethod
	def GetSteamUILanguage():
		if Steam.IsSteamLoaded():
			return Steam.cdll.GetSteamUILanguage()
		else:
			return ""
	# Returns true/false if Steam overlay is enabled.
	@staticmethod
	def IsOverlayEnabled():
		if Steam.IsSteamLoaded():
			return Steam.cdll.IsOverlayEnabled()
		else:
			return False
	# Returns true if Steam & the Steam Overlay are running in Big Picture mode.
	@staticmethod
	def IsSteamInBigPictureMode():
		if Steam.IsSteamLoaded():
			return Steam.cdll.IsSteamInBigPictureMode()
		else:
			return False
	# Is Steam running in VR?
	@staticmethod
	def IsVRHeadsetStreamingEnabled():
		if Steam.IsSteamLoaded():
			return Steam.cdll.IsVRHeadsetStreamingEnabled()
		else:
			return False
	# Sets the inset of the overlay notification from the corner specified by SetOverlayNotificationPosition.
	@staticmethod
	def SetOverlayNotificationInset(horizontal, vertical):
		if Steam.IsSteamLoaded():
			return Steam.cdll.SetOverlayNotificationInset(horizontal, vertical)
		else:
			return
	# Set the position where overlay shows notifications.
	@staticmethod
	def SetOverlayNotificationPosition(pos):
		if Steam.IsSteamLoaded():
			return Steam.cdll.SetOverlayNotificationPosition(pos)
		else:
			return
	# Set whether the HMD content will be streamed via Steam In-Home Streaming.
	@staticmethod
	def SetVRHeadsetStreamingEnabled(enabled):
		if Steam.IsSteamLoaded():
			return Steam.cdll.SetVRHeadsetStreamingEnabled(enabled)
		else:
			return
	# Activates the Big Picture text input dialog which only supports gamepad input.
	@staticmethod
	def ShowGamepadTextInput(inputMode, lineInputMode, description, maxText, presetText):
		if Steam.IsSteamLoaded():
			return Steam.cdll.ShowGamepadTextInput()
		else:
			return False
	# Ask SteamUI to create and render its OpenVR dashboard.
	@staticmethod
	def StartVRDashboard():
		if Steam.IsSteamLoaded():
			return Steam.cdll.StartVRDashboard()
		else:
			return