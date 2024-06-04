from django.db.models import IntegerChoices, TextChoices


class Roles(IntegerChoices):
    ADMIN = 0
    OC = 1
    TC = 2
    LEADER = 3
    MEMBER = 4
    STAFF = 5


class GroupTypes(IntegerChoices):
    POOL = 0
    STEPLADDER = 1


class GroupStatus(IntegerChoices):
    NO_STATUS = 0
    RUNNING = 1
    ENDED = 2
    STOPPED = 3


class TeamStatus(IntegerChoices):
    ACTIVE = 0
    WAITING = 1
    ELIMINATED = 2
    CHAMPION = 3


class MatchStatus(IntegerChoices):
    NO_STATUS = 0
    ERROR = 1
    IN_QUEUE = 2
    RUNNING = 3
    ENDED = 4
    STOPPED = 5


class ResultStatus(IntegerChoices):
    UPLOADED = 0
    NOT_CHECKED = 1
    PASSED = 2
    FAILED = 3


class RunnerStatus(IntegerChoices):
    NOT_RESPONDING = 0
    UP = 1
    DOWN = 2


class QueueStatus(IntegerChoices):
    RUNNING = 0
    WAITING = 1
    STOPPED = 2


class Visibility(IntegerChoices):
    PUBLIC = 0
    TEAM = 1
    TECHNICAL_COMMITTEE = 2
    PRIVATE = 3


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
