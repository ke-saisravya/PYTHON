# Dice

#Dice
import random
GiveInputToRun=input("Type 'run' to roll the dice")
while(GiveInputToRun == "run"):
    RangeOfDice=random.randint(1,6)
    if (RangeOfDice == 1):
        print("     ")
        print("     ")
        print("  *  ")
        print("     ")
        print("     ")
    if (RangeOfDice == 2):
        print("     ")
        print(" *   ")
        print("     ")
        print("   * ")
        print("     ")
    if (RangeOfDice == 3):
        print("      ")
        print(" *    ")
        print("   *  ")
        print("     *")
        print("      ")
    if (RangeOfDice == 4):
        print("      ")
        print(" *  * ")
        print("      ")
        print(" *  * ")
        print("      ")
    if (RangeOfDice == 5):
        print("      ")
        print(" *   *")
        print("   *  ")
        print(" *   *")
        print("      ")
    if (RangeOfDice == 6):
        print("      ")
        print(" * *  ")
        print(" * *  ")
        print(" * *  ")
        print("      ")
    GiveInputToRun=input("Type 'run' to continue")

