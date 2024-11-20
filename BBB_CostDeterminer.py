import tkinter as tk

class Card:
    def __init__(self, name, attack, defense, life, abilityTarget1, abilityTarget2, numElements):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.life = life
        self.abilityTarget1 = abilityTarget1
        self.abilityTarget2 = abilityTarget2
        self.numElements = numElements

    def costDetermination(self):
        totalCost = 0
        avg = (self.attack + self.defense + self.life) / 3
        if self.abilityTarget1 == "Single":
            totalCost += 1
        elif self.abilityTarget1 == "SoloBattlefield":
            totalCost += 2
        elif self.abilityTarget1 == "AllBattlefield":
            totalCost += 3
        elif self.abilityTarget1 == "None":
            totalCost += 0
        if self.abilityTarget2 == "Single":
            totalCost += 1
        elif self.abilityTarget2 == "SoloBattlefield":
            totalCost += 2
        elif self.abilityTarget2 == "AllBattlefield":
            totalCost += 3
        elif self.abilityTarget2 == "None":
            totalCost += 0
        totalCost += (self.numElements - 1)
        totalCost += avg
        return totalCost
  

def calculateCost():
    attack = int(attackEntry.get())
    defense = int(defenseEntry.get())
    life = int(lifeEntry.get())
    numElements = int(numElementsEntry.get())

    ability1 = "None"
    ability2 = "None"
    if singleTargetSpecialAbility1_var.get():
        ability1 = "Single"
    elif singleBattlefieldSpecialAbility1_var.get():
        ability1 = "SoloBattlefield"
    elif entireBattlefieldSpecialAbility1_var.get():
        ability1 = "AllBattlefield"
    if singleTargetSpecialAbility2_var.get():
        ability2 = "Single"
    elif singleBattlefieldSpecialAbility2_var.get():
        ability2 = "SoloBattlefield"
    elif entireBattlefieldSpecialAbility2_var.get():
        ability2 = "AllBattlefield"

    card = Card("CustomCard", attack, defense, life, ability1, ability2, numElements)
    cost = round(card.costDetermination(), 2)
    resultLabel.config(text=f"Total Cost: {cost}")


root = tk.Tk()
root.title("Cost Evaluation for Elemental's")

attackLabel = tk.Label(root, text="Attack:", width=20)
attackLabel.grid(row=1, column=0, sticky=tk.W)
defenseLabel = tk.Label(root, text="Defense:", width=20)
defenseLabel.grid(row=1, column=1, sticky=tk.W)
lifeLabel = tk.Label(root, text="Life:", width=20)
lifeLabel.grid(row=1, column=2, sticky=tk.W)
numElementsLabel = tk.Label(root, text="Num. Elements:", width=20)
numElementsLabel.grid(row=1, column=3, sticky=tk.W)

attackEntry = tk.Entry(root, width=10)
attackEntry.grid(row=2, column=0)
defenseEntry = tk.Entry(root, width=10)
defenseEntry.grid(row=2, column=1)
lifeEntry = tk.Entry(root, width=10)
lifeEntry.grid(row=2, column=2)
numElementsEntry = tk.Entry(root, width=10)
numElementsEntry.grid(row=2, column=3)

# Variables to store checkbox states
noSpecialAbility_var = tk.IntVar()
singleTargetSpecialAbility1_var = tk.IntVar()
singleTargetSpecialAbility2_var = tk.IntVar()
singleBattlefieldSpecialAbility1_var = tk.IntVar()
singleBattlefieldSpecialAbility2_var = tk.IntVar()
entireBattlefieldSpecialAbility1_var = tk.IntVar()
entireBattlefieldSpecialAbility2_var = tk.IntVar()

noSpecialAbility = tk.Checkbutton(root, text="No Ability's", variable=noSpecialAbility_var)
noSpecialAbility.grid(row=3, column=0, sticky=tk.W)
singleTargetSpecialAbility1 = tk.Checkbutton(root, text="Single Target, Ability 1", variable=singleTargetSpecialAbility1_var)
singleTargetSpecialAbility1.grid(row=4, column=0, sticky=tk.W)
singleTargetSpecialAbility2 = tk.Checkbutton(root, text="Single Target, Ability 2", variable=singleTargetSpecialAbility2_var)
singleTargetSpecialAbility2.grid(row=4, column=1, sticky=tk.W)
singleBattlefieldSpecialAbility1 = tk.Checkbutton(root, text="Target Single Battlefield, Ability 1", variable=singleBattlefieldSpecialAbility1_var)
singleBattlefieldSpecialAbility1.grid(row=5, column=0, sticky=tk.W)
singleBattlefieldSpecialAbility2 = tk.Checkbutton(root, text="Target Single Battlefield, Ability 2", variable=singleBattlefieldSpecialAbility2_var)
singleBattlefieldSpecialAbility2.grid(row=5, column=1, sticky=tk.W)
entireBattlefieldSpecialAbility1 = tk.Checkbutton(root, text="Target Entire Battlefield, Ability 1", variable=entireBattlefieldSpecialAbility1_var)
entireBattlefieldSpecialAbility1.grid(row=6, column=0, sticky=tk.W)
entireBattlefieldSpecialAbility2 = tk.Checkbutton(root, text="Target Entire Battlefield, Ability 2", variable=entireBattlefieldSpecialAbility2_var)
entireBattlefieldSpecialAbility2.grid(row=6, column=1, sticky=tk.W)

submitButton = tk.Button(root, text="Calculate", command=calculateCost)
submitButton.grid(row=7, column=1)

resultLabel = tk.Label(root, text="Total Cost: ")
resultLabel.grid(row=8, column=1)

root.mainloop()
