#!/usr/bin/env python

KNOB_DICT_FILENAME='swis_knobs.txt'
KEYFILE_LIST_FILENAME='install_server_tword.txt'

knobDict = {}
keyFilenames = [ ]

with open(KEYFILE_LIST_FILENAME) as knobFile:
     #Remove comments
     lines =  (l for l in knobFile if not l.startswith('#'))
     #Remove blank lines
     lines = [line for line in lines if line.strip()]
     for line in  lines:
         (key, val) = line.split()
         knobDict[key] = val

with open(KNOB_DICT_FILENAME) as keyFile:
     #Remove comments
     lines =  (l for l in keyFile if not l.startswith('#'))
     #Remove blank lines
     keyFilenames = [line for line in lines if line.strip()]

dataToParse = ''

for keyFile in keyFilenames:
     with open(keyFile.strip(),'r') as CurrentKeyFile:
          dataToParse = CurrentKeyFile.read()
     #print "knobDict: %s" % knobDict
     for key in knobDict:
         #Exceptional case with ITECNODE key
         if key == "ITECNODE":
             dataToParse = dataToParse.replace('itec_swis_%instance%',str(knobDict[key]))
         #Other keys
         else:    
             dataToParse = dataToParse.replace('%'+str(key)+'%',str(knobDict[key]))
             #print "key: %s" % key
     with open(keyFile.strip(),'w') as CurrentKeyFile:
          CurrentKeyFile.write(dataToParse)

