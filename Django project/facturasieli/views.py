# facturasieli/views.py
# --------------------------------------------------------------------------- #
#                                  I N D E X                                  #
# --------------------------------------------------------------------------- #

from facturasieli.views.index import index


# --------------------------------------------------------------------------- #
#                           R E G I S T R A T I O N                           #
# --------------------------------------------------------------------------- #

from facturasieli.views.registration import register
from facturasieli.views.registration import create_otp
from facturasieli.views.registration import send_otp_mail
from facturasieli.views.registration import otp_validation
from facturasieli.views.registration import custom_log_in
from facturasieli.views.registration import log_out


# --------------------------------------------------------------------------- #
#              R E G I S T R A T I O N    T R A N S I T I O N S               #
# --------------------------------------------------------------------------- #

from facturasieli.views.registration.transitions import welcome
from facturasieli.views.registration.transitions import goodbye


# --------------------------------------------------------------------------- #
#                                P R O F I L E                                #
# --------------------------------------------------------------------------- #

from facturasieli.views.profile import public_profile
from facturasieli.views.profile import edit_profile


# --------------------------------------------------------------------------- #
#                                S E R V I C E                                #
# --------------------------------------------------------------------------- #

from facturasieli.views.service import handle_service
from facturasieli.views.service import display_service
