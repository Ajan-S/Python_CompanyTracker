import tkinter as tk
from tkinter import messagebox
import json

class CompanyTrackerApp:
    
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
        
        
        #Search bar which allows specific items to be searched in the list to easily delete.
        self.search_label = tk.Label(root, text="Search company:")
        self.search_label.pack()
        
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()
        self.search_entry.bind("<KeyRelease>", self.search_companies)
        
        self.company_listbox = tk.Listbox(root)
        self.company_listbox.pack()
        
        self.populate_listbox()
        
    #Checks for a json file holding all the companies being tracked.    
    def load_companies(self):
        try:
            with open(self.filename, "r") as file:
                return set(json.load(file))
        except (FileNotFoundError, json.JSONDecodeError):
            return set()
    
    #Saves the list of companies currently being tracked in the json file.
    def save_companies(self):
        with open(self.filename, "w") as file:
            json.dump(list(self.companies), file)
    
    #Adds company to the list of company, checks for duplicates.
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
    
    #Removes selected company from the list of companies, and saves new list to json file.
    def remove_company(self):
        selected = self.company_listbox.curselection()
        if selected:
            company = self.company_listbox.get(selected)
            self.companies.remove(company)
            self.company_listbox.delete(selected)
            self.save_companies()
        else:
            messagebox.showerror("Error", "Please select a company to remove.")
    
    #Clears all companies from the list to start new list.
    def clear_companies(self):
        self.companies.clear()
        self.company_listbox.delete(0, tk.END)
        self.save_companies()
        messagebox.showinfo("Success", "All companies have been cleared from the list.")
    
    #Inserts all the companies in the json file into the listbox
    def populate_listbox(self, filtered_companies=None):
        self.company_listbox.delete(0, tk.END)
        companies_to_show = filtered_companies if filtered_companies is not None else self.companies
        for company in sorted(companies_to_show):
            self.company_listbox.insert(tk.END, company)
    
    #Search bar to search for individual companies within the listbox to delete it.
    def search_companies(self, event):
        query = self.search_entry.get().strip().lower()
        filtered_companies = {c for c in self.companies if query in c}
        self.populate_listbox(filtered_companies)


if __name__ == "__main__":
    root = tk.Tk()
    app = CompanyTrackerApp(root)
    root.mainloop()