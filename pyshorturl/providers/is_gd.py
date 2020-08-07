
from .v_gd import Vgd, VgdError


ISGD_SERVICE_URL = "http://is.gd/%s.php"


class IsgdError(VgdError):
    pass


class Isgd(Vgd):

    exception_class = IsgdError
    service_url = ISGD_SERVICE_URL
