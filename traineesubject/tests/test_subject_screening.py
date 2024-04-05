from django.test import TestCase
from ..models.subject_screening import SubjectScreening
from edc_constants.constants import FEMALE,YES, NO, NOT_APPLICABLE


class SubjectScreeningTest(TestCase):

    def test_subject_screening(self):
        subject_screening_instance = SubjectScreening.objects.create(
            gender=FEMALE,
            citizen=YES,
            legal_marriage=NOT_APPLICABLE,
            marriage_certificate=NOT_APPLICABLE,
            literate=YES,
            is_minor=NO
        )
        self.assertIsInstance(subject_screening_instance, SubjectScreening)

    def test_subject_screening_identifier(self):
        subject_screening_instance = SubjectScreening.objects.create(
            gender=FEMALE,
            citizen=YES,
            legal_marriage=YES,
            marriage_certificate=YES,
            literate=YES,
            is_minor=NO
        )
        self.assertIsNotNone(subject_screening_instance.screening_identifier)

    def test_subject_screening_minor(self):
        subject_screening_instance = SubjectScreening.objects.create(
            gender=FEMALE,
            citizen=YES,
            legal_marriage=NOT_APPLICABLE,
            marriage_certificate=NOT_APPLICABLE,
            literate=YES,
            is_minor=YES
        )
        self.assertFalse(subject_screening_instance.is_eligible)