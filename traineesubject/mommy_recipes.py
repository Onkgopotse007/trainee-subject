from dateutil.relativedelta import relativedelta
from edc_base.utils import get_utcnow
from edc_constants.constants import ALIVE, YES, NO, ON_STUDY
from edc_constants.constants import PARTICIPANT
from edc_visit_tracking.constants import SCHEDULED
from faker import Faker
import faker
from model_mommy.recipe import Recipe, seq
from traineesubject.models import demographics
from traineesubject.models.community_engagement import CommunityEngagement
from traineesubject.models.educational_questionaire import EducationalQuestionaire
from traineesubject.models.subject_consent import SubjectConsent
from traineesubject.models.subject_locator import SubjectLocator
from traineesubject.models.subject_visit import SubjectVisit
from traineesubject.models.subject_screening import SubjectScreening


fake = Faker()

subjectscreening = Recipe(
    SubjectScreening,
    enrollment_interest=YES,
    citizen=YES,
    is_minor=NO,
    enrollment_site='Otse_clinic',
)

subjectconsent = Recipe(
    SubjectConsent,
    subject_identifier=None,
    consent_datetime=get_utcnow(),
    dob=(get_utcnow() - relativedelta(years=25)).date(),
    first_name=fake.first_name,
    last_name=fake.last_name,
    initials='XX',
    gender='F',
    language='en',
    identity_type='OMANG',
    is_dob_estimated=NO,
    citizen=YES,
    version='1',
    identity='123421234',
    confirm_identity='123421234',
    consent_reviewed=YES,
    assessment_score=YES,
    verbal_script=YES,
    study_questions=YES,
)


subjectlocator = Recipe(
    SubjectLocator,
    subject_identifier=None,
    date_signed=get_utcnow().date())

subjectvisit = Recipe(
    SubjectVisit,
    report_datetime=get_utcnow(),
    reason=SCHEDULED,
    info_source=PARTICIPANT)

educationalquestionaire = Recipe(
    EducationalQuestionaire,
)

communityengagement = Recipe(
    CommunityEngagement,
)

demographic = Recipe (
    demographics,
)