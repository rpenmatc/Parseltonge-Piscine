import sys
states_dictionary =  { 'Alabama' : 'Montgomery',
'Alaska' : 'Juneau', 
'Arizona' : 'Phoenix', 
'Arkansas' : 'Little Rock', 
'California' : 'Sacramento',
'Colorado' : 'Denver',
'Connecticut' : 'Hartford',
'Delaware' : 'Dover', 
'Florida' : 'Tallahassee', 
'Georgia' :'Atlanta', 
'Hawaii' : 'Honolulu', 
'Idaho' : 'Boise', 
'Illinois' : 'Springfield', 
'Indiana': 'Indianapolis', 
'Iowa': 'Des Moines', 
'Kansas': 'Topeka', 
'Kentucky' : 'Frankfort', 
'Louisiana' : 'Baton Rouge', 
'Maine' : 'Augusta',
'Maryland' : 'Annapolis',
'Massachusetts' : 'Boston',
'Michigan' : 'Lansing',
'Minnesota' : 'Saint Paul',
'Mississippi' : 'Jackson',
'Missouri' : 'Jefferson City',
'Montana' : 'Helena',
'Nebraska' : 'Lincoln',
'Nevada' : 'Carson City',
'New Hampshire' : 'Concord',
'New Jersey' : 'Trenton',
'New Mexico' : 'Santa Fe',
'New York' : 'Albany',
'North Carolina' : 'Raleigh',
'North Dakota' : 'Bismarck',
'Ohio' : 'Columbus',
'Oklahoma' : 'Oklahoma City',
'Oregon' : 'Salem',
'Pennsylvania' : 'Harrisburg',
'Rhode Island' : 'Providence',
'South Carolina' : 'Columbia',
'South Dakota' : 'Pierre',
'Tennessee' : 'Nashville',
'Texas' : 'Austin',
'Utah' : 'Lake City',
'Vermont' : 'Montpelier',
'Virginia' : 'Richmond',
'Washington' : 'Olympia',
'West Virginia' : 'Charleston',
'Wisconsin' : 'Madison',
'Wyoming' : 'Cheyenne'}
forev = True
inv_map = {v: k for k, v in states_dictionary.items()}
while forev == True:
    x = input("Ready: ")
    if x in states_dictionary:
        print(states_dictionary[x])
    elif x in inv_map:
        print(inv_map[x])
    elif x == "Done":
        break
    else:
        print("nil")