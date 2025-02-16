# Python_CompanyTracker
The Python Company Tracker is an application which holds a list of companies that you have an interest in. You can add to the list of companies, remove from the list of companies and clear the list to start a new one. 

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
        
        self.label = tk.Label(root, text="Enter company name:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        
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
  








