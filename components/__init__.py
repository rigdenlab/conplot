from enum import Enum


class EmailIssueReference(Enum):
    BUG = '1'
    FORGOT_PSSWRD = '2'
    OTHER = '3'


def SessionStoreModal(*args, **kwargs):
    from components.modals import SessionStoreModal

    return SessionStoreModal(*args, **kwargs)


def SuccessContactFormModal(*args, **kwargs):
    from components.modals import SuccessContactFormModal

    return SuccessContactFormModal(*args, **kwargs)


def InvalidContactFormModal(*args, **kwargs):
    from components.modals import InvalidContactFormModal

    return InvalidContactFormModal(*args, **kwargs)


def SlackConnectionErrorModal(*args, **kwargs):
    from components.modals import SlackConnectionErrorModal

    return SlackConnectionErrorModal(*args, **kwargs)


def MissingInputModal(*args, **kwargs):
    from components.modals import MissingInputModal

    return MissingInputModal(*args, **kwargs)


def RepeatedInputModal(*args, **kwargs):
    from components.modals import RepeatedInputModal

    return RepeatedInputModal(*args, **kwargs)


def InvalidFormatModal(*args, **kwargs):
    from components.modals import InvalidFormatModal

    return InvalidFormatModal(*args, **kwargs)


def InvalidInputModal(*args, **kwargs):
    from components.modals import InvalidInputModal

    return InvalidInputModal(*args, **kwargs)


def SessionTimedOutModal(*args, **kwargs):
    from components.modals import SessionTimedOutModal

    return SessionTimedOutModal(*args, **kwargs)


def MismatchModal(*args, **kwargs):
    from components.modals import MismatchModal

    return MismatchModal(*args, **kwargs)


def SuccesfulLoginToast(*args, **kwargs):
    from components.toasts import SuccesfulLoginToast

    return SuccesfulLoginToast(*args, **kwargs)


def SuccesfulLogoutToast(*args, **kwargs):
    from components.toasts import SuccesfulLogoutToast

    return SuccesfulLogoutToast(*args, **kwargs)


def StoredSessionsList(*args, **kwargs):
    from components.listgrpoups import StoredSessionsList

    return StoredSessionsList(*args, **kwargs)


def SessionTimedOutToast(*args, **kwargs):
    from components.toasts import SessionTimedOutToast

    return SessionTimedOutToast(*args, **kwargs)


def SuccesfulSessionDeleteToast(*args, **kwargs):
    from components.toasts import SuccesfulSessionDeleteToast

    return SuccesfulSessionDeleteToast(*args, **kwargs)


def SuccesfulSessionLoadToast(*args, **kwargs):
    from components.toasts import SuccesfulSessionLoadToast

    return SuccesfulSessionLoadToast(*args, **kwargs)


def InvalidLoginCollapse(*args, **kwargs):
    from components.collapse import InvalidLoginCollapse

    return InvalidLoginCollapse(*args, **kwargs)


def InvalidNewUserCollapse(*args, **kwargs):
    from components.collapse import InvalidNewUserCollapse

    return InvalidNewUserCollapse(*args, **kwargs)


def InvalidAddTrackCollapse(*args, **kwargs):
    from components.collapse import InvalidAddTrackCollapse

    return InvalidAddTrackCollapse(*args, **kwargs)


def InvalidFileCollapse(*args, **kwargs):
    from components.collapse import InvalidFileCollapse

    return InvalidFileCollapse(*args, **kwargs)


def AdditionalTracksUploadCard(*args, **kwargs):
    from components.cards import AdditionalTracksUploadCard

    return AdditionalTracksUploadCard(*args, **kwargs)


def ChangeUserPasswordCard(*args, **kwargs):
    from components.cards import ChangeUserPasswordCard

    return ChangeUserPasswordCard(*args, **kwargs)


def UserLoginCard(*args, **kwargs):
    from components.cards import UserLoginCard

    return UserLoginCard(*args, **kwargs)


def StoreSessionCard(*args, **kwargs):
    from components.cards import StoreSessionCard

    return StoreSessionCard(*args, **kwargs)


def MandatoryUploadCard(*args, **kwargs):
    from components.cards import MandatoryUploadCard

    return MandatoryUploadCard(*args, **kwargs)


def NoAdditionalTracksCard(*args, **kwargs):
    from components.cards import NoAdditionalTracksCard

    return NoAdditionalTracksCard(*args, **kwargs)


def ContactDisplayControlCard(*args, **kwargs):
    from components.cards import DisplayControlCard

    return ContactDisplayControlCard(*args, **kwargs)


def NavBar(*args, **kwargs):
    from components.navbar import NavBar

    return NavBar(*args, **kwargs)


def Header(*args, **kwargs):
    from components.headers import Header

    return Header(*args, **kwargs)


def MandatoryInputHeader(*args, **kwargs):
    from components.headers import MandatoryInputHeader

    return MandatoryInputHeader(*args, **kwargs)


def StoreSessionHeader(*args, **kwargs):
    from components.headers import StoreSessionHeader

    return StoreSessionHeader(*args, **kwargs)


def AdditionalInputHeader(*args, **kwargs):
    from components.headers import AdditionalInputHeader

    return AdditionalInputHeader(*args, **kwargs)


def DisplayControlHeader(*args, **kwargs):
    from components.headers import DisplayControlHeader

    return DisplayControlHeader(*args, **kwargs)


def UploadButton(*args, **kwargs):
    from components.buttons import UploadButton

    return UploadButton(*args, **kwargs)


def UserAccountDropdownMenu(*args, **kwargs):
    from components.misc import UserAccountDropdownMenu

    return UserAccountDropdownMenu(*args, **kwargs)


def AddTrackButton(*args, **kwargs):
    from components.buttons import AddTrackButton

    return AddTrackButton(*args, **kwargs)


def FilenameAlert(*args, **kwargs):
    from components.alerts import FilenameAlert

    return FilenameAlert(*args, **kwargs)


def SuccessChangePasswordAlert(*args, **kwargs):
    from components.alerts import SuccessChangePasswordAlert

    return SuccessChangePasswordAlert(*args, **kwargs)


def FailChangePasswordAlert(*args, **kwargs):
    from components.alerts import FailChangePasswordAlert

    return FailChangePasswordAlert(*args, **kwargs)


def SuccessCreateUserAlert(*args, **kwargs):
    from components.alerts import SuccessCreateUserAlert

    return SuccessCreateUserAlert(*args, **kwargs)


def ErrorAlert(*args, **kwargs):
    from components.alerts import ErrorAlert

    return ErrorAlert(*args, **kwargs)


def SuccessLogoutAlert(*args, **kwargs):
    from components.alerts import SuccessLogoutAlert

    return SuccessLogoutAlert(*args, **kwargs)


def ContactForgotPsswrdAlert(*args, **kwargs):
    from components.alerts import ContactForgotPsswrdAlert

    return ContactForgotPsswrdAlert(*args, **kwargs)


def SuccessLoginAlert(*args, **kwargs):
    from components.alerts import SuccessLoginAlert

    return SuccessLoginAlert(*args, **kwargs)


def PlotPlaceHolder(*args, **kwargs):
    from components.misc import PlotPlaceHolder

    return PlotPlaceHolder(*args, **kwargs)


def NoPageFoundCard(*args, **kwargs):
    from components.cards import NoPageFoundCard

    return NoPageFoundCard(*args, **kwargs)


def UserStoredSessionsCard(*args, **kwargs):
    from components.cards import UserStoredSessionsCard

    return UserStoredSessionsCard(*args, **kwargs)


def CreateUserCard(*args, **kwargs):
    from components.cards import CreateUserCard

    return CreateUserCard(*args, **kwargs)


def UserLogoutCard(*args, **kwargs):
    from components.cards import UserLogoutCard

    return UserLogoutCard(*args, **kwargs)


def DisplayControlCard(*args, **kwargs):
    from components.cards import DisplayControlCard

    return DisplayControlCard(*args, **kwargs)


def HelpToolTip(*args, **kwargs):
    from components.tooltips import HelpToolTip

    return HelpToolTip(*args, **kwargs)


def ExampleLinkBadge(*args, **kwargs):
    from components.badges import ExampleLinkBadge

    return ExampleLinkBadge(*args, **kwargs)


def HelpBadge(*args, **kwargs):
    from components.badges import HelpBadge

    return HelpBadge(*args, **kwargs)


def InvalidFormatCard(*args, **kwargs):
    from components.cards import InvalidFormatCard

    return InvalidFormatCard(*args, **kwargs)


def TrackLayoutSelector(*args, **kwargs):
    from components.inputgroups import TrackLayoutSelector

    return TrackLayoutSelector(*args, **kwargs)


def StoreSessionNameInput(*args, **kwargs):
    from components.inputgroups import StoreSessionNameInput

    return StoreSessionNameInput(*args, **kwargs)


def ContactFormatSelector(*args, **kwargs):
    from components.inputgroups import ContactFormatSelector

    return ContactFormatSelector(*args, **kwargs)


def LFactorSelector(*args, **kwargs):
    from components.inputgroups import LFactorSelector

    return LFactorSelector(*args, **kwargs)


def UserNameInput(*args, **kwargs):
    from components.inputgroups import UserNameInput

    return UserNameInput(*args, **kwargs)


def PasswordInput(*args, **kwargs):
    from components.inputgroups import PasswordInput

    return PasswordInput(*args, **kwargs)


def SizeSelector(*args, **kwargs):
    from components.inputgroups import SizeSelector

    return SizeSelector(*args, **kwargs)


def Button(*args, **kwargs):
    from components.buttons import Button

    return Button(*args, **kwargs)


def AdditionalTrackFormatSelector(*args, **kwargs):
    from components.inputgroups import AdditionalTrackFormatSelector

    return AdditionalTrackFormatSelector(*args, **kwargs)


def StartNewSessionLink(*args, **kwargs):
    from components.links import StartNewSessionLink

    return StartNewSessionLink(*args, **kwargs)


def GitHubLink(*args, **kwargs):
    from components.links import GitHubLink

    return GitHubLink(*args, **kwargs)


def ConPlotLink(*args, **kwargs):
    from components.links import ConPlotLink

    return ConPlotLink(*args, **kwargs)


def ContactBugAlert(*args, **kwargs):
    from components.alerts import ContactBugAlert

    return ContactBugAlert(*args, **kwargs)


def EmailInput(*args, **kwargs):
    from components.inputgroups import EmailInput

    return EmailInput(*args, **kwargs)


def NameInput(*args, **kwargs):
    from components.inputgroups import NameInput

    return NameInput(*args, **kwargs)


def ProblemDescriptionInput(*args, **kwargs):
    from components.inputgroups import ProblemDescriptionInput

    return ProblemDescriptionInput(*args, **kwargs)


def EmailIssueSelect(*args, **kwargs):
    from components.inputgroups import EmailIssueSelect

    return EmailIssueSelect(*args, **kwargs)
