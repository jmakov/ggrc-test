from lib.constants import locator


class ObjectData(object):
    obj_create = {
        'programs': locator.LhnMenu.PROGRAMS_LINK,
        'create_program': locator.LhnMenu.PROGRAMS_CREATE_NEW,
        'title': locator.ModalCreateNewProgram.TITLE_UI,
        'programs_count': locator.LhnMenu.PROGRAMS_COUNT[1],

        'workflows': locator.LhnMenu.WORKFLOWS_LINK,
        'create_workflow': locator.ModalCreateNewWorkflow.WF_CREATE_NEW,
        'wf_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'workflows_count': locator.LhnMenu.WORKFLOWS_COUNT[1],

        'audits': locator.LhnMenu.AUDITS_LINK,
        'create_audit': locator.ModalCreateNewAudit.AUDIT_CREATE_NEW,
        'program_checkbox': locator.ModalCreateNewAudit.CLICK_PROGRAM_CHECKBOX,
        'audit_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'audits_count': locator.LhnMenu.AUDITS_COUNT[1],

        'ctrl_asses': locator.LhnMenu.CTRL_ASSES_LINK,
        'create_ctrl_asses':
            locator.ModalCreateNewControlAsses.CONTROL_ASSES_CREATE_NEW,
        'ctrl_asses_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'control_checkbox':
            locator.ModalCreateNewControlAsses.CLICK_CONTROL_CHECKBOX,
        'audit_checkbox':
            locator.ModalCreateNewControlAsses.CLICK_AUDIT_CHECKBOX,
        'ctrl_asses_count': locator.LhnMenu.CTRL_ASSES_COUNT[1],

        'issues': locator.LhnMenu.ISSUES_LINK,
        'create_issue': locator.ModalCreateNewIssue.ISSUE_CREATE_NEW,
        'issue_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'issues_count': locator.LhnMenu.ISSUES_COUNT[1],

        'directives': locator.LhnMenu.DIRECTIVES,

        'regulations': locator.Directives.REGULATIONS,
        'create_regulation':
            locator.ModalCreateNewRegulation.REGULATION_CREATE_NEW,
        'regulation_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'regulations_count': locator.Directives.REGULATIONS_COUNT[1],

        'policies': locator.Directives.POLICIES,
        'create_policy': locator.ModalCreateNewPolicy.POLICY_CREATE_NEW,
        'policy_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'policies_count': locator.Directives.POLICIES_COUNT[1],

        'standards': locator.Directives.STANDARDS,
        'create_standard': locator.ModalCreateNewStandard.STANDARD_CREATE_NEW,
        'standard_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'standards_count': locator.Directives.STANDARDS_COUNT[1],

        'contracts': locator.Directives.CONTRACTS,
        'create_contract': locator.ModalCreateNewContract.CONTRACT_CREATE_NEW,
        'contract_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'contracts_count': locator.Directives.CONTRACTS_COUNT[1],

        'clauses': locator.Directives.CLAUSES,
        'create_clause': locator.ModalCreateNewClause.CLAUSE_CREATE_NEW,
        'clause_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'clauses_count': locator.Directives.CLAUSES_COUNT[1],

        'sections': locator.Directives.SECTIONS,
        'create_section': locator.ModalCreateNewSection.SECTION_CREATE_NEW,
        'section_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'policy_checkbox': locator.ModalCreateNewSection.CLICK_POLICY_CHECKBOX,
        'sections_count': locator.Directives.SECTIONS_COUNT[1],

        'ctrl_obj': locator.LhnMenu.CONT_OBJ,

        'controls': locator.ControlObjectives.CONTROLS,
        'create_control': locator.ModalCreateNewControl.CONTROL_CREATE_NEW,
        'control_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'controls_count': locator.ControlObjectives.CONTROLS_COUNT[1],

        'objectives': locator.ControlObjectives.OBJECTIVES,
        'create_objective':
            locator.ModalCreateNewObjective.OBJECTIVE_CREATE_NEW,
        'objective_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'objectives_count': locator.ControlObjectives.OBJECTIVES_COUNT[1],

        'ppl_grp': locator.LhnMenu.PPL_GRP,

        'people': locator.PeopleGroups.PEOPLE,
        'create_person': locator.ModalCreateNewPerson.PERSON_CREATE_NEW,
        'person_email': locator.ModalCreateNewPerson.PERSON_EMAIL,
        'people_count': locator.PeopleGroups.PEOPLE_COUNT[1],

        'org_gropus': locator.PeopleGroups.ORG_GROUPS,
        'create_org_gropu':
            locator.ModalCreateNewOrgGroup.ORG_GROUP_CREATE_NEW,
        'org_gropu_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'org_groups_count': locator.PeopleGroups.ORG_GROUPS_COUNT[1],

        'vendors': locator.PeopleGroups.VENDORS,
        'create_vendor': locator.ModalCreateNewVendor.VENDOR_CREATE_NEW,
        'vendor_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'vendors_count': locator.PeopleGroups.VENDORS_COUNT[1],

        'assets': locator.LhnMenu.ASSETS,

        'systems': locator.AssetsBusiness.SYSTEMS,
        'create_system': locator.ModalCreateNewSystem.SYSTEM_CREATE_NEW,
        'system_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'systems_count': locator.AssetsBusiness.SYSTEMS_COUNT[1],

        'processes': locator.AssetsBusiness.PROCESSES,
        'create_process': locator.ModalCreateNewProcess.PROCESS_CREATE_NEW,
        'process_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'processes_count': locator.AssetsBusiness.PROCESSES_COUNT[1],

        'data_assets': locator.AssetsBusiness.DATA_ASSETS,
        'create_data_asset':
            locator.ModalCreateNewDataAsset.DATA_ASSET_CREATE_NEW,
        'data_asset_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'data_assets_count': locator.AssetsBusiness.DATA_ASSETS_COUNT[1],

        'products': locator.AssetsBusiness.PRODUCTS,
        'create_product': locator.ModalCreateNewProduct.PRODUCT_CREATE_NEW,
        'product_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'products_count': locator.AssetsBusiness.PRODUCTS_COUNT[1],

        'projects': locator.AssetsBusiness.PROJECTS,
        'create_project': locator.ModalCreateNewProject.PROJECT_CREATE_NEW,
        'project_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'projects_count': locator.AssetsBusiness.PROJECTS_COUNT[1],

        'facilities': locator.AssetsBusiness.FACILITIES,
        'create_facility': locator.ModalCreateNewFacility.FACILITY_CREATE_NEW,
        'facility_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'facilities_count': locator.AssetsBusiness.FACILITIES_COUNT[1],

        'markets': locator.AssetsBusiness.MARKETS,
        'create_market': locator.ModalCreateNewMarket.MARKET_CREATE_NEW,
        'market_title': locator.ModalCreateNewWorkflow.WF_TITLE,
        'markets_count': locator.AssetsBusiness.MARKETS_COUNT[1],

        'risks_threats': locator.LhnMenu.RISKS,

        'risks': locator.RiskThreats.RISKS,
        'create_risk': locator.ModalCreateNewRisk.RISK_CREATE_NEW,
        'risk_title': locator.ModalCreateNewRisk.RISK_TITLE,
        'risk_owner': locator.ModalCreateNewRisk.RISK_OWNER,
        'risks_count': locator.RiskThreats.RISKS_COUNT[1],

        'threat_actors': locator.RiskThreats.THREAT_ACTORS,
        'create_threat_actor':
            locator.ModalCreateNewThreatActor.THREAT_ACTOR_CREATE_NEW,
        'threat_actor_title':
            locator.ModalCreateNewThreatActor.THREAT_ACTOR_TITLE,
        'threat_actors_count': locator.RiskThreats.THREAT_ACTORS_COUNT[1]
    }
