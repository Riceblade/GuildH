from time import sleep
import replit
import random

replit.clear()

#variabels

def loading():

  porcent = 0
  loading = True
  loadingtime = random.uniform(0.1,  0.9)

  while loading == True:
      print ("""Loading...\n
      [""", porcent, "%]\n")
      sleep (0.3)
      porcent = porcent + 1
      replit.clear()

      if porcent == 100:
        replit.clear()
        print("first download done...")
        sleep (2)
        porcent = 0

loading()