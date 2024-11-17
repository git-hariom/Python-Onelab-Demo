"""
This code is responsible for deciding which tests need to be performed and where the reports need to be saved.
"""

## Performs the MDD check with ICD and .ucDef file for Simulatio.

import os
import MDD_ICD_Checker as ICD_Check
import MDD_ucDef_Checker as SPS_Check
import MDD_Model_Checker as Model_Check

ICD_path = r'C:\Users\516318\Desktop\ToolDev\ICD.xlsx'
MDD_path = r'C:\Users\516318\Desktop\ToolDev\MDD.xlsx'
ucDef_path = r'C:\Users\516318\Desktop\ToolDev\SPS.ucdef'
Model_path = r'C:\Users\516318\Desktop\ToolDev\Model.ucdef'

reportMDD_path = r"C:\Users\Public\MDD_Check_Report.csv"

reportModel_path = r"C:\Users\Public\report_Model_Check.csv"

def MDDChecker_Start(MDD_path,ucDef_path,ICD_path,Model_path):

    report = ''

    if not os.path.exists(MDD_path):
        print('MDD PATH does not exist!! Please Check and try again.')
        return
    
    if os.path.exists(ucDef_path):        
        print('Comparing MDD and Simulatio ucdef')
        report += f"\n"
        report = SPS_Check.StartChecker_SPS(ucDef_path,MDD_path)
        print(f'Task Completed!! Please find the report here: {reportMDD_path}')

    if os.path.exists(ICD_path):
        print('Comparing MDD and ICD')
        report += f"\n"
        report += ICD_Check.StartChecker_ICD(ICD_path,MDD_path)
        print(f'Task Completed!! Please find the report here: {reportMDD_path}')

    file1 = open(reportMDD_path,"w")
    file1.writelines("Variable_Name,Executed_Test,Junction_Status,Error_Description\n\n" + report)

    if os.path.exists(Model_path):
        print('Performing MDD and Model Check.')
        report = Model_Check.StartChecker_Model(Model_path,MDD_path)
        print(f'Please find the report here: {reportModel_path}')

    file1 = open(reportModel_path,"w")
    file1.writelines("Variable_Name,Executed_Test,Junction_Status,Error_Description\n\n" + report)

MDDChecker_Start(MDD_path,ucDef_path,ICD_path,Model_path)