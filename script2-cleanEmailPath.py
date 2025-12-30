import sys

print(r"""
 __  __             ___  ____                      
|  \/  | __ _  ___ / _ \/ ___|                     
| |\/| |/ _` |/ __| | | \___ \                     
| |  | | (_| | (__| |_| |___) |                    
|_|__|_|\__,_|\___|\___/|____/       _   _         
 / ___| | ___  __ _ _ __ |  _ \ __ _| |_| |__  ___ 
| |   | |/ _ \/ _` | '_ \| |_) / _` | __| '_ \/ __|
| |___| |  __/ (_| | | | |  __/ (_| | |_| | | \__ \
 \____|_|\___|\__,_|_| |_|_|   \__,_|\__|_| |_|___/

The script1 must be used before you use the script2. 

Version:12.2025
Author:bobre
___________________________________________________

""")


# Check input arguments
if len(sys.argv) != 3:
    print("ERROR - Veuillez fournir le fichier d'entrée et le fichier de sortie.")
    print("Command to do : python3 script2-cleanEmailPath.py mailPathList.txt mailClearedPathList.txt")
    sys.exit(1)

# Names for input and ouput files
input_file = sys.argv[1]
output_file = sys.argv[2]

# Function to clean the paths
def transformer_chemin(chemin):
    parties = chemin.strip().split('/')
    resultat = []
    for partie in parties:
        if partie.endswith('.mbox') or partie.endswith('.emlx'):
            if partie.endswith('.mbox'):
                resultat.append(f'"{partie[:-5]}"')  # Remove .mbox and add quotes
            else:
                resultat.append(partie)  # Keep filename .emlx
    return '/' + '/'.join(resultat)

# Read input file and write output file
try:
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
        for ligne in f_in:
            # Ignore empty lines
            if ligne.strip():
                chemin_transforme = transformer_chemin(ligne)
                f_out.write(chemin_transforme + '\n')
    print(f"OK - Clean paths wrote in the file {output_file}")
    print("OK -Please use the script3")
except FileNotFoundError:
    print(f"ERROR - The file {input_file} doesn't exist")
except Exception as e:
    print(f"ERROR : {e}")
