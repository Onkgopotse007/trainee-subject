from edc_action_item import site_action_items
from edc_locator.action_items import SubjectLocatorAction as BaseSubjectLocatorAction

SUBJECT_LOCATOR_ACTION = 'submit-trainee-subject-locator'


class TraineeSubjectLocatorAction(BaseSubjectLocatorAction):
    name = SUBJECT_LOCATOR_ACTION
    display_name = 'Submit Subject Locator'
    reference_model = 'traineesubject.subjectlocator'
    admin_site_name = 'traineesubject_admin'


site_action_items.register(TraineeSubjectLocatorAction)