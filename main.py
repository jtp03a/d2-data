import json
from os import walk
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
YELLOW = "#f7f5dd"


class JSON_Converter:
  # convert the d2r excel data text files to json
  def convert_to_json(self):
    for files in enumerate(walk('./data/data/global/excel')):
      filelist = files[1][2]
      for file in filelist:
        if file.split('.')[1] == 'txt':      
          with open(f'./data/data/global/excel/{file}', 'r') as data:
            filename= file.split('.')[0]
            
            lines = data.readlines()
            col_names = lines[0].split('\t')

            datalist = []

            for line in lines[1:]:
              item = line.split('\t')
              
              datadict = {}

              for index, attribute in enumerate(item):
                if attribute != '':
                  datadict[col_names[index]] = attribute
              
              datalist.append(datadict)

            jsonString = json.dumps(datalist)

          with open (f'./jsonoutput/{filename}_json.txt', 'w') as output:
            output.write(jsonString)

# UI

def search_json_files(search_string):
  for files in enumerate(walk('./jsonoutput/')):
    filelist = files[1][2]
    for file in filelist:
      with open(f'./jsonoutput/{file}', 'r') as file_content:
        string_content = file_content.read()
        json_content = json.loads(string_content)
        for item in json_content:
          for key, value in item.items():
            if search_string.lower() in value.lower():
              item_details.config(text=item)

window = Tk()
window.title('Activity Alerts')
window.config(padx=25,pady=50,bg=YELLOW, width=600, height=800)

item_name_label = Label(text='Item Name:')
item_name_label.grid(column=0, row=0)

item_name = Entry(width = 25)
item_name.grid(column=1, row=0)

search_btn = Button(text='Search', command= lambda: search_json_files(item_name.get()))
search_btn.grid(column=1, row=2)

item_details = Label(text='')
item_details.grid(column=1, row=3)

window.mainloop()


