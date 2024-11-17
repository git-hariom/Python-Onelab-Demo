import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

#from simu_CB_Checker import StartChecker as Simu_CB_Check
#from home import JunctionCheck

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alstom Transportation App")

        # Set the window size and position it in the center
        window_width = 800
        window_height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        # Create a custom theme
        self.style = ttk.Style()
        self.style.theme_create("AlstomTheme", parent="alt", settings={
            "TButton": {
                "configure": {"background": "#0080C0", "foreground": "white", "padding": 5, "font": ('Helvetica', 12)},
                "map": {"background": [("active", "#005080")]}
            },
            "TLabel": {
                "configure": {"foreground": "#0080C0", "font": ('Helvetica', 12)}
            }
        })
        self.style.theme_use("AlstomTheme")

        # Create the main page with options for Modelization
        modelization_button = ttk.Button(self.root, text="Modelisation", command=lambda: self.show_Modelisation_page())
        modelization_button.place(relx=0.5, rely=0.45, anchor="center")

        modelization_button = ttk.Button(self.root, text="PC_Cosim Jnc Check", command=lambda: self.show_Junction_page())
        modelization_button.place(relx=0.5, rely=0.55, anchor="center")

        # Initialize variables to store references to the second and third pages
        self.second_page = None
        self.file_page = None

    def show_Modelisation_page(self):
        # Hide the main page
        self.root.withdraw()

        # Create a new window (Toplevel) for the file page
        file_page = tk.Toplevel(self.root)
        file_page.title(f"Modelisation Page")

        # Set the window size and position it in the center
        window_width = 800
        window_height = 600
        screen_width = file_page.winfo_screenwidth()
        screen_height = file_page.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        file_page.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        # Apply the custom theme to the file page
        file_page.style = ttk.Style(file_page)
        file_page.style.theme_use("AlstomTheme")

        # Create a frame to hold the content
        frame = tk.Frame(file_page, padx=20, pady=20)
        frame.pack(expand=True, fill="both")

        # Create a menu bar
        menu_bar = tk.Menu(file_page)
        file_page.config(menu=menu_bar)

        # Add "Back", "Home", "Report", and "Download" buttons to the menu bar
        menu_bar.add_command(label="Back", command=lambda: self.show_main_page(file_page))
        menu_bar.add_command(label="Home", command=self.show_main_page)
        menu_bar.add_command(label="Report", command=self.show_report_popup)
        menu_bar.add_command(label="Download", command=self.download_data)

        # Add MDD and Ucdef file upload functionality
        mdd_label = ttk.Label(frame, text="MDD File:")
        mdd_label.grid(row=0, column=0, padx=10, pady=10)

        mdd_path_var = tk.StringVar()

        def browse_mdd():
            file_path = filedialog.askopenfilename(title="Select MDD File", filetypes=[("Excel", "*.xlsx"),("XML Files", "*.xml"), ("CSV Files", "*.csv")])
            if file_path:
                mdd_path_var.set(file_path)

        mdd_browse_button = ttk.Button(frame, text="Browse", command=browse_mdd)
        mdd_browse_button.grid(row=0, column=1, padx=10, pady=10)

        mdd_path_entry = ttk.Entry(frame, textvariable=mdd_path_var, state="readonly")
        mdd_path_entry.grid(row=0, column=2, padx=10, pady=10)

        ucdef_label = ttk.Label(frame, text="Ucdef File:")
        ucdef_label.grid(row=1, column=0, padx=10, pady=10)

        ucdef_path_var = tk.StringVar()

        def browse_ucdef():
            file_path = filedialog.askopenfilename(title="Select Ucdef File", filetypes=[("Ucdef Files", "*.ucdef")])
            if file_path:
                ucdef_path_var.set(file_path)

        ucdef_browse_button = ttk.Button(frame, text="Browse", command=browse_ucdef)
        ucdef_browse_button.grid(row=1, column=1, padx=10, pady=10)

        ucdef_path_entry = ttk.Entry(frame, textvariable=ucdef_path_var, state="readonly")
        ucdef_path_entry.grid(row=1, column=2, padx=10, pady=10)

        def SubmitData():
            ucDef_path = ucdef_path_var.get()
            mdd_path = mdd_path_var.get()
            self.submit_modelisation_data(ucDef_path,mdd_path)

        # Add submit button
        submit_button = ttk.Button(frame, text="Submit", command=SubmitData)
        #submit_button = ttk.Button(frame, text="Submit", command=lambda i = ucdef_path_var.get() ,j = mdd_path_var.get() :self.submit_data(i,j))
        submit_button.grid(row=2, columnspan=3, pady=10)

    def show_Junction_page(self):
        # Hide the main page
        self.root.withdraw()

        # Create a new window (Toplevel) for the file page
        file_page = tk.Toplevel(self.root)
        file_page.title(f"PC_Cosim Junction Checker")

        # Set the window size and position it in the center
        window_width = 800
        window_height = 600
        screen_width = file_page.winfo_screenwidth()
        screen_height = file_page.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        file_page.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        # Apply the custom theme to the file page
        file_page.style = ttk.Style(file_page)
        file_page.style.theme_use("AlstomTheme")

        # Create a frame to hold the content
        frame = tk.Frame(file_page, padx=20, pady=20)
        frame.pack(expand=True, fill="both")

        # Create a menu bar
        menu_bar = tk.Menu(file_page)
        file_page.config(menu=menu_bar)

        # Add "Back", "Home", "Report", and "Download" buttons to the menu bar
        menu_bar.add_command(label="Back", command=lambda: self.show_main_page(file_page))
        menu_bar.add_command(label="Home", command=self.show_main_page)
        menu_bar.add_command(label="Report", command=self.show_report_popup)
        menu_bar.add_command(label="Download", command=self.download_data)

        # Add MDD and Ucdef file upload functionality
        cfg_label = ttk.Label(frame, text="usecode.cfg:")
        cfg_label.grid(row=0, column=0, padx=10, pady=10)

        cfg_path_var = tk.StringVar()

        def browse_usercode_cfg():
            file_path = filedialog.askopenfilename(title="Select usecode.cfg File", filetypes=[("CFG file(.cfg)", "*.cfg"),(".xml", "*.xml"), ("CSV Files", "*.csv")])
            if file_path:
                cfg_path_var.set(file_path)

        cfg_browse_button = ttk.Button(frame, text="Browse", command=browse_usercode_cfg)
        cfg_browse_button.grid(row=0, column=1, padx=10, pady=10)

        cfg_path_entry = ttk.Entry(frame, textvariable=cfg_path_var, state="readonly")
        cfg_path_entry.grid(row=0, column=2, padx=10, pady=10)

        master_ICD_label = ttk.Label(frame, text="Master ICD:")
        master_ICD_label.grid(row=1, column=0, padx=10, pady=10)

        master_ICD_var = tk.StringVar()

        def browse_master_ICD():
            file_path = filedialog.askopenfilename(title="Select Master ICD File", filetypes=[(".xlsx", "*.xlsx"),(".xls","*.xls")])
            if file_path:
                master_ICD_var.set(file_path)

        master_ICD_browse_button = ttk.Button(frame, text="Browse", command=browse_master_ICD)
        master_ICD_browse_button.grid(row=1, column=1, padx=10, pady=10)

        master_ICD_path_entry = ttk.Entry(frame, textvariable=master_ICD_var, state="readonly")
        master_ICD_path_entry.grid(row=1, column=2, padx=10, pady=10)
        
        text_field_label = ttk.Label(frame, text="Prefix of instance:")
        text_field_label.grid(row=2, column=0, padx=10, pady=10)

        text_field = ttk.Entry(frame, width=50)
        text_field.grid(row=2, column=2, padx=10, pady=10)

        def SubmitData():
            master_ICD_path = master_ICD_var.get()
            cfg_path = cfg_path_var.get()
            text = text_field.get()
            self.submit_junction_data(cfg_path,master_ICD_path,text)

        # Add submit button
        submit_button = ttk.Button(frame, text="Submit", command=SubmitData)
        #submit_button = ttk.Button(frame, text="Submit", command=lambda i = ucdef_path_var.get() ,j = mdd_path_var.get() :self.submit_data(i,j))
        submit_button.grid(row=3, columnspan=3, pady=10)

    def show_main_page(self, window=None):
        # Close the current window
        if window:
            window.destroy()

        # Re-show the main page
        self.root.deiconify()

    def show_report_popup(self, title = "Report Popup", msg = "This is the Report Popup"):
        # Open a popup displaying a directory (customization can be done later)
        report_popup = tk.Toplevel(self.root)
        report_popup.title(title)

        # Example: Display a label in the popup
        report_label = ttk.Label(report_popup, text= msg)
        report_label.pack(pady=10)

    def download_data(self):
        # Placeholder for download functionality
        pass

    def submit_modelisation_data(self,ucDef_path,mdd_path):
        # Submit data functionality
        if not ucDef_path or not mdd_path:
            self.show_report_popup("Warning","Please check the file paths again")
            return
        report = Simu_CB_Check(ucDef_path,mdd_path)
        self.show_report_popup("Report",report)
        pass
    
    def submit_junction_data(self,cfg_path,master_icd_path,text):
        JunctionCheck(cfg_path,master_icd_path,text)
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
