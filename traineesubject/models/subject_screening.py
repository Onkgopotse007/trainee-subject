from traineesubject.models.model_mixins.search_slug_model_mixin import \
    SearchSlugModelMixin
from traineesubject.screening_identifier import ScreeningIdentifier
from ..eligibility import Eligibility
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.sites import CurrentSiteManager, SiteModelMixin
from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import YES_NO, YES_NO_NA, GENDER_UNDETERMINED
from ..choices import DISINTEREST_REASON, ENROLLMENT_SITES
from edc_base.model_fields import OtherCharField
from edc_constants.constants import NOT_APPLICABLE
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_search.model_mixins import SearchSlugManager
from edc_base.utils import get_utcnow


class SubjectScreeningManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(
            screening_identifier=screening_identifier
        )


class SubjectScreening(NonUniqueSubjectIdentifierFieldMixin
    , SearchSlugModelMixin, BaseUuidModel, SiteModelMixin):
    identifier_cls = ScreeningIdentifier
    eligibility_cls = Eligibility

    screening_identifier = models.CharField(
        verbose_name="Screening Identifier",
        max_length=36,
        unique=True,
        editable=False
    )

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of the report"
    )

    enrollment_interest = models.CharField(
        verbose_name=("Does the patient want to be enrolled into the study?"),
        max_length=3,
        choices=YES_NO
    )

    disinterest_reason = models.CharField(
        verbose_name=("If no, reason patient does not wish to enroll into the study"),
        max_length=50,
        choices=DISINTEREST_REASON,
        null=True,
        blank=True
    )

    disinterest_reason_other = OtherCharField()

    citizen = models.CharField(
        verbose_name=("Is the potential paticipant a Botswana Citizen?"),
        max_length=3,
        choices=YES_NO,

    )
    legal_marriage = models.CharField(
        verbose_name=("If no," "Is participant married to a Motswana"),
        choices=YES_NO_NA,
        null=True,
        blank=False,
        max_length=3,
        help_text="If 'No', participant not be consented"
    )

    marriage_certificate = models.CharField(
        verbose_name=("If yes," "Can the participate show proof of marriage"),
        choices=YES_NO_NA,
        max_length=3,
        null=True,
        default=NOT_APPLICABLE,
        help_text="( if 'NO' STOP patient cannot be enrolled )",
    )

    marriage_certificate_no = models.CharField(
        verbose_name='What is the marriage certificate number?',
        max_length=9,
        null=True,
        blank=True,
        help_text='e.g. 000/YYYY',
    )

    is_minor = models.CharField(
        max_length=10,
        choices=YES_NO,
        verbose_name="Is a minor(Under 18)",
        help_text='If yes participant can not be consented',

    )

    guardian = models.CharField(
        verbose_name="Is a guardian available?",
        max_length=3,
        choices=YES_NO_NA,
        null=True,
        help_text='If No, participant may not be consented.',

    )

    literate = models.CharField(
        verbose_name="Is the participant literate",
        max_length=3,
        choices=YES_NO,

    )

    literate_witness = models.CharField(
        verbose_name=("If no," "Does participant have a literate witness"),
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        max_length=3
    )

    gender = models.CharField(
        verbose_name="Are you male or female?",
        max_length=6,
        choices=GENDER_UNDETERMINED

    )
    enrollment_site = models.CharField(
        max_length=50,
        null=True,
        choices=ENROLLMENT_SITES,
        help_text="Hospital where subject is recruited")

    enrollment_site_other = OtherCharField()

    is_eligible = models.BooleanField(
        default=False,
        editable=False)

    ineligibility = models.TextField(
        verbose_name="Reason not eligible",
        max_length=150,
        null=True,
        editable=False)

    is_consented = models.BooleanField(
        default=False,
        editable=False)

    history = HistoricalRecords()

    on_site = CurrentSiteManager()

    objects = SubjectScreeningManager()

    """returns a screening identifier as a string"""

    def __str__(self):
        return f'{self.screening_identifier},{self.subject_identifier}'

    """returns screening identifier as tuple of type string"""

    def natural_key(self):
        return (self.screening_identifier,)

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.extend(['screening_identifier', ])
        return fields

    def save(self, *args, **kwargs):
        if not self.id:
            self.screening_identifier = self.identifier_cls().identifier
        eligibility_obj = self.eligibility_cls(
            citizen=self.citizen,
            legal_marriage=self.legal_marriage,
            marriage_certificate=self.marriage_certificate,
            is_minor=self.is_minor,
            guardian=self.guardian,
            literate=self.literate,
            literate_witness=self.literate_witness,
            enrollment_interest=self.enrollment_interest, )
        self.is_eligible = eligibility_obj.is_eligible
        if eligibility_obj.reasons_ineligible:
            self.ineligibility = eligibility_obj.reasons_ineligible
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'traineesubject'
        verbose_name = "Trainee + Eligibility"
        verbose_name_plural = "Trainee + Eligibility"
