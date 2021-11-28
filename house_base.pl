:- dynamic here/1.

room(office).
room(hall).
room(kitchen).
room(diningroom).
room(cellar).

location(desk, office).
location(computer, office).
location(apple, kitchen).
location(broccoli, kitchen).
location(crackers, kitchen).
location(flashlight, desk).
location(washingmachine, cellar).
location(nani, washingmachine).

door(office, hall).
door(office, kitchen).
door(hall, diningroom).
door(diningroom, kitchen).
door(kitchen, cellar).

edible(apple).
edible(crackers).
tastes_yucky(broccoli).

turned_off(flashlight).
here(kitchen).

where_food(X, Y):- location(X, Y).
connected(X, Y):- door(X, Y); door(Y, X).

list_things(X, [Y]):- location(Y, X).
list_things(X, [Z]):- location(Y, X), location(Z, Y).

list_connections(X, [Y]):- connected(X, Y).

look(X, [Y]):- list_things(X, [Y]).
look(X, [Y]):- list_connections(X, [Y]).
list_edible(X, [Y]):- edible(Y), where_food(Y, X).