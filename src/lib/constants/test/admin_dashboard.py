# -*- coding: utf-8 -*-

class People(object):
    class PeopleList(object):
        FIRST_USERNAME = "...A_very_first_test_person_name"
        FIRST_EMAIL = "_a_very_first_test_person_name@testemail.com"
        FIRST_COMPANY = "A_very_first_test_person_company"

        GEN_USERNAME= "___test_person_name_"
        GEN_EMAIL_NAME = "___test_person_email_name_"
        GEN_EMAIL_DOMAIN = "testemail.com"
        GEN_COMPANY = "___test_company_"

        SEARCH = "...A_very"
        USER_ROLE = "Reader"

        NUM_NEEDED_FOR_MULTIPAGE = 51

    class FirstItem(object):
        NAME = 'NAME'
        EMAIL = 'EMAIL'
        COMPANY = 'COMPANY'
        AUTHORIZATIONS = 'AUTHORIZATIONS'

    class AdditionalContent(object):
        ITEMS_IN_LIST = ["NAME",
                         "EMAIL",
                         "COMPANY",
                         "AUTHORIZATIONS"]

        class Dropdown(object):
            ITEMS_IN_LIST = ["View Profile Page",
                             "Edit Authorizations",
                             "Edit Person"]
            EDIT_TITLE = "Edit Person"
            AUTHORIZATIONS_TITLE = "User Role Assignments"

class Roles(object):
    ITEMS_IN_LIST = ["Creator",
                     "Editor",
                     "gGRC Admin",
                     "ProgramEditor",
                     "ProgramOwner",
                     "ProgramReader",
                     "Reader",
                     "WorkflowMember",
                     "WorkflowOwner"]

    ITEMS_NOT_IN_LIST = ["Auditor"]

class CustomAttributes(object):
    FILTER = "Filter"

    ITEMS_IN_LIST = ["Workflows",
                     "Audits",
                     "Programs",
                     "Objectives",
                     "Sections",
                     "Controls",
                     "Issues",
                     "Control Assessments",
                     "Regulations",
                     "Contracts",
                     "Standards",
                     "Clauses",
                     "Policies",
                     "Vendors",
                     "Org Groups",
                     "People",
                     "Markets",
                     "Data Assets",
                     "Products",
                     "Facilities",
                     "Projects",
                     "Systems",
                     "Processes"]

    ITEMS_NOT_IN_LIST = ["Auditor"]

    class AdditionalContent(object):
        ITEMS_IN_LIST = ["Attribute name","Attribute type","Mandatory","Edit"]
        MODAL_ADD_TITLE = "Add Attribute to type Workflow"
        MODAL_EDIT_TITLE = "Edit Custom Attribute Definition"

class Export(object):
    SELECT_SYSTEMS = 'System'
    SELECT_PROCESSES = 'Process'
    SELECT_PEOPLE = 'Person'

class Import(object):
    CSV_FILENAME = '~/Downloads/export_objects.csv'
    IMPORT_SUCCESS = 'Import successful'

class EventLog(object):
    DATE_FORMATTING = "%m/%d/%Y %I:%M:%S%p"