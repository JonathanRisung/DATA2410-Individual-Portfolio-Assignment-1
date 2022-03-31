# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 16:54:58 2022

@author: Jonathan
"""

import random


def erling(a, b = None):
    good_things = ["fish", "play", "chill", "sleep", "fight", "hunt", "hugg"]
    bad_things = ["eat", "complain", "build", "think"]
    
    good_responses = ["Allons y! Yeah, I love {}!", "Sure, I haven't been {} in a while!"]
    bad_responses = ["Do we have to? I don't really like {}...", "Bro, I would.. But like.. {}? Really?"]
    neutral_responses = ["I'm in!", "Sure, let me just pack my things first!"]
    
    if a in good_things:
        return good_responses[random.randrange(2)].format(a + "ing")
    elif a in bad_things:
        return bad_responses[random.randrange(2)].format(a + "ing")
    
    return neutral_responses[random.randrange(2)]


def sebastian(a, b = None):
    good_things = ["play", "hugg", "hunt", "eat", "cry", "think"]
    bad_things = ["sleep", "build", "fish"]
    
    if a in good_things:
        return "{}? Cool suggestion, I'm comming through!".format(a + "ing")
    elif a in bad_things:
        return "Can't we just do some {} instead?".format(good_things[random.randrange(6)] + "ing")
        
    return "Yeah, sure. I'm game for {}".format(a + "ing")


def dan(a, b = None):
    responses = ["You're bad at comming up with stuff to do.. {}? Let's just watch a movie.", "Actually, Im quite tired. Also I went {} with my sister earlier."]
    
    return responses[random.randrange(1)].format(a + "ing")



def enrique(a, b = None):
    good_things = ["play", "chill", "build", "eat", "sleep", "hugg", "cry", "complain", "bowl"]
    neutral_things = ["fish"]
    
    if b is None:
        return "Bro, idk.. Just give us some options though"
    
    if a not in good_things:
        if b in good_things:
            return "I'm not so sure about the first one, but I'm all in on {}".format(b + "ing")
        if a in neutral_things:
            return "{} sound alright.".format(a + "ing")
        if b in neutral_things:
            return "If anything {} sounds like the best option.".format(b + "ing")
        
    if a in good_things:
        return "{} sounds like fun!".format(a + "ing")
        
    return "Yeah, I'm not really feeling it."
    
    
"""
action = random.choice(["play", "chill", "fish", "eat", "sleep", 
                        "cry", "hugg", "complain", "fight", "build", "hunt", 
                        "bowl", "think"])


print("\nMe: Do you guys want to {}? \n".format(action)) 
print("Erling: {}".format(erling(action))) 
print("Sebastian: {}".format(sebastian(action))) 
print("Dan: {}".format(dan(action))) 
print("Enrique: {}".format(enrique(action))) 
"""