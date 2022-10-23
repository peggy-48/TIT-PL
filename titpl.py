global listvar
listvar = []
global intvar
intvar = {}
global varlst
varlst = []
import sys
class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'
# Here starts the Tacx Interpretor Tool (TIT)
def evaluatefile(file):
   loop = 0
   cvar=0
   markervar=0
   m=[]
   a = open(file).readlines()
   for i in a:
       m.append(str(i).strip('[]').replace("\n", ""))
   for i in m:
      loop += 1
      nonparsed=str(i).strip('[]')
      distilled=nonparsed.replace(";", "")
      try:
          x=str(i).strip('[]').split(" ")
      except:
             pass
      if ';' in str(i).strip('[]'): # Yes we actually need the comma
       if nonparsed[len(nonparsed)-1] == ";": # We will be sure there is a comma at THE RIGHT PLACE
        if x == "define":
         markervar = True
        elif markervar:
           varlst.append(distilled) # Generally little sneak thing: The name of the var is in fact ;x but we fixed it with replace! (this solution is deprecated since distilled is used!)
           markervar=0
        elif distilled in varlst:
            markervar="mz"
            cvar=distilled
        elif markervar == "mz":
            if distilled == "=":
             markervar="stayalert"
        elif markervar == "stayalert":
            if distilled.isdigit():
             intvar[cvar] == distilled
            else:
                 print(bcolors.FAIL+bcolors.BOLD+"tit: line "+ str(loop)+ ": assignement not int!")
                 sys.exit()
        elif distilled == "end":
            sys.exit()
        elif distilled == "printf":
            markervar="PrintF"
        elif markervar == "PrintF":
            print(intvar[distilled])
        elif "@" in distilled:
            pass
       else:
            print(bcolors.WARNING+bcolors.BOLD+"tit: warning : line "+str(loop)+": comma incorrectly placed!")
            print(bcolors.WARNING+"passing line "+str(loop)+"\x00\x00"+bcolors.BOLD+": tit")
      else:
           print(bcolors.FAIL+bcolors.BOLD+"tit: line "+str(loop)+": no comma!")   
           sys.exit()
evaluatefile(sys.argv[1])
