def alarme(elements):
    match elements:
        case['soir', action] if action not in ['de travailler', 'd\'etudier']:
            print(
                f'La journee est bientot finie! Maintenant, il est temps {action}!')
        case['soir', _]:
            print('Il est temps de te reposer!')
        case[temps, action]:
            print(f'Bon {temps}! il est temps {action}!')
        case _:
            print('Cette entree n\'est pas valide.')

def alarme(elements):
    if (len(elements) != 2):
        print('Cette entree n\'est pas valide.')
    else:
        temps = elements[0]
        action = elements[1]

        if (temps == 'soir' and action != 'de travailler' and action != 'd\'etudier'):
            print(f'La journee est bientot finie! Maintenant, il est temps {action}!')
        elif (temps == 'soir'):
            print('Il est temps de te reposer!')
        else:
            print(f'Bon {temps}! il est temps {action}!')
    
print("------- Alarme 1 ------")
alarme(['matin', 'de se reveiller'])
print("------- Alarme 2 ------")
alarme2(['matin', 'de se reveiller'])