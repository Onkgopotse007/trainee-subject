from django.conf import settings
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from traineesubject.models.offschedule import OffSchedule
from traineesubject.models.onschedule import OnSchedule
from traineesubject.models.subject_consent import SubjectConsent
from traineesubject.models.subject_screening import SubjectScreening
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from django.db.models.signals import post_save
from edc_appointment.appointment_sms_reminder import AppointmentSmsReminder


@receiver(post_save, weak=False, sender=SubjectConsent,
          dispatch_uid='subject_consent_on_post_save')
def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """
    -Update subject screening consented flag.
    -Put participant on schedule and define community arm
    """
    if not raw:
        if created:
            update_model_fields(instance=instance,
                                model_cls=SubjectScreening,
                                fields=[
                                    ['subject_identifier', instance.subject_identifier],
                                    ['is_consented', True]])

        put_on_schedule(instance=instance)


def update_model_fields(instance=None, model_cls=None, fields=None):
    try:
        model_obj = model_cls.objects.get(
            screening_identifier=instance.screening_identifier)
    except model_cls.DoesNotExist:
        raise ValidationError(f'{model_cls} object does not exist!')
    else:
        for field, value in fields:
            setattr(model_obj, field, value)
        model_obj.save_base(update_fields=[field[0] for field in fields])


def put_on_schedule(instance=None):
    if instance:

        _, schedule = site_visit_schedules.get_by_onschedule_model(
            '  .onschedule')

        community_arm = get_community_arm(instance.screening_identifier)

        schedule.put_on_schedule(
            subject_identifier=instance.subject_identifier,
            onschedule_datetime=instance.consent_datetime)

        try:
            onschedule_obj = OnSchedule.objects.get(
                subject_identifier=instance.subject_identifier,
                community_arm__isnull=True)
        except OnSchedule.DoesNotExist:
            pass
        else:
            onschedule_obj.community_arm = community_arm
            onschedule_obj.save()


def get_community_arm(screening_identifier=None):
    if screening_identifier:

        try:
            subject_screening_obj = SubjectScreening.objects.get(
                screening_identifier=screening_identifier)
        except SubjectScreening.DoesNotExist:
            raise ValidationError('Subject screening object '
                                  'does not exist.')
        else:
            enhanced_care_communities = settings.COMMUNITIES.get('enhanced_care')

            if subject_screening_obj.enrollment_site in enhanced_care_communities:
                return 'Standard of Care'

    return None


def schedule_sms(appt_datetime, instance, consent):
    """
    Schedule or send SMS when called
    :param appt_datetime: date of the appointment from the appointment report date time
    in string format
    :param instance: Instance of the appointment created on post save
    :param consent: Participant's consent object
    :return: None
    """
    sms_message_data = (
        f'Dear+participant+Reminder+for+an+appointment+on+{appt_datetime}')
    appt_sms_reminder = AppointmentSmsReminder(
        subject_identifier=instance.subject_identifier,
        appt_datetime=instance.appt_datetime,
        sms_message_data=sms_message_data,
        recipient_number=consent.recipient_number)
    appt_reminder_date = instance.appt_datetime
    appt_sms_reminder.schedule_or_send_sms_reminder(
        appt_reminder_date=appt_reminder_date)


def get_onschedule_model_obj(schedule, subject_identifier, schedule_name):
    try:
        return schedule.onschedule_model_cls.objects.get(
            subject_identifier=subject_identifier, schedule_name=schedule_name)
    except ObjectDoesNotExist:
        return None


@receiver(post_save, weak=False, sender=OffSchedule,
          dispatch_uid='subject_off_schedule_on_post_save')
def subject_take_off_schedule(sender, instance, raw, created, **kwargs):
    for visit_schedule in site_visit_schedules.visit_schedules.values():
        for schedule in visit_schedule.schedules.values():
            onschedule_model_obj = get_onschedule_model_obj(
                schedule, instance.subject_identifier, instance.schedule_name)
            if (onschedule_model_obj
                    and onschedule_model_obj.schedule_name == instance.schedule_name):
                _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                    onschedule_model=onschedule_model_obj._meta.label_lower,
                    name=instance.schedule_name)
                schedule.take_off_schedule(
                    subject_identifier=instance.subject_identifier,
                    offschedule_datetime=instance.offschedule_datetime,
                    schedule_name=instance.schedule_name)
