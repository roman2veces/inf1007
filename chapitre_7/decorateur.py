def afficheAppel(fonction):
    print("je suis ici")
    def fonctionInterne():
        print("Appel commence ...")
        fonction()
        print("Appel termine ... ")
    
    print("je fais retourne")
    return fonctionInterne

# @afficheAppel Indique que cette fonction sera decoree par le decorateur afficheAppel
# Cela se comporte comme une appel de fonction, donc a ce moment bonjour va d'abord appele affiche appel 
# et recevera la fonction interne retournee par affiche appel, comme pour modifier bonjour 
@afficheAppel  
def bonjour():  
    print("Bonjourrr")

print("je fais dautre choses")
print("je fais dautre choses")
print("je fais dautre choses")
print("je fais dautre choses")
print("je fais dautre choses")

bonjour() # Dans l'appel de bonjour, c'est plutot la nouvelle fonction bonjour, decoree, qui va etre appelee