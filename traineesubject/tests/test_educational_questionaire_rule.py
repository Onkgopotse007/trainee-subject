from django.test import TestCase,tag
from edc_facility.import_holidays import import_holidays
from model_mommy import mommy
from dateutil.relativedelta import relativedelta
from edc_base.utils import get_utcnow
from traineesubject.models.onschedule import OnSchedule
from edc_appointment.models import Appointment
from edc_constants.constants import YES,NO
from edc_metadata.models import CrfMetadata
from edc_metadata.constants import REQUIRED, NOT_REQUIRED


@tag('rg')
class TestRuleGroup(TestCase):

    def setUp(self):
        import_holidays()

        self.subject_screening = mommy.make_recipe(
            'traineesubject.subjectscreening',
            screening_identifier ='09876'
        )

        self.subject_consent = mommy.make_recipe(
            'traineesubject.subjectconsent',
            screening_identifier =self.subject_screening.screening_identifier,
            consent_datetime=get_utcnow() - relativedelta(days=3),
        )

        self.onschedule_obj = OnSchedule.objects.get(
            subject_identifier=self.subject_consent.subject_identifier
        )
        
        self.appointment_1000 = Appointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1000T')
        
        #print("App",self.appointment_1000)
        
        self.subject_visit_1000 = mommy.make_recipe(
            'traineesubject.subjectvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow() - relativedelta(days=2),
            appointment=self.appointment_1000)
        
        
        self.educational_questionaire = mommy.make_recipe(
            'traineesubject.educationalquestionaire',
            #subject_identifier=self.subject_consent.subject_identifier,
            subject_visit=self.subject_visit_1000,
            working=YES
        )


    def test_community_engagement_form_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
            model ='traineesubject.communityengagement',
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1000T',
            visit_code_sequence ='0').entry_status,REQUIRED
        )
    
    def test_community_engagement_form_not_required(self):
        self.educational_questionaire.working = NO
        self.educational_questionaire.save()
        self.assertEqual(
            CrfMetadata.objects.get(
            model ='traineesubject.communityengagement',
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1000T',
            visit_code_sequence ='0').entry_status,NOT_REQUIRED
        )
