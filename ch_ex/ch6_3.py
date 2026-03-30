glossary = {
    'int' : 'a whole number',
    'loop' : 'a repetition of instructions until a condition is met',
    'condition' : 'a set of instructions to be run if a statement evaluates to true and to be skipped if False',
    'IDE' : 'text editor with built in developpement tools',
    'boolean' : 'Datatype that evaluates to True or False',
}

for word, meaning in glossary.items() :
    print(f"{word.upper()} : ")
    print("\t"+meaning)