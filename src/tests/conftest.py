# # header6ff05843-c222-461f-8226-36a7abe6806e
#
# import pytest
# from lib import base, base_test
# from lib.page import dashboard
#
#
# @pytest.yield_fixture(scope="function")
# def selenium():
#     """
#     Returns:
#         base.Test
#     """
#     test = base.Test()
#     test.init_resources()
#     yield test
#
#     test.close_resources()
#
#
# @pytest.yield_fixture(scope="session", autouse=True)
# def program_object():
#     """
#     Returns:
#         lib.page.modal.new_program.NewProgramPage
#     """
#     test = base.Test()
#     test.init_resources()
#     dashboard_page = dashboard.DashboardPage(test.driver)
#     lhn_menu = dashboard_page.open_lhn_menu()
#     lhn_menu.select_all_objects()
#     program_dropdown = lhn_menu.open_programs()
#     modal = program_dropdown.create_new_program()
#     modal_actions = base_test.ModalNewProgramPage(modal)
#     modal_actions.enter_test_data()
#     program_info = modal.save_and_close()
#     yield modal
#
#     program_info.delete_object()
#     test.close_resources()
