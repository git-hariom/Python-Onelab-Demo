import pandas as pd
# Define a global dictionary that will hold all the other dictionaries
excel_dict = {}

all_sheet_dicts = {}
txt12 = []
# Define a function to read the Excel file and create dictionaries for each sheet
def read_excel(icd_path):
    global excel_dict
    global all_sheet_dicts
    subrule1 = 'smart'
    subtule2 = 'spare'
    try:
        # read the excel file into a pandas DataFrame object
        excel_file = pd.ExcelFile(icd_path)
        # loop through each sheet and convert to a dictionary
        for sheet_name in excel_file.sheet_names:
            # read the sheet into a pandas DataFrame object
            sheet_df = pd.read_excel(excel_file,sheet_name=sheet_name)
            # convert the DataFrame to a dictionary
            sheet_dict = sheet_df.to_dict('records')
            # create a dictionary to store signal names and their sender equipment
            value_dict = {}
            # loop through each row in the sheet and populate the signal name and sender equipment dictionary
            for row in sheet_dict:
                signal_name = str(row.get('Signal Name', ''))
                if signal_name != "nan" and subrule1 not in signal_name and subtule2 not in signal_name:
                    value_dict[signal_name] = str(row.get('Complex Network Type', ''))
                
            # store the signal name and sender equipment dictionary for this sheet in the global dictionary
            all_sheet_dicts[sheet_name] = value_dict
        # store the global dictionary of all sheets in memory
        excel_dict = all_sheet_dicts
        #with open('erput.txt', 'w') as file:
           # file.write(str(excel_dict))
        print("Excel file loaded successfully.")
        
        return "Reading of Master Icd is Done"
    except FileNotFoundError:
        print("Error: File not found.")
def ICD_Check(Var, instance, data_type):
    global excel_dict
    #with open('excelpo.txt','w') as file:
     #       file.write(str(excel_dict))
    local = {}
    convert =""
   # Split_Var = instance
    #recipient_value = Split_Var.split("_")[-2] #should be changed to last before string 
    string_with_numbers = instance
    
    string_without_numbers = ''.join([i for i in string_with_numbers if not i.isdigit()])
    main_var =Var
    icd_var = main_var.replace("__0","")
    ut_datatype = data_type
    #sheet_ICD = instance 
    ##print(sheet_ICD)
    inst = string_without_numbers
    #print(string_with_numbers+"+"+Split_Var+"+"+inst)
    Result=''
    yj=''
    if "_" in icd_var:
        value_split = str(icd_var.split("_")[1])

    else:
        value_split = str(icd_var)
    #print(value_split)
    #sender_equipment = excel_dict[inst][icd_var]
    #print(sender_equipment)
    #sender_equipment = excel_dict[sheet_ICD][icd_var]
    for key in excel_dict.keys():
        if  key == inst:
            #print ("Yes")
            local = excel_dict[inst]
            for subkeys in local.keys():
                ##print(subkeys)
                if value_split.lower() in subkeys.lower():
                    #print("Yes2")
                    if value_split in subkeys:
                        yj = local[subkeys]
                        icd_split = yj.split("*")[0]
                        if icd_split =="CHARACTER8"  :
                            convert = "OPAQUE"
                        elif icd_split == "REAL32":
                            convert = "DOUBLE"
                        elif icd_split == "TIMEDATE48":
                            convert = "Not compatable"
                        else:
                            convert = "INT"
                    
                    #if convert == ut_datatype:
                    #print(convert + "+" + icd_split)
                        Result = "Done_"+convert 
                        return (Result)  
                    else:
                        Result = "Done1_wrong"
                        return (Result)
                    txt12.append(yj)
                    

                else:
                     Result = "NOK_Removed"#+Var
                     #return (Result)
                     continue
                
            
        else:
            continue
    
def MPU_Check(Var):
    global excel_dict
    #with open('excelpo.txt','w') as file:
     #       file.write(str(excel_dict))
    local = {}
    convert =""
    main_Var = Var
    Split_Var = main_Var.split("_")[1]
    Split_inst = main_Var.split("_")[0]
    inst = ''.join([i for i in Split_inst if not i.isdigit()])
    icd_vard = Split_Var.replace("__0","")
    Result=''
    yj=''
    for key in excel_dict.keys():
        if  key == inst:
            #print ("Yes")
            local = excel_dict[inst]
            for subkeys in local.keys():
                ##print(subkeys)
                if icd_vard.lower() in subkeys.lower():
                    if icd_vard in subkeys:
                        #print("Yes2")

                        yj = local[subkeys]
                        icd_split = yj.split("*")[0]
                        if icd_split =="CHARACTER8"  :
                            convert = "OPAQUE"
                        elif icd_split == "REAL32":
                            convert = "DOUBLE"
                        elif icd_split == "TIMEDATE48":
                            convert = "Not conpatable"
                        else:
                            convert = "INT"
                        #if convert == ut_datatype:
                        #print(convert + "+" + icd_split)
                        Result = "Done_"+convert   
                        txt12.append(yj)
                        return (Result)
                    else:
                        Result = "Done1_wrong"
                        return (Result)
                else:
                     Result = "NOK_Removed"#+Var
                     #return (Result)
                     continue
                
            
        else:
            continue

                 
   #for key in excel_dict.keys():
       #  #print(key+'\n')
    