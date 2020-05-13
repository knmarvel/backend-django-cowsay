import subprocess

def cow_translator(text, cow_version):
    """Takes text and the name of the cow we want to display
    and runs it through the terminal command line and then 
    returns the string from the commandline"""
    display_text = subprocess.Popen(f"cowsay -f {cow_version} {text}", shell=True, stdout=subprocess.PIPE).stdout.read()
    return display_text.decode('utf8')