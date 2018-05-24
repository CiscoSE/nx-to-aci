from app.apic import api_apic_base
from app.apic import cobra_apic_base


__author__ = 'Santiago Flores Kanter (sfloresk@cisco.com)'
COMMAND_WAIT_TIME = 1
REMOVED_TENANTS=['mgmt','common','infra']


class base_handler:

    @staticmethod
    def create_cobra_apic(apic_url, username, password):
        cobra_apic = cobra_apic_base.cobra_apic_base()
        cobra_apic.login(apic_url, username, password)
        return cobra_apic


    @staticmethod
    def create_api_apic(apic_url, username, password):
        return api_apic_base.api_apic_base(apic_url, username, password)
