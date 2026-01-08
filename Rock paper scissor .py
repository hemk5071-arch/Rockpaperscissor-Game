import random

class Rockpaperscissor:
    def __init__ (self):
        round = int(input("Enter how many rounds you want:"))
        self.round = round
        self.user_score = 0
        self.computer_score = 0
        
    def Computer_Choices(self):
        return random.choice(self.choices)
    
    def Play_game(self,user_choice):
        comp_choice = self.Computer_Choices()
        print("computer choose:",comp_choice)
        if user_choice == comp_choice:
            print("Tie! both choices are same")
        else:
            if user_choice =="rock":
                self.Rock(user_choice,comp_choice)
            elif user_choice =="paper":
                self.Paper(user_choice,comp_choice)
            elif user_choice == "scissor":
                self.Scissor(user_choice,comp_choice)
                    
    def Rock(self,user_choice,comp_choice):
        if user_choice == 'rock':
            if comp_choice == 'paper':
                print("computer won this round")
                self.computer_score +=1
            else:
                print("you won this round")
                self.user_score +=1
                
    def Paper(self,user_choice,comp_choice):
        if user_choice == 'paper':
            if comp_choice == 'scissor':
                print("computer won this round")
                self.computer_score +=1
            else:
                print("you won this round")
                self.user_score +=1
                
    def Scissor(self,user_choice,comp_choice):
        if user_choice == 'scissor':
            if comp_choice == 'rock':
                print("computer won this round")
                self.computer_score +=1
            else:
                print("you won this round")
                self.user_score +=1
                         
    def Round_start(self):
        self.choices = ['rock' , 'paper' , 'scissor']
        for round_num in range(1,self.round+1):
            print(f"\nRound: {round_num}")
            user_choice = input("Enter your choices:").lower()
            time=self.Play_game(user_choice)
            if user_choice in self.choices:
                continue
            else:
                print("Invalid Choices,Computer won this round")
                self.computer_score +=1
            
        self.Result()
        
    def Result(self):
        print("\n===== GAME OVER =====")
        print("Your Score:",self.user_score)
        print("Computer Score:",self.computer_score)
        
        if self.user_score > self.computer_score:
            print("\nYou won the game")
        elif self.user_score < self.computer_score:
            print("\ncomputer won the game")
        else:
            print("\nThis game is tie")
        
game = Rockpaperscissor()
game.Round_start()
        