# header6ff05843-c222-461f-8226-36a7abe6806e

from selenium.webdriver.common.by import By


class Page(object):
    BODY = (By.CSS_SELECTOR, 'body')

class Login(object):
    BUTTON_LOGIN = (By.CSS_SELECTOR, "a.btn.btn-large.btn-info")


class PageHeader(object):
    TRIGGER = (By.CSS_SELECTOR, ".lhn-trigger")

    # dropdown toggle
    PEOPLE_LIST_WIDGET = (By.CSS_SELECTOR, "ul.dropdown-menu "
                                           "li:nth-of-type(2)")
    USER_MENU = (By.CSS_SELECTOR, 'li.user.user-dropdown.dropdown')

    PROGRAM_TITLE = (By.CSS_SELECTOR, 'div#page-header span.title-content')


class HorNavBar(object):
    GGRC_ICON = (By.CSS_SELECTOR, '[href$="dashboard"].to-my-work')
    PROGRAMS = (By.CSS_SELECTOR, '[href="#program_widget"]')
    OBJECT_TITLE = (By.CSS_SELECTOR, '.title.tree-title-area')
    GEAR_ICON_CONTENT = (By.CSS_SELECTOR,
                         '[data-toggle="dropdown"].btn + .dropdown-menu')
    EDIT_PROGRAM = (By.CSS_SELECTOR,
                    '.dropdown-menu [data-object-singular="Program"]'
                    '[data-modal-class="modal-wide"]')
    EDIT_OBJECT_TEXT = (By.CSS_SELECTOR, '.ui-draggable-handle')
    START_NEW_PROGRAM = (By.CSS_SELECTOR,
                         '.quick-list [data-object-singular="Program"]')
    OBJECT_DELETED = (By.CSS_SELECTOR, '.user-string')
    CLOSE_X = (By.CSS_SELECTOR, '.pull-right.modal-dismiss')


class DropdownToggle(object):
    DASHBOARD_WIDGET = (By.CSS_SELECTOR,
                        'li.full-opacity a[href$="dashboard"]')
    DASHBOARD_WIDGET = (By.CSS_SELECTOR,
                        'li.full-opacity a[href$="dashboard"]')
    MY_WORK_PAGE = (By.CSS_SELECTOR, 'li.full-opacity a[href$="dashboard"]')
    ADMIN_MENU_OPTION = (By.CSS_SELECTOR, 'ul.dropdown-menu li '
                         'a[href$="/admin#people_list_widget"]')
    NOTIFICATIONS = (By.CSS_SELECTOR, '.notify-wrap span')
    DAILY_EMAIL = (By.CSS_SELECTOR, '.inner-list label:not(.inner)')
    REAL_TIME_EMAIL = (By.CSS_SELECTOR, '.inner-list .inner')
    DATA_IMPORT = (By.CSS_SELECTOR, 'ul.dropdown-menu a[href$="import"]')
    DATA_EXPORT = (By.CSS_SELECTOR, 'ul.dropdown-menu a[href$="export"]')
    DATA_GRID = (By.CSS_SELECTOR, 'ul.dropdown-menu a[href*="data_grid"]')
    LOGOUT = (By.CSS_SELECTOR, '.nav-logout')
    DAILY_EMAIL_CHECKBOX = (By.CSS_SELECTOR,
                            '.inner-list [value="Email_Digest"]')
    REAL_TIME_EMAIL_CHECKBOX = (By.CSS_SELECTOR,
                                '.inner-list [value="Email_Now"]')
    REAL_TIME_EMAIL_LABEL = (By.CSS_SELECTOR, '.inner')


class LhnMenu(object):
    ALL_OBJECTS = (By.CSS_SELECTOR, '[data-value="all"]')
    MY_OBJECTS = (By.CSS_SELECTOR, '[data-value="my_work"]')
    PROGRAM_CREATE_NEW = (By.CSS_SELECTOR, '[data-test-id='
                          '"button_lhn_create_new_program_522c563f"')
    PROGRAMS = (By.CSS_SELECTOR, '[data-model-name="Program"] '
                                 '.grcicon-arrow-right')
    PROGRAMS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Program"] '
                                       '.item-count')
    LHS_ITEM = (By.CSS_SELECTOR, '[test-data-id="lhs-item_3ad27b8b"]')
    PROGRAMS_LINK = (By.CSS_SELECTOR, '[data-model-name="Program"] '
                     '[data-parent=".top-level"]')
    WORKFLOWS_LINK = (By.CSS_SELECTOR, '[data-model-name="Workflow"] '
                      '[data-parent=".top-level"]')
    AUDITS_LINK = (By.CSS_SELECTOR,
                   '[data-model-name="Audit"] [data-parent=".top-level"]')
    CTRL_ASSES_LINK = (By.CSS_SELECTOR, '[data-model-name="ControlAssessment"]'
                       ' [data-parent=".top-level"]')
    ISSUES_LINK = (By.CSS_SELECTOR,
                   '[data-model-name="Issue"] [data-parent=".top-level"]')
    LHN_PIN = (By.CSS_SELECTOR, 'a.lhn-pin')
    LHN_PIN_NOT_ACTIVE = (By.CSS_SELECTOR, 'a.lhn-pin:not(.active)')
    DIRECTIVES = (By.CSS_SELECTOR, 'ul.top-level '
                  'li.governance.accordion-group:nth-of-type(1) a.top')
    CONT_OBJ = (By.CSS_SELECTOR, 'ul.top-level li.governance.accordion-group'
                ':not([data-model-name]):nth-of-type(2) a.top')
    PPL_GRP = (By.CSS_SELECTOR,
               'ul.top-level li.entities.accordion-group a.top')
    ASSETS = (By.CSS_SELECTOR,
              'ul.top-level li.business.accordion-group a.top')
    RISKS = (By.CSS_SELECTOR, 'ul.top-level li.risk.accordion-group a.top')
    REC_VIEW = (By.CSS_SELECTOR, 'div.lhs.accordion:not([data-template]) '
                'div.lhs-nav:nth-of-type(6) h2')
    WORKFLOWS_COUNT = (By.CSS_SELECTOR,
                       '[data-model-name="Workflow"] .item-count')
    AUDITS_COUNT = (By.CSS_SELECTOR,
                    '[data-object-singular="Audit"] .item-count')
    CTRL_ASSES_COUNT = (By.CSS_SELECTOR,
                        '[data-object-singular="ControlAssessment"] '
                        '.item-count')
    ISSUES_COUNT = (By.CSS_SELECTOR,
                    '[data-object-singular="Issue"] .item-count')
    HIDE_OPTIONAL = (By.CSS_SELECTOR, '#formHide')
    BAR_V = (By.CSS_SELECTOR, '.bar-v')
    LHS_CONTENT = (By.CSS_SELECTOR, '.content .sub-level.in')
    WAIT_FOR_ITEMS = (By.CSS_SELECTOR, '.sub-level.in .spinny')
    FIRST_LHN_OBJECT = (By.CSS_SELECTOR,
                        '.sub-level.in [data-model="true"]:first-child')
    LAST_LHN_OBJECT = (By.CSS_SELECTOR,
                       '.sub-level.in [data-model="true"]:last-child')


class ModalCreateNewObject(object):
    TITLE = (By.CSS_SELECTOR, '[data-id="title_txtbx"]')
    BUTTON_SAVE_AND_ADD = (By.CSS_SELECTOR,
                           '[data-toggle="modal-submit-addmore"]')
    BUTTON_SAVE_AND_CLOSE = (By.CSS_SELECTOR, '[data-toggle="modal-submit"]')
    LHS_ITEM = (By.CSS_SELECTOR, '.lhs-item')
    GEAR_ICON = (By.CSS_SELECTOR, '[data-toggle="dropdown"].btn')
    DELETE_IN_GEAR = (By.CSS_SELECTOR, '[data-toggle="modal-ajax-deleteform"]')
    DELETE = (By.CSS_SELECTOR, '[data-toggle="delete"]')
    LAST_MODAL_OBJECT = (By.CSS_SELECTOR,
                         '.ui-widget .ui-menu-item:nth-last-child(2)')
    CODE = (By.CSS_SELECTOR, '[data-id="code_txtbx"]')

    ISSUES_CONTAINER = (By.CSS_SELECTOR,
            'li[data-model-name="Issue"] '
            'ul.sub-level.cms_controllers_infinite_scroll')
    ISSUES_FIRST = (By.CSS_SELECTOR,
            'li[data-model-name="Issue"] '
            'ul.sub-level.cms_controllers_infinite_scroll li:nth-child(1)')

    ASSETS_BUSINESS_SYSTEMS_CONTAINER = (By.CSS_SELECTOR,
            'li[data-model-name="System"] '
            'ul.sub-level.cms_controllers_infinite_scroll')
    ASSETS_BUSINESS_SYSTEMS_FIRST = (By.CSS_SELECTOR,
            'li[data-model-name="System"] '
            'ul.sub-level.cms_controllers_infinite_scroll li:nth-child(1)')

    PEOPLE_GROUPS_PEOPLE_CONTAINER = (By.CSS_SELECTOR,
            'li[data-model-name="Person"] '
            'ul.sub-level.cms_controllers_infinite_scroll')
    PEOPLE_GROUPS_PEOPLE_FIRST = (By.CSS_SELECTOR,
            'li[data-model-name="Person"] '
            'ul.sub-level.cms_controllers_infinite_scroll li:nth-child(1)')

    CONTROLS_OBJECTIVES_CONTROLS_CONTAINER = (By.CSS_SELECTOR,
            'li[data-model-name="Control"] '
            'ul.sub-level.cms_controllers_infinite_scroll')
    CONTROLS_OBJECTIVES_CONTROLS_FIRST = (By.CSS_SELECTOR,
            'li[data-model-name="Control"] '
            'ul.sub-level.cms_controllers_infinite_scroll li:nth-child(1)')

    MAP_TO_PROGRAM_LINK = (By.CSS_SELECTOR,
            'div#extended-info a.map-to-page-object')
    EXTENDED_INFO_TITLE = (By.CSS_SELECTOR,
            'div#extended-info a.main-title')


class ModalCreateNewProgram(object):
    PROGRAM_CREATE_NEW = (By.CSS_SELECTOR,
                          '.add-new [data-object-singular="Program"]')
    TITLE_UI = (By.CSS_SELECTOR,
                '[data-test-id="new_program_field_title_a63ed79d"]')
    DESCRIPTION_UI = (By.CSS_SELECTOR, '[data-test-id'
                      '="new_program_field_description_77c4a06d"] '
                      'iframe.wysihtml5-sandbox')
    NOTES_UI = (By.CSS_SELECTOR,
                '[data-test-id="new_program_field_notes_75b8bc05"] '
                'iframe.wysihtml5-sandbox')
    CODE_UI = (By.CSS_SELECTOR,
               '[data-test-id="new_program_field_code_334276e2"]')
    STATE_UI = (By.CSS_SELECTOR,
                '[data-test-id="new_program_dropdown_state_036a1fa6"]')
    BUTTON_HIDE_OPTIONAL_FIELDS = (By.CSS_SELECTOR,
                                   '[data-test-id="button-toggle-1a226d7a"]')
    BUTTON_SHOW_ALL_OPTIONAL_FIELDS = (By.CSS_SELECTOR,
                                       'data-test-id="button-toggle-2c925d94"')
    PRIVATE_CHECKBOX_UI = (By.CSS_SELECTOR,
                           '[data-test-id="new_page_checkbox_ed1fdde7"]')
    PRIMARY_CONTACT_UI = (By.CSS_SELECTOR, '[data-test-id='
                          '"new_program_field_primary_contact_86160053"]')
    SECONDARY_CONTACT_UI = (By.CSS_SELECTOR, '[data-test-id='
                            '"new_program_field_secondary_contact_'
                            '86160053"]')
    BUTTON_SAVE_AND_CLOSE_UI = (By.CSS_SELECTOR, '[data-test-id='
                                '"new_program_button_save_86160053"]')
    PROGRAM_URL_UI = (By.CSS_SELECTOR, '[data-test-id='
                      '"new_program_field_program_url_86160053"]')
    REFERENCE_URL_UI = (By.CSS_SELECTOR, '[data-test-id='
                        '"new_program_field_reference_url_86160053"]')
    EFFECTIVE_DATE_UI = (By.CSS_SELECTOR, '[data-test-id='
                         '"new_program_field_effective_date_f2783a28"]')
    STOP_DATE_UI = (By.CSS_SELECTOR, '[data-test-id='
                    '"new_program_field_stop_date_f2783a28"]')
    DATE_PICKER_UI = (By.CSS_SELECTOR, '.ui-datepicker-calendar ['
                      'data-handler="selectDay"]')
    BUTTON_SAVE_AND_ADD = (By.CSS_SELECTOR,
                           '[data-toggle="modal-submit-addmore"]')
    LHS_ITEM_NEW = (By.CSS_SELECTOR, '.lhs-item')
    GEAR_ICON = (By.CSS_SELECTOR, '[data-toggle="dropdown"].btn')
    DELETE_IN_GEAR = (By.CSS_SELECTOR, '[data-toggle="modal-ajax-deleteform"]')
    DELETE = (By.CSS_SELECTOR, '[data-toggle="delete"]')


class ModalCreateNewWorkflow(object):
    # data_id = '[data-test-id$="522c563f"]'
    WF_CREATE_NEW = (By.CSS_SELECTOR,
                     '.add-new [data-object-singular="Workflow"]')
    WF_TITLE = (By.CSS_SELECTOR, '[data-id="title_txtbx"]')
    WF_ACTIVE = (By.CSS_SELECTOR, '.wf-trigger.wf-active')
    WF_DRAFT = (By.CSS_SELECTOR, '.wf-trigger.wf-draft')
    WF_INACTIVE = (By.CSS_SELECTOR, '.wf-trigger.wf-inactive')


class ModalCreateNewAudit(object):
    AUDIT_CREATE_NEW = (By.CSS_SELECTOR,
                        '.add-new [data-object-singular="Audit"]')
    CLICK_PROGRAM_CHECKBOX = (By.CSS_SELECTOR, '[data-lookup="Program"]')
    SELECT_PROGRAM = (By.CSS_SELECTOR, '.ui-menu-item .show-extended')


class ModalCreateNewControlAsses(object):
    CONTROL_ASSES_CREATE_NEW = (By.CSS_SELECTOR, '.add-new '
                                '[data-object-singular="ControlAssessment"]')
    CLICK_CONTROL_CHECKBOX = (By.CSS_SELECTOR, '[data-lookup="Control"]')
    CLICK_AUDIT_CHECKBOX = (By.CSS_SELECTOR, '[data-lookup="Audit"]')
    SELECT_OTHER = (By.CSS_SELECTOR,
                    'div + ul.ui-menu + span + ul.ui-menu li.ui-menu-item')


class ModalCreateNewIssue(object):
    ISSUE_CREATE_NEW = (By.CSS_SELECTOR,
                        '.add-new [data-object-singular="Issue"]')


class Directives(object):
    REGULATIONS = (By.CSS_SELECTOR, '[data-object-singular="Regulation"]'
                   '[data-parent=".top-level"]')
    REGULATIONS_COUNT = (By.CSS_SELECTOR, '[data-object-singular="Regulation"]'
                         ' .item-count')
    POLICIES = (By.CSS_SELECTOR, '[data-object-singular="Policy"]'
                '[data-parent=".top-level"]')
    POLICIES_COUNT = (By.CSS_SELECTOR,
                      '[data-model-name="Policy"] .item-count')
    STANDARDS = (By.CSS_SELECTOR, '[data-object-singular="Standard"]'
                 '[data-parent=".top-level"]')
    STANDARDS_COUNT = (By.CSS_SELECTOR,
                       '[data-model-name="Standard"] .item-count')
    CONTRACTS = (By.CSS_SELECTOR, '[data-object-singular="Contract"]'
                 '[data-parent=".top-level"]')
    CONTRACTS_COUNT = (By.CSS_SELECTOR,
                       '[data-model-name="Contract"] .item-count')
    CLAUSES = (By.CSS_SELECTOR, '[data-object-singular="Clause"]'
               '[data-parent=".top-level"]')
    CLAUSES_COUNT = (By.CSS_SELECTOR, '[data-model-name="Clause"] .item-count')
    SECTIONS = (By.CSS_SELECTOR, '[data-object-singular="Section"]'
                '[data-parent=".top-level"]')
    SECTIONS_COUNT = (By.CSS_SELECTOR,
                      '[data-model-name="Section"] .item-count')


class ModalCreateNewRegulation(object):
    REGULATION_CREATE_NEW = (By.CSS_SELECTOR,
                             '.add-new [data-object-singular="Regulation"]')


class ModalCreateNewPolicy(object):
    POLICY_CREATE_NEW = (By.CSS_SELECTOR,
                         '.add-new [data-object-singular="Policy"]')


class ModalCreateNewStandard(object):
    STANDARD_CREATE_NEW = (By.CSS_SELECTOR,
                           '.add-new [data-object-singular="Standard"]')


class ModalCreateNewContract(object):
    CONTRACT_CREATE_NEW = (By.CSS_SELECTOR,
                           '.add-new [data-object-singular="Contract"]')


class ModalCreateNewClause(object):
    CLAUSE_CREATE_NEW = (By.CSS_SELECTOR,
                         '.add-new [data-object-singular="Clause"]')


class ModalCreateNewSection(object):
    SECTION_CREATE_NEW = (By.CSS_SELECTOR,
                          '.add-new [data-object-singular="Section"]')
    CLICK_POLICY_CHECKBOX = (By.CSS_SELECTOR, '[data-lookup="'
                             'Policy,Regulation,Standard,Contract"]')
    SELECT_POLICY = (By.CSS_SELECTOR, '.ui-menu-item .show-extended')


class ControlObjectives(object):
    CONTROLS = (By.CSS_SELECTOR, '[data-object-singular="Control"]'
                '[data-parent=".top-level"]')
    CONTROLS_COUNT = (By.CSS_SELECTOR,
                      '[data-model-name="Control"] .item-count')
    OBJECTIVES = (By.CSS_SELECTOR, '[data-object-singular="Objective"]'
                  '[data-parent=".top-level"]')
    OBJECTIVES_COUNT = (By.CSS_SELECTOR,
                        '[data-model-name="Objective"] .item-count')


class ModalCreateNewControl(object):
    CONTROL_CREATE_NEW = (By.CSS_SELECTOR,
                          '.add-new [data-object-singular="Control"]')


class ModalCreateNewObjective(object):
    OBJECTIVE_CREATE_NEW = (By.CSS_SELECTOR,
                            '.add-new [data-object-singular="Objective"]')


class PeopleGroups(object):
    PEOPLE = (By.CSS_SELECTOR, '[data-object-singular="Person"]'
              '[data-parent=".top-level"]')
    PEOPLE_COUNT = (By.CSS_SELECTOR, '[data-model-name="Person"] .item-count')
    ORG_GROUPS = (By.CSS_SELECTOR, '[data-object-singular="OrgGroup"]'
                  '[data-parent=".top-level"]')
    ORG_GROUPS_COUNT = (By.CSS_SELECTOR,
                        '[data-model-name="OrgGroup"] .item-count')
    VENDORS = (By.CSS_SELECTOR, '[data-object-singular="Vendor"]'
               '[data-parent=".top-level"]')
    VENDORS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Vendor"] .item-count')


class ModalCreateNewPerson(object):
    PERSON_CREATE_NEW = (By.CSS_SELECTOR,
                         '.add-new [data-object-singular="Person"]')
    PERSON_EMAIL = (By.CSS_SELECTOR, '#person_email')
    PERSON_NAME = (By.CSS_SELECTOR, '#person_name')


class ModalCreateNewOrgGroup(object):
    ORG_GROUP_CREATE_NEW = (By.CSS_SELECTOR,
                            '.add-new [data-object-singular="OrgGroup"]')


class ModalCreateNewVendor(object):
    VENDOR_CREATE_NEW = (By.CSS_SELECTOR,
                         '.add-new [data-object-singular="Vendor"]')


class AssetsBusiness(object):
    SYSTEMS = (By.CSS_SELECTOR, '[data-object-singular="System"]'
               '[data-parent=".top-level"]')
    SYSTEMS_COUNT = (By.CSS_SELECTOR, '[data-model-name="System"] .item-count')
    PROCESSES = (By.CSS_SELECTOR, '[data-object-singular="Process"]'
                 '[data-parent=".top-level"]')
    PROCESSES_COUNT = (By.CSS_SELECTOR,
                       '[data-model-name="Process"] .item-count')
    DATA_ASSETS = (By.CSS_SELECTOR, '[data-object-singular="DataAsset"]'
                   '[data-parent=".top-level"]')
    DATA_ASSETS_COUNT = (By.CSS_SELECTOR,
                         '[data-model-name="DataAsset"] .item-count')
    PRODUCTS = (By.CSS_SELECTOR, '[data-object-singular="Product"]'
                '[data-parent=".top-level"]')
    PRODUCTS_COUNT = (By.CSS_SELECTOR,
                      '[data-model-name="Product"] .item-count')
    PROJECTS = (By.CSS_SELECTOR, '[data-object-singular="Project"]'
                '[data-parent=".top-level"]')
    PROJECTS_COUNT = (By.CSS_SELECTOR,
                      '[data-model-name="Project"] .item-count')
    FACILITIES = (By.CSS_SELECTOR, '[data-object-singular="Facility"]'
                  '[data-parent=".top-level"]')
    FACILITIES_COUNT = (By.CSS_SELECTOR,
                        '[data-model-name="Facility"] .item-count')
    MARKETS = (By.CSS_SELECTOR, '[data-object-singular="Market"]'
               '[data-parent=".top-level"]')
    MARKETS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Market"] .item-count')


class ModalCreateNewSystem(object):
    SYSTEM_CREATE_NEW = (By.CSS_SELECTOR,
                         '.add-new [data-object-singular="System"]')


class ModalCreateNewProcess(object):
    PROCESS_CREATE_NEW = (By.CSS_SELECTOR,
                          '.add-new [data-object-singular="Process"]')


class ModalCreateNewDataAsset(object):
    DATA_ASSET_CREATE_NEW = (By.CSS_SELECTOR,
                             '.add-new [data-object-singular="DataAsset"]')


class ModalCreateNewProduct(object):
    PRODUCT_CREATE_NEW = (By.CSS_SELECTOR,
                          '.add-new [data-object-singular="Product"]')


class ModalCreateNewProject(object):
    PROJECT_CREATE_NEW = (By.CSS_SELECTOR,
                          '.add-new [data-object-singular="Project"]')


class ModalCreateNewFacility(object):
    FACILITY_CREATE_NEW = (By.CSS_SELECTOR,
                           '.add-new [data-object-singular="Facility"]')


class ModalCreateNewMarket(object):
    MARKET_CREATE_NEW = (By.CSS_SELECTOR,
                         '.add-new [data-object-singular="Market"]')


class RiskThreats(object):
    RISKS = (By.CSS_SELECTOR,
             '[data-object-singular="Risk"][data-parent=".top-level"]')
    RISKS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Risk"] .item-count')
    THREAT_ACTORS = (By.CSS_SELECTOR, '[data-object-singular="Threat"]'
                     '[data-parent=".top-level"]')
    THREAT_ACTORS_COUNT = (By.CSS_SELECTOR,
                           '[data-model-name="Threat"] .item-count')


class ModalCreateNewRisk(object):
    RISK_CREATE_NEW = (By.CSS_SELECTOR,
                       '.add-new [data-object-singular="Risk"]')
    RISK_TITLE = (By.CSS_SELECTOR, '[name="title"]')
    RISK_DESCRIPTION = (By.CSS_SELECTOR, '.wysiwyg-area iframe[tabindex="2"]')
    RISK_OWNER = (By.CSS_SELECTOR, '[data-lookup="Person"][tabindex="3"]')


class ModalCreateNewThreatActor(object):
    THREAT_ACTOR_CREATE_NEW = (By.CSS_SELECTOR,
                               '.add-new [data-object-singular="Threat"]')
    THREAT_ACTOR_TITLE = (By.CSS_SELECTOR, '[name="title"]')


class WidgetBar(object):
    BUTTON_ADD = (By.CSS_SELECTOR, ".hidden-widgets-list")
    DROPDOWN = (By.CSS_SELECTOR, ".inner-nav-item")
    TAB_ACTIVE = (By.CSS_SELECTOR, ".object-nav .active")


class WidgetBarAddObject(object):
    CREATE_NEW_OBJECT = (By.CSS_SELECTOR, '.top-space .dropdown-toggle')

    REGULATIONS = (By.CSS_SELECTOR,
                   '.inner-nav-item [data-object-singular="Regulation"]')
    POLICIES = (By.CSS_SELECTOR,
                '.inner-nav-item [data-object-singular="Policy"]')
    STANDARDS = (By.CSS_SELECTOR,
                 '.inner-nav-item [data-object-singular="Standard"]')
    CONTRACTS = (By.CSS_SELECTOR,
                 '.inner-nav-item [data-object-singular="Contract"]')
    CLAUSES = (By.CSS_SELECTOR,
               '.inner-nav-item [data-object-singular="Clause"]')
    ADD_WIDGET = (By.CSS_SELECTOR, '[data-placement="bottom"].dropdown-toggle')


class Widget(object):
    BUTTON_SETTINGS = (By.CSS_SELECTOR,
                       '[data-test-id="button_settings_0839163b"]')
    DROPDOWN_DELETE = (By.CSS_SELECTOR,
                       '[data-test-id="dropdown_delete_0839163b"]')
    TITLE = (By.CSS_SELECTOR, '[data-test-id="title_0ad9fbaf"] h6')
    TITLE_ENTERED = (By.CSS_SELECTOR, '[data-test-id="title_0ad9fbaf"] h3')
    OBJECT_REVIEW = (By.CSS_SELECTOR,
                     '[data-test-id="title_review_0ad9fbaf"] h6')
    SUBMIT_FOR_REVIEW = (By.CSS_SELECTOR,
                         '[data-test-id="title_review_0ad9fbaf"] '
                         '[href="javascript://"]')
    DESCRIPTION = (By.CSS_SELECTOR,
                   '[data-test-id="title_description_7a906d2e"] h6')
    DESCRIPTION_ENTERED = (By.CSS_SELECTOR,
                           '[data-test-id="title_description_'
                           'content_7a906d2e"]')
    NOTES = (By.CSS_SELECTOR, '[data-test-id="title_notes_ef5bc3a71e88"] '
                              'h6')
    NOTES_ENTERED = (By.CSS_SELECTOR,
                     '[data-test-id="title_notes_ef5bc3a71e88"]')
    MANAGER = (By.CSS_SELECTOR, '[data-test-id="title_manager_7a906d2e"] '
                                'h6')
    MANAGER_ENTERED = (By.CSS_SELECTOR,
                       '[data-test-id="title_manager_7a906d2e"] '
                       '[data-test-id="text_manager_7a906d2e"]')
    PROGRAM_URL = (By.CSS_SELECTOR,
                   '[data-test-id="title_program_url_aa7d1a65"] h6')
    PROGRAM_URL_ENTERED = (By.CSS_SELECTOR,
                           '[data-test-id="text_program_url_aa7d1a65"]')
    REFERENCE_URL = (By.CSS_SELECTOR,
                     '[data-test-id="title_reference_url_aa7d1a65]')
    REFERENCE_URL_ENTERED = (By.CSS_SELECTOR,
                             '[data-test-id="text_reference_url_aa7d1a65"]')
    BUTTON_SHOW_ADVANCED = (By.CSS_SELECTOR,
                            '[data-test-id="button_advanced_cf47bc01"]')
    CODE = (By.CSS_SELECTOR, '[data-test-id="title_code_cf47bc01"] h6')
    CODE_ENTERED = (By.CSS_SELECTOR,
                    '[data-test-id="title_code_cf47bc01"] p')
    EFFECTIVE_DATE = (By.CSS_SELECTOR,
                      '[data-test-id="title_effective_date_cf47bc01"] h6')
    EFFECTIVE_DATE_ENTERED = (By.CSS_SELECTOR,
                              '[data-test-id="title_effective_date_'
                              'cf47bc01"] p')
    STOP_DATE = (By.CSS_SELECTOR,
                 '[data-test-id="title_stop_date_cf47bc01"] h6')
    STOP_DATE_ENTERED = (By.CSS_SELECTOR,
                         '[data-test-id="title_stop_date_cf47bc01"] p')
    BUTTON_SHOW_CUSTOM_ATTR = (By.CSS_SELECTOR, '[data-test-id="button_'
                                                'custom_attrs_cf47bc01"]')
    STATE = (By.CSS_SELECTOR, '[data-test-id="title_state_0ad9fbaf"] h6')
    STATE_ENTERED = (By.CSS_SELECTOR,
                     '[data-test-id="title_state_value_0ad9fbaf"]')
    PRIMARY_CONTACT = (By.CSS_SELECTOR, '[data-test-id="title_primary_'
                                        'contact_696de7244b84"] h6')
    PRIMARY_CONTACT_ENTERED = (
        By.CSS_SELECTOR, '[data-test-id="text_primary_contact_'
                         '696de7244b84"] [data-test-id="text_'
                         'manager_7a906d2e"]')
    SECONDARY_CONTACT = (
        By.CSS_SELECTOR, '[data-test-id="title_contacts_696de7244b84"] '
                         'h6:nth-child(2)')
    SECONDARY_CONTACT_ENTERED = (
        By.CSS_SELECTOR, '[data-test-id="text_secondary_contact_'
                         '696de7244b84"] [data-test-id="text_manager_'
                         '7a906d2e"]')
    PRIVATE_PROGRAM = (By.CSS_SELECTOR,
                       '[data-test-id="title_private_ec758af9"] h6')
    ICON_LOCK = (By.CSS_SELECTOR, '[data-test-id="icon_private_ec758af9"]')
    NEW_TAB = (By.CSS_SELECTOR, '[target="_blank"][href^="/"]')
    PROGRAM_TREE = (By.CSS_SELECTOR, '#program_widget .tree-structure > li')

class AdminDashboardPage(object):
    PREVIOUS_PAGE = (By.CSS_SELECTOR,
                     'a.view-more-paging:not([data-next="true"])')
    NEXT_PAGE = (By.CSS_SELECTOR,
                 'a.view-more-paging[data-next="true"]')

    class HorizontalMenu(object):
        PEOPLE_ITEM = (By.CSS_SELECTOR, 'a[href="#people_list_widget"]')
        ROLES_ITEM =  (By.CSS_SELECTOR, 'a[href="#roles_list_widget"]')
        EVENTS_ITEM = (By.CSS_SELECTOR, 'a[href="#events_list_widget"]')
        CUSTOM_ATTRIBUTES_ITEM = (By.CSS_SELECTOR,
                                        'a[href="#custom_attribute_widget"]')

    class PeopleList(object):
        GEAR_BUTTON = (By.CSS_SELECTOR, 'div.details-wrap a.dropdown-toggle')
        DROPDOWN_MENU = (By.CSS_SELECTOR, 'div.details-wrap ul.dropdown-menu')
        ADD_PERSON = (By.CSS_SELECTOR, 'li.tree-item-add > a.btn')

        SEARCH = (By.CSS_SELECTOR, 'input[name="search"]')
        USER_ROLE = (By.CSS_SELECTOR, 'select[name="user_role"]')

        LIST_ELEMENT = (By.CSS_SELECTOR, '#people_list_widget li.role')
        LIST_ELEMENT_FOR_USER_ROLE = (By.CSS_SELECTOR,
                                      '#people_list_widget li.tree-item')

        class FirstItem(object):
            id = '1'
            USERNAME = (By.CSS_SELECTOR,
                        'ul.tree-structure li.tree-item:nth-child(' + \
                        id +  \
                        ') div.row-fluid div.title')
            EMAIL = (By.CSS_SELECTOR,
                     'ul.tree-structure li.tree-item:nth-child(' + \
                     id +  \
                     ') div.row-fluid div.email')
            LEFT_ARROW = (By.CSS_SELECTOR,
                          'li.tree-item:nth-child(' + \
                          id +  \
                          ') i.grcicon-arrow-right:nth-child(2)')

            class AdditionalContent(object):
                id = '1'
                CONTAINER = (By.CSS_SELECTOR,
                    'section#people_list_widget ul.tree-structure li.tree-item:nth-child(' + id +  ') div.tier-2-info-content div.tier-content')
                ELT = (By.CSS_SELECTOR,
                    'section#people_list_widget ul.tree-structure li.tree-item:nth-child(' + id +  ') div.tier-2-info-content div.tier-content div.row-fluid')
                ELT_LABEL = (By.CSS_SELECTOR,
                    'section#people_list_widget ul.tree-structure li.tree-item:nth-child(' + id +  ') div.tier-2-info-content div.tier-content div.row-fluid h6')
                ELT_CONTENT = (By.CSS_SELECTOR,
                    'section#people_list_widget ul.tree-structure li.tree-item:nth-child(' + id +  ') div.tier-2-info-content div.tier-content div.row-fluid h3')

        class AdditionalContent(object):
            class Dropdown(object):
                UL = (By.CSS_SELECTOR,
                    'div.details-wrap.open ul.dropdown-menu')
                LI = (By.CSS_SELECTOR,
                    'div.details-wrap.open ul.dropdown-menu li')
                LI_SUB = (By.CSS_SELECTOR,
                    'div.details-wrap.open ul.dropdown-menu li a')

                EDIT = (By.CSS_SELECTOR,
                    'div.details-wrap.open ul.dropdown-menu li:nth-child(3)')
                AUTHORIZATIONS = (By.CSS_SELECTOR,
                    'div.details-wrap ul.dropdown-menu li:nth-child(2)')

        class AddPerson(object):
            NAME = (By.CSS_SELECTOR, "input#person_name")
            EMAIL = (By.CSS_SELECTOR, 'input#person_email')
            COMPANY = (By.CSS_SELECTOR, 'input#person_company')
            ADDMORE = (By.CSS_SELECTOR,
                'div.modal a[data-toggle="modal-submit-addmore"')

    class Roles(object):
        LIST = (By.CSS_SELECTOR, 'section#roles_list_widget')
        LIST_ELEMENT = (By.CSS_SELECTOR, 'section#roles_list_widget li.role')
        LIST_ELEMENT_NAME = (By.CSS_SELECTOR, '#roles_list_widget li.role div.title')

    class Events(object):
        LIST = (By.CSS_SELECTOR, 'section#events_list_widget')
        LIST_ELEMENT = (By.CSS_SELECTOR, '#events_list_widget li.tree-item')
        LIST_ELEMENT_NAME = (By.CSS_SELECTOR, '#events_list_widget li.tree-item div.item-data')

        FIRST_LIST_ELEMENT_DATE = (By.CSS_SELECTOR, '#events_list_widget li.tree-item:nth-child(1) div.item-data span.event-time')

    class CustomAttributes(object):
        FILTER = (By.CSS_SELECTOR,
            '.filter-title-wrap > div:nth-child(1) > h6:nth-child(1)')
        LIST = (By.CSS_SELECTOR, 'ul#ui-id-1')
        LIST_ELEMENT = (By.CSS_SELECTOR,
            'ul#ui-id-1>.cms_controllers_tree_view_node')
        LIST_ELEMENT_NAME = (By.CSS_SELECTOR,
            'ul#ui-id-1>.cms_controllers_tree_view_node div.row-fluid div.item-data div')

        LEFT_ARROW = (By.CSS_SELECTOR,
            '#custom_attribute_widget li.tree-item:nth-child(1) div.openclose i.grcicon-arrow-right')

        class AdditionalContent(object):
            id = '1'
            ADDITIONAL_DATA = (By.CSS_SELECTOR,
                '#custom_attribute_widget  li.tree-item:nth-child(' + id + \
                ') div.tier-2-info-content div.table-wrap ')

            LIST = (By.CSS_SELECTOR,
                '#custom_attribute_widget  li.tree-item:nth-child(' + id + \
                ') div.tier-2-info-content div.table-wrap table thead tr ')
            LIST_ELEMENT = (By.CSS_SELECTOR,
                '#custom_attribute_widget  li.tree-item:nth-child(' + id + \
                ') div.tier-2-info-content div.table-wrap table thead tr ' + \
                'th')
            LIST_ELEMENT_NAME = LIST_ELEMENT

            ADD_BUTTON = (By.CSS_SELECTOR,
                '#custom_attribute_widget  li.tree-item:nth-child(' + id +  \
                ') div.tier-2-info-content div.table-wrap  a[data-original-title="Add Attribute"]')
            EDIT_BUTTON = (By.CSS_SELECTOR,
                '#custom_attribute_widget  li.tree-item:nth-child(' + id + \
                ') div.tier-2-info-content div.table-wrap  tbody ul.tree-action-list li:nth-child(1) a')

class Export(object):
    SELECT = (By.CSS_SELECTOR,
        '#csv_export > csv-export export-group export-panel select')
    SELECT2 = (By.CSS_SELECTOR,
        '#csv_export > csv-export export-group export-panel[panel_number="1"] select')
    SELECT3 = (By.CSS_SELECTOR,
        '#csv_export > csv-export export-group export-panel[panel_number="2"] select')
    ADD_ANOTHER = (By.CSS_SELECTOR,
        '#addAnotherObjectType')
    EXPORT_OBJECTS = (By.CSS_SELECTOR,
        'button#export-csv-button')

class Import(object):
    IMPORT_OBJECTS = (By.CSS_SELECTOR, 'button#import_btn')
    IMPORT_BUTTON = (By.CSS_SELECTOR, 'button#import_btn')
    IMPORT_FILE = (By.CSS_SELECTOR, 'input.csv-upload')

class Modal(object):
    CLOSE = (By.CSS_SELECTOR,
             'a.modal-dismiss')
    TITLE = (By.CSS_SELECTOR,
             'div.modal div.modal-header h2')
    BUTTON_SUCCESS = (By.CSS_SELECTOR,
                      'a.btn-success')
