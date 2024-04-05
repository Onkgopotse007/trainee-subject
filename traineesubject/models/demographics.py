from django.db import models
from traineesubject.choices import HOUSEMATE, MARITAL_STATUS
from traineesubject.models.model_mixins.crf_model_mixin import CrfModelMixin


class Demographic(CrfModelMixin):
    marital_status = models.CharField(
        verbose_name="What is your marital status",
        choices=MARITAL_STATUS,
        max_length=20,
    )

    women_number_husbands = models.IntegerField(
        verbose_name=(
            "How many wives does your husband have (including traditional marriage),"
            " including yourself?"),
        blank=True,
        null=True,

    )

    men_number_wives = models.IntegerField(
        verbose_name="How many wives do you have, including traditional marriage?",
        blank=True,
        null=True,

    )

    housemate = models.CharField(
        verbose_name="Who do you currently live with?",
        choices=HOUSEMATE,
        max_length=20

    )

    class Meta:
        app_label = 'traineesubject'
        verbose_name = 'Demographics'
