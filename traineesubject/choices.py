from edc_constants.constants import OTHER, OFF_STUDY,NO,YES
from edc_constants.constants import NOT_APPLICABLE

"""
Custom choice for trainee_subject 
"""
COMMUNITY_ACTIVITY = (
    ("Very active", "Very active"),
    ("Somewhat active", "Somewhat active"),
    ("Not active at all", "Not active at all"),
    ("Don't want to answer", "Don't want to answer")
)


DISINTEREST_REASON = (
    ('dont_want_to_participate', 'I don\'t want to be part of a study'),
    ('dont_think_I_have_condition', 'I don\'t think I have the condition'),
    ('partner_doesnt_want_to_participate', 'My partner doesn\'t want me to participate'),
    (OTHER, 'Other (specify)')
)


ENROLLMENT_SITES = (
    ('mmathethe_clinic', 'Mmathethe clinic'),
    ('molapowabojang_clinic', 'Molapowabojang clinic'),
    ('otse_clinic', 'Otse clinic'),
    ('mmankgodi_clinic', 'Mmankgodi clinic'),
    ('lentsweletau_clinic', 'Lentsweletau clinic'),
    ('letlhakeng_clinic', 'Letlhakeng clinic'),
    ('oodi_clinic', 'Oodi clinic'),
    ('bokaa_clinic', 'Bokaa clinic'),
    ('metsimotlhabe_clinic', 'Metsimotlhabe clinic'),
    ('shoshong_clinic', 'Shoshong clinic'),
    ('sheleketla_clinic', 'Sheleketla clinic'),
    ('ramokgonami_clinic', 'Ramokgonami clinic'),
    ('lerala_clinic', 'Lerala clinic'),
    ('maunatlala_clinic', 'Maunatlala clinic'),
    ('sefophe_clinic', 'Sefophe clinic'),
    ('mmadinare_primary_hospital', 'Mmadinare Primary Hospital'),
    ('manga_clinic', 'Manga clinic'),
    ('mandunyane_clinic', 'Mandunyane clinic'),
    ('mathangwane_clinic', 'Mathangwane clinic'),
    ('tati_siding_clinic', 'Tati Siding clinic'),
    ('masunga_primary_hospital', 'Masunga Primary Hospital'),
    ('masunga_clinic', 'Masunga clinic'),
    ('mathangwane_clinic', 'Mathangwane clinic'),
    ('nata_clinic', 'Nata clinic'),
    (OTHER, 'Other (specify)')

)
HOUSEMATE = ( 
    ("Alone", "Alone"),
    ("Partner_or_Spouse","Partner_or_Spouse"),
    ("Sibilings","Siblings"),
    ("Other","Other"),
    ("Don't want to answer", "Don't want to answer"),
    
)

IDENTITY_TYPE = (
    ('country_id', 'Country ID number'),
    ('passport', 'Passport'),
    ('birth_certificate', 'Birth Certificate'),
    (OTHER, 'Other'),
)
MAJOR_COMMUNITY_PROBLEMS = (
    (" HIV/AIDS", " HIV/AIDS"),
    ("Schools", "Schools"),
    ("Sewer", "Sewer"),
    ("Unemployment", "Unemployment"),
    ("Roads", "Roads"),
    ("Water", "Water"),
    ("House", "House"),
    ("Malaria", "Malaria"),
    ('dont_know', 'Dont Know'),
)
OCCUPATION = (
    ("Farmer (own land)", "Farmer (own land)"),
    ("Farm work on employers land", "Farm work on employers land"),
    ("Domestic worker", "Domestic worker"),
    ("Work in bar/ hotel/ guest house/ entertainment venue", "Work in bar/ hotel/ guest house/ entertainment venue"),
    ("Fishing", "Fishing"),
    ("Mining", "Mining"),
    ("Tourism/game parks", "Tourism/game parks"),
    ("Working in shop / small business", "Working in shop / small business"),
    ("Informal selling", "Informal selling"),
    ("Commercial sex work", "Commercial sex work"),
    ("Transport (trucker/ taxi driver)", "Transport (trucker/ taxi driver)"),
    ("Factory worker", "Factory worker"),
    ("Guard (security company)", "Guard (security company)"),
    ("Police/ Soldier", "Police/ Soldier"),
    ("Clerical and office work", "Clerical and office work"),
    ("Government worker", "Government worker"),
    ("Teacher", "Teacher"),
    ("Health care worker", "Health care worker"),
    ("Other professional", "Other professional"),
    ("Don't want to answer", "Don't want to answer"),
    ("Other", "Other"),
    (NOT_APPLICABLE, 'Not Applicable'),
)

SALARY = (
    ("No income", "No income"),
    ("1 - 199 pula", "1 - 199 pula"),
    ("200 - 499 pula", "200 - 499 pula"),
    ("500 - 999 pula", "500 - 999 pula"),
    ("1000 - 4999 pula", "1000 - 4999 pula"),
    ("More than 10,000 pula", "More than 10,000 pula"),
    (NOT_APPLICABLE, 'Not Applicable'),
)

STUDY_SITES = (
    ('40', 'Gaborone'),
)

SMS_STATUS = (
    ('sms_sent', 'SMS sent'),
    ('sms_not_sent', 'SMS not sent'),
)

REASON_NOT_DRAWN = (
    ('collection_failed', 'Tried, but unable to obtain sample from patient'),
    ('absent', 'Patient did not attend visit'),
    ('refused', 'Patient refused'),
    ('no_supplies', 'No supplies'),
    (OTHER, 'Other'),
    (NOT_APPLICABLE, 'Not Applicable'))


VISIT_TYPE = (
    ('referral', 'Referral'),
    ('return', 'Return'),
)

VISIT_UNSCHEDULED_REASON = (
    ('routine_oncology', 'Routine oncology clinic visit (i.e. planned chemo, follow-up)'),
    ('ill_oncology', 'Ill oncology clinic visit'),
    ('patient_called', 'Patient called to come for visit'),
    (NOT_APPLICABLE, 'Not Applicable'),
    (OTHER, 'Other, specify:'),
)

VISIT_REASON = (
    ('initial_visit/contact', 'Initial visit/contact'),
    ('fu_visit/contact', 'Follow up visit/contact'),
    ('unscheduled_visit/contact', 'Unscheduled visit/contact'),
    ('missed_visit', 'Missed visit'),
    ('death', 'Death'),
    (OFF_STUDY, 'Off study (use only when taking subject off study)'),
    ('deferred', 'Deferred'),
)

VISIT_INFO_SOURCE = (
    ('clinic_visit', 'Clinic visit with participant'),
    ('other_contact_subject', 'Other contact with participant (i.e telephone call)'),
    ('contact_health worker', 'Contact with health care worker'),
    ('contact_family/designated_person',
     'Contact with family or designated person who can provide information'),
    (OTHER, 'Other,specify'),
)
WORK_TYPE = (
    ('formal_employment', 'Formal employment'),
    ('temporary_employment', 'Temporary Employment'),
    ('part_time_employment', 'Part-Time Employment'),
    ('self_employed', 'Self Employed'),
    ('self_employed_making_money_full_time', 'Self Employed Making Money Full Time'),
    ('self_employed_making_money_part_time', 'Self Employed Making Money Part Time'),
    (OTHER, 'Other'),
    (NOT_APPLICABLE, 'Not Applicable'),
    

)

YES_NO_DW =(
    (YES, YES),
    (NO, NO),
    ('does_not_work','Does not work')
)

YES_NO_NA_DA =(
    (YES, YES),
    (NO, NO),
    (NOT_APPLICABLE, 'Not Applicable'),
    ('doesnt_want_to_answer', 'Does not want to answer')
)

YES_NO_DK_DA =(
    (YES, YES),
    (NO, NO),
    ('dont_know', 'Dont Know'),
    ('doesnt_want_to_answer', 'Does not want to answer'),
    (NOT_APPLICABLE, 'Not Applicable'),
)





MARITAL_STATUS =(
    ("Single", "Single"),
    ("Married","Married"),
    ("Divorced","Divorced"),
    ("Widowed","Widowed")
)

REASON_FOR_EXIT = (
    ('death', 'Patient death'),
    ('ltfu', 'Patient lost to follow-up'),
    ('eval_complete', 'Cancer evaluation complete'),
    ('declines_further_eval',
     'Patient or clinician declines further evaluation'),
    ('patient_requests_removal', 'Patient requests removal from Potlako'),
    ('clinician_requests_removal', 'Clinician requests removal from Potlako'),
    (OTHER, 'Other (specify)'),
)




