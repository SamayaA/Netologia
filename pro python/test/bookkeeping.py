documents = [
    {
        "type": "passport",
        "number": "2207 876234",
        "name": "Василий Гупкин"
    },
    {
        "type": "invoice",
        "number": "11-2", 
        "name": "Геннадий Покемонов"
     },
    {
        "type": "insurance", 
        "number": "10006", 
        "name": "Аристарх Павлов"
    }
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def find_document_owner(number) :
  name = ''
  for doc in documents :
    if doc["number"] == number :
      name = doc["name"]
      return name
  if name == '' :
    return 'The number of document does not exist '
  

def find_shelf(number) :
  for shelf , numbers in directories.items() :
    shelf_num = ''
    if number in numbers :
      shelf_num = shelf
      return shelf_num
  if shelf_num == '' :
    return 'The number of document does not exist '
  

def add_document(number , type_document , name , shelf) :
  doc_dict = dict()
  doc_dict["type"] = type_document
  doc_dict["number"] = number
  doc_dict["name"] = name
  documents.append(doc_dict)
  if shelf in directories.keys() :
    directories[shelf].append(number)
  else :
    print(f'The {shelf} shelf has been addded')
    directories[shelf] = list()
    directories[shelf].append(number)


def delete_document(number) :
  exist = ''
  for doc in documents :
    if doc["number"] == number :
      documents.remove(doc)
      exist = 'yes'
  if (find_shelf(number) == 'The number of document does not exist ') :
    print('The number of document is not on the shelf')
  else :
    index = directories[find_shelf(number)].index(number)
    del directories[find_shelf(number)][index]
  if (exist == '') :
    print ('The number of document doesnt exist')

  

def replace_document(number , shelf_num) :
  if find_document_owner(number) == 'The number of document does not exist ' :
    print("The document does not exist")
    return 0
  if shelf_num in  directories.keys() :
    directories[shelf_num].append(number)
  else:
    print("We can't replace document. The entered shelf does not exist.")
    return 0
  index = directories[find_shelf(number)].index(number)
  del directories[find_shelf(number)][index]
  
  

def add_shelf(shelf) :
  if shelf in  directories.keys() :
    print("The shelf exist")
  else :
    directories[shelf] = list()


def main() :
    while True :
        menu_annotation = f"\nEnter: \n'p' to find the name of person \
            \n's' to find the shelf where is document \
            \n'l' to get list of documents \n'a' to add new document \
            \n'd' to delete document \n'm' to replace the document \
            \n'as' to add shelf\nanything else to exit\n"
        command_to_do = input(f'{menu_annotation}')
        if command_to_do == 'p' :
            num_doc = input('Enter the number of document ')
            name = find_document_owner(num_doc)
            if name == 'The number of document does not exist ' :
                print(name)
            else :
                print(f'The name is {name}')
        elif command_to_do == 's' :
            num_doc = input('Enter the number of document ')
            shelf_num = find_shelf(num_doc)
            if shelf_num == 'The number of document does not exist ' :
                print(shelf_num)
            else :
                print(f'The document  on the {shelf_num} shelf')

        elif command_to_do == 'l' :
            length = len(documents)
            for index in range(0 , length):
                print(documents[index]['type'] , documents[index]['number'] , documents[index]['name'])

        elif command_to_do == 'a' :
            num_doc = input('Enter the number of new document ')
            type_doc = input('Enter the type of new document ')
            name_doc = input('Enter the name of owner new document ')
            shelf_doc = input('Enter the shelf to place new document ')
            add_document(num_doc , type_doc , name_doc , shelf_doc)

        elif command_to_do == 'd' :
            num_doc = input('Enter the number of document to delete ')
            delete_document(num_doc)

        elif command_to_do == 'm' :
            num_doc = input('Enter the number of document ')
            shelf_doc = input('Enter the shelf to place the document ')
            replace_document(num_doc , shelf_doc)

        elif command_to_do == 'as' :
            shelf_doc = input('Enter number of new shelf ')
            add_shelf(shelf_doc)

        else :
            break

main()