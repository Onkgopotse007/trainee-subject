from django.test import TestCase
from edc_constants.constants import NO,YES
from ..eligibility import Eligibility

class TestEligibility(TestCase):

    """Participants which are not are eligible"""

    def test_valid_participant_eligibility(self):
        eligibility = Eligibility(is_minor=NO,
                                  citizen=YES)
        self.assertTrue(eligibility.is_eligible)

    """Participants which are minors are in eligible"""
    def test_age_in_years_ineligibility(self):
        eligibility =Eligibility(is_minor=YES,
                                 citizen=YES)
        self.assertFalse(eligibility.is_eligible)
        self.assertIn('Participant is a Minor',
                      eligibility.reasons_ineligible)

    """Participants who are not citizens and are not married to citizens are not eligible"""
    def test_citizen_ineligibility(self):
        eligibility = Eligibility(is_minor=NO,
                                  citizen=NO,legal_marriage=NO)
        self.assertFalse(eligibility.is_eligible)
        self.assertIn("Not a Botswana citizen and not married to a Motswana",
                      eligibility.reasons_ineligible)

    """Participants who are not citizens,married to motswana but cant present proof"""
    def test_nationality_married_ineligibility(self):
        eligibility = Eligibility (is_minor=NO,citizen=NO,
                                   legal_marriage=YES,marriage_certificate=NO)
        self.assertFalse(eligibility.is_eligible)
        self.assertIn("Not a citizen but married to a Motswana with no proof",
                      eligibility.reasons_ineligible)

    """Participants who are not literate and have no literate witness"""
    def test_illetrate_ineligibility(self):
        eligibility =Eligibility (is_minor=NO,
                                  citizen=YES,literate=NO,literate_witness=NO)
        self.assertFalse(eligibility.is_eligible)
        self.assertIn("Not literate and no literate Witness",
                      eligibility.reasons_ineligible)
        

    