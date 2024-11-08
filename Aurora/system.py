import os

def title(title):
    os.system(f'title {title}' if os.name == 'nt' else f'echo -ne "\033]0;{title}\007"')
    
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    