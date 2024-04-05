"""from django.test import TestCase
from ..models.subject_screening import SubjectScreening
from ..models.subject_consent import SubjectConsent
from edc_constants.constants import YES, NO, FEMALE, OTHER,NOT_APPLICABLE
from edc_base.utils import get_utcnow


class SubjectConsentTest(TestCase):

    def setUp(self):
        self.screening_obj = SubjectScreening.objects.create(
            gender=FEMALE,
            citizen=YES,
            legal_marriage=NOT_APPLICABLE,
            marriage_certificate=NOT_APPLICABLE,
            literate=YES,
            is_minor=NO

        )

    def test_subject_consent(self):
        subject_consent_obj = SubjectConsent.objects.create(
            subject_identifier=None,
            screening_identifier=self.screening_obj.screening_identifier,
            dob=get_utcnow(),
            first_name="Nandipa",
            last_name="Magudumane",
            initials='NM',
            gender=self.screening_obj.gender,
            identity='999929999',
            confirm_identity='999929999',
            identity_type='OMANG',
            is_dob_estimated='-',
        
        )

        self.assertIsInstance(subject_consent_obj, SubjectConsent)

    def test_subject_consent_identifier(self):
        subject_consent_obj = SubjectConsent.objects.create(
            subject_identifier=None,
            screening_identifier=self.screening_obj.screening_identifier,
            dob=get_utcnow(),
            first_name="Nandipa",
            last_name="Magudumane",
            initials='NM',
            gender=self.screening_obj.gender,
            identity='999929999',
            confirm_identity='999929999',
            identity_type='OMANG',
            is_dob_estimated='-',
        
        )
        self.assertIsNotNone(subject_consent_obj.subject_identifier)"""