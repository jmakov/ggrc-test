


class LandingPage(object):
    BUTTON_LOGIN = "a.btn.btn-large.btn-info"


class PageHeader(object):
    TRIGGER = ".lhn-trigger"

    class DropdownToggle(object):
        PEOPLE_LIST_WIDGET = "ul.dropdown-menu li:nth-of-type(2)"

    class LhnMenu(object):
        ALL_OBJECTS = '[data-test-id="all_objects_e0345ec4"]'
        MY_OBJECTS = '[data-test-id="my_objects_6fa95ae1"]'
        PROGRAM_CREATE_NEW = '[data-test-id=' \
                             '"button_lhn_create_new_program_522c563f"'
        PROGRAMS = '[data-model-name="Program"] .grcicon-arrow-right'
        PROGRAMS_COUNT = '[data-model-name="Program"] .item-count'

        class CreateNewProgram(object):
            TITLE = '[data-test-id="new_program_field_title_a63ed79d"]'
            DESCRIPTION = '[data-test-id' \
                          '="new_program_field_description_77c4a06d"] ' \
                'iframe.wysihtml5-sandbox'
            NOTES = '[data-test-id="new_program_field_notes_75b8bc05"] ' \
                'iframe.wysihtml5-sandbox'
            CODE = '[data-test-id="new_program_field_code_334276e2"]'
            STATE = '[data-test-id="new_program_dropdown_state_036a1fa6"]'
            PRIVATE_CHECKBOX = '[data-test-id="new_page_checkbox_ed1fdde7"]'
            PRIMARY_CONTACT = '[data-test-id=' \
                '"new_program_field_primary_contact_86160053"]'
            SECONDARY_CONTACT = '[data-test-id=' \
                '"new_program_field_secondary_contact_86160053"]'
            BUTTON_SAVE_AND_CLOSE = '[data-test-id=' \
                '"new_program_button_save_86160053"]'
            PROGRAM_URL = '[data-test-id=' \
                '"new_program_field_program_url_86160053"]'
            REFERENCE_URL = '[data-test-id=' \
                '"new_program_field_reference_url_86160053"]'
            EFFECTIVE_DATE = '[data-test-id=' \
                '"new_program_field_effective_date_f2783a28"]'
            STOP_DATE = '[data-test-id=' \
                '"new_program_field_stop_date_f2783a28"]'
            DATE_PICKER = '.ui-datepicker-calendar [data-handler="selectDay"]'


class WidgetBar(object):
    BUTTON_ADD = ".hidden-widgets-list"
    DROPDOWN = ".inner-nav-item"
    TAB = '[data-test-id="tab_cbebea55"]'

    class ProgramInfo(object):
        TITLES = ".span6"
        DESCRIPTIONS = ".span12"
        ADVANCED = ".span4"
