import time
from DrissionPage import ChromiumPage, ChromiumOptions
from DrissionPage.common import By
import random
import string
import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
import datetime
import threading
import ctypes

class CloudflareBypasser:
    def __init__(self, driver: ChromiumPage):
        self.driver = driver
    def click_cycle(self):
        if self.driver.wait.ele_displayed('xpath://div/iframe', timeout=5):
            iframe = self.driver.get_frame('xpath://div/iframe')
            time.sleep(1)
            # Click on the CAPTCHA button if it's found inside the iframe
            iframe.ele("Verify you are human", timeout=5).click()

    def is_bypassed(self):
        title = self.driver.title.lower()
        return "just a moment" not in title

    def write_into_field(self, text, field_xpath):
        element = self.driver.ele(field_xpath)
        element.clear()
        element.input(text)

    def bypass(self):
        while not self.is_bypassed():
            print("Verification page detected. Trying to bypass...")
            self.click_cycle()
            time.sleep(3)

    def refresh_page(self):
        self.driver.refresh()

    def get_current_url(self):
        return self.driver.url
    
    
    def find_last_otp_paragraph(self):
        paragraphs = self.driver.get_tab(1).eles('tag:p')
        otp_paragraph = None
        for paragraph in paragraphs:
            text = paragraph.text
            if "The OTP for your application with VFS Global is" in text:
                otp_paragraph = paragraph
        return otp_paragraph
   

  
    def find_button_start(self):                        
     buttons = self.driver.eles(locator=('css selector', 'mat-button-wrapper'))  # Adjust the CSS selector as needed
     for button in buttons:
        button_text = button.text.strip()
        print(button_text)
        if button_text == "Start New Booking":
            return button
     return None  # Return None if button is not found



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
import datetime
import time
import threading

class AutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VfS bot GUI")
        self.root.configure(bg="grey")
        self.root.geometry("650x420")

        self.create_widgets()
        self.automation_thread = None
        self.stop_flag = threading.Event()
        
        self.configure_grid()

    def configure_grid(self):
        for i in range(10):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(5):
            self.root.grid_columnconfigure(j, weight=1)
    
    def create_widgets(self):
        self.start_button = tk.Button(self.root, text="Start", command=self.start_automation, bg="green", fg="white", font=("Arial", 12, "bold"))
        self.start_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_app, bg="red", fg="white", font=("Arial", 12, "bold"))
        self.quit_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        self.proxy_label = tk.Label(self.root, text="Select Proxy:", bg="grey", fg="white", font=("Arial", 10, "bold"))
        self.proxy_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        self.proxy_var = tk.StringVar()
        self.proxy_dropdown = ttk.Combobox(self.root, textvariable=self.proxy_var)
        self.proxy_dropdown['values'] = ("Proxy 1", "Proxy 2", "Proxy 3")
        self.proxy_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        self.type_label = tk.Label(self.root, text="Select Type:", bg="grey", fg="white", font=("Arial", 10, "bold"))
        self.type_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        
        self.type_var = tk.StringVar()
        self.type_dropdown = ttk.Combobox(self.root, textvariable=self.type_var)
        self.type_dropdown['values'] = ("Legalisation", "Long Stay")
        self.type_dropdown.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.user_info = {
            "Email VFS": tk.StringVar(),
            "Password VFS": tk.StringVar(),
            "Centre": tk.StringVar(),
            "Name": tk.StringVar(),
            "Last Name": tk.StringVar(),
            "Gender": tk.StringVar(),
            "Email": tk.StringVar(),
            "Date of Birth (dd/mm/yyyy)": tk.StringVar(),
            "Nationality": tk.StringVar(),
            "Passport Number": tk.StringVar(),
            "Passport Expiry Date (dd/mm/yyyy)": tk.StringVar(),
            "Contact Number (full)": tk.StringVar(),
            "Contact Number (only 3 digits)": tk.StringVar(),
            "Visa Type": self.type_var,
            "Email Gmail": tk.StringVar(),
            "Password Gmail": tk.StringVar(),
            "Refresh Time": tk.StringVar(),
            
        }

        self.create_user_info_inputs()
    def create_user_info_inputs(self):
        row_index = 3
        nationalities = [
            "Afghan", "Albanian", "Algerian", "American", "Andorran", "Angolan", "Antiguan", "Argentine", "Armenian", "Australian",
            "Austrian", "Azerbaijani", "Bahamian", "Bahraini", "Bangladeshi", "Barbadian", "Belarusian", "Belgian", "Belizean", "Beninese",
            "Bhutanese", "Bolivian", "Bosnian", "Botswanan", "Brazilian", "British", "Bruneian", "Bulgarian", "Burkinabe", "Burmese",
            "Burundian", "Cambodian", "Cameroonian", "Canadian", "Cape Verdean", "Central African", "Chadian", "Chilean", "Chinese", "Colombian",
            "Comoran", "Congolese", "Costa Rican", "Croatian", "Cuban", "Cypriot", "Czech", "Danish", "Djiboutian", "Dominican",
            "Dutch", "East Timorese", "Ecuadorean", "Egyptian", "Emirian", "Equatorial Guinean", "Eritrean", "Estonian", "Ethiopian", "Fijian",
            "Filipino", "Finnish", "French", "Gabonese", "Gambian", "Georgian", "German", "Ghanaian", "Greek", "Grenadian",
            "Guatemalan", "Guinea-Bissauan", "Guinean", "Guyanese", "Haitian", "Herzegovinian", "Honduran", "Hungarian", "Icelander", "Indian",
            "Indonesian", "Iranian", "Iraqi", "Irish", "Israeli", "Italian", "Ivorian", "Jamaican", "Japanese", "Jordanian",
            "Kazakhstani", "Kenyan", "Kittian and Nevisian", "Kuwaiti", "Kyrgyz", "Laotian", "Latvian", "Lebanese", "Liberian", "Libyan",
            "Liechtensteiner", "Lithuanian", "Luxembourger", "Macedonian", "Malagasy", "Malawian", "Malaysian", "Maldivian", "Malian", "Maltese",
            "Marshallese", "Mauritanian", "Mauritian", "Mexican", "Micronesian", "Moldovan", "Monacan", "Mongolian", "Moroccan", "Mosotho",
            "Motswana", "Mozambican", "Namibian", "Nauruan", "Nepalese", "New Zealander", "Nicaraguan", "Nigerian", "Nigerien", "North Korean",
            "Northern Irish", "Norwegian", "Omani", "Pakistani", "Palauan", "Panamanian", "Papua New Guinean", "Paraguayan", "Peruvian", "Polish",
            "Portuguese", "Qatari", "Romanian", "Russian", "Rwandan", "Saint Lucian", "Salvadoran", "Samoan", "San Marinese", "Sao Tomean",
            "Saudi", "Scottish", "Senegalese", "Serbian", "Seychellois", "Sierra Leonean", "Singaporean", "Slovakian", "Slovenian", "Solomon Islander",
            "Somali", "South African", "South Korean", "Spanish", "Sri Lankan", "Sudanese", "Surinamer", "Swazi", "Swedish", "Swiss",
            "Syrian", "Taiwanese", "Tajik", "Tanzanian", "Thai", "Togolese", "Tongan", "Trinidadian or Tobagonian", "Tunisian", "Turkish",
            "Tuvaluan", "Ugandan", "Ukrainian", "Uruguayan", "Uzbekistani", "Vatican", "Venezuelan", "Vietnamese", "Welsh", "Yemenite",
            "Zambian", "Zimbabwean"
            ]
        genders = ["Female", "Male", "Not specified"]

        grouped_inputs = [
            ("Centre" , "Refresh Time"),
            ("Email VFS", "Password VFS"),
            ("Name", "Last Name"),
            ("Gender", "Nationality"),
            ("Email", "Date of Birth (dd/mm/yyyy)"),
            ("Passport Number", "Passport Expiry Date (dd/mm/yyyy)"),
            ("Contact Number (full)", "Contact Number (only 3 digits)")
            ]
        
        centre= ["Alexendira" , "Cairo"]

        for group in grouped_inputs:
            for col, key in enumerate(group):
                label = tk.Label(self.root, text=key + ":", bg="grey", fg="white", font=("Arial", 9, "bold"))
                label.grid(row=row_index, column=col*2, padx=5, pady=3, sticky="e")

                if key == "Nationality":
                    self.nationality_dropdown = ttk.Combobox(self.root, textvariable=self.user_info[key], values=nationalities, width=20)
                    widget=self.nationality_dropdown
                elif key == "Gender":
                    self.gender_dropdown = ttk.Combobox(self.root, textvariable=self.user_info[key], values=genders, width=20)
                    widget=self.gender_dropdown
                elif "Password" in key:
                    widget = tk.Entry(self.root, textvariable=self.user_info[key], show="*", width=20)
                elif "Centre" in key : 
                    self.center_dropdown = ttk.Combobox(self.root, textvariable=self.user_info[key], values=centre, width=20)
                    widget=self.center_dropdown
                else:
                    widget = tk.Entry(self.root, textvariable=self.user_info[key], width=20)

                widget.grid(row=row_index, column=col*2+1, padx=5, pady=3, sticky="ew")

            row_index += 1

    # Add Gmail fields (initially hidden)
        self.gmail_label = tk.Label(self.root, text="Email Gmail:", bg="grey", fg="white", font=("Arial", 9, "bold"))
        self.gmail_label.grid(row=row_index, column=0, padx=10, pady=10, sticky="e")
        self.gmail_entry = tk.Entry(self.root, textvariable=self.user_info["Email Gmail"], width=20)
        self.gmail_entry.grid(row=row_index, column=1, padx=10, pady=10, sticky="ew")
        self.gmail_pw_label = tk.Label(self.root, text="Password Gmail:", bg="grey", fg="white", font=("Arial", 9, "bold"))
        self.gmail_pw_label.grid(row=row_index, column=2, padx=10, pady=10, sticky="e")
        self.gmail_pw_entry = tk.Entry(self.root, textvariable=self.user_info["Password Gmail"], show="*", width=20)
        self.gmail_pw_entry.grid(row=row_index, column=3, padx=10, pady=10, sticky="ew")

    #   Bind the type dropdown to a function that shows/hides Gmail fields
        self.type_dropdown.bind("<<ComboboxSelected>>", self.toggle_gmail_fields)

    def toggle_gmail_fields(self, event=None):
        if self.type_var.get() == "Long Stay":
            self.gmail_label.grid(row=len(self.user_info) + 1, column=0, padx=10, pady=10, sticky="e")
            self.gmail_entry.grid(row=len(self.user_info) + 1, column=1, padx=10, pady=10, sticky="ew")
            self.gmail_pw_label.grid(row=len(self.user_info) + 1, column=2, padx=10, pady=10, sticky="e")
            self.gmail_pw_entry.grid(row=len(self.user_info) + 1, column=3, padx=10, pady=10, sticky="ew")
        else:
            self.gmail_label.grid_remove()
            self.gmail_entry.grid_remove()
            self.gmail_pw_label.grid_remove()
            self.gmail_pw_entry.grid_remove()


    def start_automation(self):
        proxy = self.proxy_var.get()
        type_ = self.type_var.get()
        user_info = {key: var.get() for key, var in self.user_info.items()}
        
        if not proxy or not type_ :
            messagebox.showerror("Error", "All fields must be filled out")
            return

        if user_info['Visa Type'] == "Long Stay":
            if not all(user_info.values()):
                messagebox.showerror("Error", "All fields must be filled out")
                return
        elif user_info['Visa Type'] == "Legalisation":
            if user_info['Email Gmail'] or user_info['Password Gmail']:
                messagebox.showerror("Error", "Email Gmail and Password Gmail should be empty for Legalisation")
                return
        # Email format check for all email fields
        email_fields = ["Email", "Email VFS"]
        if type_ == "Long Stay":
            email_fields.append("Email Gmail")

        for email_field in email_fields:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", user_info[email_field]):
             messagebox.showerror("Error", f"Invalid email format for {email_field}")
             return

        try:
            dob = datetime.datetime.strptime(user_info["Date of Birth (dd/mm/yyyy)"], "%d/%m/%Y")
            passport_expiry = datetime.datetime.strptime(user_info["Passport Expiry Date (dd/mm/yyyy)"], "%d/%m/%Y")
        except ValueError:
         messagebox.showerror("Error", "Invalid date format. Use dd/mm/yyyy")
         return

        if passport_expiry.year <= 2024:
         messagebox.showwarning("Warning", "Passport is going to expire in 2024. Please change it.")
    
        contact_number_3_digits = user_info["Contact Number (only 3 digits)"]
        if not contact_number_3_digits.isdigit() or len(contact_number_3_digits) > 3 or len(contact_number_3_digits) < 2:
            messagebox.showerror("Error", "Contact Number (only 3 digits) must be exactly 3 or 2 digits")
            return

        contact_number_full = user_info["Contact Number (full)"]
        if not contact_number_full.isdigit():
            messagebox.showerror("Error", "Contact Number (full) must be all digits")
            return
        
        secondes_number= user_info["Refresh Time"]
        if not secondes_number.isdigit():
            messagebox.showerror("Error","Refresh Time is the number in seconds (number)")
            return

    # Convert selected index to value + 1 for gender, visa type, and nationality
        gender_index = self.gender_dropdown.current() + 1
        nationality_index = self.nationality_dropdown.current() + 1
        centre_index=self.center_dropdown.current() + 1
        refrechtime=int(user_info["Refresh Time"])
        user_info["Gender"] = gender_index
        user_info["Nationality"] = nationality_index
        user_info["Centre"]= centre_index
        self.user_info["Gender"] = gender_index
        self.user_info["Nationality"] = nationality_index
        user_info["Refresh Time"]=refrechtime
        self.switch_to_status_window()
        self.automation_thread = threading.Thread(target=self.run_automation_script, args=(proxy, type_, user_info))
        self.automation_thread.start()
    
    def switch_to_status_window(self):
        self.status_window = tk.Toplevel(self.root)
        self.status_window.title("Automation Status")
        self.status_window.geometry("400x300")
        
        self.status_text = tk.Text(self.status_window, wrap=tk.WORD, width=40, height=15)
        self.status_text.pack(padx=10, pady=10)
        
        self.stop_button = tk.Button(self.status_window, text="Stop", command=self.stop_automation, bg="red", fg="white")
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.retry_button = tk.Button(self.status_window, text="Retry", command=self.retry_automation, bg="yellow", fg="black")
        self.retry_button.pack(side=tk.RIGHT, padx=10, pady=10)
        
        self.root.withdraw()

    def stop_automation(self):
        if self.automation_thread and self.automation_thread.is_alive():
            self.stop_flag.set()
            self.update_status("Stopping automation...")
            # Forcefully terminate the thread if it doesn't stop within 5 seconds
            thread_id = self.automation_thread.ident
            time.sleep(5)
            if self.automation_thread.is_alive():
                self.terminate_thread(thread_id)
            self.update_status("Automation stopped.")
        else:
            self.update_status("No automation running.")
    def terminate_thread(self, thread_id):
        """Terminates a python thread from another thread."""
        if not thread_id:
            return
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), 0)
        
    def retry_automation(self):
        if self.automation_thread and self.automation_thread.is_alive():
            messagebox.showinfo("Info", "Automation is still running. Please stop it first.")
            return
        
        self.stop_flag.clear()
        self.status_text.delete(1.0, tk.END)
        self.update_status("Retrying automation...")
        
        proxy = self.proxy_var.get()
        type_ = self.type_var.get()
        user_info = {key: var.get() for key, var in self.user_info.items()}
        
        self.automation_thread = threading.Thread(target=self.run_automation_script, args=(proxy, type_, user_info))
        self.automation_thread.start()

    def update_status(self, message):
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        self.status_window.update()

    def run_automation_script(self, proxy, type_, user_info):
        try:
            self.update_status(f"Starting automation with proxy: {proxy}, type: {type_}")
            self.update_status("Filling in user information...")
            time.sleep(1)
            
            for key, value in user_info.items():
                self.update_status(f"{key}: {value}")
                time.sleep(0.5)
                if self.stop_flag.is_set():
                    self.update_status("Automation stopped.")
                    return
            
            # Call the main function here
            main(user_info, self.update_status, self.stop_flag)
            
        except Exception as e:
            self.update_status(f"Error occurred: {str(e)}")
        finally:
            self.update_status("Automation finished.")
    
    def quit_app(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.quit()

def extract_otp(text):
        """
        Extracts the OTP code from a given text string.
    
        Args:
            text (str): The text containing the OTP code.
        
        Returns:
            str: The extracted OTP code.
        """
        otp_pattern = r'\b\d{6}\b'
        match = re.search(otp_pattern, text)
        if match:
            return match.group()
        else:
            return None
def generate_random_2_digit_number():
    """
    Generate a random 2-digit number.
    """
    return random.randint(10, 99)
def generate_random_10_digit_number():
    """
    Generate a random 10-digit number.
    """
    return ''.join(random.choices(string.digits, k=10))   
def generate_random_email(domain="example.com"):
    """
    Generate a random email address with the given domain.
    """
    username_length = random.randint(5, 10)  # Random username length between 5 and 10
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    email = f"{username}@{domain}"
    return email  
def main(user_info,update_status, stop_flag):
    # Initialize DrissionPage ChromiumPage instance
    options = ChromiumOptions()
    driver = ChromiumPage(options)
    driver.clear_cache()
    # Initialize CloudflareBypasser with the driver instance
    cf_bypasser = CloudflareBypasser(driver)
    update_status("Initializing driver...")
    time.sleep(2)
    # Navigate to the login page where CAPTCHA needs to be bypassed
    driver.get("https://visa.vfsglobal.com/egy/en/ita/login")
    driver.clear_cache()
    # Perform CAPTCHA bypass
    cf_bypasser.bypass()    
    # Perform writing into email and password fields
    login_xpath = '#mat-input-0'
    password_xpath = '#mat-input-1'
    
    # Input login email
    while(not(cf_bypasser.driver.ele(login_xpath))):
        time.sleep(1)
    cf_bypasser.driver.ele(login_xpath).input(user_info['Email VFS'])

    # Input password
    cf_bypasser.driver.ele(password_xpath).input(user_info['Password VFS'])
    # Selector for the Sign In button
    sign_in_button_selector = (By.XPATH, "/html/body/app-root/div/div/app-login/section/div/div/mat-card/form/button")
    update_status("Attempting login...")
    time.sleep(2)
    
    loginpageurl=cf_bypasser.driver.url
    
    while(loginpageurl==cf_bypasser.driver.url ):
        cf_bypasser.driver.ele(sign_in_button_selector).click()

        time.sleep(3)
    update_status("login successfull . . .")


    time.sleep(5)    
    start_new_booking_button_selector = (cf_bypasser.find_button_start())
    
    
    while(not(cf_bypasser.driver.ele(start_new_booking_button_selector))):
        time.sleep(1)
        
    cf_bypasser.driver.ele(start_new_booking_button_selector).parent().click(by_js=True)
    
    select_option= (By.XPATH, "/html/body/app-root/div/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[1]/mat-form-field")
    
    time.sleep(1)


    selectpanelopition=(By.XPATH,'//*[@id="mat-select-0-panel"]')
    selectpanell2=(By.XPATH,'/html/body/app-root/div/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[2]/mat-form-field')
    selectoption2=(By.XPATH,'//*[@id="mat-select-4-panel"]')
    
    #selectpanel3=(By.XPATH,'/html/body/app-root/div/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[3]/mat-form-field')
    #selectoption3=(By.XPATH,'//*[@id="mat-select-2-panel"]')
    i=user_info["Centre"]
    url=""
    continuebutton=(By.XPATH,'/html/body/app-root/div/div/app-eligibility-criteria/section/form/mat-card[2]/button')
    j=0
    if(user_info['Visa Type']=='Legalisation'):
        j=1
    else:
        j=2    
    while(not(url.endswith("your-details"))):
            while(not(cf_bypasser.driver.ele(selectpanelopition))):
                while(not(cf_bypasser.driver.ele(select_option))):
                    time.sleep(1)
                cf_bypasser.driver.ele(select_option).click()
                time.sleep(1)
            if(len(cf_bypasser.driver.ele(selectpanelopition).children())<i):
                i=1
            cf_bypasser.driver.ele(selectpanelopition).child(i).click()
            cf_bypasser.driver.scroll.to_bottom()
            while(not(cf_bypasser.driver.ele(selectoption2))):
                while(not(cf_bypasser.driver.ele(selectpanell2))):
                    time.sleep(1)
                cf_bypasser.driver.ele(selectpanell2).click()
                time.sleep(1)
            cf_bypasser.driver.ele(selectoption2).child(j).click()          
            time.sleep(1)
            if(i==user_info["Centre"]):              
                cf_bypasser.driver.ele(continuebutton).click()
            i=i+1 
            time.sleep(user_info["Refresh Time"])
            url=cf_bypasser.driver.url
            cf_bypasser.driver.set.cookies.clear()
             
    time.sleep(5)
    update_status("Rendez-vous catched . . . ")
    time.sleep(2)
    #filling INPUT DATA
    
    firstnameinput=('#mat-input-2')
    lastnameinput=('#mat-input-3')
    genderselectinput=('#mat-select-8')
    genderselectoptions=('#mat-select-8-panel')
    Dataofbirthinput=('#dateOfBirth')
    Nationalityinput=('#mat-select-10')
    nationalityoption=('#mat-select-10-panel')
    passportnumberinput=('#mat-input-4')
    passportdateinput=('#passportExpirtyDate')
    contactnumberinputonly2shirfs=('#mat-input-5')
    contactnumberinputfull=('#mat-input-6')
    email2input=('#mat-input-7')
    
    
    #### filling input values
    cf_bypasser.driver.ele(firstnameinput).input(user_info['Name'])
    time.sleep(1)
    cf_bypasser.driver.ele(lastnameinput).input(user_info['Last Name'])
    while(not(cf_bypasser.driver.ele(genderselectoptions))):
        cf_bypasser.driver.ele(genderselectinput).click()
        time.sleep(2)
    cf_bypasser.driver.ele(genderselectoptions).child(user_info['Gender']).click()
    time.sleep(1)
    cf_bypasser.driver.ele(Dataofbirthinput).input(user_info['Date of Birth (dd/mm/yyyy)'])
    while(not(cf_bypasser.driver.ele(nationalityoption))):
        cf_bypasser.driver.ele(Nationalityinput).click()
        time.sleep(2)        
    
    cf_bypasser.driver.ele(nationalityoption).child(user_info['Nationality']).click()
    time.sleep(1)
    cf_bypasser.driver.ele(passportnumberinput).input(user_info['Passport Number'])
    time.sleep(1)
    cf_bypasser.driver.ele(passportdateinput).input(user_info['Passport Expiry Date (dd/mm/yyyy)'])
    time.sleep(1)
    #randomnumber2dig=generate_random_2_digit_number()
    cf_bypasser.driver.ele(contactnumberinputonly2shirfs).input(user_info['Contact Number (only 3 digits)'])
    time.sleep(1)
    cf_bypasser.driver.ele(contactnumberinputfull).input(user_info['Contact Number (full)'])
    time.sleep(1)
    cf_bypasser.driver.ele(email2input).input(user_info['Email'])
    time.sleep(1)
    
    savebutton=(By.XPATH,'/html/body/app-root/div/div/app-applicant-details/section/mat-card[2]/app-dynamic-form/div/div/app-dynamic-control/div/div/div[2]/button')
    cf_bypasser.driver.ele(savebutton).click()
    
    time.sleep(2)
    continuebutton2=(By.XPATH,'/html/body/app-root/div/div/app-applicant-details/section/mat-card[2]/div[2]/div[2]/button')
    
    time.sleep(10)
    cf_bypasser.driver.ele(continuebutton2).click()
    time.sleep(10)
    update_status("Data inserted .......")
    time.sleep(2)
    oururl=cf_bypasser.driver.url
    #### no email stuff select date avaliable
    if(not(oururl.endswith("book-appointment"))):
        print(f"OTP CHeck . . . ")
        update_status("OTP CHeck . . .")
        time.sleep(2)
        generateotpbutton=(By.XPATH,'/html/body/app-root/div/div/app-applicant-details/section/mat-card/mat-card/div/div/button')
        while(not(cf_bypasser.driver.ele(generateotpbutton))):
            time.sleep(1)
        cf_bypasser.driver.ele(generateotpbutton).click()
        time.sleep(1)
          ################# gmail connect
 
    
        cf_bypasser.driver.new_tab("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AS5LTASF9iJdZImgf-cNcdXKqQIBC0BPZoPyBXNdtWJObP6GIoU3FGLII21G_oS6dnzk3Z8Sgfs4cw&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1493317219%3A1719752056755944&ddm=0")
        time.sleep(5)
        while(not(cf_bypasser.driver.get_tab(1).ele('#identifierId'))):
            time.sleep(1)
        
        cf_bypasser.driver.get_tab(1).ele('#identifierId').input(user_info['Email Gmail'])
    
        suivantbutton=(By.XPATH,'//*[@id="identifierNext"]/div/button')
    
        while(not(cf_bypasser.driver.get_tab(1).ele(suivantbutton))):
            time.sleep(1)
      
        cf_bypasser.driver.get_tab(1).ele(suivantbutton).click()
    
        passwordinput=(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')
    

        time.sleep(4)
    
        while(not(cf_bypasser.driver.get_tab(1).ele(passwordinput))):
            time.sleep(1)
        cf_bypasser.driver.get_tab(1).ele(passwordinput).input(user_info['Password Gmail'])
        time.sleep(1)
        clicksuivant =(By.XPATH,'//*[@id="passwordNext"]/div/button')
        while(not(cf_bypasser.driver.get_tab(1).ele(clicksuivant))):
            time.sleep(1)

        cf_bypasser.driver.get_tab(1).ele(clicksuivant).click()

    
        time.sleep(10)
        #end of gmail connect 
       
        ####### actualisé + take message 
        actualise=(By.XPATH,'//*[@id=":4"]/div/div[1]/div[1]/div/div/div[4]/div/div/div')
        while(not(cf_bypasser.driver.get_tab(1).ele(actualise))):
            time.sleep(1)    
        cf_bypasser.driver.get_tab(1).ele(actualise).hover()

        cf_bypasser.driver.get_tab(1).ele(actualise).click()
        cf_bypasser.driver.scroll.to_bottom()
    
    
        time.sleep(10)
    
        cf_bypasser.driver.get_tab(1).ele(actualise).hover()

        cf_bypasser.driver.get_tab(1).ele(actualise).click()
    
        time.sleep(10)
   
        firstdm=(By.XPATH,'//*[@id=":2a"]')
    
        while(not(cf_bypasser.driver.get_tab(1).ele(firstdm))):
            time.sleep(1)    
        cf_bypasser.driver.get_tab(1).ele(firstdm).hover()
        cf_bypasser.driver.get_tab(1).ele(firstdm).click()
    
        tp_paragraph = cf_bypasser.find_last_otp_paragraph()
        if tp_paragraph:
            print(tp_paragraph.text)
        else:
            print("No OTP paragraph found.")
        
        otpcodeinput = (By.XPATH,'/html/body/app-root/div/div/app-applicant-details/section/mat-card/mat-card/div/div[2]/div[3]/div/mat-form-field/div/div[1]/div[3]/input')
        time.sleep(10)
        cf_bypasser.driver.ele(otpcodeinput).input(extract_otp(tp_paragraph.text))
        
        verifyotp=(By.XPATH,'/html/body/app-root/div/div/app-applicant-details/section/mat-card/mat-card/div/div[2]/div[4]/button')
        
        while(not(cf_bypasser.driver.ele(verifyotp))):
            time.sleep(1)
        
        cf_bypasser.driver.ele(verifyotp).click()
        time.sleep(5)
        continuefromotp=(By.XPATH,'/html/body/app-root/div/div/app-applicant-details/section/mat-card/div[2]/div[2]/button')
        cf_bypasser.driver.get_tab(1).close()

        cf_bypasser.driver.ele(continuefromotp).click()
        time.sleep(10)
        print(f"OTP BYPASSED . . . ")
        update_status("OTP BYPASSED . . .")
        time.sleep(2)
        cf_bypasser.driver.scroll.down(100)              
        
    locator= ('css selector', 'td.date-availiable')
    
    caldendertable=(By.XPATH,'/html/body/app-root/div/div/app-book-appointment-split-slot/section/mat-card[1]/div[2]/div/div/full-calendar/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody')
    
    e=1
    m=1
    avaliabledate=""
    nextmonthbutton=(By.XPATH,"/html/body/app-root/div/div/app-book-appointment-split-slot/section/mat-card[1]/div[2]/div/div/full-calendar/div[1]/div[3]/div/button[2]")
    while(not(avaliabledate)):
        if(e>5):
            m=+1
            e=1
            cf_bypasser.driver.ele(nextmonthbutton).click()
            time.sleep(3)
            
        avaliabledate=cf_bypasser.driver.ele(caldendertable).child(e).child(locator=locator,index=1)
        e=e+1
        if(m>4):
            break
    
    
    if(avaliabledate):
        print(avaliabledate)
        cf_bypasser.driver.ele(avaliabledate).click()
        time.sleep(5)
    else:
        raise ValueError('no appointement allowed now ')    
    
    
    
    firsthour=('#STRadio1')
    time.sleep(1)
    while(not(cf_bypasser.driver.ele(firsthour))):
        cf_bypasser.driver.ele(avaliabledate).click()
        time.sleep(1)
    cf_bypasser.driver.ele(firsthour).click()
    
    time.sleep(2)
    
    saveagainbutton=(By.XPATH,'/html/body/app-root/div/div/app-book-appointment-split-slot/section/mat-card[2]/div/div[2]/button')
    while(not(cf_bypasser.driver.ele(saveagainbutton))):
        time.sleep(1)
    cf_bypasser.driver.ele(saveagainbutton).click()
    
    time.sleep(10)
    print(f"Calendaire checked . . . ")
    update_status("Calendaire checked . . . ")
    time.sleep(2)


    #################### last check
    
    
    termcheck1=('#mat-checkbox-1')
    termcheck2=('#mat-checkbox-2')
    urlcheck=cf_bypasser.driver.url
    cf_bypasser.driver.scroll.to_bottom()
    while(urlcheck==cf_bypasser.driver.url):
        
        while(not(cf_bypasser.driver.ele(termcheck1))):
            time.sleep(1)
        cf_bypasser.driver.ele(termcheck1).check()
        time.sleep(2)
        while(not(cf_bypasser.driver.ele(termcheck2))):
            time.sleep(1)
        cf_bypasser.driver.ele(termcheck2).check()
    
        lastbutton=(By.XPATH,'/html/body/app-root/div/div/app-review-and-payment/section/form/mat-card[2]/div/div[2]/button')
        time.sleep(2)
        cf_bypasser.driver.ele(lastbutton).click(by_js=True)
        time.sleep(4)
        
        
        if stop_flag.is_set():
            update_status("Automation stopped.")
        return
    
    update_status("Appointment booked successfully!")
    print(f"Finish Successfull . . . ")    
if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationApp(root)
    root.mainloop()     
        
    
    
        
  
    
        

    
    