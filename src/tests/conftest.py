# header6ff05843-c222-461f-8226-36a7abe6806e

import sys
import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__)) + "/../"
print "conftest: PROJECT_ROOT_PATH = " + PROJECT_ROOT_PATH
sys.path.append(PROJECT_ROOT_PATH)
PROJECT_SRC_PATH = PROJECT_ROOT_PATH + "src/"
sys.path.append(PROJECT_SRC_PATH)
print "conftest: PROJECT_SRC_PATH = " + PROJECT_SRC_PATH

import pytest
from lib import base, base_test
from lib.page import dashboard


@pytest.yield_fixture(scope="class")
def selenium():
    """
    Returns:
        base.Test
    """
    test = base.Test()
    test.init_resources()
    yield test

    test.close_resources()


@pytest.yield_fixture(scope="session", autouse=False)
def program_object():
    """
    Returns:
        lib.page.modal.new_program.NewProgramPage
    """
    test = base.Test()
    test.init_resources()
    dashboard_page = dashboard.DashboardPage(test.driver)
    lhn_menu = dashboard_page.open_lhn_menu()
    lhn_menu.select_all_objects()
    program_dropdown = lhn_menu.open_programs()
    modal = program_dropdown.create_new_program()
    modal_actions = base_test.ModalNewProgramPage(modal)
    modal_actions.enter_test_data()
    program_info = modal.save_and_close()
    yield modal

    program_info.delete_object()
    test.close_resources()


@pytest.yield_fixture(scope="function", autouse=False)
def lhn_menu_setup():
    test = base.Test()
    test.init_resources()
    lhn_menu = dashboard.DashboardPage(test.driver)

    yield lhn_menu

    test.close_resources()


@pytest.yield_fixture(scope="function", autouse=False)
def user_mail_menu_setup():
    test = base.Test()
    test.init_resources()
    user_mail_menu = dashboard.DashboardPage(test.driver)

    yield user_mail_menu

    test.close_resources()


@pytest.yield_fixture(scope="function", autouse=False)
def hor_nav_bar_setup():
    test = base.Test()
    test.init_resources()
    user_mail_menu = dashboard.DashboardPage(test.driver)

    yield user_mail_menu

    test.close_resources()


@pytest.yield_fixture(scope="function", autouse=False)
def widget_setup():
    test = base.Test()
    test.init_resources()
    widget = dashboard.DashboardPage(test.driver)

    yield widget

    test.close_resources()
