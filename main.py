import random

def hangman():
    while True:
        # Status des Galgenmänchens
        hangman_stage = [
        # 0 Leben (Tod)
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |
        """,
        # 1 Leben
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / 
        |
        """,
        # 2 Leben
        """
        ------
        |    |
        |    O
        |   /|\\
        |    
        |
        """,
        # 3 Leben
        """
        ------
        |    |
        |    O
        |   /|
        |    
        |
        """,
        # 4 Leben
        """
        ------
        |    |
        |    O
        |    |
        |    
        |
        """,
        # 5 Leben
        """
        ------
        |    |
        |    O
        |    
        |    
        |
        """,
        # 6 Leben (Startzustand)
        """
        ------
        |    |
        |    
        |    
        |    
        |
        """
    ]

        # Liste mit wörten
        word_list = [
            "python",           # 6 Buchstaben
            "hangman",          # 7 Buchstaben
            "programmieren",    # 13 Buchstaben
            "informatik",       # 10 Buchstaben
            "computer"          # 8 Buchstaben
            ]

        # Speichert ein zufälliges Wort aus wordList
        secret_word = random.choice(word_list)

        # Nimmt das secret_word und ersetzt die Buchstaben durch "_" 
        display_word = len(secret_word) * ["_"]

        # Printet das secret_word mit den "_" und leerzeichen zwischen den zeichen
        print(" ".join(display_word))

        # Verfügbare Leben
        lives = 6
        print(f"Leben: {lives}")

        # Liste wo schon erratenen Buchstaben gespeichert werden
        guessedLetters = []



        # Prüft ob das spiel vorbei ist


        while "_" in display_word and lives > 0:
                
            # Benutzereingabe: Buchstaben erraten
            guess = input("Rate einen Buchstaben: ")


            if guess.isalpha() and len(guess) == 1:
                if guess in guessedLetters:
                    print("Dieser Buchstabe wurde schon erraten.\n Versuche es erneut: ")
                    continue

                else:
                    # speichert guess in guessedLetters 
                    guessedLetters.append(guess)
                    
                    if guess.lower() in secret_word:
                        
                        print("Dieser Buchstabe ist richtig!")
                        
                        for i in range(len(secret_word)):
                            if secret_word[i] == guess:
                                display_word[i] = guess
                        print(f"Leben: {lives}")
                        print(hangman_stage[lives])


                    else:
                        print("falsch")
                        lives -= 1
                        print(f"Leben: {lives}")
                        print(hangman_stage[lives])
                        
                    print(" ".join(display_word))

            else:
                print("Ungültige Eingabe!")

        if "".join(display_word) == secret_word:
                print("Glückwunsch. Du hast gewonnen!")
                
        else:
                print(f"Schade. Du hast verloren. Das gesuchte Wort war '{secret_word}'.")

        quit_or_cont = input("Möchtest du noch eine Runde Spielen? (y/n): \n")

        if quit_or_cont.lower() == "n":
            break
        elif quit_or_cont.lower() == "y":
            continue
        else:
            print("Ungültige Eingabe!")

hangman()
