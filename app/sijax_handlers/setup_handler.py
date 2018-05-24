"""

Helper for views.py

"""
from base_handler import base_handler
import traceback
from utils import get_ntp_server

DOCKER_URL = 'unix://var/run/docker.sock'


class setup_handler(base_handler):
    def __init__(self):
        """
        Manages all operations related to the creation of docker containers
        :return:
        """
        self.apic_object = None

    def set_up(self, object_response, form_values):
        try:
            # Connect to the APIC
            self.apic_object = base_handler.create_cobra_apic(form_values['apic_url'],
                                                              form_values['apic_username'],
                                                              form_values['apic_password'])

            # Get ntp ip from configuration
            ntp_server_ip = get_ntp_server(form_values['configuration'])

            # Create NTP pol and provider
            self.apic_object.create_ntp_server(ntp_server_ip, 'first-setup-ntp')

            # Update the GUI
            object_response.script("create_notification('Configuration done', '', 'success', 5000);")
        except Exception as e:
            # Update the GUI
            object_response.script("create_notification('Something went wrong', '" + str(e).replace("'", "").
                                   replace('"', '').replace("\n", "")[0:100] + "', 'danger', 0)")
            print traceback.print_exc()
        finally:
            object_response.script("$('#set_up_response').html('');")