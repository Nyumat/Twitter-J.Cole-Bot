import os

def getRequired():
    
    print(f'Installing Libraries')
    
    os.system('pip install tweepy')
    os.system('pip install logging')
    os.system('pip install requests')
    os.system('pip install sys')
    os.system('pip install regex')
    os.system('pip install bs4')
    os.system('pip install lxml')
    

def install():
    getRequired()
    print(f'Required Libraries now installed.')
    
print(f'Install Required Libraries [y/n]?')

input = input(">> ")

if input == 'y':
    install()
else:  
    os._exit(0)
    