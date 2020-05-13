import subprocess

def cow_translator(text, cow_version):
    """Takes text and the name of the cow we want to display
    and runs it through the terminal command line and then 
    returns the string from the commandline"""
    cla = "cowsay -f " + cow_version + " " + text
    display_text = subprocess.check_output(cla, shell=True)
    return display_text.decode('utf8')

print(cow_translator("moo","dragon"))