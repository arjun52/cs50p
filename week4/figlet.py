from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
font = figlet.getFonts()
if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(font))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv["font"] and sys.argv[2] in font):
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("bad")
ok = input("input:")
print(figlet.renderText(ok))
