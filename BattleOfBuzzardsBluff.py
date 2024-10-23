# this is going to be a simple program to capture the general features of my game

import tkinter as tk
import random

class Card(): 
    def __init__(self, name, combinedCost, picture, color1, color2=None):
        self.name = name
        self.combinedCost = combinedCost
        self.picture = picture
        self.color1 = color1
        self.color2 = color2
    # Setters/Getters
    def getName(self):
        return self.name
    def setName(self, n):
        self.name = n
    def getCombinedCost(self):
        return self.combinedCost
    def setCombinedCost(self, cc):
        self.combinedCost = cc
    def getPicture(self):
        return self.picture
    def setPicture(self, p):
        self.picture = p
    def getColor1(self):
        return self.color1
    def setColor1(self, c1):
        self.color1 = c1
    def getColor2(self):
        return self.color2
    def setColor2(self, c2):
        self.color2 = c2

class Elemental(Card):
    def __init__(self, name, combinedCost, picture, attack, defense, lifeTotal, color1, color2 = None):
        super().__init__(name, combinedCost, picture, color1, color2)
        self.attack = attack
        self.defense = defense
        self.lifeTotal = lifeTotal
    # Setters/Getters
    def setAttack(self, a):
        self.attack = a
    def getAttack(self):
        return self.attack
    def setDefense(self, d):
        self.defense = d
    def getDefense(self):
        return self.defense
    def setLifeTotal(self, lt):
        self.lifeTotal = lt
    def getLifeTotal(self):
        return self.lifeTotal
    def setColor1(self, c1):
        self.color1 = c1
    def getColor1(self):
        return self.color1
    def setColor2(self, c2):
        self.color2 = c2
    def getColor2(self):
        return self.color2

class Support(Card):
    def __init__(self, name, combinedCost, picture, ability1, ability2, color1, color2=None):
        super().__init__(name, combinedCost, picture, color1, color2)
        self.ability1 = ability1
        self.ability2 = ability2
    # Setters/Getters
    def getAbility1(self):
        return self.ability1
    def setAbility1(self, a1):
        self.ability1 = a1
    def getAbility2(self):
        return self.ability2
    def setAbility2(self, a2):
        self.ability2 = a2
    
class Objective(Support):
    def __init__(self, name, combinedCost, picture, ability1, ability2, color1, color2=None):
        super().__init__(self, name, combinedCost, picture, ability1, ability2, color1, color2)
    
class Augment(Support):
    def __init__(self, name, combinedCost, picture, ability1, ability2, color1, color2=None):
        super().__init__(self, name, combinedCost, picture, ability1, ability2, color1, color2)

class Battlefield():
    def __init__(self, elementalSlots, supportSlots, objectiveSlot, augmentationSlots):
        self.elementalSlots = elementalSlots
        self.supportSlots = supportSlots
        self.objectiveSlots = objectiveSlot
        self.augmentationSlots = augmentationSlots



