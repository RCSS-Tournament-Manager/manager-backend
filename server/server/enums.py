from django.db.models import IntegerChoices, TextChoices


class Roles(IntegerChoices):
    ADMIN = 0, "Admin"
    OC = 1, "Operational Committee"
    TC = 2, "Technical Committee"
    LEADER = 3, "Team Leader"
    MEMBER = 4, "Team Member"
    STAFF = 5, "Team Staff"


class GroupTypes(IntegerChoices):
    POOL = 0, "Pool"
    STEPLADDER = 1, "Stepladder"


class GroupStatus(IntegerChoices):
    NO_STATUS = 0, "No Status"
    RUNNING = 1, "Running"
    ENDED = 2, "Ended"
    STOPPED = 3, "Stopped"


class TeamStatus(IntegerChoices):
    ACTIVE = 0, "Active"
    WAITING = 1, "Waiting"
    ELIMINATED = 2, "Eliminated"
    CHAMPION = 3, "Champion"


class MatchStatus(IntegerChoices):
    NO_STATUS = 0, "No Status"
    ERROR = 1, "Error"
    IN_QUEUE = 2, "In Queue"
    RUNNING = 3, "Running"
    ENDED = 4, "Ended"
    STOPPED = 5, "Stopped"


class ResultStatus(IntegerChoices):
    UPLOADED = 0, "Uploaded"
    NOT_CHECKED = 1, "Not Checked"
    PASSED = 2, "Passed"
    FAILED = 3, "Failed"


class RunnerStatus(IntegerChoices):
    NOT_RESPONDING = 0, "Not Responding"
    UP = 1, "Up"
    DOWN = 2, "Down"


class QueueStatus(IntegerChoices):
    RUNNING = 0, "Running"
    WAITING = 1, "Waiting"
    STOPPED = 2, "Stopped"


class Visibility(IntegerChoices):
    PUBLIC = 0, "Public"
    TEAM = 1, "Team"
    TECHNICAL_COMMITTEE = 2, "Technical Committee"
    PRIVATE = 3, "Private"


class ContentType(TextChoices):
    TEXT = "text/plain"
    HTML = "text/html"
    MARKDOWN = "text/markdown"
    JSON = "application/json"
    XML = "application/xml"
    CSV = "text/csv"
    PDF = "application/pdf"
    WORD = "application/msword"
    EXCEL = "application/vnd.ms-excel"
    POWERPOINT = "application/vnd.ms-powerpoint"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"
    IMAGE_GIF = "image/gif"
    AUDIO_MP3 = "audio/mpeg"
    AUDIO_WAV = "audio/wav"
    VIDEO_MP4 = "video/mp4"
    VIDEO_AVI = "video/x-msvideo"
