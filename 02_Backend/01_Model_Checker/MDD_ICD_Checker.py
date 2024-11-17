"""  CODE OVERVIEW
-> .ICD Data converted into dictionary

-> Use data directly while reading excel to reduce looping need.

-> TestCase 1: Check whether the name is same and record the error.
    Record the error.
-> TestCase 2: MDD out is ICD OUT
    No action required
-> TestCase 3: MDD IN is ICD IN
    No action required
-> TestCase 4: MDD OUT is ICD IN
    Action: record this error
-> TestCase 5: MDD IN is ICD OUT
    Action: record this error
-> TestCase 6: ICD var not present in MDD
    Action: Record this error.
-> TestCase 7: MDD var not present in ICD
    Action: Record this error.
-> TestCase 8: MDD OUT is in MDD IN
    Action: Record this error
-> TestCase 9: MDD IN is in MDD OUT
    Action: Record this error

*** Check Data types in testcase 1 and 2 as multiple datatypes match a single one in ICD file

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

## READ MDD SHEETS ONLY
## Alias and Car combinations to be looked through.(Ex: STA PAI A MDD)

import xml.etree.ElementTree as eTree
import pandas as pd
import os

# Dictionary for Input variables in .ICD file 
var_dict_in_ICD = {}
# Dictionary for Output variables in .ICD file
var_dict_out_ICD = {}

reportFile_path = r"C:\Users\Public\report_MDD_ICD_Check.txt"

report_msg = ""

## Read ICD ##
def ReadData_ICD(ICD_path):

    name = 'Signal Name'
    dtype = 'Control_Build_Type'

    # Reading the excel file
    vars_MDD = pd.read_excel(ICD_path)

    ############################################################################################################
    # Might need to add "smart" as a string to ignore.
    ############################################################################################################
    for i in range(len(vars_MDD[name])):
        varName = str(vars_MDD[name][i]).replace('<','').replace('>','')
        if "_c" in varName.casefold() and "spare" not in varName.casefold():
            var_dict_in_ICD[varName.casefold()] = [varName,str(vars_MDD[dtype][i]).casefold()]
        elif "_i" in varName.casefold() and "spare" not in varName.casefold():
            var_dict_out_ICD[varName.casefold()] = [varName,str(vars_MDD[dtype][i]).casefold()]

## MDD file read ##
def ReadData_MDD(MDD_path):

    # Reading the excel file
    vars_MDD = pd.read_excel(MDD_path)

    # Calling Check function for checking the MDD variables with the .ICD file
    Check_MDD_ICD(vars_MDD)

##Check Vars in MDD for 
def Check_MDD_ICD(vars_MDD):
     
    ## Precising the Column Name for MDD
    name = 'Variable Name'
    dtype = 'Data Type'
    inout = 'Input/Output'
    origin = 'Origin'
    dest = 'Destination'

    # Iterating over variables of the MDD and checking the testcases
    for i in range(len(vars_MDD[name])):
        if str(vars_MDD[name][i]) != 'nan' and str(vars_MDD[name][i])[0:2] != '//':
            varName = str(vars_MDD[name][i])
            if vars_MDD[inout][i].casefold() == 'input':
                if vars_MDD[origin][i].casefold() == 'mpu':
                    TestCase_CheckforIN(varName,vars_MDD[dtype][i])                            
            
            elif vars_MDD[inout][i].casefold() == 'output':
                if vars_MDD[dest][i].casefold() == 'mpu':
                    TestCase_CheckforOUT(varName,vars_MDD[dtype][i])                 
                            

## MDD Input variable Checks ##
def TestCase_CheckforIN(var_Name,var_DataType):   
    
    if var_Name.casefold() in var_dict_in_ICD:
        # TestCase 1
        if var_Name != var_dict_in_ICD[var_Name.casefold()][0]:
            MakeReport(f"{var_Name},ICD,Failed,NAME MISMATCH\n")

        # TestCase 2
        if var_DataType.casefold() == var_dict_in_ICD[var_Name.casefold()][1]:
            MakeReport(f"{var_Name},ICD,Passed,NA\n")

        else:
            MakeReport(f"{var_Name},ICD,Failed,DataType Not matching(MDD: {var_DataType} || ICD: {var_dict_in_ICD[var_Name.casefold()][1]})\n")
    
    # TestCase 4
    if var_Name.casefold() in var_dict_out_ICD:
        MakeReport(f"{var_Name},ICD,Failed,Is as a input in MDD and output in ICD\n")
    
    # TestCase 6
    if var_Name.casefold() not in var_dict_out_ICD and var_Name.casefold() not in var_dict_in_ICD:
        MakeReport(f"{var_Name},ICD,Failed,not present in ICD\n")

    # Removing key from dict..
    var_dict_in_ICD.pop(var_Name.casefold(),None)
    var_dict_out_ICD.pop(var_Name.casefold(),None)


## MDD Output variable Checks ##
def TestCase_CheckforOUT(var_Name,var_DataType):

    if var_Name.casefold() in var_dict_out_ICD:
        #TestCase 1
        if var_Name != var_dict_out_ICD[var_Name.casefold()][0]:
            MakeReport(f"{var_Name},ICD,Failed,NAME MISMATCH\n")

        # TestCase 3
        if var_DataType.casefold() == var_dict_out_ICD[var_Name.casefold()][1]:
            MakeReport(f"{var_Name},ICD,Passed,NA\n")
        else:
            MakeReport(f"{var_Name},ICD,Failed,DataType Not matching(MDD: {var_DataType} || ICD: {var_dict_out_ICD[var_Name.casefold()][1]})\n")

    # TestCase 4
    if var_Name.casefold() in var_dict_in_ICD:
        MakeReport(f"{var_Name},ICD,Failed,is as a output in ICD and MDD\n")

    # TestCase 7
    if var_Name.casefold() not in var_dict_in_ICD and var_Name.casefold() not in var_dict_out_ICD:
        MakeReport(f"{var_Name},ICD,Failed,Not present in ICD\n")

    # Removing key from dict..
    var_dict_in_ICD.pop(var_Name.casefold(),None)
    var_dict_out_ICD.pop(var_Name.casefold(),None)

## TestCase 5
def RemainingVars_ICD():
    for i in var_dict_out_ICD:
        MakeReport(f"{var_dict_out_ICD[i][0]},ICD,Missing,not present in MDD\n")
    for i in var_dict_in_ICD:
        MakeReport(f"{var_dict_in_ICD[i][0]},ICD,Missing,not present in MDD\n")

def MakeReport(msg):
    global report_msg
    report_msg += str(msg)

def StartChecker_ICD(ICD_path, MDD_path):

    ReadData_ICD(ICD_path)
    ReadData_MDD(MDD_path)

    #Checking TestCase 5
    ##############################################################################################################################################
    # When implementing check for aliases.
    ##############################################################################################################################################
    # RemainingVars_ICD()

    # if(os.path.exists(reportFile_path)):
    #     file2 = open(reportFile_path,"w")
    #     file2.writelines(report_msg)

    return report_msg