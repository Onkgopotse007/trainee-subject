from django.apps import AppConfig as DjangoConfig
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_device.device_permission import DeviceAddPermission, DeviceChangePermission, \
    DevicePermissions
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from edc_device.constants import CENTRAL_SERVER, CLIENT, NODE_SERVER
from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_visit_tracking.apps import (AppConfig as BaseEdcVisitTrackingAppConfig)
from edc_sms.apps import AppConfig as BaseEdcSmsAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT


class AppConfig(DjangoConfig):
    name = 'traineesubject'
    verbose_name = "Trainee Subject +Crfs"
    admin_site_name = 'traineesubject_admin'


class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
    country = 'botswana'
    definitions = {
        '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                             slots=[100, 100, 100, 100, 100, 100, 100]),
        '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                             slots=[100, 100, 100, 100, 100])}


class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
    use_settings = True
    device_permissions = DevicePermissions(
        DeviceAddPermission(
            model='plot.plot',
            device_roles=[CENTRAL_SERVER, CLIENT]),
        DeviceChangePermission(
            model='plot.plot',
            device_roles=[NODE_SERVER, CENTRAL_SERVER, CLIENT]))


class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    default_appt_type = 'clinic'
    apply_community_filter = True
    send_sms_reminders = True
    configurations = [
        AppointmentConfig(
            model='edc_appointment.appointment',
            related_visit_model='traineesubject.subjectvisit')
    ]


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    visit_models = {
        'traineesubject': (
            'subject_visit', 'traineesubject.subjectvisit')}


class EdcSmsAppConfig(BaseEdcSmsAppConfig):
    locator_model = 'traineesubject.subjectlocator'
    consent_model = 'traineesubject.subjectconsent'
    sms_model = 'traineesubject.sms'


class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
    reason_field = {'traineesubject.subjectvisit': 'reason'}
    other_visit_reasons = ['off study', 'deferred', 'death']
    other_create_visit_reasons = [
        'initial_visit/contact', 'fu_visit/contact',
        'missed_visit', 'unscheduled_visit/contact']
    create_on_reasons = [SCHEDULED, UNSCHEDULED] + other_create_visit_reasons
    delete_on_reasons = [LOST_VISIT] + other_visit_reasons
