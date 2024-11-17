import xml.etree.ElementTree as ET
import pandas as pd
import BaseRule as br
import RuleICD as icd
#import Simulatio as Simu
from Result import tableresult
from Graph import graphres


# Load the XML file
def JunctionCheck(cfgpath,icdpath,projectname):
    tree = ET.parse(cfgpath)
    icd_excel = icd.read_excel(icdpath)
    #Simu.Simulatio_convertor()
    # Get the root element
    root = tree.getroot()
    icd_rule1 = "_C"
    icd_rule2 = "_I"
    Rule2Result = ""
    # Create empty lists for each column
    xml_data = []
    #conf_type = int(input("Please enter Your configuration type: 1(Pcosim), 2(TestBench), 3(TrainLab)"))
    Project_name = projectname
    # Loop through each usercode and its varrefs to extract data into the lists
    for uc in root.findall('.//userCodes'):
        uc_name = uc.get('name')
        for varrefs in ['inputVarRefs', 'ouputVarRefs']:
            for io_point in uc.find(varrefs).findall('.//ioPoints'):
                data_type = io_point.get('dataType')
                path_name = io_point.get('pathName')
                data_name = io_point.get('name')
                if path_name == None:
                    jc = "Not Junctioned"
                else:
                    jc = "Junctioned"
                if data_type == None:
                    tp = "DOUBLE"
                else:
                    tp = data_type
                xml_data.append({
                    'Usercode name': uc_name,
                    'VarRefs': varrefs.replace('Var', '').upper(),
                    'Variable name': data_name,
                    'Data type':tp,
                    'Path name': path_name,
                    'Result': None,
                    'Junction_check': jc,
                    'Desc': None,
                    'Status': None,
                    'Rule_Name':None
                })
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(xml_data)
    
    # Write the DataFrame to an Excel file
    df.to_excel(r'C:\Users\Public\usercode.xlsx', index=False)

    # Loop over each row of the DataFrame and update the "Junction_check" column
    for i in range(len(df.index)):
        VarRule1 = df.iloc[i, 2]  # Get the value in the "Path name" column
        Rule1Result = br.var_check(VarRule1)
        ####################################################################
                            #Rule1:Base Rule 
        ###################################################################                   
        if Rule1Result == "True" and df.iloc[i,6]=="Not Junctioned":
            df.iloc[i,5] ="Pass"
            df.iloc[i,7] ="Rule#1: Base Rule"
            df.iloc[i,8] = "Check Done"
            df.iloc[i,9] = "Rule#1"
        elif Rule1Result == "True" and df.iloc[i,6]== "Junctioned":
            df.iloc[i,5] ="Fail"
            df.iloc[i,7] ="Rule#1: Base Rule"
            df.iloc[i,8] = "Check Done"
            df.iloc[i,9] = "Rule#1"
        ###################################################################
                            #Rule2:ICD Rule for 
        ###################################################################
        if df.iloc[i,8]!="Check Done" and df.iloc[i,1] == "INPUTREFS" :#and conf_type == 1: and df.iloc[i,1] == "INPUTREFS" :
            VarRule2= df.iloc[i, 2] 
            DataType_Chenk =df.iloc[i,3] 
            jc_name = df.iloc[i,4]
            Instance_Val = df.iloc[i, 0] 
            substring = Project_name + "_" 
            inst_main = Instance_Val.replace(substring,"")
            value1 = inst_main.split("_")
            value_Split = value1[0]
           # print(value_Split)

            if ((icd_rule1 in VarRule2 or icd_rule2 in VarRule2) and not VarRule2.startswith(("SB", "SR","HR","HB","LB","Plus","XR","XP","input","output","v_build","v_dischar","FLT","HV","APC","K")) and ("BIO" not in Instance_Val and "MPU" not in Instance_Val)):
                Rule2Result=icd.ICD_Check(VarRule2,value_Split,DataType_Chenk)
                #print(Rule2Result)

                if Rule2Result != None :
                    Split_Var2 = Rule2Result.split("_")[1]
                    Split_Var1 = Rule2Result.split("_")[0]
                else:
                    Split_Var1 = "NOK"
                    Split_Var2 = "NOK"

                Split_Var3 = VarRule2.split("_")[1]

                if Split_Var1 == "Done" and df.iloc[i,6]== "Junctioned":           
                    JC_Var = jc_name.split("/")
                    comp_name = JC_Var[-1]
                   # print(comp_name)
                    if Split_Var3 in df.iloc[i,4] : #implement the == not in check for the instance also 
                        if  Split_Var2 == DataType_Chenk:
                            df.iloc[i,5] ="Pass"
                            df.iloc[i,7] ="Rule#2: ICD_Rule"
                            df.iloc[i,8] = "Check Done"
                            df.iloc[i,9] = "Rule#2"
                        else:
                            #print(Split_Var2)
                            df.iloc[i,5] ="Fail" 
                            df.iloc[i,7] ="Rule#2: ICD_Rule Data_Type Mismatch DataType ="+Split_Var2
                            df.iloc[i,8] = "Check Done"
                            df.iloc[i,9] = "Rule#2"                        
                    else :
                        df.iloc[i,5] ="Fail"
                        df.iloc[i,7] ="Rule#2: ICD_Rule Junctioned with a wrong variable"
                        df.iloc[i,8] = "Check Done"    
                        df.iloc[i,9] = "Rule#2"  

                elif  Split_Var1 == "Done" and df.iloc[i,6]== "Not Junctioned" :
                    df.iloc[i,5] ="Fail"
                    df.iloc[i,7] ="Rule#2: ICD_Rule Should be Junctioned"
                    df.iloc[i,8] = "Check Done"
                    df.iloc[i,9] = "Rule#2"

                elif Split_Var1 == "NOK":
                    df.iloc[i,5] ="Fail"
                    df.iloc[i,7] ="Rule#2: ICD_Rule Missing Varible in ICD"
                    df.iloc[i,8] ="Check Done"
                    df.iloc[i,9] = "Rule#2"
                elif Split_Var1 == "Done1":
                    df.iloc[i,5] ="Fail"
                    df.iloc[i,7] ="Rule#2: ICD_Rule Wrong Naming"
                    df.iloc[i,8] ="Check Done"
                    df.iloc[i,9] = "Rule#2"
                #elif Split_Var1 == ""
            if ("MPU" == value_Split and df.iloc[i,8] !="Check Done" and df.iloc[i,1] == "INPUTREFS" ):
                VarRule2
                MPU_Split = VarRule2.split("_")

                MPU_mainvar = MPU_Split[1]
                #print(MPU_mainvar)
                if ((icd_rule1 in VarRule2 or icd_rule2 in VarRule2) and not VarRule2.startswith(("SB", "SR","HR","HB","LB","Plus","XR","XP","input","output","v_build","v_dischar","FLT","HV","APC","LI","LO","K"))):
                    Rule2ResultSub=icd.MPU_Check(VarRule2)
                    if Rule2ResultSub != None :
                        Split_Var2 = Rule2ResultSub.split("_")[1]
                        Split_Var1 = Rule2ResultSub.split("_")[0]
                    else:
                        Split_Var1 = "NOK"
                        Split_Var2 = "NOK"
                    if Split_Var1 == "Done" and df.iloc[i,6]== "Junctioned" and ("BIO" not in Instance_Val):
                       # print("Hi")
                        if MPU_mainvar in df.iloc[i,4] :
                            if  Split_Var2 == DataType_Chenk:
                                #ccprint("done")
                                df.iloc[i,5] ="Pass"
                                df.iloc[i,7] ="Rule#2: ICD_Rule"
                                df.iloc[i,8] = "Check Done"
                                df.iloc[i,9] = "Rule#2"
                            else:
                            #print(Split_Var2)
                                df.iloc[i,5] ="Fail" 
                                df.iloc[i,7] ="Rule#2: ICD_Rule Data_Type Mismatch DataType ="+Split_Var2
                                df.iloc[i,8] = "Check Done" 
                                df.iloc[i,9] = "Rule#2"
                        else:
                           # print(Split_Var3 +"main" + df.iloc[i,4])
                            df.iloc[i,5] ="Fail"
                            df.iloc[i,7] ="Rule#2: ICD_Rule Wrong Junction"
                            df.iloc[i,8] ="Check Done" 
                            df.iloc[i,9] = "Rule#2"
                    elif  Split_Var1 == "Done" and df.iloc[i,6]== "Not Junctioned" :
                        df.iloc[i,5] ="Fail"
                        df.iloc[i,7] ="Rule#2: ICD_Rule Should be Junctioned"
                        df.iloc[i,8] = "Check Done"
                        df.iloc[i,9] = "Rule#2"

                    elif Split_Var1 == "NOK":
                        df.iloc[i,5] ="Fail"
                        df.iloc[i,7] ="Rule#2: ICD_Rule Missing Varible in ICD"
                        df.iloc[i,8] ="Check Done"
                        df.iloc[i,9] = "Rule#2"

                    elif Split_Var1 == "Done1":
                        df.iloc[i,5] ="Fail"
                        df.iloc[i,7] ="Rule#2: ICD_Rule Wrong Naming"
                        df.iloc[i,8] ="Check Done"
                        df.iloc[i,9] = "Rule#2"










        #print(VarRule2+"!!!") 


        #if Rule2Result == "Done" and :


        #print (a)    
    # Write the updated DataFrame to the same Excel file
    df.to_excel(r'C:\Users\Public\usercode.xlsx', index=False)
    tableresult()
    graphres()

