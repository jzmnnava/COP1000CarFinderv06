#Define File Name
file_name = 'AllowedVehiclesList.txt'

#Function to Read from File
def read_vehicles_from_file():
  try:
    with open(file_name,'r') as file:
      vehicles = [line.strip() for line in file.readlines()]
  except FileNotFoundError:
    vehicles = []
  return vehicles

#Function to write the vehicles to the file
def write_vehicles_to_file(vehicles):
  with open(file_name,'w') as file:
    for vehicle in vehicles:
      file.write(f'{vehicle}\n')

#Define function to print the menu
def print_menu():
 print('********************************')
 print('AutoCountry Vehicle Finder v0.6')
 print('********************************')
 print('Please Enter the following number below from the following menu:')
 print('1. PRINT all Authorized Vehicles')
 print('2. SEARCH for Authorized Vehicle')
 print('3. ADD Authorized Vehicle')
 print('4. DELETE Authorized Vehicle')  
 print('5. Exit') 
 print('********************************')  

#Define function to print the list of authorized vehicles
def print_vehicles():
  vehicles = read_vehicles_from_file()
  print('\nThe AutoCountry sales manager as authorized the purchase and selling of the following vehicles:')
  for vehicle in vehicles:
    print(vehicle)
  print ()

#Define function to search for a vehicle
def search_vehicle():
  vehicle_name = input('\nPlease Enter the full vehichle name: ')
  vehicles = read_vehicles_from_file()
  if vehicle_name in vehicles:
     print(f'\n{vehicle_name} is an authorized vehicle')
  else:
      print(f'\n{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again.') 
  print () 

#Define function to add a vehicle
def add_vehicle():
  vehicle_name = input('\n Please enter the full vehicle name you would like to add: ')
  vehicles = read_vehicles_from_file()
  if vehicle_name in vehicles: 
    print(f'\n {vehicle_name} is already an authorized vehicle.')
  else:
    vehicles.append(vehicle_name)
    write_vehicles_to_file(vehicles)
    print(f'\nYou have added "{vehicle_name}" as an authorized vehicle.')
  print()

#Define function to delete a function
def delete_vehicle():
   vehicle_name = input('\nPlease Enter the full Vehicle Name you would like to REMOVE: ')
   vehicles = read_vehicles_from_file()
   if vehicle_name in vehicles:
      confirmation = input(f'\nAre you sure you want to remove "{vehicle_name}" from the Authorized Vehicles List? ')
      if confirmation.lower() == 'yes':
         vehicles.remove(vehicle_name)
         write_vehicles_to_file(vehicles)
         print(f'\nYou have REMOVED "{vehicle_name}" as an authorized vehicle.')
      elif confirmation.lower() == 'no':
         print_menu()
      else:
         print(f'\n"{vehicle_name}" is not found in the Authorized Vehicle list.')
      print()

#Define the main loop
while True:
  print_menu()
  choice = input('\nEnter your choice:')

  if choice == '1':
    print_vehicles()
  elif choice == '2':
    search_vehicle()
  elif choice == '3':
    add_vehicle()
  elif choice == '4':
     delete_vehicle()
  elif choice == '5':
    print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
    break
  else:
    print('Invalid choice, please try again')
