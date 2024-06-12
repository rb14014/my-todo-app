FILE_PATH= "todos.txt"

def get_todos(filepath=FILE_PATH):
    """ Read a text file and return the list of
    to-do items.
     """ #Docstring do dokumentacji
    with open(filepath, 'r') as file_local:
        todos_local= file_local.readlines() #zmienna lokalna
    return todos_local

# print(help(get_todos))
def write_todos(todos_arg, filepath=FILE_PATH): #Parametry z domyśłnymi wartościami lepiej dawać jako ostatnie, jak mamy mieszana konwencję
    """ Write to-do items to the text file.
     """ #Docstring do dokumentacji
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
        print(todos_arg)

if __name__ == "__main__": #To jest sposób aby poniższe polecenia nie były wykonywane po imporcie w innyk skryptach np w cli.py
    print("Hello from functions")
    print(get_todos())