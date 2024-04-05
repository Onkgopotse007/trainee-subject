from edc_constants.constants import NO,YES

class Eligibility:

    def __init__(self,is_minor=None,guardian=None,citizen=None,legal_marriage=None,
                 marriage_certificate=None,literate=None,verbal_consent=None,
                 literate_witness=None,enrollment_interest=None):
        
        self.reasons_ineligible =[]

        if citizen== NO and legal_marriage == NO:
            self.reasons_ineligible.append(
                "Not a Botswana citizen and not married to a Motswana")
        if citizen == NO and legal_marriage == YES and marriage_certificate == NO:
            self.reasons_ineligible.append(
                "Not a citizen but married to a Motswana with no proof")
        if is_minor ==YES:
            self.reasons_ineligible.append(
                "Participant is a Minor")
        if is_minor ==YES and guardian ==NO:
            self.reasons_ineligible.append(
                "Participant is a Minor and does not have a guardian")
        if literate == NO and literate_witness ==NO :
            self.reasons_ineligible.append(
                "Not literate and no literate Witness")
        if enrollment_interest == NO:
            self.reasons_ineligible.append(
                "Did not want to enroll")
        if verbal_consent == NO:
            self.reasons_ineligible.append(
                'Refused verbal consent.')
            
        

        self.is_eligible = False if self.reasons_ineligible else True