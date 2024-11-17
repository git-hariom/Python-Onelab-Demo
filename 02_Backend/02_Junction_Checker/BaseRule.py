def var_check(variable_name):
    a = variable_name
    if a.startswith("HMI") or a.startswith("OBS"): # to check the varible contains any name which starts with the name HMI
        #print("True" + a)
        b = "True"
    else:
       # print("False" + a)
        b = "False"
    return b