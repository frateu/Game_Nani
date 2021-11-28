from pyswip import Prolog
from pyswip.core import PL_PRUNED
from pyswip import Atom

PATH_ = ""
prolog = Prolog()
prolog.consult(PATH_ + "house_base.pl")

# ----------------------- TESTES -----------------------

# result_ = prolog.query("door(hall, X)")
# print(list(result_)[0]['X']) # pegar só o nome do lugar {'X': 'lugar'}

# result_ = prolog.query("where_food(apple,Y)")
# print(list(result_));

# result_ = prolog.query("list_things(office, [Y])")

# # modelo de exibição para quando tiver uma lista
# for res in list(result_):
#     print(res['Y'])

# result_ = prolog.query("list_connections(office, [Y])")

# for res in list(result_):
#     print(res['Y'])

# result_ = prolog.query("look(office, [Y])")

# for res in list(result_):
#     print(res['Y'])

# ----------------------- INICIO -----------------------

# ----------------------- AINDA FALTA FAZER A PARTE DELE COMER E ISSO ATUALIAR UMA LISTA -----------------------

def whereAmI():
    resultHere = prolog.query("here(X)")
    actualRoom = list(resultHere)[0]['X']
    return actualRoom

def nextStep():
    actualRoom = whereAmI()
    allConnections = prolog.query("list_connections({0}, [Y])".format(actualRoom))
    listConnections = []
    for res in list(allConnections):
        listConnections.append(str(res['Y']))

    cont = 1

    print("\nWhere the you want to go now?")
    for room in listConnections:
        print("     Press {0} to walk to {1}.".format(str(cont), room))
        cont = cont + 1

    opt = input("   Option: ")

    for nxt in range(cont):
        if opt == str(nxt):
            updateLook(listConnections[nxt - 1])

def updateLook(actualRoom):
    resutlLook = prolog.query("look({0}, [Y])".format(actualRoom))
    prolog.retract("here(X)")
    prolog.asserta("here({0})".format(actualRoom))

    allConnections = prolog.query("list_connections({0}, [Y])".format(actualRoom))
    allObjects = prolog.query("list_things({0}, [Y])".format(actualRoom))

    listConnections = []
    for res in list(allConnections):
        listConnections.append(str(res['Y']))

    listObjects = []
    for res in list(allObjects):
        listObjects.append(str(res['Y']))

    print("\n----------------------------")
    print("\nAtual Room: ", actualRoom)

    for res in list(resutlLook):
        if listConnections.count(res['Y']) > 0:
            print("Room Connected: ", res['Y'])
        else:
            print("Object: ", res['Y'])
    
    if listObjects.count('nani') > 0:
        print('\nYou found the Nani, now you can go sleep!')
    else:
        nextStep()

updateLook(whereAmI())