sessionss=expInfo['session']
partss=expInfo['participant']

# initialize variables and read in files
import csv
import random
import os
score=0
msg="$%.2f" %(score)
key=[]
message="fail"
massage="fail"
iterd=1

condss= list(csv.reader(open('conditions.csv',"rU")))
condss=condss[1:4]
condss=random.sample(condss,3)
capitalss= list(csv.reader(open('capital.csv',"rU")))
capitals=[]
for i in range(len(capitalss)):
  if capitalss[i]==['0']:
    capitals.append(0)
  else:
    capitals.append(1)

picturess=list(csv.reader(open('test2.csv',"rU")))
pictures=picturess[1:26]
zBack=list(csv.reader(open('zeroback.csv',"rU")))
zBack=zBack[1]
matches= list(csv.reader(open('matches.csv',"rU")))
matched=matches[1:22]
pics= list(csv.reader(open('test2.csv',"rU")))
corAn="1"
order= list(csv.reader(open('order.csv',"rU")))
order=random.sample(order,4)
ord=-1
col="white"
logButton=[]
logType=[]
logCond=[]
logBlock=[]
logTrial=[]
logWord=[]
logCaps=[]
logRT=[]
logAcc=[]
logTarget=[]
logFixOn=[]
logStimOn=[]
logStimOff=[]
logFixOff=[]
logDeltaMoney=[]
logTotalMoney=[]
logReward=[]
logLoss=[]
logMessage=[]
logMessage2=[]
logMessage3=[]
logColorr=[]
logCorAn=[]
logRating=[]
Block=0
message2=""
colorr=""
message3=""

# so, we will need loops for 1)trials, 2)sessions, and 3)blocks
# this begins the block loop
for i in range(4):
  itt=0
  ord=ord+1
  typee=order[ord]
  condss=random.sample(condss,3)
  iteration=0
  Block=Block+1

  ## now begins the sessions loop
  for j in range(3):
    iteration=0
    cond=condss[itt]
    if typee==['A']:
      if cond==['win']:
        reward=.25
        loss=0
        message="3-back"
        message2="win 25c"
        message3=""
        colorr="green"
      elif cond==['lose']:
        reward=0
        loss=-.25
        message="3-back"
        message2="lose 25c"
        message3=""
        colorr="red"
      elif cond==['nothing']:
        reward=0
        loss=0
        message="3-back"
        message2="no win, no lose"
        message3=""
        colorr="white"
    elif typee==['B']:
      if cond==['win']:
        reward=.25
        loss=0
        message="0-back"
        message3="Target = 'Corn'"
        message2="win 25c"
        colorr="green"
      elif cond==['lose']:
        reward=0
        loss=-.25
        message="0-back"
        message3="Target = 'Corn'"
        message2="lose 25c"
        colorr="red"
      elif cond==['nothing']:
        reward=0
        loss=0
        message="0-back"
        message2="no win, no lose"
        message3="Target = 'Corn'"
        colorr="white"

    itt=itt+1
    match=random.sample(matched,21)
    match.insert(0,['no'])
    match.insert(1,['no'])
    match.insert(2,['no'])
    pictures=random.sample(pictures,24)
    TrialN=0
    capitals=random.sample(capitals,len(capitals))

    ### now begins the trials loop
    for k in range(24):
      cap=capitals[iteration]
      fourBackFull=keyFull
      fourBack=fourBackFull[cap]
      keyFull=twoBackFull
      key=keyFull[cap]
      twoBackFull=previousFull
      twoBack=twoBackFull[cap]
      previousFull=curPicFull
      previous=previousFull[cap]
      currentFull=pictures[iteration]
      current=currentFull[cap]
      zeroBack=zBack[cap]
      if typee == ['A']:
        if match[iteration] == ['no']:
          curPic = current
          curPicFull=currentFull
          corAn = "1"
          while curPicFull==keyFull:
            curPicFull=random.sample(pictures,1)
            curPicFull=curPicFull[0]
            current = curPicFull[cap]
            curPic = current

        elif match[iteration] == ['one']:
          curPic = previous
          curPicFull=previousFull
          corAn = "1"
          while curPicFull==keyFull:
            curPicFull=random.sample(pictures,1)
            curPicFull=curPicFull[0]
            current=curPicFull[cap]
            curPic = current

        elif match[iteration] == ['two']:
          curPic = twoBack
          curPicFull = twoBackFull
          corAn = "1"
          while curPicFull==keyFull:
            curPicFull=random.sample(pictures,1)
            curPicFull=curPicFull[0]
            current=curPicFull[cap]
            curPic = current

        elif match[iteration] == ['four']:
          curPic = fourBack
          curPicFull=fourBackFull
          corAn = "1"
          while curPicFull==keyFull:
            curPicFull=random.sample(pictures,1)
            curPicFull=curPicFull[0]
            current=curPicFull[cap]
            curPic = current

        elif match[iteration] == ['yes']:
          curPic = key
          curPicFull = keyFull
          corAn = "4"
      elif typee == ['B']:
        if match[iteration] == ['yes']:
          curPic = zeroBack
          curPicFull=zBack
          corAn = "4"
        else:
          curPicFull=currentFull
          while curPicFull==zBack:
            curPicFull=random.sample(pictures,1)
            curPicFull=curPicFull[0]

          curPic = curPicFull[cap]
          corAn = "1"

      if typee==['A']:
        logType.append(3)
      elif typee==['B']:
        logType.append(0)

      if cond==['win']:
        logCond.append("win")
      elif cond==['lose']:
        logCond.append("lose")
      elif cond==['nothing']:
        logCond.append("nothing")

      logBlock.append(Block)
      TrialN=TrialN+1
      logTrial.append(TrialN)
      logWord.append(curPic)
      if cap==0:
        logCaps.append("lower")
      elif cap==1:
        logCaps.append("upper")

      if match[iteration]==['yes']:
        logTarget.append("target")
      else:
        logTarget.append("non-target")

      iteration=iteration+1

      logReward.append(reward)
      logLoss.append(loss)
      logMessage.append(message)
