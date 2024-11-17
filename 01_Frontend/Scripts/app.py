import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

#from MDD_Checker import MDDChecker_Start

# from home import JunctionCheck as CheckJunctions
# from Wizard_CSV import WizardFile_CSV as wizard

LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs) 

        #self.geometry("800x600")
        self.title("OneLab")
        
        # creating a container
        container = tk.Frame(self, bg="#FC8F54")
        container.pack(side="top", fill = "none", expand = True)

        # initializing frames to an empty array
        self.frames = {} 

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartMenu, Modelization, JunctionChecker, Wizard_csvCreator, TestLab, V0_Model_Creator):

            frame = F(container, self)

            # initializing frame of that object from
            # OneLab, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(StartMenu)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# first window frame OneLab

class StartMenu(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg="#FC8F54")        

        ##################### Modelization ################################
        button1 = ttk.Button(self, text ="Modelization",
        command = lambda : controller.show_frame(Modelization),width=20)
    
        # putting the button in its place by
        # using grid
        button1.place(relx = 0.5, rely = 0.1, anchor="center")

        ##################### Junction Checker ################################
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Junction Checker",
        command = lambda : controller.show_frame(JunctionChecker),width=20)
    
        # putting the button in its place by
        # using grid
        button2.place(relx = 0.5, rely = 0.25, anchor="center")

        ##################### Wizard csv Creator ################################
         ## button to show frame 2 with text layout2
        button3 = ttk.Button(self, text ="Wizard csv Creator",
        command = lambda : controller.show_frame(Wizard_csvCreator),width=20)
        
        # putting the button in its place by
        # using grid
        button3.place(relx = 0.5, rely = 0.4, anchor="center")

        ##################### TestLab ################################
         ## button to show frame 2 with text layout2
        button4 = ttk.Button(self, text ="TestLab",
        command = lambda : controller.show_frame(TestLab),width=20)
    
        # putting the button in its place by
        # using grid
        button4.place(relx = 0.5, rely = 0.55, anchor="center")

        ##################### V0 Model Creator ################################
         ## button to show frame 2 with text layout2
        button4 = ttk.Button(self, text ="Create V0 Model",
        command = lambda : controller.show_frame(V0_Model_Creator),width=20)
    
        # putting the button in its place by
        # using grid
        button4.place(relx = 0.5, rely = 0.7, anchor="center")

        
# Modelization page
class Modelization(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)

        # Add MDD and Ucdef file upload functionality

        #MDD path label and browse button functionality
        mdd_label = ttk.Label(self, text="MDD File:")
        mdd_label.grid(row=0, column=0, padx=10, pady=10)

        mdd_path_var = tk.StringVar()

        def browse_mdd():
            file_path = filedialog.askopenfilename(title="Select MDD File", filetypes=[("Excel", "*.xlsx"),("XML Files", "*.xml"), ("CSV Files", "*.csv")])
            if file_path:
                mdd_path_var.set(file_path)

        mdd_browse_button = ttk.Button(self, text="Browse", command=browse_mdd)
        mdd_browse_button.grid(row=0, column=1, padx=10, pady=10)

        mdd_path_entry = ttk.Entry(self, textvariable=mdd_path_var, state="readonly", width = 50)
        mdd_path_entry.grid(row=0, column=2, padx=10, pady=10)

        #ucDef path label and browse button functionality
        ucdef_label = ttk.Label(self, text="Ucdef File:")
        ucdef_label.grid(row=1, column=0, padx=10, pady=10)

        ucdef_path_var = tk.StringVar()

        def browse_ucdef():
            file_path = filedialog.askopenfilename(title="Select Simulatio ucDef File", filetypes=[("Ucdef Files", "*.ucdef")])
            if file_path:
                ucdef_path_var.set(file_path)

        ucdef_browse_button = ttk.Button(self, text="Browse", command=browse_ucdef)
        ucdef_browse_button.grid(row=1, column=1, padx=10, pady=10)

        ucdef_path_entry = ttk.Entry(self, textvariable=ucdef_path_var, state="readonly", width = 50)
        ucdef_path_entry.grid(row=1, column=2, padx=10, pady=10)

        #ICD path label and browse button functionality
        ICD_label = ttk.Label(self, text="ICD:")
        ICD_label.grid(row=2, column=0, padx=10, pady=10)

        ICD_path_var = tk.StringVar()

        def browse_ICD():
            file_path = filedialog.askopenfilename(title="Select ICD File", filetypes=[("Excel", "*.xlsx"),("XML Files", "*.xml"), ("CSV Files", "*.csv")])
            if file_path:
                ICD_path_var.set(file_path)

        ICD_browse_button = ttk.Button(self, text="Browse", command=browse_ICD)
        ICD_browse_button.grid(row=2, column=1, padx=10, pady=10)

        ICD_path_entry = ttk.Entry(self, textvariable=ICD_path_var, state="readonly", width = 50)
        ICD_path_entry.grid(row=2, column=2, padx=10, pady=10)

        #Model_ucDef path label and browse button functionality
        model_label = ttk.Label(self, text="Model UcDef:")
        model_label.grid(row=3, column=0, padx=10, pady=10)

        model_path_var = tk.StringVar()

        def browse_model_ucdef():
            file_path = filedialog.askopenfilename(title="Select Model ucDef File", filetypes=[("Ucdef Files", "*.ucdef")])
            if file_path:
                model_path_var.set(file_path)

        model_browse_button = ttk.Button(self, text="Browse", command=browse_model_ucdef)
        model_browse_button.grid(row=3, column=1, padx=10, pady=10)

        model_path_entry = ttk.Entry(self, textvariable=ICD_path_var, state="readonly", width = 50)
        model_path_entry.grid(row=3, column=2, padx=10, pady=10)

        #Submit Data path functionality
        def SubmitData():
            ucDef_path = ucdef_path_var.get()
            mdd_path = mdd_path_var.get()
            ICD_path = ICD_path_var.get()
            Model_path = model_path_var.get()

            self.submit_modelisation_data(ucDef_path,mdd_path,ICD_path,Model_path)

        # Add submit button
        submit_button = ttk.Button(self, text="Submit", command=SubmitData)
        #submit_button = ttk.Button(frame, text="Submit", command=lambda i = ucdef_path_var.get() ,j = mdd_path_var.get() :self.submit_data(i,j))
        submit_button.grid(row=4, column=2, pady=10)

        # home button to go back to start page
        button1 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartMenu))
    
        button1.grid(row = 4, column = 1,  pady = 10)

    def submit_modelisation_data(self,ucDef_path,mdd_path,ICD_path,Model_path):
        # Submit data functionality
        if not ucDef_path or not mdd_path:
            self.show_report_popup("Warning","Please check the file paths again")
            return
        report = MDDChecker_Start(mdd_path,ucDef_path,ICD_path,Model_path)
        self.show_report_popup("Report",report)
        pass

    def show_report_popup(self, title = "Report Popup", msg = "This is the Report Popup"):
        # Open a popup displaying a directory (customization can be done later)
        report_popup = tk.Toplevel(self)
        report_popup.title(title)

        # Example: Display a label in the popup
        report_label = ttk.Label(report_popup, text= msg)
        report_label.pack(pady=10)

# Junction Checker page
class JunctionChecker(tk.Frame): 
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        #cfg file path label and browse button functionality
        cfg_label = ttk.Label(self, text="usecode.cfg:")
        cfg_label.grid(row=0, column=0, padx=10, pady=10)

        cfg_path_var = tk.StringVar()

        def browse_usercode_cfg():
            file_path = filedialog.askopenfilename(title="Select usecode.cfg File", filetypes=[("CFG file(.cfg)", "*.cfg"),(".xml", "*.xml"), ("CSV Files", "*.csv")])
            if file_path:
                cfg_path_var.set(file_path)

        cfg_browse_button = ttk.Button(self, text="Browse", command=browse_usercode_cfg)
        cfg_browse_button.grid(row=0, column=1, padx=10, pady=10)

        cfg_path_entry = ttk.Entry(self, textvariable=cfg_path_var, state="readonly", width = 50)
        cfg_path_entry.grid(row=0, column=2, padx=10, pady=10)

        #MAster ICD path label and browse button functionality
        master_ICD_label = ttk.Label(self, text="Master ICD:")
        master_ICD_label.grid(row=1, column=0, padx=10, pady=10)

        master_ICD_var = tk.StringVar()

        def browse_master_ICD():
            file_path = filedialog.askopenfilename(title="Select Master ICD File", filetypes=[(".xlsx", "*.xlsx"),(".xls","*.xls")])
            if file_path:
                master_ICD_var.set(file_path)

        master_ICD_browse_button = ttk.Button(self, text="Browse", command=browse_master_ICD)
        master_ICD_browse_button.grid(row=1, column=1, padx=10, pady=10)

        master_ICD_path_entry = ttk.Entry(self, textvariable=master_ICD_var, state="readonly", width = 50)
        master_ICD_path_entry.grid(row=1, column=2, padx=10, pady=10)

        #ucDef path label and browse button functionality
        ucdef_label = ttk.Label(self, text="Simulatio ucDef:")
        ucdef_label.grid(row=2, column=0, padx=10, pady=10)

        ucdef_path_var = tk.StringVar()

        def browse_ucdef():
            file_path = filedialog.askopenfilename(title="Select ucdef File", filetypes=[("Ucdef Files", "*.ucdef")])
            if file_path:
                ucdef_path_var.set(file_path)

        ucdef_browse_button = ttk.Button(self, text="Browse", command=browse_ucdef)
        ucdef_browse_button.grid(row=2, column=1, padx=10, pady=10)

        ucdef_path_entry = ttk.Entry(self, textvariable=ucdef_path_var, state="readonly", width = 50)
        ucdef_path_entry.grid(row=2, column=2, padx=10, pady=10)
        
        #Prefix of Instance label and text entry field
        instance_label = ttk.Label(self, text="Project Name:")
        instance_label.grid(row=3, column=0, padx=10, pady=10)

        instance_field = ttk.Entry(self, width=50)
        instance_field.grid(row=3, column=2, padx=10, pady=10)

        #BRIO instance name label and text entry field
        brio_instance_label = ttk.Label(self, text="BRIO instance:")
        brio_instance_label.grid(row=4, column=0, padx=10, pady=10)

        brio_instance_field = ttk.Entry(self, width=50)
        brio_instance_field.grid(row=4, column=2, padx=10, pady=10)

        #Fetch data to submit to the checking function
        def SubmitData():
            master_ICD_path = master_ICD_var.get()
            cfg_path = cfg_path_var.get()
            ucdef_path = ucdef_path_var.get()
            instancePrefix = instance_field.get()
            brio_instance = brio_instance_field.get()
            self.submit_junctionChecker_data(cfg_path,master_ICD_path,ucdef_path,instancePrefix,brio_instance)

        # Add submit button
        submit_button = ttk.Button(self, text="Submit", command=SubmitData)
        #submit_button = ttk.Button(frame, text="Submit", command=lambda i = ucdef_path_var.get() ,j = mdd_path_var.get() :self.submit_data(i,j))
        submit_button.grid(row=5, columnspan=3, pady=10)

        # home button to go back to start page
        button1 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartMenu))
    
        button1.grid(row = 5, column = 1,  pady = 10)

        def submit_junctionChecker_data(self,cfg_path,master_ICD_path,ucdef_path,instancePrefix,brio_instance):
            # Submit data functionality
            if not ucdef_path:
                self.show_report_popup("Warning","Please check the file paths again")
                return
            CheckJunctions(cfg_path,master_ICD_path,ucdef_path,instancePrefix,brio_instance)
            # self.show_report_popup("Report",report)
            pass

        def show_report_popup(self, title = "Report Popup", msg = "This is the Report Popup"):
            # Open a popup displaying a directory (customization can be done later)
            report_popup = tk.Toplevel(self)
            report_popup.title(title)

            # Example: Display a label in the popup
            report_label = ttk.Label(report_popup, text= msg)
            report_label.pack(pady=10)

# Wizard csv Creator page
class Wizard_csvCreator(tk.Frame): 
    def __init__(self, parent, controller):
 
        tk.Frame.__init__(self, parent)
 
        #cfg file path label and browse button functionality
        cfg_label = ttk.Label(self, text="Controller .Ucdef_File:")
        cfg_label.grid(row=0, column=0, padx=10, pady=10)
 
        controller_path_var = tk.StringVar()
 
        def browse_usercode_cfg():
            file_path = filedialog.askopenfilename(title="Select usecode.cfg File", filetypes=[("Ucdef Files", "*.ucdef")])
            if file_path:
                controller_path_var.set(file_path)
 
        cfg_browse_button = ttk.Button(self, text="Browse", command=browse_usercode_cfg)
        cfg_browse_button.grid(row=0, column=1, padx=10, pady=10)
 
        cfg_path_entry = ttk.Entry(self, textvariable=controller_path_var, state="readonly", width = 50)
        cfg_path_entry.grid(row=0, column=2, padx=10, pady=10)
       
 
        #cfg file path label and browse button functionality
        cfg_label = ttk.Label(self, text="Env .Ucdef_File:")
        cfg_label.grid(row=1, column=0, padx=10, pady=10)
 
        ENV_path_var = tk.StringVar()
 
        def browse_usercode_cfg():
            file_path = filedialog.askopenfilename(title="Select usecode.cfg File", filetypes=[("Ucdef Files", "*.ucdef")])
            if file_path:
                ENV_path_var.set(file_path)
 
        cfg_browse_button = ttk.Button(self, text="Browse", command=browse_usercode_cfg)
        cfg_browse_button.grid(row=1, column=1, padx=10, pady=10)
 
        cfg_path_entry = ttk.Entry(self, textvariable=ENV_path_var, state="readonly", width = 50)
        cfg_path_entry.grid(row=1, column=2, padx=10, pady=10)
 
        #MAster ICD path label and browse button functionality
       
        #Prefix of Instance label and text entry field
        instance_label = ttk.Label(self, text="Instance name of Controller :")
        instance_label.grid(row=3, column=0, padx=10, pady=10)
 
        Controller_inst = ttk.Entry(self, width=50)
        Controller_inst.grid(row=3, column=2, padx=10, pady=10)
 
        #BRIO instance name label and text entry field
        brio_instance_label = ttk.Label(self, text="Instance name of ENV :")
        brio_instance_label.grid(row=4, column=0, padx=10, pady=10)
 
        ENV_inst = ttk.Entry(self, width=50)
        ENV_inst.grid(row=4, column=2, padx=10, pady=10)
 
        #Fetch data to submit to the checking function
        def SubmitData():
            #master_ICD_path = master_ICD_var.get()
            Controller = controller_path_var.get()
            ENV = ENV_path_var.get()
            Controller_inst1 = Controller_inst.get()
            ENV_inst1 = ENV_inst.get()
            self.submit_wizard_data(Controller,ENV,Controller_inst1,ENV_inst1)
 
        # Add submit button
        submit_button = ttk.Button(self, text="Submit", command=SubmitData)
        #submit_button = ttk.Button(frame, text="Submit", command=lambda i = ucdef_path_var.get() ,j = mdd_path_var.get() :self.submit_data(i,j))
        submit_button.grid(row=5, columnspan=3, pady=10)
 
        # home button to go back to start page
        button1 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartMenu))
   
        button1.grid(row = 5, column = 1,  pady = 10)
 
    def submit_wizard_data(self,Controller,ENV,Controller_inst1,ENV_inst1):
        #Submit data functionality
        if not Controller:
            self.show_report_popup("Warning","Please check the file paths again")
            return
        wizard(Controller,ENV,Controller_inst1,ENV_inst1)

# TestLab page
class TestLab(tk.Frame): 
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        # home button to go back to start page
        button1 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartMenu))
    
        button1.grid(row = 4, column = 1,  pady = 10)

#V0 Model Creator
class V0_Model_Creator(tk.Frame): 
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        # home button to go back to start page
        button1 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartMenu))
    
        button1.grid(row = 4, column = 1,  pady = 10)

# Driver Code
app = tkinterApp()
app.mainloop()
