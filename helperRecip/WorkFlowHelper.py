'''
Created on May 26, 2014

@author: uduong
@description This class is created holds all functions related to WorkFlow only.  Elements are also stored locally to the function that use it.
It's unlikely that elements are used by others when you purposely write it for a specifiec function.  Also, when Elements and Helpers classes 
are getting bigger they become unmanageable.  



'''

from datetime import datetime
from lib2to3.tests.support import driver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from helperRecip.Helpers import Helpers, log_time


class WorkFlowHelper(Helpers):
    
    '''
    Any elements that are shared among the functions can go here
    '''
    
    
    startWorkflow_bt = '//button[@type="submit" and @href="#workflowStart"]'
    endWorkflow_bt = '//button[@type="submit" and @class="btn end-workflow"]'





    #@log_time
    # objecName: Controls or Projects, etc.
    # relevantTo: Program
    def addObjects(self, objectName, relevantTo, whatItem):
        add_object_lk = '//a[@href="#objectSelector" and @data-mapping="objects"]' 
        add_new_rule_lk = '//a[@id="addFilterRule"]'
        object_select_drdn = '//select[@id="objects_type"]' 
        add_selected_bt = '//a[@id="addSelected"]'
        relevantTo_drdn = '//div[@id="filters"]//select[@class="input-small"]'
        search_txtbx = '//div[@id="filters"]//select[@class="input-small"]/../div[@class="objective-selector"]//input'
        search_bt = '//a[@id="objectReview"]'
        total_count = '//div[@id="middle_column"]/section[@class="widget objectives objects_widget widget-active"]//span[@id="objectsCounter"]'
        # check the count first
        
        countBefore = self.util.getTextFromXpathString(total_count)
        print countBefore
        
        self.util.clickOn(add_object_lk)
        self.util.selectFromDropdownByValue(object_select_drdn, objectName)
        self.util.selectFromDropdownByValue(relevantTo_drdn, relevantTo)
        self.util.inputTextIntoField(whatItem, search_txtbx)
        self.util.clickOn(search_bt)
        
        # TODO no real data is shown so can't progress further
        
        self.util.clickOn(add_selected_bt)
       
       
        # wait before checking count
        time.sleep(1)
        countAfter = self.util.getTextFromXpathString(total_count)
        
        if countAfter > countBefore:
            return True
        else:
            return False
        
       
       # after adding the total count should increase by one
       
       
    

    @log_time
    # Return true if addTask succeed and not error out
    def addTask(self, taskName="", selectAll=False): 
        add_task_lk = '//a[@href="#objectSelector" and @data-mapping="tasks"]' 
        checkboxAll_chbx = '//input[@id="objectAll"]'
        addSelected_bt = '//a[@id="addSelected"]'
        task_table = '//div[@id="objectSelector"]/div[@class="results"]//ul'
        
        if selectAll == True:
            self.util.clickOn(addSelected_bt)  # just click on the button
        else:
            self.util.clickOn(checkboxAll_chbx)  # it's checked by default so click to uncheck it
            
            count = self.util.countChildren(task_table) 
            print "DEBUG, count: " + count
            
            for x in range(2, count):
                xpath = task_table + '/li[' + x + ']//div[@class="tree-title-area"]/i'
                title = self.util.getTextFromXpathString(xpath)
                print "DEBUG, title: " + title
                if title == taskName:  # if found, click on the checkbox next to it
                    self.util.clickOn(task_table + '//input[@type="checkbox"]')  # check it
                    break  # get out
        
        self.util.clickOn(addSelected_bt)
        return True
           
           
    @log_time
    # Create a new task from a window popped up by "add task".  That means the window must be up already before this 
    # function can be used.
    # To test the Cancel feature, set save=False
    def createNewTask(self, title, detail_description, save=True):
        create_task_bt = '//a[@class="btn btn-add addTaskModal"]'
        summary_title_txtbx = '//input[@id="task-title"]'
        detail_txtbx = '//div[@id="newTask"]//textarea[@id="program_description"]'
        save_bt = '//a[@id="addTask"]' 
        cancel_bt = '//a[@id="addTask"]/../../../div/div/a[@data-dismiss="modal"]'
           
        self.util.clickOn(create_task_bt)
        self.util.inputTextIntoField(title, summary_title_txtbx)
        self.util.inputTextIntoField(detail_description, detail_txtbx)
        if save==True:
            self.util.clickOn(save_bt)
        else:
            self.util.clickOn(cancel_bt)
           
                
    @log_time
    # Return true if addPerson succeed and not error out
    def addPerson(self, personName="", selectAll=False):
        add_person_lk = '//a[@href="#objectSelector" and @data-mapping="person"]' 
        checkboxAll_chbx = '//input[@id="objectAll"]'
        addSelected_bt = '//a[@id="addSelected"]'
        task_table = '//div[@id="objectSelector"]/div[@class="results"]//ul'
        
        if selectAll == True:
            self.util.clickOn(addSelected_bt)  # just click on the button
        else:
            count = self.util.countChildren(task_table) 
            print "count: " + count
            
            for x in range(2, count):
                xpath = task_table + '/li[' + x + ']//div[@class="tree-title-area"]/i'
                title = self.util.getTextFromXpathString(xpath)
                print "title: " + title
                if title == personName:  # if found, click on the checkbox next to it
                    self.util.clickOn(task_table + '//input[@type="checkbox"]')  # check it
                    break  # get out
        
        self.util.clickOn(addSelected_bt)
        return True        

    @log_time
    # Return true if addTaskGroup succeed and not error out    
    # if you want to test the Cancel feature then set save=False
    # date format: "2014_05_27", for test purpose please use current date
    def addTaskGroup(self, groupName, personName, date, save=True):
        group_txtbx = '//input[@id="new_object_name"]'
        search_txtbox = '//input[@id="new_object_name"]'
        save_bt = '//a[@id="addTaskGroup"]'
        cancel_bt = '//a[@id="cancelTaskGroup"]'
        calendar_picker = '//input[@id="tg_end_date"]'
        month_label = '//div[@id="ui-datepicker-div"]//span[@class="ui-datepicker-month"]'
        year_label = '//div[@id="ui-datepicker-div"]//span[@class="ui-datepicker-year"]'
        date_table = '//table[@class="ui-datepicker-calendar"]/tbody'

        self.util.inputTextIntoField(groupName, group_txtbx)
        self.util.inputTextIntoField(personName, search_txtbox)
        
        if save == True:
            self.util.clickOn(save_bt)
        else:
            self.util.clickOn(cancel_bt)

        day = str(datetime.now())
        
        day = day[8:10]
        
        # dateTable = WebElement(self.driver.findElement(By.TAG_NAME("table")));
        # List<WebElement> tableRows = yourTable.findElements(By.TAG_NAME("tr"));
        
        # just pick the current day from the day table        
        for row in range (1, 5):
            for column in range (1, 7):
                xpath = str(date_table + '/tr[' + row + ']/td[' + column + ']/a')
                theDay = self.util.clickOn(xpath)
                if (day == theDay):
                    self.util.clickOn(xpath)
                    break  # inner loop
                else:
                    continue;
                
            break  # outer loop
        
        return True    
        
    @log_time
    def startWorkFlow(self, proceed=True):       
        proceed_bt = '//a[@id="confirmStartWorkflow"]'
        cancel_bt = '//a[@id="cancelStartWorkflow"]'
        self.util.clickOn(self.startWorkflow_bt)
        time.sleep(.5)
        if proceed == True:
            self.util.clickOn(proceed_bt)
        else:
            self.util.clickOn(cancel_bt)
            
        
    @log_time
    def stopWorkFlow(self):
        self.util.clickOn(self.endWorkflow_bt)
        
        
           
    @log_time
    # unmap first item in the list -- from the top
    def unmapPerson(self, personName):
        # TODO add search by title in the future
        
        firstItem = '//div[@id="middle_column"]/section[@class="widget entities people_widget widget-active"]//span[@class="person-holder"]'
        unmap_lk = '//div[@id="middle_column"]//a[@class="info-action unmap pull-right"]'
        total_count_label = '//div[@id="middle_column"]/section[@class="widget entities people_widget widget-active"]//span[@class="object_count"]'
        count = self.util.getTextFromXpathString(total_count_label)
        
        self.util.hoverOver(firstItem)
        self.util.clickOn(firstItem)
        self.util.clickOn(unmap_lk)
        
        
    @log_time
    # unmap first item in the list -- from the top
    def deleteTaskGroup(self, groupName):        
        # TODO add search by title in the future
        count_xpath = '//div[@id="middle_column"]/section[@class="widget programs task_groups_widget widget-active"]//h2'
        title = '//div[@id="middle_column"]/section[@class="widget programs task_groups_widget widget-active"]//div[@class="tree-title-area"]'
        trash_icon = '//span[@class="counter removeTaskGroup"]/i'
        
        countBefore = self.util.getTextFromXpathString(count_xpath)
        # TODO Need to parse out the counter
        
        
        self.util.clickOn(trash_icon)
        time.sleep(1)
        
        if self.util.getTextFromXpathString(count_xpath) == countBefore-1:
            return True
        else:
            return False

    #@log_time
    # navigate inner panel on WorkFlow, e.g., Objects, Task Groups
    def navigateToMenuItem(self, fromWhatWorkflow, menuItem):
        workflow_menu  = '//li[@class="programs accordion-group workflow-group"]'
        workflow_items = '//li[@class="programs accordion-group workflow-group"]/ul[@class="sub-level"]/li[INDEX]//span'
        count_xpath = '//li[@class="programs accordion-group workflow-group"]//span[@class="item-count"]'
        
        self.util.clickOn(workflow_menu) # click on WorkFlow to expand it
        
        count = self.util.getTextFromXpathString(count_xpath)
        
        for x in count:
            label_text = self.util.getTextFromXpathString(workflow_items.replace("INDEX", x)) # click on WorkFlow to expand it
            
            if fromWhatWorkflow==label_text:
                self.util.clickOn(workflow_items.replace("INDEX", x))
                break
            else:
                continue
    
        
        
        
    @log_time
    # Already in WorkFlow window, just want to select different menu item, e.g., Task Groups
    def selectInnerNavMenuItem(self, menuItem):
        ul_menu = '//ul[@class="nav internav innernav-arrow program cms_controllers_inner_nav ui-sortable workflow-nav"]'
        li_Objects = ul_menu + '/li[2]'
        li_Tasks = ul_menu + '/li[2]'
        li_People = ul_menu + '/li[2]'
        li_TaskGroups = ul_menu + '/li[2]'
        li_History = ul_menu + '/li[@class="history_object"]'
        li_CurrentCycle = ul_menu + '/li[@class="progress-object  finished"]'
        
        if menuItem == "Objects":
            self.util.clickOn(li_Objects)
        elif menuItem == "Tasks":
            self.util.clickOn(li_Tasks)
        elif menuItem == "People":
            self.util.clickOn(li_People)
        elif menuItem == "Task Groups":
            self.util.clickOn(li_TaskGroups)
        elif menuItem == "History":
            self.util.clickOn(li_History)
        elif menuItem == "Current Cycle":
            self.util.clickOn(li_CurrentCycle)
            
            
            
            
            
            