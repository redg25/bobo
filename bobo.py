#!/usr/bin/env python3
import json
import PySimpleGUI as sg
sg.theme('Dark Amber')    # Add some color for fun

database_file = "book.json"
def read_data():
    with open(database_file, "r") as fp:
        return json.load(fp)

def write_data(info):
    with open(database_file, "w") as fp:
        json.dump(info, fp, indent=2)

info = read_data()
data = [[item["date"], item["author"], item["title"], item["series"]] for item in sorted(info, key=lambda x: x["date"], reverse=True)]

# Todo - make author and series filter drop-downs
# add labels for drop downs
# get keyboard shortcuts working


# 1- the layout
layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-AUTHOR-'), sg.Input(key="-SERIES-")],
          [sg.Table(
                values=data,
                headings=["Date Read", "Author", "Title", "Series", ],
                key="-BOOKTABLE-",
                # hide_vertical_scroll=True,
                # row_height=15,
                # col_widths=100
          )],
          [sg.Button('Show'), sg.Button('Exit')]]

# 2 - the window
window = sg.Window('Pattern 2', layout)

# 3 - the event loop
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        print("author", values["-AUTHOR-"])
        print("series", values["-SERIES-"])
        author = values["-AUTHOR-"]
        series = values["-SERIES-"]
        data = [[item["date"], item["author"], item["title"], item["series"]] for item in sorted(info, key=lambda x: x["date"], reverse=True)]
        if author:
            data = [x for x in data if x[1] == author]
        if series:
            data = [x for x in data if x[3] == series]

        # window['-OUTPUT-'].update(values['-AUTHOR-'])
        window["-BOOKTABLE-"].update(data)

        # In older code you'll find it written using FindElement or Element
        # window.FindElement('-OUTPUT-').Update(values['-IN-'])
        # A shortened version of this update can be written without the ".Update"
        # window['-OUTPUT-'](values['-IN-'])

# 4 - the close
window.close()
