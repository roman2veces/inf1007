phrase = "hollllll      aaaaaaa"
histogramme = {lettre: phrase.count(lettre) for lettre in phrase}
histogramme_list = list(histogramme.items())
print(sorted(histogramme_list, key=lambda liste: liste[1], reverse=True))

    