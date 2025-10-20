def olaMundo():
    print("Olá, Mundo!")

      
      x = 5 #Variavel global
      def soma():
        x = 10 #Variavel local
        print(x)
        return x + 1 
      
      soma()
      print(x)