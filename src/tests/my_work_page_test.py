import sys
import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__)) + "/../"
print "conftest: PROJECT_ROOT_PATH = " + PROJECT_ROOT_PATH
sys.path.append(PROJECT_ROOT_PATH)
PROJECT_SRC_PATH = PROJECT_ROOT_PATH + "src/"
sys.path.append(PROJECT_SRC_PATH)
print "conftest: PROJECT_SRC_PATH = " + PROJECT_SRC_PATH

from lib.page import dashboard
from lib.constants import locator
from lib.page import user_email_menu
from lib.page import hor_nav_bar
from lib.page.modal import create_object
from lib import base
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException


# class MyWorkPage(base.Test):
#     def setup(self):
#         """
#         Creates a new program page and saves it.
#         """
#         self.init_resources()
#         self.dashboard_page = dashboard.DashboardPage(self.driver)
#         # self.dashboard_page.navigate_to()
#
#     def teardown(self):
#         self.close_resources()


class TestLhnMenu(base.Test):
    def test_lhn_stays_expanded(self, lhn_menu_setup):
        """
        Checkes if the lhn menu expadns and stays that way.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu._click_when_visible(locator.PageHeader.TRIGGER)
        time.sleep(1)
        element = lhn_menu._get_element_when_visible(
            locator.LhnMenu.LHN_PIN).is_displayed()
        assert element

    def test_lhn_contains(self, lhn_menu_setup):
        """
        Opens LHN menu and tests all objects in the menu, that are avaliabe.
        Also tests if the PIN icon is displayed and if "OFF" state and if
        All objects alement is active by default.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu._click_when_visible(locator.PageHeader.TRIGGER)

        obj_list = {
            locator.LhnMenu.MY_OBJECTS: 'My objects',
            locator.LhnMenu.ALL_OBJECTS: 'All objects',
            locator.LhnMenu.PROGRAMS_LINK: 'Programs',
            locator.LhnMenu.WORKFLOWS_LINK: 'Workflows',
            locator.LhnMenu.AUDITS_LINK: 'Audits',
            locator.LhnMenu.CTRL_ASSES_LINK: 'Control Assessments',
            locator.LhnMenu.ISSUES_LINK: 'Issues',
            locator.LhnMenu.DIRECTIVES: 'Directives',
            locator.LhnMenu.CONT_OBJ: 'Controls/Objectives',
            locator.LhnMenu.PPL_GRP: 'People/Groups',
            locator.LhnMenu.ASSETS: 'Assets/Business',
            locator.LhnMenu.RISKS: 'Risks/Threats',
            locator.LhnMenu.REC_VIEW: 'Recently Viewed'
        }

        lhn_menu._get_element_when_clickable(locator.LhnMenu.LHN_PIN)
        # time.sleep(5)

        for key, value in obj_list.items():
            element = lhn_menu._get_element_when_visible(key).text
            assert value.lower() in element.lower()

        element = lhn_menu._get_element_when_visible(
            locator.LhnMenu.LHN_PIN_NOT_ACTIVE).is_displayed()
        assert element

        element = lhn_menu._find_element_by_css(
            locator.LhnMenu.ALL_OBJECTS)[0].get_attribute('class')
        assert 'active' in element, 'All objects element wasn\'t active'

    def test_lhn_programs_count(self, lhn_menu_setup, programs_num=2):
        """
        Creates a few programs, counts the programs in the LHN dropdown
        menu and compares that number to the number right of programs.
        Deletes the created programs.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('programs')
        identifier = lhn_menu.lhn_create_objects(
            'create_program', programs_num)
        lhn_menu.lhn_count_objects('programs_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_workflows_count(self, lhn_menu_setup, workflows_num=1):
        """
        Creates a few workflows, counts the workflows in the LHN dropdown
        menu and compares that number to the number right of workflows.
        Deletes the created workflows.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('workflows')
        identifier = lhn_menu.lhn_create_objects(
            'create_workflow', workflows_num)
        lhn_menu.lhn_count_objects('workflows_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_audits_count(self, lhn_menu_setup, audits_num=1):
        """
        Creates a few audits, counts the audits in the LHN dropdown
        menu and compares that number to the number right of audits.

        Note: To create an audit, you have to create a program first.
        By deleting the program, the audits asigned to that program will
        also be deleted.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('programs')
        id_program = lhn_menu.lhn_create_objects(
            'create_program', 1)
        lhn_menu.lhn_create_objects_setup('audits')
        lhn_menu.lhn_create_objects(
            'create_audit', audits_num, id_program)
        lhn_menu.lhn_count_objects('audits_count')
        lhn_menu.lhn_delete_objects(id_program, 'programs')

    def test_lhn_control_assessments_count(
            self, lhn_menu_setup, ctrl_asses_num=1):
        """
        Creates a few control assessments, counts the control assessments in
        the LHN dropdown menu and compares that number to the number right of
        control assessments.

        Note: To create an control assessment, you have to create a program,
        an audit and a control first.
        By deleting the program, the audit asigned to that program will
        also be deleted. By deleting the control, the control assessments
        asigned to that control will also be deleted.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('programs')
        id_program = lhn_menu.lhn_create_objects('create_program', 1)
        lhn_menu.lhn_create_objects_setup('audits')
        id_audit = lhn_menu.lhn_create_objects(
            'create_audit', 1, id_program[0])
        lhn_menu.lhn_create_objects_setup('ctrl_obj', 'controls')
        id_ctrl = lhn_menu.lhn_create_objects('create_control', 1)

        lhn_menu.lhn_create_objects_setup('ctrl_asses')
        id_ctrl_asses = lhn_menu.lhn_create_objects(
            'create_ctrl_asses', ctrl_asses_num, id_ctrl[0], id_audit[0])

        lhn_menu.lhn_count_objects('ctrl_asses_count')

        lhn_menu.lhn_delete_objects(id_program, 'programs')
        lhn_menu.lhn_delete_objects(id_ctrl_asses, 'ctrl_asses')
        lhn_menu.lhn_delete_objects(id_ctrl, 'ctrl_obj', 'controls')

    def test_lhn_issues_count(self, lhn_menu_setup, issue_num=1):
        """
        Creates a few issues, counts the issues in the LHN dropdown
        menu and compares that number to the number right of issues.
        Deletes the created workflows.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('issues')
        identifier = lhn_menu.lhn_create_objects('create_issue', issue_num)
        lhn_menu.lhn_count_objects('issues_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_regulations_count(self, lhn_menu_setup, regulation_num=1):
        """
        Creates a few regulations, counts the regulations in the LHN dropdown
        menu and compares that number to the number right of regulations.
        Deletes the created regulations.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('directives', 'regulations')
        identifier = lhn_menu.lhn_create_objects(
            'create_regulation', regulation_num)
        lhn_menu.lhn_count_objects('regulations_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_policies_count(self, lhn_menu_setup, policy_num=1):
        """
        Creates a few policies, counts the policies in the LHN dropdown
        menu and compares that number to the number right of policies.
        Deletes the created policies.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('directives', 'policies')
        identifier = lhn_menu.lhn_create_objects('create_policy', policy_num)
        lhn_menu.lhn_count_objects('policies_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_standards_count(self, lhn_menu_setup, standard_num=1):
        """
        Creates a few standards, counts the standards in the LHN dropdown
        menu and compares that number to the number right of standards.
        Deletes the created standards.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('directives', 'standards')
        identifier = lhn_menu.lhn_create_objects(
            'create_standard', standard_num)
        lhn_menu.lhn_count_objects('standards_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_contracts_count(self, lhn_menu_setup, contract_num=1):
        """
        Creates a few contracts, counts the contracts in the LHN dropdown
        menu and compares that number to the number right of contracts.
        Deletes the created contracts.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('directives', 'contracts')
        identifier = lhn_menu.lhn_create_objects(
            'create_contract', contract_num)
        lhn_menu.lhn_count_objects('contracts_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_clauses_count(self, lhn_menu_setup, clause_num=1):
        """
        Creates a few clauses, counts the clauses in the LHN dropdown
        menu and compares that number to the number right of clauses.
        Deletes the created clauses.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('directives', 'clauses')
        identifier = lhn_menu.lhn_create_objects('create_clause', clause_num)
        lhn_menu.lhn_count_objects('clauses_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_sections_count(self, lhn_menu_setup, section_num=1):
        """
        Creates a few sections, counts the sections in the LHN dropdown
        menu and compares that number to the number right of sections.

        Note: To create a section, you have to create a policie first.
        By deleting the policie, the sections asigned to that policie will
        also be deleted.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('directives', 'policies')
        id_policy = lhn_menu.lhn_create_objects('create_policy', 1)
        lhn_menu.lhn_create_objects_setup('sections')
        lhn_menu.lhn_create_objects(
            'create_section', section_num, id_policy[0])
        lhn_menu.lhn_count_objects('sections_count')
        lhn_menu.lhn_delete_objects(id_policy, 'policies')

    def test_lhn_controls_count(self, lhn_menu_setup, control_num=1):
        """
        Creates a few controls, counts the controls in the LHN dropdown
        menu and compares that number to the number right of controls.
        Deletes the created controls.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('ctrl_obj', 'controls')
        identifier = lhn_menu.lhn_create_objects('create_control', control_num)
        lhn_menu.lhn_count_objects('controls_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_objectives_count(self, lhn_menu_setup, objective_num=1):
        """
        Creates a few objectives, counts the objectives in the LHN dropdown
        menu and compares that number to the number right of objectives.
        Deletes the created objectives.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('ctrl_obj', 'objectives')
        identifier = lhn_menu.lhn_create_objects(
            'create_objective', objective_num)
        lhn_menu.lhn_count_objects('objectives_count')
        lhn_menu.lhn_delete_objects(identifier)

    def lhn_people_count(self, lhn_menu_setup, person_num=1):
        """
        Creates a few persons, counts the persons in the LHN dropdown
        menu and compares that number to the number right of people.
        Warning: Object people can NOT be deleted.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('ppl_grp', 'people')
        lhn_menu.lhn_create_objects('create_person', person_num)
        lhn_menu.lhn_count_objects('people_count')

    def test_lhn_org_groups_count(self, lhn_menu_setup, org_grp_num=1):
        """
        Creates a few org groups, counts the org groups in the LHN dropdown
        menu and compares that number to the number right of org groups.
        Deletes the created org groups.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('ppl_grp', 'org_gropus')
        identifier = lhn_menu.lhn_create_objects(
            'create_org_gropu', org_grp_num)
        lhn_menu.lhn_count_objects('org_groups_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_vendors_count(self, lhn_menu_setup, vendor_num=1):
        """
        Creates a few vendors, counts the vendors in the LHN dropdown
        menu and compares that number to the number right of vendors.
        Deletes the created vendors.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('ppl_grp', 'vendors')
        identifier = lhn_menu.lhn_create_objects('create_vendor', vendor_num)
        lhn_menu.lhn_count_objects('vendors_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_systems_count(self, lhn_menu_setup, system_num=1):
        """
        Creates a few systems, counts the systems in the LHN dropdown
        menu and compares that number to the number right of systems.
        Deletes the created systems.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('assets', 'systems')
        identifier = lhn_menu.lhn_create_objects('create_system', system_num)
        lhn_menu.lhn_count_objects('systems_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_processes_count(self, lhn_menu_setup, process_num=1):
        """
        Creates a few processes, counts the processes in the LHN dropdown
        menu and compares that number to the number right of processes.
        Deletes the created processes.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('assets', 'processes')
        identifier = lhn_menu.lhn_create_objects('create_process', process_num)
        lhn_menu.lhn_count_objects('processes_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_data_assets_count(self, lhn_menu_setup, data_asset_num=1):
        """
        Creates a few data assets, counts the data assets in the LHN dropdown
        menu and compares that number to the number right of data assets.
        Deletes the created data assets.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('assets', 'data_assets')
        identifier = lhn_menu.lhn_create_objects(
            'create_data_asset', data_asset_num)
        lhn_menu.lhn_count_objects('data_assets_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_products_count(self, lhn_menu_setup, product_num=1):
        """
        Creates a few products, counts the products in the LHN dropdown
        menu and compares that number to the number right of products.
        Deletes the created products.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('assets', 'products')
        identifier = lhn_menu.lhn_create_objects('create_product', product_num)
        lhn_menu.lhn_count_objects('products_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_projects_count(self, lhn_menu_setup, project_num=1):
        """
        Creates a few projects, counts the projects in the LHN dropdown
        menu and compares that number to the number right of projects.
        Deletes the created projects.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('assets', 'projects')
        identifier = lhn_menu.lhn_create_objects('create_project', project_num)
        lhn_menu.lhn_count_objects('projects_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_facilities_count(self, lhn_menu_setup, facility_num=1):
        """
        Creates a few facilities, counts the facilities in the LHN dropdown
        menu and compares that number to the number right of facilities.
        Deletes the created facilities.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('assets', 'facilities')
        identifier = lhn_menu.lhn_create_objects(
            'create_facility', facility_num)
        lhn_menu.lhn_count_objects('facilities_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_markets_count(self, lhn_menu_setup, market_num=1):
        """
        Creates a few markets, counts the markets in the LHN dropdown
        menu and compares that number to the number right of markets.
        Deletes the created markets.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('assets', 'markets')
        identifier = lhn_menu.lhn_create_objects('create_market', market_num)
        lhn_menu.lhn_count_objects('markets_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_risks_count(self, lhn_menu_setup, risk_num=1):
        """
        Creates a few risks, counts the risks in the LHN dropdown
        menu and compares that number to the number right of risks.
        Deletes the created risks.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup('risks_threats', 'risks')
        identifier = lhn_menu.lhn_create_objects('create_risk', risk_num)
        lhn_menu.lhn_count_objects('risks_count')
        lhn_menu.lhn_delete_objects(identifier)

    def test_lhn_threat_actors_count(self, lhn_menu_setup, threat_actor_num=1):
        """
        Creates a few threat actors, counts the threat actors in the LHN
        dropdown menu and compares that number to the number right of
        threat actors. Deletes the created threat actors.
        """
        lhn_menu = lhn_menu_setup.open_lhn_menu_new()
        lhn_menu.lhn_create_objects_setup(
            'risks_threats', 'threat_actors')
        identifier = lhn_menu.lhn_create_objects(
            'create_threat_actor', threat_actor_num)
        lhn_menu.lhn_count_objects('threat_actors_count')
        lhn_menu.lhn_delete_objects(identifier)


class TestUserEmail(base.Test):
    def user_email_role_title(self, string):
        """
        Get two strings in user@example.com, My Work and the role title
        the user is holding (if Admin == Superuser)
        """
        string = string.split()
        my_work = string[0] + ' ' + string[1]
        role_title = string[2][1:-1]
        return my_work, role_title

    def test_click_user_email(self, user_mail_menu_setup):
        """
        Clicks on user@example.com dropdown menu.
        """
        user_mail_menu_setup.open_user_dropdown_new()

    def test_user_email_menu(self, user_mail_menu_setup):
        """
        Clicks on user@example.com dropdown menu and checkes if the objects in
        obj_list are avaliabe.Checkes if My Work is avaliable and that it has
        a user in parenthesis. If that user is Admin, check if the admin
        dashboard is avaliabe.
        """
        user_email_menu = user_mail_menu_setup.open_user_dropdown_new()

        element = user_email_menu._get_element_when_visible(
            locator.DropdownToggle.MY_WORK_PAGE).text

        element = self.user_email_role_title(element)
        assert element[0].lower() == 'My Work'.lower()

        # Need all the titles to compare!
        # Some alternative: assert element[1] == 'Superuser'
        assert len(element[1]) > 0

        if element[1].lower() == 'Superuser'.lower():
            element = user_email_menu._get_element_when_visible(
                locator.DropdownToggle.ADMIN_MENU_OPTION).text
            assert element.lower() == 'Admin Dashboard'.lower()

        obj_list = {
            locator.DropdownToggle.NOTIFICATIONS: 'Notifications',
            locator.DropdownToggle.DAILY_EMAIL: 'Daily email digest',
            locator.DropdownToggle.REAL_TIME_EMAIL: 'Real-time email updates',
            locator.DropdownToggle.DATA_IMPORT: 'Data import',
            locator.DropdownToggle.DATA_EXPORT: 'Data export',
            locator.DropdownToggle.DATA_GRID: 'Data grid',
            locator.DropdownToggle.LOGOUT: 'Logout'
        }

        for key, value in obj_list.items():
            element = user_email_menu._get_element_when_visible(key).text
            assert value.lower() in element.lower()

    def user_email_checkboxes(self, user_mail_menu_setup):
        """
        Clicks on both checkboxes in user@example.com menu
        and checks if they are working correctly.
        """
        user_email_menu = user_mail_menu_setup.open_user_dropdown_new()

        label = user_email_menu._find_element_by_css(
            locator.DropdownToggle.REAL_TIME_EMAIL_LABEL
            )[0].get_attribute("outerHTML").split('>')[0]

        if 'disabled' in label:
            user_email_menu._click_when_visible(
                locator.DropdownToggle.DAILY_EMAIL_CHECKBOX)

            daily = user_email_menu._find_element_by_css(
                locator.DropdownToggle.DAILY_EMAIL_CHECKBOX
                )[0].get_attribute("outerHTML")
            real_time = user_email_menu._find_element_by_css(
                locator.DropdownToggle.REAL_TIME_EMAIL_CHECKBOX
                )[0].get_attribute("outerHTML")
            label = user_email_menu._find_element_by_css(
                locator.DropdownToggle.REAL_TIME_EMAIL_LABEL
                )[0].get_attribute("outerHTML").split('>')[0]
            assert 'disabled' in daily, daily
            assert 'disabled' in real_time, real_time
            assert 'disabled' not in label, label

            user_email_menu._click_when_visible(
                locator.DropdownToggle.REAL_TIME_EMAIL_CHECKBOX)

            daily = user_email_menu._find_element_by_css(
                locator.DropdownToggle.DAILY_EMAIL_CHECKBOX
                )[0].get_attribute("outerHTML")
            real_time = user_email_menu._find_element_by_css(
                locator.DropdownToggle.REAL_TIME_EMAIL_CHECKBOX
                )[0].get_attribute("outerHTML")
            assert 'disabled' in daily, daily
            assert 'disabled' in real_time, real_time
        else:
            user_email_menu._get_element_when_clickable(
                locator.DropdownToggle.DAILY_EMAIL_CHECKBOX).click()

            daily = user_email_menu._find_element_by_css(
                locator.DropdownToggle.DAILY_EMAIL_CHECKBOX
                )[0].get_attribute("outerHTML")
            real_time = user_email_menu._find_element_by_css(
                locator.DropdownToggle.REAL_TIME_EMAIL_CHECKBOX
                )[0].get_attribute("outerHTML")
            label = user_email_menu._find_element_by_css(
                locator.DropdownToggle.REAL_TIME_EMAIL_LABEL
                )[0].get_attribute("outerHTML").split('>')[0]
            assert 'disabled' in daily, daily
            assert 'disabled' in real_time, real_time
            assert 'disabled' in label, label

            user_email_menu._click_when_visible(
                locator.DropdownToggle.DAILY_EMAIL_CHECKBOX)

            daily = user_email_menu._find_element_by_css(
                locator.DropdownToggle.DAILY_EMAIL_CHECKBOX
                )[0].get_attribute("outerHTML")
            real_time = user_email_menu._find_element_by_css(
                locator.DropdownToggle.REAL_TIME_EMAIL_CHECKBOX
                )[0].get_attribute("outerHTML")
            label = user_email_menu._find_element_by_css(
                locator.DropdownToggle.REAL_TIME_EMAIL_LABEL
                )[0].get_attribute("outerHTML").split('>')[0]
            assert 'disabled' in daily, daily
            assert 'disabled' in real_time, real_time
            assert 'disabled' not in label, label

            user_email_menu._click_when_visible(
                locator.DropdownToggle.REAL_TIME_EMAIL_CHECKBOX)

            daily = user_email_menu._find_element_by_css(
                locator.DropdownToggle.DAILY_EMAIL_CHECKBOX
                )[0].get_attribute("outerHTML")
            real_time = user_email_menu._find_element_by_css(
                locator.DropdownToggle.REAL_TIME_EMAIL_CHECKBOX
                )[0].get_attribute("outerHTML")
            assert 'disabled' in daily, daily
            assert 'disabled' in real_time, real_time

            user_email_menu._click_when_visible(
                locator.DropdownToggle.DAILY_EMAIL_CHECKBOX)
            user_email_menu._get_element_when_visible(
                locator.DropdownToggle.DAILY_EMAIL_CHECKBOX)


class TestHorNavBar(base.Test):
    def test_hor_nav_bar_dropdown(self, hor_nav_bar_setup):
        """
        Checks if the dropdown list appears.

        In horizontal navigation bar, click on one tab, then click on an
        object. Click on the gear icon and ckeck if the dropdown list appears.

        Also creates and deletes a program.
        """
        objs = ('Edit Program', 'Get permalink', 'View Program', 'Delete')

        hor_nav_bar_tabs = hor_nav_bar_setup.open_dashboard()

        identifier = hor_nav_bar_tabs.start_new_program(1)
        hor_nav_bar_tabs._click_when_visible(locator.HorNavBar.GGRC_ICON)

        hor_nav_bar_tabs._click_when_visible(locator.HorNavBar.PROGRAMS)
        hor_nav_bar_tabs._click_when_visible(locator.HorNavBar.OBJECT_TITLE)
        hor_nav_bar_tabs._click_when_visible(
            locator.ModalCreateNewObject.GEAR_ICON)

        elements = hor_nav_bar_tabs._get_element_when_visible(
            locator.HorNavBar.GEAR_ICON_CONTENT).text.splitlines()

        for obj in objs:
            assert obj in elements

        hor_nav_bar_tabs.hor_nav_bar_delete(identifier)

    def test_hor_nav_bar_confirm_edit(self, hor_nav_bar_setup):
        """
        Checks if the Edit modal in gear icon can be opend.

        Also creates and deletes a program.
        """
        hor_nav_bar_tabs = hor_nav_bar_setup.open_dashboard()

        identifier = hor_nav_bar_tabs.start_new_program(1)
        hor_nav_bar_tabs._click_when_visible(locator.HorNavBar.GGRC_ICON)

        hor_nav_bar_tabs._click_when_visible(locator.HorNavBar.PROGRAMS)
        hor_nav_bar_tabs._click_when_visible(locator.HorNavBar.OBJECT_TITLE)
        hor_nav_bar_tabs._click_when_visible(
            locator.ModalCreateNewObject.GEAR_ICON)
        hor_nav_bar_tabs._click_when_visible(locator.HorNavBar.EDIT_PROGRAM)
        hor_nav_bar_tabs._get_element_when_visible(
            locator.HorNavBar.EDIT_OBJECT_TEXT)
        hor_nav_bar_tabs._click_when_visible(locator.HorNavBar.CLOSE_X)

        hor_nav_bar_tabs.hor_nav_bar_delete(identifier)

    def test_hor_nav_bar_delete(self, hor_nav_bar_setup, programs_num=2):
        """
        Creates a few programs and deletes them.

        Confirms program deletion.
        """
        hor_nav_bar_tabs = hor_nav_bar_setup.open_dashboard()
        identifier = hor_nav_bar_tabs.start_new_program(programs_num)
        hor_nav_bar_tabs.hor_nav_bar_delete(identifier)
        hor_nav_bar_tabs.confirm_deletion(identifier)

    def hor_nav_bar_delete_objects(self, hor_nav_bar_setup):
        """
        This is NOT a test method!

        Note: You have to click on the desired object in
              the Horizontal Navigation Bar to delete it.
        """
        hor_nav_bar_tabs = hor_nav_bar_setup.open_dashboard()
        hor_nav_bar_tabs.hor_nav_bar_delete_objects()
