# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 23 - Contact List
# Date: 11/1/2019

# function to convert list of comma seperated lines to a dictionary
def get_dictionary(input_string_list):
    ''' arguments: input list of strings.  each string is a line with comma seperated values,
        return: dictionary with the first line/headers as keys '''

    # initialize empty list of dictionaries
    dict_list = []

    # use headers to initialize 
    headers = input_string_list[0].split(',')

    # iterate through remaining lines in file
    for line_num in range(1,len(input_string_list)):
        # split line on comma
        this_line = input_string_list[line_num].split(',')

        # list to hold tuples
        tup_list = []

        # iterate through each column header
        for col in range(len(headers)): 
            # append a dictionary with each header
            tup_list.append( (headers[col], this_line[col]) )

        # append tuple as a dict to dict list
        dict_list.append(dict(tup_list))

    # return list of dictionaries
    return dict_list

# function to create dictionary input
def create(headers):
    ''' arguments: list of headers,
        returns: a dictionary of header/value pairs'''

    # declare list for holding inputs
    new_entry_list = []

    # get input.  iterate through headers, get string for each one
    for i in range(len(headers)):
        # append input to list
        new_entry_list.append(input(f"Please input {headers[i]}: "))

    # tuple list for later converting to dictionary
    tup_list = []

    # use header and new entry list to create tuple, which will be converted to a dictionary
    for i in range(len(new_entry_list)):
        # append header/value pair to tuple list
        tup_list.append(  (headers[i],new_entry_list[i])  )

    # cast tuple to a dictionary and return
    return dict(tup_list)

# function to retrieve/dispay info
def retrieve(dict_list, lookup):
    ''' arguments: the list of dictionaries and the column label that'll be used to lookup 
        returns: string of lookup values'''

    user_input = input(f"Please input what {lookup} you'd like data for: ")

    # iterate through dictionary list
    for entry in dict_list:
        # if name matches input
        if entry[lookup] == user_input:
            # return current element
            return entry

    # return none if not found
    return None

# function to update data in list of dictionaries
def update(dict_list, headers):
    ''' arguments: the list of dictionaries and the column label that'll be used to lookup 
        returns: string of lookup values'''

    # get user input
    user_input = input(f"Please input the {headers[0]} you'd like to update data for: ")

    # flag to catch if name is not found
    name_found_flag = False

    # iterate through dictionary list to find data
    for entry in dict_list:
        # if name matches input
        if entry[headers[0]] == user_input:
            # update name found flag to true
            name_found_flag = True
            # data found, now update
            for header in headers:                  # using headers here to account for variable width CSVs
                entry[header] = input(f"Please input new {header}: ")

    # if name wasn't found, return None
    if name_found_flag:
        return dict_list
    else: 
        return None

# function to delete data from list of dictionaries
def delete(dict_list, headers):
    ''' arguments: the list of dictionaries and the column label that'll be used to lookup 
        returns: string of lookup values'''

    # get user input
    user_input = input(f"Please input the {headers[0]} you'd like to delete data for: ")

    # flag to catch if name is not found
    name_found_flag = False

    # iterate through dictionary list to find data
    for i in range(len(dict_list)-1,-1,-1):
        # if name matches input
        if dict_list[i][headers[0]] == user_input:
            # update name found flag to true
            name_found_flag = True
            # data found, now delete
            dict_list.pop(i)

    # if name wasn't found, return None
    if name_found_flag:
        return dict_list
    else: 
        return None


# main

# open file
with open('lab23_spreadsheet.csv', 'r') as file:
    # load each line into list of strings call 'lines'
    lines = file.read().split('\n')

# get dictionary from csv
dict_list = get_dictionary(lines)
# get header by seperating out commas on first line
header = lines[0].split(',')
# print final dict
print(dict_list)


## version 2: CRUD REPL
while True:
    # get operation input
    user_operation = input("Commands:\n(c) create\n(r) retrieve\n(u) update\n(d) delete\n(s) show data\n(q) quit\nPlease make selection: ")
    user_operation = user_operation.lower()

    # initiate action depending on input
    # create
    if user_operation == 'c':
        dict_list.append(create(header))
    # retrieve
    elif user_operation == 'r':
        # get lookup data
        lookup_data = retrieve(dict_list, header[0])       # hardcoding the lookup string since we only want to look up by name
        # if lookup was not found in data
        if not lookup_data:
            print(f"That {header[0]} was not found.")
        else:
            print(lookup_data)
    # update
    elif user_operation == 'u':
        # get updated list of dictionaries
        updated_dict = update(dict_list, header)
        # if dictionary was successully updated, updated dict_list
        if updated_dict:
            dict_list = updated_dict.copy()
        else:
            print("Data not successfully updated")
    # delete
    elif user_operation == 'd':
        # get updated list of dictionaries
        updated_dict = delete(dict_list, header)
        # if dictionary was successully updated, updated dict_list
        if updated_dict:
            dict_list = updated_dict.copy()
        else:
            print("Data not found, delete was unsuccessful")
    # show data
    elif user_operation == 's':
        print(dict_list)    
    # quit
    elif user_operation == 'q':
        print("Quitting program.")
        break
    # unknown input
    else:
        print(f'user input is {user_operation}')
        print("Bad input, please try again.\n")