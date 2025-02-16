# Python_CompanyTracker
The Python Company Tracker is an application which holds a list of companies that you have an interest in. You can add to the list of companies, remove from the list of companies and clear the list to start a new one. 

## Contents
- [How To Run](#how-to-run)
- [How it Works](#how-it-works)
    - [Initialisation](#initialisation)
    - [File Handling](#file-handling)
    - [UI Display](#ui-display)
    - [List Management](#list-management)

## How To Run
In order to run the file you must:
  1. Install Python onto your computer
  2. Run the program in terminal with py .\CompanyTracker.py or python .\CompanyTracker.py

## How it Works
Listed below are the key functions that have been implemented and how they work:
### Initialisation
```python
    def __init__(self, root):
        self.root = root
        self.root.title("Company Tracker")
        
        #File which holds the list of companies that are currently being tracked.
        self.filename = "companies.json"
        self.companies = self.load_companies()
        
        self.company_input_label = tk.Label(root, text="Enter company name:")
        self.company_input_label.pack()
        
        self.company_input_field = tk.Entry(root)
        self.company_input_field.pack()
        
        
        #Buttons to incorparate all of the features of the Company List Tracker.
        self.add_button = tk.Button(root, text="Add Company", command=self.add_company)
        self.add_button.pack()
        
        self.remove_button = tk.Button(root, text="Remove Company", command=self.remove_company)
        self.remove_button.pack()
        
        #Clear Button to clear all companies currently in list.
        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_companies)
        self.clear_button.pack()
```
  The initialisation function initialises the GUI application. The input box, buttons that add, remove and clear the list as well as a searchbar to search the listbox are added to the application in this function. The searchbar will automatically filter out all the names where the substring typed out doesn't appear.
```python
#Search bar which allows specific items to be searched in the list to easily delete.
        self.search_label = tk.Label(root, text="Search company:")
        self.search_label.pack()
        
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()
        self.search_entry.bind("<KeyRelease>", self.search_companies)
        
        self.listbox = tk.Listbox(root)
        self.listbox.pack()
        
        self.populate_listbox()
```
The initialisation function calls the load_companies and populate_listbox functions, to store the list in the json file as a set in a variable called companies and to take the set and display it in a listbox called companylist. 

### File Handling
  In order to handle the list of comapnies that are being tracked by the application a json file called companies is used. This is to make sure that the companies that are being tracked is saved somewhere even when the application has been closed. The load function below loads the json file converting its contents from a list to a set, if no file has been found it returns an empty set. As json files can only save lists, the function converts the list into a set to make sure that there are no duplicate companies being displayed.
```python
  def load_companies(self):
        try:
            with open(self.filename, "r") as file:
                return set(json.load(file))
        except (FileNotFoundError, json.JSONDecodeError):
            return set()
```
  The save companies function, saves the list that is currently being displayed in the listbox into the json file.
  ```python
     def save_companies(self):
        with open(self.filename, "w") as file:
            json.dump(list(self.companies), file)
  ```
### UI Display
In order for a better UI, a listbox which displays the list of companies in the json file is implemented as well as a searchbar which can be used to search through this listbox. The listbox is first filled by calling the function populate_listbox, which first clears the listbox if anything is in it. Then it fills it with the content in the json file, or just the companies that contain the substring being searched in the search bar.
```python
     def populate_listbox(self, filtered_companies=None):
        self.company_listbox.delete(0, tk.END)
        companies_to_show = filtered_companies if filtered_companies is not None else self.companies
        for company in sorted(companies_to_show):
            self.company_listbox.insert(tk.END, company)
```
The searchbar is implemented with a search companies function, which is called every time a character is inputted into the seachbar. It checks through the contents of the listbox and checks if the substring is in any of the companies within the listbox. If it is it displays only these companies in the listbox.
```python
    def search_companies(self, event):
        query = self.search_entry.get().strip().lower()
        filtered_companies = {c for c in self.companies if query in c}
        self.populate_listbox(filtered_companies)
```

### List Management
  In order to manage the list, three functions are implemented. An add function, a remove function and a clear function. The add function, appends the list with the company that has been typed into the input field and into the listbox. An error will popup with a suitable message if nothing is in the input field or if the company is already in the list. After a company has been added the input field is cleared and the new list is saved in the json file.
  ```python
    def add_company(self):
        company = self.company_input_field .get().strip().lower()
        if company and company not in self.companies:
            self.companies.add(company)
            self.company_listbox.insert(tk.END, company)
            self.save_companies()
            self.company_input_field.delete(0, tk.END)
        elif company in self.companies:
            messagebox.showerror("Error", "Company is already in your list.")
        else:
            messagebox.showerror("Error", "Please enter a company name.")
  ```
The remove function removes a company that has been selected by the list cursor. The company is removed from the set of companies and from the listbox, finally being saved into the json file. If no company has been selected a suitable error message is displayed.
```python
  def remove_company(self):
        selected = self.company_listbox.curselection()
        if selected:
            company = self.company_listbox.get(selected)
            self.companies.remove(company)
            self.company_listbox.delete(selected)
            self.save_companies()
        else:
            messagebox.showerror("Error", "Please select a company to remove.")
```
Finally a clear function is implemented. This fuction clears the list of all the companies and saves the empty list into the file. After clearing all the companies a message is displayed to show that it has been completed.
```python
   def clear_companies(self):
        self.companies.clear()
        self.company_listbox.delete(0, tk.END)
        self.save_companies()
        messagebox.showinfo("Success", "All companies have been cleared from the list.")
```
  








