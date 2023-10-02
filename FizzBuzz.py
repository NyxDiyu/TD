class FizzBuzz:
    def affiche(self, nombre):
        resultat=""

        for i in range(1, nombre + 1):
            if i%15==0 :
                resultat += "Fizz"
            elif i%5==0 :
                resultat += "Lol"
            elif i%3==0 :
                resultat += "IsLol"
            else:
                resultat += str(i)
                
        return resultat
