from game import Game

def get_user_menu_choice():
    while True:
        choice = input("Select an option:\n1. Play a new game\n2. Show scores\n3. Quit\nEnter your choice: ")
        if choice in {'1', '2', '3'}:
            return choice
        else:
            print("Invalid input. Please try again.")

def print_results(results):
    print("Results:")
    print(f"Total games played: {sum(results.values())}")
    print(f"Total games won: {results['win']}")
    print(f"Total games lost: {results['loss']}")
    print(f"Total games drawn: {results['draw']}")
    print("Thank you for playing!")

def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == '1':
            game = Game()
            game_result = game.play()
            results[game_result] += 1
        elif choice == '2':
            print_results(results)
        else:
            print_results(results)
            break

if __name__ == '__main__':
    main()
