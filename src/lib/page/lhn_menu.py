from selenium.webdriver.common.by import By
from lib import base
from lib.constants import locator
from lib.page.modal import new_program
import time
import uuid


class LhnMenu(base.Page):
    pass
#     _lhn_menu_open = selector.PageHeader
#     LHN_MENU = base.Locator(By.CSS_SELECTOR, _lhn_menu_open.TRIGGER)
#
#     _lhn_menu = selector.PageHeader.LhnMenu
#     LHN_PIN = base.Locator(By.CSS_SELECTOR, _lhn_menu.LHN_PIN)
#     MY_OBJECTS = base.Locator(By.CSS_SELECTOR, _lhn_menu.MY_OBJECTS)
#     ALL_OBJECTS = base.Locator(By.CSS_SELECTOR, _lhn_menu.ALL_OBJECTS)
#     LHN_PIN_NOT_ACTIVE = base.Locator(
#         By.CSS_SELECTOR, _lhn_menu.LHN_PIN_NOT_ACTIVE)
#     PROGRAMS_LINK = base.Locator(By.CSS_SELECTOR, _lhn_menu.PROGRAMS_LINK)
#     WORKFLOWS_LINK = base.Locator(By.CSS_SELECTOR, _lhn_menu.WORKFLOWS_LINK)
#     AUDITS_LINK = base.Locator(By.CSS_SELECTOR, _lhn_menu.AUDITS_LINK)
#     CTRL_ASSES_LINK = base.Locator(By.CSS_SELECTOR, _lhn_menu.CTRL_ASSES_LINK)
#     ISSUES_LINK = base.Locator(By.CSS_SELECTOR, _lhn_menu.ISSUES_LINK)
#     DIRECTIVES = base.Locator(By.CSS_SELECTOR, _lhn_menu.DIRECTIVES)
#     CONT_OBJ = base.Locator(By.CSS_SELECTOR, _lhn_menu.CONT_OBJ)
#     PPL_GRP = base.Locator(By.CSS_SELECTOR, _lhn_menu.PPL_GRP)
#     ASSETS = base.Locator(By.CSS_SELECTOR, _lhn_menu.ASSETS)
#     RISKS = base.Locator(By.CSS_SELECTOR, _lhn_menu.RISKS)
#     REC_VIEW = base.Locator(By.CSS_SELECTOR, _lhn_menu.REC_VIEW)
#     PROGRAMS_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR,  _lhn_menu.PROGRAMS_CREATE_NEW)
#     # PROGRAMS_COUNT = base.Locator(By.CSS_SELECTOR, _lhn_menu.PROGRAMS_COUNT)
#
#     _create_program = selector.PageHeader.LhnMenu.CreateNewProgram
#     TITLE = base.Locator(By.CSS_SELECTOR, _create_program.TITLE)
#     LHS_ITEM_NEW = base.Locator(By.CSS_SELECTOR, _create_program.LHS_ITEM_NEW)
#     GEAR_ICON = base.Locator(By.CSS_SELECTOR, _create_program.GEAR_ICON)
#     DELETE_IN_GEAR = base.Locator(
#         By.CSS_SELECTOR, _create_program.DELETE_IN_GEAR)
#     DELETE = base.Locator(By.CSS_SELECTOR, _create_program.DELETE)
#     BUTTON_SAVE_AND_ADD = base.Locator(
#         By.CSS_SELECTOR, _create_program.BUTTON_SAVE_AND_ADD)
#
#     _create_workflow = selector.PageHeader.LhnMenu.CreateNewWorkflow
#     WF_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_workflow.WF_CREATE_NEW)
#     WF_TITLE = base.Locator(By.CSS_SELECTOR, _create_workflow.WF_TITLE)
#     WF_ACTIVE = base.Locator(By.CSS_SELECTOR, _create_workflow.WF_ACTIVE)
#     WF_DRAFT = base.Locator(By.CSS_SELECTOR, _create_workflow.WF_DRAFT)
#     WF_INACTIVE = base.Locator(By.CSS_SELECTOR, _create_workflow.WF_INACTIVE)
#
#     _create_audit = selector.PageHeader.LhnMenu.CreateNewAudit
#     AUDIT_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_audit.AUDIT_CREATE_NEW)
#     CLICK_PROGRAM_CHECKBOX = base.Locator(
#         By.CSS_SELECTOR, _create_audit.CLICK_PROGRAM_CHECKBOX)
#     # AUDIT_PROGRAMS_CREATE_NEW = base.Locator(
#     #     By.CSS_SELECTOR, _create_audit.AUDIT_PROGRAMS_CREATE_NEW)
#     SELECT_PROGRAM = base.Locator(
#         By.CSS_SELECTOR, _create_audit.SELECT_PROGRAM)
#
#     _create_ctrl_asses = selector.PageHeader.LhnMenu.CreateNewControlAsses
#     CONTROL_ASSES_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_ctrl_asses.CONTROL_ASSES_CREATE_NEW)
#     CLICK_CONTROL_CHECKBOX = base.Locator(
#         By.CSS_SELECTOR, _create_ctrl_asses.CLICK_CONTROL_CHECKBOX)
#     CLICK_AUDIT_CHECKBOX = base.Locator(
#         By.CSS_SELECTOR, _create_ctrl_asses.CLICK_AUDIT_CHECKBOX)
#
#     _create_issue = selector.PageHeader.LhnMenu.CreateNewIssue
#     ISSUE_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_issue.ISSUE_CREATE_NEW)
#
#     _directives = selector.PageHeader.LhnMenu.Directives
#     REGULATIONS = base.Locator(By.CSS_SELECTOR, _directives.REGULATIONS)
#     POLICIES = base.Locator(By.CSS_SELECTOR, _directives.POLICIES)
#     STANDARDS = base.Locator(By.CSS_SELECTOR, _directives.STANDARDS)
#     CONTRACTS = base.Locator(By.CSS_SELECTOR, _directives.CONTRACTS)
#     CLAUSES = base.Locator(By.CSS_SELECTOR, _directives.CLAUSES)
#     SECTIONS = base.Locator(By.CSS_SELECTOR, _directives.SECTIONS)
#
#     _create_regulation = selector.PageHeader.LhnMenu.Directives\
#         .CreateNewRegulation
#     REGULATION_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_regulation.REGULATION_CREATE_NEW)
#
#     _create_policy = selector.PageHeader.LhnMenu.Directives.CreateNewPolicy
#     POLICY_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_policy.POLICY_CREATE_NEW)
#
#     _create_standard = selector.PageHeader.LhnMenu.Directives.CreateNewStandard
#     STANDARD_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_standard.STANDARD_CREATE_NEW)
#
#     _create_contract = selector.PageHeader.LhnMenu.Directives.CreateNewContract
#     CONTRACT_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_contract.CONTRACT_CREATE_NEW)
#
#     _create_clause = selector.PageHeader.LhnMenu.Directives.CreateNewClause
#     CLAUSE_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_clause.CLAUSE_CREATE_NEW)
#
#     _create_section = selector.PageHeader.LhnMenu.Directives.CreateNewSection
#     SECTION_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_section.SECTION_CREATE_NEW)
#     CLICK_POLICY_CHECKBOX = base.Locator(
#         By.CSS_SELECTOR, _create_section.CLICK_POLICY_CHECKBOX)
#
#     _ctrl_obj = selector.PageHeader.LhnMenu.ControlObjectives
#     CONTROLS = base.Locator(By.CSS_SELECTOR, _ctrl_obj.CONTROLS)
#     OBJECTIVES = base.Locator(By.CSS_SELECTOR, _ctrl_obj.OBJECTIVES)
#
#     _create_control = selector.PageHeader.LhnMenu.ControlObjectives\
#         .CreateNewControl
#     CONTROL_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_control.CONTROL_CREATE_NEW)
#
#     _create_objective = selector.PageHeader.LhnMenu.ControlObjectives\
#         .CreateNewObjective
#     OBJECTIVE_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_objective.OBJECTIVE_CREATE_NEW)
#
#     _ppl_groups = selector.PageHeader.LhnMenu.PeopleGroups
#     PEOPLE = base.Locator(By.CSS_SELECTOR, _ppl_groups.PEOPLE)
#     ORG_GROUPS = base.Locator(By.CSS_SELECTOR, _ppl_groups.ORG_GROUPS)
#     VENDORS = base.Locator(By.CSS_SELECTOR, _ppl_groups.VENDORS)
#
#     _create_person = selector.PageHeader.LhnMenu.PeopleGroups.CreateNewPerson
#     PERSON_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_person.PERSON_CREATE_NEW)
#     PERSON_EMAIL = base.Locator(By.CSS_SELECTOR, _create_person.PERSON_EMAIL)
#
#     _create_org_grp = selector.PageHeader.LhnMenu.PeopleGroups\
#         .CreateNewOrgGroup
#     ORG_GROUP_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_org_grp.ORG_GROUP_CREATE_NEW)
#
#     _create_vendor = selector.PageHeader.LhnMenu.PeopleGroups.CreateNewVendor
#     VENDOR_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_vendor.VENDOR_CREATE_NEW)
#
#     _assets_business = selector.PageHeader.LhnMenu.AssetsBusiness
#     SYSTEMS = base.Locator(By.CSS_SELECTOR, _assets_business.SYSTEMS)
#     PROCESSES = base.Locator(By.CSS_SELECTOR, _assets_business.PROCESSES)
#     DATA_ASSETS = base.Locator(By.CSS_SELECTOR, _assets_business.DATA_ASSETS)
#     PRODUCTS = base.Locator(By.CSS_SELECTOR, _assets_business.PRODUCTS)
#     PROJECTS = base.Locator(By.CSS_SELECTOR, _assets_business.PROJECTS)
#     FACILITIES = base.Locator(By.CSS_SELECTOR, _assets_business.FACILITIES)
#     MARKETS = base.Locator(By.CSS_SELECTOR, _assets_business.MARKETS)
#
#     _create_system = selector.PageHeader.LhnMenu.AssetsBusiness.CreateNewSystem
#     SYSTEM_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_system.SYSTEM_CREATE_NEW)
#
#     _create_process = selector.PageHeader.LhnMenu.AssetsBusiness\
#         .CreateNewProcess
#     PROCESS_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_process.PROCESS_CREATE_NEW)
#
#     _create_data_asset = selector.PageHeader.LhnMenu.AssetsBusiness\
#         .CreateNewDataAsset
#     DATA_ASSET_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_data_asset.DATA_ASSET_CREATE_NEW)
#
#     _create_product = selector.PageHeader.LhnMenu.AssetsBusiness\
#         .CreateNewProduct
#     PRODUCT_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_product.PRODUCT_CREATE_NEW)
#
#     _assets_business = selector.PageHeader.LhnMenu.AssetsBusiness\
#         .CreateNewProject
#     PROJECT_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _assets_business.PROJECT_CREATE_NEW)
#
#     _create_facility = selector.PageHeader.LhnMenu.AssetsBusiness\
#         .CreateNewFacility
#     FACILITY_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_facility.FACILITY_CREATE_NEW)
#
#     _create_market = selector.PageHeader.LhnMenu.AssetsBusiness.CreateNewMarket
#     MARKET_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_market.MARKET_CREATE_NEW)
#
#     _risk_threats = selector.PageHeader.LhnMenu.RiskThreats
#     RISKS_LOWER = base.Locator(By.CSS_SELECTOR, _risk_threats.RISKS)
#     THREAT_ACTORS = base.Locator(By.CSS_SELECTOR, _risk_threats.THREAT_ACTORS)
#
#     _create_risk = selector.PageHeader.LhnMenu.RiskThreats.CreateNewRisk
#     RISK_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_risk.RISK_CREATE_NEW)
#     RISK_TITLE = base.Locator(By.CSS_SELECTOR, _create_risk.RISK_TITLE)
#     RISK_DESCRIPTION = base.Locator(
#         By.CSS_SELECTOR, _create_risk.RISK_DESCRIPTION)
#     RISK_OWNER = base.Locator(By.CSS_SELECTOR, _create_risk.RISK_OWNER)
#
#     _create_threat_actor = selector.PageHeader.LhnMenu.RiskThreats\
#         .CreateNewThreatActor
#     THREAT_ACTOR_CREATE_NEW = base.Locator(
#         By.CSS_SELECTOR, _create_threat_actor.THREAT_ACTOR_CREATE_NEW)
#     THREAT_ACTOR_TITLE = base.Locator(
#         By.CSS_SELECTOR, _create_threat_actor.THREAT_ACTOR_TITLE)
#
#     obj_create = {
#         'programs': PROGRAMS_LINK,
#         'create_program': PROGRAMS_CREATE_NEW,
#         'title': TITLE,
#         'programs_count': selector.PageHeader.LhnMenu.PROGRAMS_COUNT,
#
#         'workflows': WORKFLOWS_LINK,
#         'create_workflow': WF_CREATE_NEW,
#         'wf_title': WF_TITLE,
#         'workflows_count': selector.PageHeader.LhnMenu.WORKFLOWS_COUNT,
#
#         'audits': AUDITS_LINK,
#         'create_audit': AUDIT_CREATE_NEW,
#         'program_checkbox': CLICK_PROGRAM_CHECKBOX,
#         'audit_title': WF_TITLE,
#         'audits_count': selector.PageHeader.LhnMenu.AUDITS_COUNT,
#
#         'ctrl_asses': CTRL_ASSES_LINK,
#         'create_ctrl_asses': CONTROL_ASSES_CREATE_NEW,
#         'ctrl_asses_title': WF_TITLE,
#         'control_checkbox': CLICK_CONTROL_CHECKBOX,
#         'audit_checkbox': CLICK_AUDIT_CHECKBOX,
#         'ctrl_asses_count': selector.PageHeader.LhnMenu.CTRL_ASSES_COUNT,
#
#         'issues': ISSUES_LINK,
#         'create_issue': ISSUE_CREATE_NEW,
#         'issue_title': WF_TITLE,
#         'issues_count': selector.PageHeader.LhnMenu.ISSUES_COUNT,
#
#         'directives': DIRECTIVES,
#
#         'regulations': REGULATIONS,
#         'create_regulation': REGULATION_CREATE_NEW,
#         'regulation_title': WF_TITLE,
#         'regulations_count':
#             selector.PageHeader.LhnMenu.Directives.REGULATIONS_COUNT,
#
#         'policies': POLICIES,
#         'create_policy': POLICY_CREATE_NEW,
#         'policy_title': WF_TITLE,
#         'policies_count':
#             selector.PageHeader.LhnMenu.Directives.POLICIES_COUNT,
#
#         'standards': STANDARDS,
#         'create_standard': STANDARD_CREATE_NEW,
#         'standard_title': WF_TITLE,
#         'standards_count':
#             selector.PageHeader.LhnMenu.Directives.STANDARDS_COUNT,
#
#         'contracts': CONTRACTS,
#         'create_contract': CONTRACT_CREATE_NEW,
#         'contract_title': WF_TITLE,
#         'contracts_count':
#             selector.PageHeader.LhnMenu.Directives.CONTRACTS_COUNT,
#
#         'clauses': CLAUSES,
#         'create_clause': CLAUSE_CREATE_NEW,
#         'clause_title': WF_TITLE,
#         'clauses_count': selector.PageHeader.LhnMenu.Directives.CLAUSES_COUNT,
#
#         'sections': SECTIONS,
#         'create_section': SECTION_CREATE_NEW,
#         'section_title': WF_TITLE,
#         'policy_checkbox': CLICK_POLICY_CHECKBOX,
#         'sections_count':
#             selector.PageHeader.LhnMenu.Directives.SECTIONS_COUNT,
#
#         'ctrl_obj': CONT_OBJ,
#
#         'controls': CONTROLS,
#         'create_control': CONTROL_CREATE_NEW,
#         'control_title': WF_TITLE,
#         'controls_count':
#             selector.PageHeader.LhnMenu.ControlObjectives.CONTROLS_COUNT,
#
#         'objectives': OBJECTIVES,
#         'create_objective': OBJECTIVE_CREATE_NEW,
#         'objective_title': WF_TITLE,
#         'objectives_count':
#             selector.PageHeader.LhnMenu.ControlObjectives.OBJECTIVES_COUNT,
#
#         'ppl_grp': PPL_GRP,
#
#         'people': PEOPLE,
#         'create_person': PERSON_CREATE_NEW,
#         'person_email': PERSON_EMAIL,
#         # 'person_title': WF_TITLE,
#         'people_count': selector.PageHeader.LhnMenu.PeopleGroups.PEOPLE_COUNT,
#
#         'org_gropus': ORG_GROUPS,
#         'create_org_gropu': ORG_GROUP_CREATE_NEW,
#         'org_gropu_title': WF_TITLE,
#         'org_groups_count':
#             selector.PageHeader.LhnMenu.PeopleGroups.ORG_GROUPS_COUNT,
#
#         'vendors': VENDORS,
#         'create_vendor': VENDOR_CREATE_NEW,
#         'vendor_title': WF_TITLE,
#         'vendors_count':
#             selector.PageHeader.LhnMenu.PeopleGroups.VENDORS_COUNT,
#
#         'assets': ASSETS,
#
#         'systems': SYSTEMS,
#         'create_system': SYSTEM_CREATE_NEW,
#         'system_title': WF_TITLE,
#         'systems_count':
#             selector.PageHeader.LhnMenu.AssetsBusiness.SYSTEMS_COUNT,
#
#         'processes': PROCESSES,
#         'create_process': PROCESS_CREATE_NEW,
#         'process_title': WF_TITLE,
#         'processes_count':
#             selector.PageHeader.LhnMenu.AssetsBusiness.PROCESSES_COUNT,
#
#         'data_assets': DATA_ASSETS,
#         'create_data_asset': DATA_ASSET_CREATE_NEW,
#         'data_asset_title': WF_TITLE,
#         'data_assets_count':
#             selector.PageHeader.LhnMenu.AssetsBusiness.DATA_ASSETS_COUNT,
#
#         'products': PRODUCTS,
#         'create_product': PRODUCT_CREATE_NEW,
#         'product_title': WF_TITLE,
#         'products_count':
#             selector.PageHeader.LhnMenu.AssetsBusiness.PRODUCTS_COUNT,
#
#         'projects': PROJECTS,
#         'create_project': PROJECT_CREATE_NEW,
#         'project_title': WF_TITLE,
#         'projects_count':
#             selector.PageHeader.LhnMenu.AssetsBusiness.PROJECTS_COUNT,
#
#         'facilities': FACILITIES,
#         'create_facility': FACILITY_CREATE_NEW,
#         'facility_title': WF_TITLE,
#         'facilities_count':
#             selector.PageHeader.LhnMenu.AssetsBusiness.FACILITIES_COUNT,
#
#         'markets': MARKETS,
#         'create_market': MARKET_CREATE_NEW,
#         'market_title': WF_TITLE,
#         'markets_count':
#             selector.PageHeader.LhnMenu.AssetsBusiness.MARKETS_COUNT,
#
#         'risks_threats': RISKS,
#
#         'risks': RISKS_LOWER,
#         'create_risk': RISK_CREATE_NEW,
#         'risk_title': RISK_TITLE,
#         'risk_owner': RISK_OWNER,
#         # 'risk_description': RISK_DESCRIPTION,
#         'risks_count': selector.PageHeader.LhnMenu.RiskThreats.RISKS_COUNT,
#
#         'threat_actors': THREAT_ACTORS,
#         'create_threat_actor': THREAT_ACTOR_CREATE_NEW,
#         'threat_actor_title': THREAT_ACTOR_TITLE,
#         'threat_actors_count':
#             selector.PageHeader.LhnMenu.RiskThreats.THREAT_ACTORS_COUNT
#     }
#
#     def open_lhn_menu(self):
#         self._click_when_visible(self.LHN_MENU)
#
#     def click_object(self, obj):
#         self._click_when_visible(self.obj_create[obj])
#
#     def click_create_new_object(self, obj):
#         self._click_when_visible(self.obj_create[obj])
#
#     def enter_title(self, obj, title):
#         self._find_field_and_enter_data(self.obj_create[obj], title)
#
#     def save_and_add_other(self):
#         self._click_when_visible(self.BUTTON_SAVE_AND_ADD)
#
#     def click_gear_icon(self):
#         self._click_when_visible(self.GEAR_ICON)
#
#     def click_delete_gear_icon(self):
#         self._click_when_visible(self.DELETE_IN_GEAR)
#
#     def click_delete(self):
#         self._click_when_visible(self.DELETE)
#
#     def click_workflows_draft(self):
#         self._click_when_visible(self.WF_DRAFT)
#
#     def element_in_bracket(self, obj):
#         return self._driver.find_elements_by_css_selector(self.obj_create[obj])
#
#     def enter_data(self, data):
#         self._find_iframe_and_enter_data(self.RISK_DESCRIPTION, data)
#
#     def wait_while_lhn_moving(self, obj):
#         # return self._get_element_when_visible(self.obj_create[obj])
#         return self._driver.find_elements_by_css_selector(self.obj_create[obj])
#
#     def lhn_click_and_wait(self, obj):
#         """
#         This is a helper method for object creation in LHN menu.
#
#         Method waits for the LHN menu to complete an action.
#         Example: opens the LHN menu, opens a dropdown menu (+ create new).
#
#         Note: Method should NOT use time.sleep.
#
#         Args:
#             obj (locator): src.lib.page.lhn_menu
#         """
#         time.sleep(3)
#         self.click_object(obj)
#
#         # ALTERNATIVE:
#         # Web driver exception: element not clicable at point (chrome driver).
#         # Errors: Constantly clicks on random elements.
#         #
#         # while True:
#         #     try:
#         #         self.click_create_new_object(obj)
#         #         break
#         #     except:
#         #         pass # or time.sleep(0.1)
#
#         # ALTERNATIVE #2:
#         # The code below waits for the element (in LHN menu) to stop moving.
#         # (Possible) Errors: Clicks on random objects are possible while the
#         # LHN waits for objects to fully load before clicking on +Create New.
#         #
#         # old_location = {}
#         # new_location = self.wait_while_lhn_moving(obj)[0].location
#         # # new_location = self.driver.find_elements_by_css_selector ...
#         #
#         # while old_location != new_location:
#         #     temp_location = new_location
#         #     time.sleep(0.1) # Pass time between old and new location
#         #     new_location = self.wait_while_lhn_moving(
#         #         obj)[0].location
#         #     old_location = temp_location
#         # self.click_object(obj)
#
#     def lhn_create_objects_setup(self, *args):
#         """
#         Opens LHN menu and clicks on an object to create a new one.
#
#         Navigates to the correct +Create New element. If the object is in the
#         OBJECTS submenu (DIRECTIVES, CONTROLS/OBJECTIVES ...), two clicks are
#         needed for navigation (two arguments).
#
#         Args:
#             *args (locators): src.lib.page.lhn_menu
#         """
#         lhn = self._driver.find_elements_by_css_selector(
#             selector.PageHeader.TRIGGER
#             )[0].get_attribute("outerHTML").split('>')[0]
#         if 'active' not in lhn:
#             self.open_lhn_menu()
#
#         # Click on the arrow of an object (ex: PROGRAMS (NUM))
#         for obj_link in args:
#             self.lhn_click_and_wait(obj_link)
#
#     def lhn_create_objects(self, create_obj, enter_title, obj_num):
#         """
#         Creates an object in LHN menu.
#
#         Note: Locators in src.lib.page.lhn_menu
#
#         Args:
#             create_obj (locator): Click +Create New
#             enter_title (locator): Enter object title (email for people test)
#             obj_num (int): the number of objects to create
#         """
#         select_obj = {
#             'create_audit': 'program_checkbox',
#             'create_section': 'policy_checkbox',
#         }
#
#         self.lhn_click_and_wait(create_obj)
#
#         # Programs or policies object have already create an self.identirier
#         if create_obj in select_obj.keys():
#             self.id_obj = self.identifier
#
#         # Also used for Control Assessments
# #         if create_obj == 'create_control':
# #             try:
# #                 self.id_control = self.identifier[:]
# #             except AttributeError:
# #                 pass
#
#         # The identifier stores UUIDs for lhn_delete_objects method
#         self.identifier = []
#
# #         if create_obj in select_obj.keys()[0]:
# #             self.id_audit = self.identifier
#
#         # For loop creates the number of objects specified by obj_num
#         for i in xrange(obj_num):
#             _identifier = str(uuid.uuid4())
#
#             # If audits
#             if create_obj in select_obj.keys():
#                 j = 0
#                 while True:
#                     self.click_object(select_obj[create_obj])
#                     self._get_element_when_visible(self.SELECT_PROGRAM)
#
#                     elements = self._driver.find_elements_by_css_selector(
#                         selector.PageHeader.LhnMenu.CreateNewAudit
#                         .SELECT_PROGRAM)
#                     element = elements[j]
#                     e = element.text
#                     if e in self.id_obj:
#                         element.click()
#                         break
#                     j += 1
#
#             # _identifier for title creation
#             if enter_title != 'person_email':
#                 self.enter_title(enter_title, _identifier)
#             else:
#                 self.enter_title(
#                     enter_title, _identifier + '@example.com')
#
#             if create_obj == 'create_risk':
#                 self.enter_data(_identifier)
#                 k = 0
#                 while True:
#                     self.click_object('risk_owner')
#                     self._get_element_when_visible(self.SELECT_PROGRAM)
#                     elements = self._driver.find_elements_by_css_selector(
#                         selector.PageHeader.LhnMenu.CreateNewAudit
#                         .SELECT_PROGRAM)
#                     element = elements[k]
#                     e = element.text
#                     # if e in self.id_obj:
#                     element.click()
#                     break
#                     # k += 1
#
#             if create_obj == 'create_ctrl_asses':
#                 ctrl_asses_key = ('audit_checkbox', 'control_checkbox')
#
#                 for j in xrange(2):
#                     k = 0
#                     while True:
#                         self.click_object(ctrl_asses_key[j])
#                         self._get_element_when_visible(self.SELECT_PROGRAM)
#                         # time.sleep(2)
#                         elements = self._driver.find_elements_by_css_selector(
#                             selector.PageHeader.LhnMenu.CreateNewAudit
#                             .SELECT_PROGRAM)
#                         element = elements[k]
#                         e = element.text
#                         if ctrl_asses_key[j] == 'audit_checkbox':
#                             element.click()
#                             break
#                         if e in self.id_control:
#                             element.click()
#                             break
#                         k += 1
#
#             # Save & Add Another - as long as range isn't on the last index
#             if i != xrange(obj_num)[-1]:
#                 self.save_and_add_other()
#                 save_and_add = self._driver.find_elements_by_css_selector(
#                     selector.PageHeader.LhnMenu.CreateNewProgram
#                     .BUTTON_SAVE_AND_ADD)[0].get_attribute("outerHTML")
#
#                 # While Save & Add Another not clickable again
#                 while 'pending-ajax' in save_and_add:
#                     time.sleep(0.1)
#                     save_and_add = self._driver.find_elements_by_css_selector(
#                         selector.PageHeader.LhnMenu.CreateNewProgram
#                         .BUTTON_SAVE_AND_ADD)[0].get_attribute("outerHTML")
#
#             # Save & Close
#             else:
#                 self.save_and_close()
#                 # self.wait_for_redirect()
#
#             # The identifier stores UUIDs for lhn_delete_objects method
#             self.identifier.append(_identifier)
#
#         time.sleep(1)
#         lhn = self._driver.find_elements_by_css_selector(
#             selector.PageHeader.TRIGGER
#             )[0].get_attribute("outerHTML").split('>')[0]
#         if 'active' not in lhn:
#             self.open_lhn_menu()
#
#         # Return currently broken (returns None)
#         return self.identifier
#
#     def lhn_count_objects(self, obj):
#         if obj == 'workflows_count':
#             self.click_workflows_draft()
#
#         time.sleep(2)
#         self._get_element_when_visible(self.LHS_ITEM_NEW)
#
#         elements_count = self._driver.find_elements_by_css_selector(
#             selector.PageHeader.LhnMenu.CreateNewProgram.LHS_ITEM_NEW)
#
#         element = self.element_in_bracket(obj)[0].text
#
#         assert len(elements_count) <= int(element), \
#             'Elements in brackets must be higer or equal to the counted ' \
#             'elements'
#
#     def lhn_delete_objects(self, ident, obj=None):
#         lhn = self._driver.find_elements_by_css_selector(
#             selector.PageHeader.TRIGGER
#             )[0].get_attribute("outerHTML").split('>')[0]
#         if 'active' not in lhn:
#             self.open_lhn_menu()
#
#         obj_link = ('programs', 'policies')
#         if obj in obj_link:
#             self.click_object(obj)
#
#         time.sleep(1)
#         self._get_element_when_visible(self.LHS_ITEM_NEW)
#         elements_count = self._driver.find_elements_by_css_selector(
#             selector.PageHeader.LhnMenu.CreateNewProgram.LHS_ITEM_NEW)
#
#         i = 0
#         while len(ident) > 0:
#             element = elements_count[i]
#
#             if element.text in ident:
#                 ident.remove(element.text)
#                 while True:
#                     try:
#                         element.click()
#                         break
#                     except:
#                         pass
#                 self.click_gear_icon()
#                 self.click_delete_gear_icon()
#                 self.click_delete()
#                 self.wait_for_redirect()
#
#                 if len(ident) != 0:
#                     time.sleep(1)
#                     lhn = self._driver.find_elements_by_css_selector(
#                         selector.PageHeader.TRIGGER
#                         )[0].get_attribute("outerHTML").split('>')[0]
#                     if 'active' not in lhn:
#                         self.open_lhn_menu()
#
#                     self._get_element_when_visible(self.LHS_ITEM_NEW)
#                     elements_count = self._driver \
#                         .find_elements_by_css_selector(
#                             selector.PageHeader.LhnMenu.CreateNewProgram
#                             .LHS_ITEM_NEW)
#                 i = -1
#             i += 1
#
#     def lhn_delete_object(self, obj_link=['directives', 'policies']):
#         """
#         Metod used for object deletion.
#
#         Note: Not a test method.
#         """
#         self.lhn_menu = self.my_work_page.open_lhn_menu_new()
#         for link in obj_link:
#             self.lhn_menu.click_object(link)
#         if obj_link == 'workflows':
#             self.lhn_menu.click_workflows_draft()
#         self.lhn_menu._get_element_when_visible(lhn_menu.LhnMenu.LHS_ITEM_NEW)
#         elements_count = self.driver.find_elements_by_css_selector(
#                 selector.PageHeader.LhnMenu.CreateNewProgram.LHS_ITEM_NEW)
#         i = 0
#         element = elements_count[i]
#         while len(elements_count) > 0:
#             while True:
#                 try:
#                     element.click()
#                     break
#                 except:
#                     pass
#             self.lhn_menu.click_gear_icon()
#             self.lhn_menu.click_delete_gear_icon()
#             self.lhn_menu.click_delete()
#             self.wait_for_redirect()
#             self.my_work_page.open_lhn_menu_new()
#             self.lhn_menu._get_element_when_visible(
#                 lhn_menu.LhnMenu.LHS_ITEM_NEW)
#             elements_count = self.driver.find_elements_by_css_selector(
#                 selector.PageHeader.LhnMenu.CreateNewProgram.LHS_ITEM_NEW)
#             element = elements_count[i]
