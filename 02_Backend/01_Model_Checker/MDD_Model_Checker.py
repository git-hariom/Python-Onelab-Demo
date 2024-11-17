"""
-> .ucdef Data converted into dictionary

-> Use data directly while reading excel to reduce looping need.

-> TestCase 1: Check if variable exists. If exists, compare name
    Action: Record Error, if name does not match
-> TestCase 2: MDD IN is ucDef in
    No action required
-> TestCase 3: MDD IN is ucDef OUT
    Action: record this error
-> TestCase 4: MDD OUT is ucDef OUT
    No action required
-> TestCase 5: MDD OUT is ucDef IN
    Action: record this error
-> TestCase 6: MDD var not present in ucDef
    Action: Record this error.
-> TestCase 7: ucDef var not present in MDD
    Action: Record this error.

*** Check Data types in testcase 1 and 2 as multiple datatypes match a single on in ucDef file

Additional Requirements ADDED:
    > Need to read the CAB and identifier columns and add them to the dict. and later while checking the names should be added to the variable name..
    ******
    > Should check if the identifier/number variables are not missing the MDD.. 
    ******
    
    > Car and alias names already present
    > Multiple Interface tabs in one MDD
    
    > To chek how to use it for SILs
"""

"""
MDD is ok if the test is completed.'MDD QUALITY ASSURED.'
"""

"""
.ucdef of Model generated in U-test when imported and MDD check.
"""

## READ MDD SHEETS ONLY
## Alias and Car combinations to be looked through.(Ex: STA PAI A MDD)

import xml.etree.ElementTree as eTree
import pandas as pd
import os

# Dictionary for Input variables in .ucDef file 
var_dict_in_ucDef = {}
# Dictionary for Output variables in .ucDef file
var_dict_out_ucDef = {}

report_msg = ""

#Model ucDef
## usercode.ucdef file read ##
def ReadData_Model(Model_path):
    
    # Open the ucdef as xml file
    with open(Model_path,'r') as xml_file:
        #xml_tree is the ucDef file converted to a tree for ease of reading th variables
        xml_tree = eTree.parse(xml_file)

    xml_file.close()

    # Getting the root of the element tree
    root = xml_tree.getroot()

    # var.attrib['datatype'] is not working as there are some vars without datatype attrib.
    # Making input and output vars dictionary
    for child in root:
        if child.tag == 'outputs':
            for var in child:
                var_dict_out_ucDef[var.attrib['name'].casefold().replace('__0','')] = [var.attrib['name'].replace('__0','')]               
        elif child.tag == 'inputs':
            for var in child:
                var_dict_in_ucDef[var.attrib['name'].casefold().replace('__0','')] = [var.attrib['name'].replace('__0','')]

## MDD file read ##
def ReadData_MDD(MDD_path):

    # Reading the excel file
    vars_MDD = pd.read_excel(MDD_path)

    # Calling Check function for checking the MDD variables with the .ucDef file
    Check_MDD_ucdef(vars_MDD)

##Check Vars in MDD for 
def Check_MDD_ucdef(vars_MDD):
     
    ## Precising the Column Name for MDD
    name = 'Variable Name'
    dtype = 'Data Type'
    inout = 'Input/Output'
    car = 'Car'
    alias = 'Alias'
    origin = 'Origin'
    dest = 'Destination'

    # Iterating over variables of the MDD and checking the testcases
    for i in range(len(vars_MDD[name])):
        if str(vars_MDD[name][i]) != 'nan' and str(vars_MDD[name][i])[0:2] != '//':
            if vars_MDD[inout][i].casefold() == 'input':
                if vars_MDD[origin][i].casefold() != '':
                    varName = str(vars_MDD[name][i])
                    TestCase_CheckforIN(varName,vars_MDD[dtype][i])

            elif vars_MDD[inout][i].casefold() == 'output':
                if vars_MDD[dest][i].casefold() != '':
                    varName = str(vars_MDD[name][i])
                    TestCase_CheckforOUT(varName,vars_MDD[dtype][i])
                            

## MDD Input variable Checks ##
def TestCase_CheckforIN(var_Name,var_DataType):
    
    #TestCase 2
    if var_Name.casefold() in var_dict_in_ucDef:
         #TestCase 1
        if var_Name != var_dict_in_ucDef[var_Name.casefold()][0]:
            MakeReport(f"{var_Name},Model,Failed,NAME MISMATCH\n")
        else:
            MakeReport(f"{var_Name},Model,Passed,NA\n")
    
    # TestCase 3
    if var_Name.casefold() in var_dict_out_ucDef:
        MakeReport(f"{var_Name},Model,Failed,Is as a input in ucDef and MDD\n")
    
    # TestCase 6
    if var_Name.casefold() not in var_dict_in_ucDef and var_Name.casefold() not in var_dict_out_ucDef:
        MakeReport(f"{var_Name},Model,Failed,not present in Model\n")

    # Removing key from dict..
    var_dict_in_ucDef.pop(var_Name.casefold(),None)
    var_dict_out_ucDef.pop(var_Name.casefold(),None)


## MDD Output variable Checks ##
def TestCase_CheckforOUT(var_Name,var_DataType):

    if var_Name.casefold() in var_dict_out_ucDef:
        #TestCase 4
        if var_Name != var_dict_out_ucDef[var_Name.casefold()][0]:
            #TestCase 1
            MakeReport(f"{var_Name},Model,Failed,NAME MISMATCH\n")
        else:
            MakeReport(f"{var_Name},Model,Passed,NA\n")

    # TestCase 5
    if var_Name.casefold() in var_dict_in_ucDef:
        MakeReport(f"{var_Name},Model,Failed,Is as a output in ucDef and MDD\n")

    # TestCase 6
    if var_Name.casefold() not in var_dict_in_ucDef and var_Name.casefold() not in var_dict_out_ucDef:
        MakeReport(f"{var_Name},Model,Failed,not present in Model\n")

    # Removing key from dict..
    var_dict_in_ucDef.pop(var_Name.casefold(),None)
    var_dict_out_ucDef.pop(var_Name.casefold(),None)

## TestCase 7
def RemainingVars_ucDef():
    for i in var_dict_out_ucDef:
        MakeReport(f"{var_dict_in_ucDef[i][0]},Model,Failed,not present in MDD\n")
    for i in var_dict_in_ucDef:
        MakeReport(f"{var_dict_in_ucDef[i][0]},Model,Failed,not present in MDD\n")

def MakeReport(msg):
    global report_msg
    report_msg += str(msg)

def StartChecker_Model(ucDef_path, MDD_path):

    ReadData_Model(ucDef_path)
    ReadData_MDD(MDD_path)

    #Checking TestCase 5
    ##############################################################################################################################################
    # When implementing check for aliases.
    ##############################################################################################################################################
    #RemainingVars_ucDef()

    # if(os.path.exists(reportFile_path)):
    #     file2 = open(reportFile_path,"w")
    #     file2.writelines(report_msg)

    return report_msg