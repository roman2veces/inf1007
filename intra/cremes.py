from itertools import combinations

def marchand_de_creme_glacee(saveurs, enrobages):
    def _fonction(nombre_de_boules):
            k = 0
            options = 1
            if (nombre_de_boules == 2):
                while k != len(saveurs) - 1:
                    for index_saveur in range(k, len(saveurs)):
                        if saveurs[index_saveur] != saveurs[k]:
                            for enrobage in enrobages:
                                print(f"Option {options} : {saveurs[k]}, {saveurs[index_saveur]} avec un enrobage {enrobage}")
                                options += 1 
                    k += 1
            
            elif (nombre_de_boules == 3):
                for index, enrobage in enumerate(enrobages):
                    print(f"Option {index + 1} : {saveurs[0]}, {saveurs[1]}, {saveurs[2]} avec un enrobage {enrobage}")
         
    return _fonction

generateur_de_creme_glacee = marchand_de_creme_glacee(saveurs=['chocolat', 'vanille', 'noisette'], 
                                                      enrobages=['chocolat belge', 'pistache'])
generateur_de_creme_glacee(nombre_de_boules=2)



# def marchand_de_creme_glacee(saveurs, enrobages):
#     def _fonction(nombre_de_boules):
#             k = 0
#             options = 1
        
#             option_str = f"Option {options} : "
#             combinaisons = []

#             combinaison = [0 for i in range(nombre_de_boules)]

#             while k != len(saveurs) - 1:
#                 for saveur in saveurs:
#                     for index in range(nombre_de_boules):
#                         combinaison[index] = saveur

#                     combinaison[index]([saveurs[k], saveurs[index]])
#             combinaison = [saveurs[boule] for boule in range(nombre_de_boules)]
#             for saveur in saveurs:
#                 for boule in range(nombre_de_boules):
#                     option_str += f"boule"
#                 print(f"")
            
#             if (nombre_de_boules == 2):
#                 while k != len(saveurs) - 1:
#                     for index_saveur in range(k, len(saveurs)):
#                         if saveurs[index_saveur] != saveurs[k]:
#                             for enrobage in enrobages:
#                                 print(f"Option {options} : {saveurs[k]}, {saveurs[index_saveur]} avec un enrobage {enrobage}")
#                                 options += 1 
#                     k += 1
            
#             elif (nombre_de_boules == 3):
#                 for index, enrobage in enumerate(enrobages):
#                     print(f"Option {index + 1} : {saveurs[0]}, {saveurs[1]}, {saveurs[2]} avec un enrobage {enrobage}")
         
#     return _fonction

