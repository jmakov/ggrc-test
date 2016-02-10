# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: jernej@reciprocitylabs.com
# Maintained By: jernej@reciprocitylabs.com

from selenium.webdriver.common.by import By


class Login(object):
  BUTTON_LOGIN = (By.CSS_SELECTOR, "a.btn.btn-large.btn-info")


class PageHeader(object):
  BUTTON_LHN = (By.CSS_SELECTOR, ".lhn-trigger")
  BUTTON_DASHBOARD = (By.CSS_SELECTOR, '.header-content .to-my-work['
                                       'href="/dashboard"]')
  BUTTON_SEARCH = (By.CSS_SELECTOR, '.header-content ['
                                    'data-toggle="unified-search"]')
  BUTTON_MY_TASKS = (By.CSS_SELECTOR, '.header-content ['
                                      'href="/dashboard#task_widget"]')
  BUTTON_ALL_OBJECTS = (By.CSS_SELECTOR, '.header-content ['
                                         'href="/objectBrowser"]')
  BUTTON_USER_DROPDOWN = (
      By.CSS_SELECTOR, '.header-content .dropdown-toggle')
  BUTTON_HELP = (By.CSS_SELECTOR, '.header-content [id="#page-help"]')

  # dropdown toggle
  BUTTON_ADMIN_DASHBOARD = (
      By.CSS_SELECTOR, '.dropdown-menu [href="/admin#people_list_widget"]')
  BUTTON_MY_WORK = (By.CSS_SELECTOR, '.dropdown-menu [href="/dashboard"]')
  BUTTON_DATA_IMPORT = (By.CSS_SELECTOR, '.dropdown-menu [href="/import"]')
  BUTTON_DATA_EXPORT = (By.CSS_SELECTOR, '.dropdown-menu [href="/export"]')
  BUTTON_LOGOUT = (By.CSS_SELECTOR, '.dropdown-menu [href="/logout"]')


class Dashboard(object):
  BUTTON_START_NEW_PROGRAM = (
      By.CSS_SELECTOR, '.quick-list [data-object-singular="Program"]')
  BUTTON_START_NEW_AUDIT = (
      By.CSS_SELECTOR, '.quick-list [data-object-singular="Audit"]')
  BUTTON_START_NEW_WORKFLOW = (
      By.CSS_SELECTOR, '.quick-list [data-object-singular="Workflow"]')
  BUTTON_CREATE_NEW_OBJECT = (
      By.CSS_SELECTOR, '.quick-list [href="#"]')
  BUTTON_ALL_OBJECTS = (By.CSS_SELECTOR, '.quick-list '
                                         '[href="/objectBrowser"]')


class LhnMenu(object):
  LHN_MENU = (By.ID, "lhn")
  MODAL = (By.CSS_SELECTOR, '[id="ajax-lhn_modal-javascript:--"]')

  FILTER = (By.CSS_SELECTOR, '.lhs-search')
  FILTER_TEXT_BOX = (By.CSS_SELECTOR, '.lhs-search>.widgetsearch')
  FILTER_SUBMIT_BUTTON = (
      By.CSS_SELECTOR, '.lhs-search>.widgetsearch-submit')
  FILTER_CLEAR_BUTTON = (
      By.CSS_SELECTOR, '.lhs-search [data-title="Clear filters"]')

  LHS_ITEM = (By.CSS_SELECTOR, '[test-data-id="lhs-item_3ad27b8b"]')
  ALL_OBJECTS = (By.CSS_SELECTOR, '[data-test-id="all_objects_e0345ec4"]')
  MY_OBJECTS = (By.CSS_SELECTOR, '[data-test-id="my_objects_6fa95ae1"]')

  # lhn items
  PROGRAMS = (By.CSS_SELECTOR, '[data-model-name="Program"]')
  WORKFLOWS = (By.CSS_SELECTOR, '[data-model-name="Workflow"]')
  AUDITS = (By.CSS_SELECTOR, '[data-model-name="Audit"]')
  ASSESSMENTS = (By.CSS_SELECTOR,
                 '[data-model-name="Assessment"]')
  REQUESTS = (By.CSS_SELECTOR, '[data-model-name="Request"]')
  ISSUES = (By.CSS_SELECTOR, '[data-model-name="Issue"]')
  DIRECTIVES = (By.CSS_SELECTOR, '[data-test-id="directives_66116337"]')
  REGULATIONS = (By.CSS_SELECTOR, '[data-model-name="Regulation"]')
  POLICIES = (By.CSS_SELECTOR, '[data-model-name="Policy"]')
  STANDARDS = (By.CSS_SELECTOR, '[data-model-name="Standard"]')
  CONTRACTS = (By.CSS_SELECTOR, '[data-model-name="Contract"]')
  CLAUSES = (By.CSS_SELECTOR, '[data-model-name="Clause"]')
  SECTIONS = (By.CSS_SELECTOR, '[data-model-name="Section"]')
  CONTROLS_OR_OBJECTIVES = (By.CSS_SELECTOR,
                            '[data-test-id="controls/objectives_66116337"]')
  CONTROLS = (By.CSS_SELECTOR, '[data-model-name="Control"]')
  OBJECTIVES = (By.CSS_SELECTOR, '[data-model-name="Objective"]')
  PEOPLE_OR_GROUPS = (By.CSS_SELECTOR,
                      '[data-test-id="people/groups_66116337"]')
  PEOPLE = (By.CSS_SELECTOR, '[data-model-name="Person"]')
  ORG_GROUPS = (By.CSS_SELECTOR, '[data-model-name="OrgGroup"]')
  ASSETS_OR_BUSINESS = (By.CSS_SELECTOR,
                        '[data-test-id="assets/business_66116337"]')
  SYSTEMS = (By.CSS_SELECTOR, '[data-model-name="System"]')
  PROCESSES = (By.CSS_SELECTOR, '[data-model-name="Process"]')
  DATA_ASSETS = (By.CSS_SELECTOR, '[data-model-name="DataAsset"]')
  ACCESS_GROUPS = (By.CSS_SELECTOR, '[data-model-name="AccessGroup"]')
  VENDORS = (By.CSS_SELECTOR, '[data-model-name="Vendor"]')
  PRODUCTS = (By.CSS_SELECTOR, '[data-model-name="Product"]')
  PROJECTS = (By.CSS_SELECTOR, '[data-model-name="Project"]')
  RISK_OR_THREATS = (By.CSS_SELECTOR,
                     '[data-test-id="risk/threats_66116337"]')
  RISKS = (By.CSS_SELECTOR, '[data-model-name="Risk"]')
  FACILITIES = (By.CSS_SELECTOR, '[data-model-name="Facility"]')
  MARKETS = (By.CSS_SELECTOR, '[data-model-name="Market"]')
  THREATS = (By.CSS_SELECTOR, '[data-model-name="Threat"]')

  # buttons create new lhn_modal
  BUTTON_CREATE_NEW_PROGRAM = (
      By.CSS_SELECTOR,
      '[data-model-name="Program"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_NEW_WORKFLOW = (
      By.CSS_SELECTOR,
      '[data-model-name="Workflow"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_NEW_AUDIT = (
      By.CSS_SELECTOR,
      '[data-model-name="Audit"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_NEW_CONTROL_ASSESSMENT = (
      By.CSS_SELECTOR,
      '[data-model-name="ControlAssessment"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_NEW_REQUEST = (
      By.CSS_SELECTOR,
      '[data-model-name="Request"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_ISSUE = (
      By.CSS_SELECTOR,
      '[data-model-name="Issue"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_REGULATION = (
      By.CSS_SELECTOR,
      '[data-model-name="Regulation"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_POLICY = (
      By.CSS_SELECTOR,
      '[data-model-name="Policy"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_STANDARD = (
      By.CSS_SELECTOR,
      '[data-model-name="Standard"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_CONTRACT = (
      By.CSS_SELECTOR,
      '[data-model-name="Contract"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_CLAUSE = (
      By.CSS_SELECTOR,
      '[data-model-name="Clause"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_SECTION = (
      By.CSS_SELECTOR,
      '[data-model-name="Section"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_CONTROL = (
      By.CSS_SELECTOR,
      '[data-model-name="Control"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_OBJECTIVE = (
      By.CSS_SELECTOR,
      '[data-model-name="Objective"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_PERSON = (
      By.CSS_SELECTOR,
      '[data-model-name="Person"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_ORG_GROUP = (
      By.CSS_SELECTOR,
      '[data-model-name="OrgGroup"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_VENDOR = (
      By.CSS_SELECTOR,
      '[data-model-name="Vendor"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_ACCESS_GROUP = (
      By.CSS_SELECTOR,
      '[data-model-name="AccessGroup"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_SYSTEM = (
      By.CSS_SELECTOR,
      '[data-model-name="System"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_PROCESS = (
      By.CSS_SELECTOR,
      '[data-model-name="Process"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_DATA_ASSET = (
      By.CSS_SELECTOR,
      '[data-model-name="DataAsset"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_PRODUCT = (
      By.CSS_SELECTOR,
      '[data-model-name="Product"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_PROJECT = (
      By.CSS_SELECTOR,
      '[data-model-name="Project"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_FACILITY = (
      By.CSS_SELECTOR,
      '[data-model-name="Facility"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_MARKET = (
      By.CSS_SELECTOR,
      '[data-model-name="Market"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_RISK = (
      By.CSS_SELECTOR,
      '[data-model-name="Risk"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')
  BUTTON_CREATE_THREAT = (
      By.CSS_SELECTOR,
      '[data-model-name="Threat"] ['
      'data-test-id="button_lhn_create_new_program_522c563f"]')

  # count locators
  PROGRAMS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Program"] '
                                     '.item-count')
  WORKFLOWS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Workflow"] '
                                      '.item-count')
  AUDITS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Audit"] .item-count')
  ASSESSMENTS_COUNT = (By.CSS_SELECTOR,
                       '[data-model-name="Assessment"] '
                       '.item-count')
  ISSUES_COUNT = (By.CSS_SELECTOR, '[data-model-name="Issue"] .item-count')
  REQUESTS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Request"] '
                                     '.item-count')
  REGULATIONS_COUNT = (By.CSS_SELECTOR,
                       '[data-model-name="Regulation"] .item-count')
  POLICIES_COUNT = (By.CSS_SELECTOR,
                    '[data-model-name="Policy"] .item-count')
  STANDARDS_COUNT = (By.CSS_SELECTOR,
                     '[data-model-name="Standard"] .item-count')
  CONTRACTS_COUNT = (By.CSS_SELECTOR,
                     '[data-model-name="Clause"] .item-count')
  CLAUSES_COUNT = (By.CSS_SELECTOR,
                   '[data-model-name="Regulation"] .item-count')
  SECTIONS_COUNT = (By.CSS_SELECTOR,
                    '[data-model-name="Section"] .item-count')
  CONTROL_COUNT = (
      By.CSS_SELECTOR, '[data-model-name="Control"] .item-count')
  OBJECTIVES_COUNT = (By.CSS_SELECTOR, '[data-model-name="Objective"] '
                                       '.item-count')
  PEOPLE_COUNT = (By.CSS_SELECTOR, '[data-model-name="Person"] .item-count')
  ORG_GROUPS_COUNT = (By.CSS_SELECTOR, '[data-model-name="OrgGroup"] '
                                       '.item-count')
  VENDORS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Vendor"] .item-count')
  ACCESS_GROUPS_COUNT = (By.CSS_SELECTOR, '[data-model-name="AccessGroup"] '
                                          '.item-count')
  SYSTEMS_COUNT = (By.CSS_SELECTOR, '[data-model-name="System"] .item-count')
  PROCESSES_COUNT = (By.CSS_SELECTOR, '[data-model-name="Process"] '
                                      '.item-count')
  DATA_ASSETS_COUNT = (By.CSS_SELECTOR, '[data-model-name="DataAsset"] '
                                        '.item-count')
  PRODUCTS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Product"] '
                                     '.item-count')
  PROJECTS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Project"] '
                                     '.item-count')
  FACILITIES_COUNT = (By.CSS_SELECTOR, '[data-model-name="Facility"] '
                                       '.item-count')
  MARKETS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Market"] .item-count')
  RISKS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Risk"] .item-count')
  THREATS_COUNT = (By.CSS_SELECTOR, '[data-model-name="Threat"] .item-count')

  # workflows labels
  WORKFLOWS_ACTIVE = (By.CSS_SELECTOR, '[data-for="Workflow"]>['
                                       'data-value="Active"]')
  WORKFLOWS_DRAFT = (By.CSS_SELECTOR, '[data-for="Workflow"]>['
                                      'data-value="Draft"]')
  WORKFLOWS_INACTIVE = (By.CSS_SELECTOR, '[data-for="Workflow"]>['
                                         'data-value="Inactive"]')

  # spinny
  SPINNY_PROGRAMS = (By.CSS_SELECTOR, '[data-model-name="Program"] .spinny')
  SPINNY_WORKFLOWS = (
      By.CSS_SELECTOR, '[data-model-name="Workflow"] .spinny')
  SPINNY_AUDITS = (By.CSS_SELECTOR, '[data-model-name="Audit"] .spinny')
  SPINNY_CONTROL_ASSESSMENTS = (
      By.CSS_SELECTOR, '[data-model-name="ControlAssessment"] .spinny')
  SPINNY_REQUESTS = (By.CSS_SELECTOR, '[data-model-name="Request"] .spinny')
  SPINNY_ISSUES = (By.CSS_SELECTOR, '[data-model-name="Issue"] .spinny')
  SPINNY_REGULATIONS = (
      By.CSS_SELECTOR, '[data-model-name="Regulation"] .spinny')
  SPINNY_POLICIES = (By.CSS_SELECTOR, '[data-model-name="Policy"] .spinny')
  SPINNY_STANDARDS = (
      By.CSS_SELECTOR, '[data-model-name="Standard"] .spinny')
  SPINNY_CONTRACTS = (
      By.CSS_SELECTOR, '[data-model-name="Contract"] .spinny')
  SPINNY_CLAUSES = (By.CSS_SELECTOR, '[data-model-name="Clause"] .spinny')
  SPINNY_SECTIONS = (By.CSS_SELECTOR, '[data-model-name="Section"] .spinny')
  SPINNY_CONTROLS = (By.CSS_SELECTOR, '[data-model-name="Control"] .spinny')
  SPINNY_OBJECTIVES = (
      By.CSS_SELECTOR, '[data-model-name="Objective"] .spinny')
  SPINNY_PEOPLE = (By.CSS_SELECTOR, '[data-model-name="Person"] .spinny')
  SPINNY_ORG_GROUPS = (
      By.CSS_SELECTOR, '[data-model-name="OrgGroup"] .spinny')
  SPINNY_VENDORS = (By.CSS_SELECTOR, '[data-model-name="Vendor"] .spinny')
  SPINNY_ACCESS_GROUPS = (
      By.CSS_SELECTOR, '[data-model-name="AccessGroup"] .spinny')
  SPINNY_SYSTEMS = (By.CSS_SELECTOR, '[data-model-name="System"] .spinny')
  SPINNY_PROCESSES = (By.CSS_SELECTOR, '[data-model-name="Process"] .spinny')
  SPINNY_DATA_ASSETS = (
      By.CSS_SELECTOR, '[data-model-name="DataAsset"] .spinny')
  SPINNY_PRODUCTS = (By.CSS_SELECTOR, '[data-model-name="Product"] .spinny')
  SPINNY_PROJECTS = (By.CSS_SELECTOR, '[data-model-name="Project"] .spinny')
  SPINNY_FACILITIES = (
      By.CSS_SELECTOR, '[data-model-name="Facility"] .spinny')
  SPINNY_MARKETS = (By.CSS_SELECTOR, '[data-model-name="Market"] .spinny')
  SPINNY_RISKS = (By.CSS_SELECTOR, '[data-model-name="Risk"] .spinny')
  SPINNY_THREATS = (By.CSS_SELECTOR, '[data-model-name="Threat"] .spinny')


class ModalCreateNewProgram(object):
  UI_TITLE = (By.CSS_SELECTOR,
              '[data-test-id="new_program_field_title_a63ed79d"]')
  UI_DESCRIPTION = (By.CSS_SELECTOR,
                    '[data-test-id="new_program_field_description_1fb8bc06"]'
                    '>iframe.wysihtml5-sandbox')
  NOTES_UI = (By.CSS_SELECTOR,
              '[data-test-id="new_program_field_notes_75b8bc05"]'
              '>iframe.wysihtml5-sandbox')
  UI_CODE = (By.CSS_SELECTOR,
             '[data-test-id="new_program_field_code_334276e2"]')
  UI_STATE = (By.CSS_SELECTOR,
              '[data-test-id="new_program_dropdown_state_036a1fa6"]')
  BUTTON_HIDE_OPTIONAL_FIELDS = (By.ID, "formHide")
  BUTTON_SHOW_ALL_OPTIONAL_FIELDS = (By.ID, "formHide")
  UI_PRIMARY_CONTACT = (By.CSS_SELECTOR, '[data-test-id='
                                         '"new_program_field_primary_contact_'
                                         '86160053"]')
  DROPDOWN_CONTACT = (By.CSS_SELECTOR, '.ui-menu-item')
  UI_SECONDARY_CONTACT = (By.CSS_SELECTOR, '[data-test-id='
                                           '"new_program_field_secondary_'
                                           'contact_'
                                           '86160053"]')
  BUTTON_SAVE_AND_CLOSE = (By.CSS_SELECTOR, '[data-toggle="modal-submit"]')
  BUTTON_SAVE_AND_ADD_ANOTHER = (By.CSS_SELECTOR,
                                 '[data-toggle="modal-submit-addmore"]')
  UI_PROGRAM_URL = (By.CSS_SELECTOR, '[data-test-id='
                                     '"new_program_field_program_url_'
                                     '86160053"]')
  UI_REFERENCE_URL = (By.CSS_SELECTOR, '[data-test-id='
                                       '"new_program_field_reference_url_'
                                       '86160053"]')
  UI_EFFECTIVE_DATE = (By.CSS_SELECTOR, '[data-test-id='
                                        '"new_program_field_effective_date_'
                                        'f2783a28"]')
  UI_STOP_DATE = (By.CSS_SELECTOR, '[data-test-id='
                                   '"new_program_field_stop_date_f2783a28"]')
  DATE_PICKER = (By.CSS_SELECTOR, '.ui-datepicker-calendar ['
                                  'data-handler="selectDay"]')
  TITLE = (By.CSS_SELECTOR, '[data-test-id="label_title_2c925d94"]')
  DESCRIPTION = (By.CSS_SELECTOR,
                 '[data-test-id="label_description_2c925d94"]')

  PRIVACY = (By.CSS_SELECTOR, '[data-test-id="label_privacy_2c925d94"]')
  PROGRAM_URL = (By.CSS_SELECTOR,
                 '[data-test-id="label_program_url_2c925d94"]')


class ModalCustomAttribute(object):
  MODAL_TITLE = (By.CSS_SELECTOR, '.modal-header h2')
  ATTRIBUTE_TITLE = (By.CSS_SELECTOR, '.modal-body div:nth-child(1)>label')
  INLINE_HELP = (By.CSS_SELECTOR, '.modal-body div:nth-child(2)>label')
  ATTRIBUTE_TYPE = (By.CSS_SELECTOR, '.modal-header h2')
  PLACEHOLDER = (By.CSS_SELECTOR, '.modal-header h2')
  MANDATORY = (By.CSS_SELECTOR, '.modal-header h2')
  UI_ATTRIBUTE_TITLE = (
      By.CSS_SELECTOR, '.modal-body div:nth-child(1)>input[tabindex="1"]')
  UI_INLINE_HELP = (
      By.CSS_SELECTOR,
      '.modal-body div:nth-child(1)>input[tabindex="4"]')
  UI_PLACEHOLDER = (By.CSS_SELECTOR, '.modal-body div:nth-child(2)>input')
  CHECKBOX_MANDATORY = (By.CSS_SELECTOR, '.modal-body [type="checkbox"]')
  BUTTON_SAVE = (By.CSS_SELECTOR, '.modal-footer .confirm-buttons '
                                  '[data-toggle="modal-submit"]')
  BUTTON_ADD_ANOTHER = (
      By.CSS_SELECTOR,
      '.modal-footer .confirm-buttons [data-toggle="modal-submit-addmore"]'
  )


class WidgetBar(object):
  BUTTON_ADD = (By.CSS_SELECTOR,
                '[data-test-id="button_widget_add_2c925d94"]')
  TAB_WIDGET = (By.CSS_SELECTOR, ".object-nav .active")
  ADMIN_PEOPLE = (By.CSS_SELECTOR, '[href="#people_list_widget"]')
  ADMIN_ROLES = (By.CSS_SELECTOR, '[href="#roles_list_widget"]')
  ADMIN_EVENTS = (By.CSS_SELECTOR, '[href="#events_list_widget"]')
  ADMIN_CUSTOM_ATTRIBUTE = (By.CSS_SELECTOR,
                            '[href="#custom_attribute_widget"]')

  INFO = (By.CSS_SELECTOR, '[href="#info_widget"]')
  CUSTOM_ATTRIBUTES = (By.CSS_SELECTOR, '[href="#custom_attribute_widget"]')
  EVENTS = (By.CSS_SELECTOR, '[href="#events_list_widget"]')
  ROLES = (By.CSS_SELECTOR, '[href="#roles_list_widget"]')
  PEOPLE = (By.CSS_SELECTOR, '[href="#person_widget"]')
  MARKETS = (By.CSS_SELECTOR, '[href="#market_widget"]')
  ACCESS_GROUPS = (By.CSS_SELECTOR, '[href="#access_group_widget"]')
  ASSESSMENT = (By.CSS_SELECTOR, '[href="#assessment_widget"]')
  AUDITS = (By.CSS_SELECTOR, '[href="#audit_widget"]')
  CLAUSES = (By.CSS_SELECTOR, '[href="#clause_widget"]')
  CONTRACTS = (By.CSS_SELECTOR, '[href="#contract_widget"]')
  CONTROLS = (By.CSS_SELECTOR, '[href="#control_widget"]')
  DATA_ASSETS = (By.CSS_SELECTOR, '[href="#data_asset_widget"]')
  ISSUES = (By.CSS_SELECTOR, '[href="#issue_widget"]')
  FACILITIES = (By.CSS_SELECTOR, '[href="#facility_widget"]')
  OBJECTIVES = (By.CSS_SELECTOR, '[href="#objective_widget"]')
  ORG_GROUPS = (By.CSS_SELECTOR, '[href="#org_group_widget"]')
  POLICIES = (By.CSS_SELECTOR, '[href="#policy_widget"]')
  PROCESSES = (By.CSS_SELECTOR, '[href="#process_widget"]')
  PRODUCTS = (By.CSS_SELECTOR, '[href="#product_widget"]')
  PROJECTS = (By.CSS_SELECTOR, '[href="#project_widget"]')
  REGULATIONS = (By.CSS_SELECTOR, '[href="#regulation_widget"]')
  REQUESTS = (By.CSS_SELECTOR, '[href="#request_widget"]')
  SECTIONS = (By.CSS_SELECTOR, '[href="#section_widget"]')
  STANDARDS = (By.CSS_SELECTOR, '[href="#standard_widget"]')
  SYSTEMS = (By.CSS_SELECTOR, '[href="#system_widget"]')
  VENDORS = (By.CSS_SELECTOR, '[href="#vendor_widget"]')
  RISKS = (By.CSS_SELECTOR, '[href="#risks_widget"]')
  THREATS = (By.CSS_SELECTOR, '[href="#threats_widget"]')
  RISK_ASSESSMENTS = (By.CSS_SELECTOR, '[href="#risk_assessments_widget"]')
  WORKFLOWS = (By.CSS_SELECTOR, '[href="#workflow_widget"]')
  TASKS = (By.CSS_SELECTOR, '[href="#task_widget"]')


class WidgetBarButtonAddDropdown(object):
  AUDITS = (By.CSS_SELECTOR, '[data-test-id="button_widget_add_2c925d94"] '
                             '[href="#audit_widget"]')
  CONTROLS = (By.CSS_SELECTOR, '[data-test-id="button_widget_add_2c925d94"] '
                               '[href="#control_widget"]')
  DATA_ASSETS = (By.CSS_SELECTOR,
                 '[data-test-id="button_widget_add_2c925d94"] '
                 '[href="#data_asset_widget"]')
  ISSUES = (By.CSS_SELECTOR, '[data-test-id="button_widget_add_2c925d94"] '
                             '[href="#issues_widget"]')
  OBJECTIVES = (By.CSS_SELECTOR,
                '[data-test-id="button_widget_add_2c925d94"] '
                '[href="#objective_widget"]')
  POLICIES = (By.CSS_SELECTOR, '[data-test-id="button_widget_add_2c925d94"] '
                               '[href="#policy_widget"]')
  PRODUCTS = (By.CSS_SELECTOR, '[data-test-id="button_widget_add_2c925d94"] '
                               '[href="#product_widget"]')
  REGULATIONS = (By.CSS_SELECTOR,
                 '[data-test-id="button_widget_add_2c925d94"] '
                 '[href="#regulation_widget"]')
  SYSTEMS = (By.CSS_SELECTOR, '[data-test-id="button_widget_add_2c925d94"] '
                              '[href="#system_widget"]')
  RISKS = (By.CSS_SELECTOR, '[data-test-id="button_widget_add_2c925d94"] '
                            '[href="#risk_widget"]')
  WORKFLOWS = (
      By.CSS_SELECTOR, '[data-test-id="button_widget_add_2c925d94"] '
                       '[href="#workflow_widget"]')
  CONTRACTS = (
      By.CSS_SELECTOR, '[data-test-id="button_widget_add_2c925d94"] '
                       '[href="#contract_widget"]')
  ASSESSMENTS = (By.CSS_SELECTOR,
                 '[data-test-id="button_widget_add_2c925d94"] '
                 '[href="#assessment_widget"]')
  FACILITIES = (By.CSS_SELECTOR,
                '[data-test-id="button_widget_add_2c925d94"] '
                '[href="#facility_widget"]')
  MARKETS = (By.CSS_SELECTOR, '[data-test-id="button_widget_add_2c925d94"] '
                              '[href="#market_widget"]')
  ORG_GROUPS = (By.CSS_SELECTOR,
                '[data-test-id="button_widget_add_2c925d94"] '
                '[href="#org_groups_widget"]')
  PROCESSES = (By.CSS_SELECTOR,
               '[data-test-id="button_widget_add_2c925d94"] '
               '[href="#process_widget"]')
  PROJECTS = (By.CSS_SELECTOR,
              '[data-test-id="button_widget_add_2c925d94"] '
              '[href="#project_widget"]')
  STANDARDS = (By.CSS_SELECTOR,
               '[data-test-id="button_widget_add_2c925d94"] '
               '[href="#standard_widget"]')
  VENDORS = (By.CSS_SELECTOR, '[data-test-id="button_widget_add_2c925d94"] '
                              '[href="#vendor_widget"]')
  THREAD_ACTORS = (By.CSS_SELECTOR,
                   '[data-test-id="button_widget_add_2c925d94"] '
                   '[href="#thread_actors_widget"]')
  WORKFLOW_TASKS = (By.CSS_SELECTOR,
                    '[data-test-id="button_widget_add_2c925d94"] '
                    '[href="#task_widget"]')
  PERSON = (By.CSS_SELECTOR,
            '[data-test-id="button_widget_add_2c925d94"] '
            '[href="#person_widget"]')
  PROGRAM = (By.CSS_SELECTOR,
             '[data-test-id="button_widget_add_2c925d94"] '
             '[href="#program_widget"]')
  ACCESS_GROUP = (By.CSS_SELECTOR,
                  '[data-test-id="button_widget_add_2c925d94"] '
                  '[href="#access_group_widget"]')
  CLAUSE = (By.CSS_SELECTOR,
            '[data-test-id="button_widget_add_2c925d94"] '
            '[href="#clause_widget"]')
  REQUEST = (By.CSS_SELECTOR,
             '[data-test-id="button_widget_add_2c925d94"] '
             '[href="#request_widget"]')
  SECTION = (By.CSS_SELECTOR,
             '[data-test-id="button_widget_add_2c925d94"] '
             '[href="#section_widget"]')
  THREAT = (By.CSS_SELECTOR,
            '[data-test-id="button_widget_add_2c925d94"] '
            '[href="#threat_widget"]')


class Widget(object):
  DROPDOWN_SETTINGS = (By.CSS_SELECTOR, '.info-pane-utility')
  DROPDOWN_SETTINGS_MEMBERS = (By.CSS_SELECTOR, '.info-pane-utility'
                                                ' .dropdown-menu li')
  ALERT_LINK_COPIED = (By.CSS_SELECTOR, '.alert.alert-success')
  DROPDOWN_DELETE = (By.CSS_SELECTOR,
                     '[data-test-id="dropdown_delete_0839163b"]')
  MODAL_DELETE = (By.ID, '[id="ajax-lhn_modal-javascript:--"]')
  MODAL_DELETE_CLOSE = (By.CSS_SELECTOR, '.lhn_modal .grcicon-x-grey')

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
                   '[data-test-id="title_reference_url_aa7d1a65"]')
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
  STATE = (By.CSS_SELECTOR,
           '[dadata-test-id="new_program_button_save_and_new_86160053"'
           ' ta-test-id="title_state_0ad9fbaf"] h6')
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


class AdminCustomAttributes(object):
  FILTER_INPUT_FIELD = (By.CLASS_NAME, 'filter-input')
  FILTER_BUTTON_SUBMIT = (By.CSS_SELECTOR, '.filter-button>[type="submit"]')
  FILTER_BUTTON_RESET = (By.CSS_SELECTOR, '.filter-button>[type="reset"]')
  BUTTON_WORKFLOWS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(1) div '
                                       '.openclose')
  BUTTON_RISK_ASSESSMENTS = (By.CSS_SELECTOR, '.tree-structure li:nth-child('
                                              '2) div .openclose')
  BUTTON_THREATS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(3) div '
                                     '.openclose')
  BUTTON_RISKS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(4) div '
                                   '.openclose')
  BUTTON_PROGRAMS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(5) div '
                                      '.openclose')
  BUTTON_AUDITS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(6) div '
                                    '.openclose')
  BUTTON_OBJECTIVES = (By.CSS_SELECTOR,
                       '.tree-structure li:nth-child(7) div .openclose')
  BUTTON_SECTIONS = (By.CSS_SELECTOR,
                     '.tree-structure li:nth-child(8) div .openclose')
  BUTTON_CONTROLS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(9) div '
                                      '.openclose')
  BUTTON_ISSUES = (By.CSS_SELECTOR, '.tree-structure li:nth-child(10) div '
                                    '.openclose')
  BUTTON_ASSESSMENTS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(11) '
                                         'div .openclose')
  BUTTON_STANDARDS = (By.CSS_SELECTOR,
                      '.tree-structure li:nth-child(12) div .openclose')
  BUTTON_REGULATIONS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(13) '
                                         'div .openclose')
  BUTTON_POLICIES = (By.CSS_SELECTOR, '.tree-structure li:nth-child(14) div '
                                      '.openclose')
  BUTTON_CONTRACTS = (By.CSS_SELECTOR,
                      '.tree-structure li:nth-child(15) div .openclose')
  BUTTON_CLAUSES = (By.CSS_SELECTOR, '.tree-structure li:nth-child(16) div '
                                     '.openclose')
  BUTTON_REQUESTS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(17) div '
                                      '.openclose')
  BUTTON_VENDORS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(18) div '
                                     '.openclose')
  BUTTON_PEOPLE = (By.CSS_SELECTOR, '.tree-structure li:nth-child(19) div '
                                    '.openclose')
  BUTTON_ACCESS_GROUPS = (By.CSS_SELECTOR,
                          '.tree-structure li:nth-child(20) div .openclose')
  BUTTON_ORG_GROUPS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(21) '
                                        'div .openclose')
  BUTTON_PRODUCTS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(22) div '
                                      '.openclose')
  BUTTON_MARKETS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(23) div '
                                     '.openclose')
  BUTTON_PROCESSES = (By.CSS_SELECTOR,
                      '.tree-structure li:nth-child(24) div .openclose')
  BUTTON_FACILITIES = (By.CSS_SELECTOR, '.tree-structure li:nth-child(25) '
                                        'div .openclose')
  BUTTON_PROJECTS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(26) div '
                                      '.openclose')
  BUTTON_DATA_ASSETS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(27) '
                                         'div .openclose')
  BUTTON_SYSTEMS = (By.CSS_SELECTOR, '.tree-structure li:nth-child(28) div '
                                     '.openclose')

  # Dropdown add custom attribute lhn_modal buttons
  BUTTON_ADD_CUSTOM_PROGRAM_ATTR = (
      By.CSS_SELECTOR, '.tree-structure li:nth-child(5)'
                       ' [data-toggle="modal-ajax-form"]')
