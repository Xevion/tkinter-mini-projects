import json, random, datetime, os, faker
from functools import partial
from tkinter import ttk
from tkinter import *

fake = faker.Faker()

# Basic Structure of what assignment's data looks like
class Assignment:
    def __init__(self):
        self.dateDue = fake.date()
        self.dateAssigned = fake.date()
        self.name = fake.text(max_nb_chars=15)[:-1]
        self.category = random.choice(['Daily', 'Major', 'Quiz'])
        self.weight = random.choice([1.0, 1.0, random.randint(1, 7) * 0.5])
        self.score = random.choice([100, random.randint(90, 100), random.randint(10, 100)])
        self.totalPoints = 100
        self.weightedTotalPoints = self.weight * self.totalPoints
        self.weightedScore = self.weight * self.score
        self.percentage = int((self.weightedScore / self.weightedTotalPoints) * 100)

class Class:
    def __init__(self):
        self.className = fake.bs()
        self.assignments = [Assignment() for _ in range(10)]

class Window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_interface()
    
    def randomSet(self):
        self.choices = [item[1] for item in random.choices(self.treeIDs, k=3)]
        self.class_assignments.selection_set(self.choices)
        print(self.class_assignments.selection())

    def assignments_init(self):
        self.class_notebook = ttk.Notebook(self.assignments)
        self.class_tabs = []
        self.classes = [Class() for _ in range(3)]

        longestName = max([int(max([6.5 * len(assignment.name) for assignment in individualClass.assignments])) for individualClass in self.classes])

        for classIndex, individualClass in enumerate(self.classes):
            # Create a new frame binded to the Class Notebook
            class_frame = Frame(self.class_notebook)

            # All the column's in order
            columnStrings = ['Date Due', 'Assigned', 'Name', 'Category', 'Weight', 'Score', 'Weighted Score', 'Total Points', 'Weighted Total Points', 'Percentage']
            columnWidths = [80,              80,      longestName, 80,      80,       80,         100,             80,               130,                  80]

            # Create a new TreeView (table) object
            self.class_assignments = ttk.Treeview(class_frame, columns=columnStrings[1:])
            
            # Create all the Column's for it
            for index, columnString in enumerate(list(columnStrings)):
                self.class_assignments.heading('#{}'.format(index), text=columnString)
                self.class_assignments.column('#{}'.format(index), minwidth=columnWidths[index], width=columnWidths[index])
            
            self.treeIDs = []
            # Insert a assignment with all it's values
            for index, assignment in enumerate(individualClass.assignments):
                tree_id = self.class_assignments.insert('', 'end', text=assignment.dateDue, values=(assignment.dateAssigned, assignment.name,
                assignment.category, assignment.weight, assignment.score, assignment.weightedScore, assignment.totalPoints,
                assignment.weightedTotalPoints, '{}%'.format(assignment.percentage)))
                self.treeIDs.append((index, tree_id))
            
            self.find_worst_button = Button(class_frame, text='Button1', command=partial(self.randomSet, classIndex))
            # self.randomSet()

            for x in range(11):
                Grid.columnconfigure(class_frame, x, weight=1)
            for y in range(3):
                Grid.rowconfigure(class_frame, y, weight=1)

            # Grid the new Finished Table & Buttons
            self.class_assignments.grid(column=0, row=0, padx=5, pady=5, columnspan=10)
            self.find_worst_button.grid(column=0, row=1, padx=5, pady=5, sticky=N+S+E+W)

            # Add a new tab, using this class's frame for the data
            self.class_notebook.add(class_frame, text=individualClass.className)
            self.class_tabs.append(class_frame)
        
        self.class_notebook.grid(column=0, row=0)

    def init_interface(self):
        # Window Configurations
        self.parent.title("Gradebook Fetcher")
        self.parent.config(background="lavender")

        # Notebook for displaying tabs
        self.notebook = ttk.Notebook(self.parent)
        self.assignments = Frame(self.notebook)
        self.assignments_init()
        self.notebook.add(self.assignments, text='Assignments')
        self.notebook.grid(column=0, row=0, padx=5, pady=5)

def main():
    root = Tk()
    x = Window(root)
    root.mainloop()

if __name__ == "__main__":
    main()