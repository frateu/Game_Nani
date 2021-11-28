from pyswip import Prolog
from pyswip.core import PL_PRUNED
from pyswip import Atom
from pyswip.prolog import PrologError

PATH_ = ""
prolog = Prolog()
prolog.consult(PATH_ + "house_base.pl")

def whereAmI():
    resultHere = prolog.query("here(X)")
    actualRoom = list(resultHere)[0]['X']
    return actualRoom

def nextStep(whatIEat):
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
            updateLook(listConnections[nxt - 1], whatIEat)

def updateLook(actualRoom, whatIEat):
    resutlLook = prolog.query("look({0}, [Y])".format(actualRoom))
    prolog.retract("here(X)")
    prolog.asserta("here({0})".format(actualRoom))

    allConnections = prolog.query("list_connections({0}, [Y])".format(actualRoom))
    allObjects = prolog.query("list_things({0}, [Y])".format(actualRoom))
    allEdible = prolog.query("list_edible({0}, [Y])".format(actualRoom))

    listConnections = []
    for res in list(allConnections):
        listConnections.append(str(res['Y']))

    listObjects = []
    for res in list(allObjects):
        listObjects.append(str(res['Y']))

    for res in list(allEdible):
        whatIEat.append(str(res['Y']))

    print("\n----------------------------")
    print("\nAtual Room: ", actualRoom)

    for res in list(resutlLook):
        if listConnections.count(res['Y']) > 0:
            print("Room Connected: ", res['Y'])
        else:
            print("Object: ", res['Y'])
    
    for food in whatIEat:
        print("Food Eaten: {0}".format(food))

    if listObjects.count('nani') > 0:
        print('\nYou found the Nani, now you can go sleep!')
    else:
        nextStep(whatIEat)

if __name__ == "__main__":
    whatIEat = []
    updateLook(whereAmI(), whatIEat)