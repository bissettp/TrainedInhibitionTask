"""
runprobContextTask
"""

from psychopy import core, event
import smtplib
import json
import webbrowser
from prob_context_task import probContextTask
from make_config import makeConfigList, makePracticeConfigList, makeFullInfoPracticeConfigList
from test_bot import test_bot
import glob
from Load_Data import load_data

#set-up some variables

verbose=True
fullscr= True
subdata=[]
practice_on = True
task_on = True
test_on = True
#fullInfo refers to instructions and practice where subjects are explicitely
#told that they either have to pay attention to color OR shape.
fullInfo = True
bot_on = False
bot_mode = "ignore_base" #other for optimal

# set things up for practice, training and tests
try:
    f = open('IDs.txt','r')
    lines = f.readlines()
    f.close()
    last_id = lines[-1][:-1]
    subject_code = raw_input('Last subject: "%s". Input new subject code: ' % last_id);
except IOError:
    subject_code = raw_input('Input first subject code: ');
f = open('IDs.txt', 'a')
f.write(subject_code + '\n')
f.close()

#set up some task variables ##PB: might consider using train and test for all the following variables instead of test and task sometimes. 
train_mins = 45 #train_length in minutes
test_mins = 30 #test_length in minutes
avg_test_trial_len = 2.25 #in seconds
avg_task_trial_len = avg_test_trial_len + 1 #factor in FB
#Find the minimum even number of blocks to last at least train_length minutes
task_len = int(round(train_mins*60/avg_task_trial_len/4)*4) # Prominent theories in memory assume that instances are the unit of learning, which would argue for having the same number of trials for each subject and not the same amount of time for each subject
test_len = int(round(test_mins*60/avg_test_trial_len/4)*4)
recursive_p = .9
if fullInfo:
    taskname = 'Prob_Context_FullInfo'
else:
    taskname = 'Prob_Context'


#set up config files
practice_config_file = '../Config_Files/Prob_Context_Practice_config.npy'
task_config_file = makeConfigList(taskname = taskname, iden = subject_code, exp_len = task_len, recursive_p = recursive_p)

if fullInfo == False:
    practice_config_file = makePracticeConfigList(taskname = taskname + '_Practice')
else:
    practice_config_file = makeFullInfoPracticeConfigList(taskname = taskname + '_Practice')
practice=probContextTask(practice_config_file,subject_code, fullscreen = fullscr, mode = 'practice')

task=probContextTask(task_config_file,subject_code, fullscreen = fullscr)
if bot_on == True:
    task.setBot(bot = test_bot(task_config_file, mode = bot_mode), mode = "full")
task.writeToLog(task.toJSON())



#************************************
# Start Practice
#************************************

if practice_on:
    # prepare to start
    practice.setupWindow()
    practice.defineStims()
    if fullInfo == False:
        task_intro_text = [
            'Welcome\n\nPress 5 to move through instructions',
            """
            This experiment starts with a training phase followed by a testing phase.
            Training will last about 45 minutes and testing will last 30 minutes.
            
            Your performance on the training AND test phase determines your bonus payment. 
            To perform well on the test phase you'll need to stay
            motivated and learn as much as possible in the training phase.
            """,
            """
            In the training phase, shapes will appear on the screen
            one at a time, and you will need to learn how to respond to them.
            
            Your responses will consist of one of four buttons: 'd', 'f', 'j' and 'k'.
            Use your index and middle fingers on both hands to respond.
            
            The goal is to learn the best key(s) to press for each shape.
            
            Press '5' to see the four shapes that will be used in practice.
            """,
            """
            As you could see, these shapes differ in their identity (which
            shape they are) and their color.
            
            Your responses should depend on these features.
            """,
            """
            The shape's vertical position will also be changing on each trial.
            
            The best key to press in response to each shape 
            partially depends on the shape's vertical position. 
            
            After you press '5' you'll see two example trials.
            """,
            """
            After you press a key, the shape will disappear and 
            you will get a point if you responded correctly.
            
            After the training phase, there will be a test phase 
            with no feedback. You will still be earning points, and these
            test phase points will also be used to determine your bonus pay.
            
            It is therefore very important that you use the points 
            in the training phase to learn how to best respond to each shape 
            and how your response depends on the shape's vertical position.
            """,
            """
            You must respond while the shape is on the screen.
            Please respond as quickly and accurately as possible.
            
            The task is hard! Stay motivated and try to learn
            all you can.
            
            We will start with a brief practice session. 
            Please wait for the experimenter.
            """
        ]
    else:
        task_intro_text = [
            'Welcome\n\nPress 5 to move through instructions',
            """
            This experiment starts with a training phase followed by a testing phase.
            Training will last 45 minutes and testing will last 30 minutes.
            
            Your performance on the training AND test phase determines your bonus payment. 
            To perform well on the test phase you'll need to stay
            motivated and learn as much as possible in the training phase.
            """,
            """
            In the training phase, shapes will appear on the screen
            one at a time, and you will need to learn how to respond to them.
            
            Your responses will consist of one of four buttons: 'd', 'f', 'j' and 'k'.
            Use your index and middle fingers on both hands to respond.
            
            The goal is to learn the best key(s) to press for each shape.
            After you press a key, the shape will disappear and 
            you will get a point if you responded correctly.
            
            Press '5' to see the four shapes that will be used in practice.
            """,
            """
            As you could see, these shapes differ in their identity (which
            shape they are) and their color.
            
            Your responses should depend on these features. At certain points
            in the experiment you should respond based on color, and at other times
            you should respond based on identity, but not both at the same time.
            
            We will now practice responding to the shapes. For these trials,
            just pay attention to the identity of the shape when making your response.
            
            Please wait for the experimenter.
            """,
            """
            In those trials, one key worked for the pentagon, and one worked for the triangle.
            
            We'll now practice responding to the color of the shape.
            
            Please wait for the experimenter.
            """,
            """
            As you may have noticed, the shape's vertical position on the screen
            changes on each trial.
            
            The vertical position of the shape partially
            determines whether you should respond based on color or identity.
            """,
            """
            After the training phase, there will be a test phase 
            with no feedback. You will still be earning points, and these
            test phase points will also be used to determine your bonus pay.
            
            It is therefore important that you use the points 
            in the training phase to learn when to respond based on 
            the color or identity of the shapes and how your response
            depends on the shape's vertical position.
            """,
            """
            You must respond while the shape is on the screen.
            Please respond as quickly and accurately as possible.
            
            The task is hard! Stay motivated and try to learn
            all you can.
            
            We will start with a brief practice session. 
            Please wait for the experimenter.
            """
        ]
    
    for line in task_intro_text:
        practice.presentTextToWindow(line)
        resp,practice.startTime=practice.waitForKeypress(practice.trigger_key)
        practice.checkRespForQuitKey(resp)
        event.clearEvents()
        if 'used in practice' in line:
            practice.presentStims(mode = 'practice')
            resp,practice.startTime=practice.waitForKeypress(practice.trigger_key)
            practice.checkRespForQuitKey(resp)
        if "pay attention to the identity of the shape" in line:
            startTime = core.getTime()
            for trial in practice.stimulusInfo[0:12]:
                # wait for onset time
                while core.getTime() < trial['onset'] + startTime:
                        key_response=event.getKeys(None,True)
                        if len(key_response)==0:
                            continue
                        for key,response_time in key_response:
                            if practice.quit_key==key:
                                practice.shutDownEarly()
                trial=practice.presentTrial(trial)
            elapsed_time = core.getTime() - startTime
            core.wait(1)
        if "responding to the color of the shape" in line:
            startTime = core.getTime()
            for trial in practice.stimulusInfo[12:24]: #Onset time FIx!
                # wait for onset time
                while core.getTime() < trial['onset'] + startTime - elapsed_time:
                        key_response=event.getKeys(None,True)
                        if len(key_response)==0:
                            continue
                        for key,response_time in key_response:
                            if practice.quit_key==key:
                                practice.shutDownEarly()
                trial=practice.presentTrial(trial)
            elapsed_time = core.getTime() - startTime + elapsed_time
            core.wait(1)
    
    for trial in practice.stimulusInfo:
        # wait for onset time
        while core.getTime() < trial['onset'] + practice.startTime:
                key_response=event.getKeys(None,True)
                if len(key_response)==0:
                    continue
                for key,response_time in key_response:
                    if practice.quit_key==key:
                        practice.shutDownEarly()
        trial=practice.presentTrial(trial)
    
    practice.presentTextToWindow(
    """
    That's enough practice. Before we start the experiment
    press 5 to see the shapes you will have to respond to
    during the training and test phases.
    """)
    resp,task.startTime=practice.waitForKeypress(practice.trigger_key)
    task.checkRespForQuitKey(resp)
    practice.presentStims(mode = 'task')
    resp,practice.startTime=practice.waitForKeypress(practice.trigger_key)
    practice.checkRespForQuitKey(resp)
    
    # clean up
    practice.closeWindow()

#************************************
# Start training
#************************************

if task_on:
    # prepare to start
    task.setupWindow()
    task.defineStims()
    if bot_on == False:
        task.presentTextToWindow(
            """
            We will now start the experiment.
            
            There will be one break half way through. As soon
            as you press '5' the experiment will start so get ready!
            
            Please wait for the experimenter.
            """)
        resp,task.startTime=task.waitForKeypress(task.trigger_key)
        task.checkRespForQuitKey(resp)
        event.clearEvents()
    else:
        task.startTime = core.getTime()
        
    
    pause_trial = task.stimulusInfo[len(task.stimulusInfo)/2]
    pause_time = 0
    for trial in task.stimulusInfo:
        if not task.bot:
            if trial == pause_trial:
                time1 = core.getTime()
                task.presentTextToWindow("Take a break! Press '5' when you're ready to continue.")
                task.waitForKeypress(task.trigger_key)
                task.clearWindow()
                pause_time = core.getTime() - time1
        
        #if botMode = short, don't wait for onset times
        if task.botMode != 'short':
            # wait for onset time
            while core.getTime() < trial['onset'] + task.startTime + pause_time:
                    key_response=event.getKeys(None,True)
                    if len(key_response)==0:
                        continue
                    for key,response_time in key_response:
                        if task.quit_key==key:
                            task.shutDownEarly()
                        elif task.trigger_key==key:
                            task.trigger_times.append(response_time-task.startTime)
                            task.waitForKeypress()
                            continue
    
        trial=task.presentTrial(trial)
        task.writeToLog(json.dumps(trial))
        task.alldata.append(trial)
        #print('state = ' + str(trial['state'])+ ', value: ' + str(np.mean(trial['context']))) 
        
    task.writeToLog(json.dumps({'trigger_times':task.trigger_times}))
    task.writeData()
    if bot_on == False:
        task.presentTextToWindow('Thank you. Please wait for the experimenter.')
        task.waitForKeypress(task.quit_key)


    # clean up
    task.closeWindow()

#************************************
# Send text about task performance
#************************************

    if bot_on == False:   
        username = "thedummyspeaks@gmail.com"
        password = "r*kO84gSzzD4"
        atttext = "9148155478@txt.att.net"
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(username,password)
        message = "Training done."
        
        msg = """From: %s
        To: %s
        Subject: text-message
        
        %s""" % (username, atttext, message)
        server.sendmail(username, atttext, msg)
        server.quit()

#************************************
# Start test
#************************************

if test_on:
    #if experiment crashed for some reason between train and test set task_on
    #to false and the experiment will load up the parameters from the training
    if task_on == False:
        train_file = glob.glob('../RawData/' + subject_code + '*Context_20*yaml')[0]
        train_name = train_file[11:-5]
        taskinfo, df, dfa = load_data(train_file, train_name, mode = 'train')
        action_keys = taskinfo['action_keys']
        states = taskinfo['states']
        ts_order = [states[0]['ts'],states[1]['ts']] 
    else:
        action_keys = task.getActions()
        ts_order = task.getTSorder()
    test_config_file = makeConfigList(taskname = taskname + '_noFB', iden = subject_code, exp_len = test_len, 
                                      recursive_p = recursive_p, FBDuration = 0, FBonset = 0, action_keys = action_keys,
                                      ts_order = ts_order)
                                      
    test=probContextTask(test_config_file,subject_code, fullscreen = fullscr)
    if bot_on == True:
        test.setBot(bot = test_bot(test_config_file, mode = bot_mode), mode = "full")

    test.writeToLog(test.toJSON())
    
    # prepare to start
    test.setupWindow()
    test.defineStims()
    if bot_on == False:
        test.presentTextToWindow(
            """
            In this next part the feedback will be invisible. You ##Invisible seems like strange way to put it. Maybe "In the nexst part you will not receive feedback after each response"...
            are still earning points, though, and these points are
            used to determine your bonus.
            
            Do your best to respond to the shapes as you learned to
            in the last section.
            
            Please wait for the experimenter.
            """)
                            
        resp,test.startTime=test.waitForKeypress(test.trigger_key)
        test.checkRespForQuitKey(resp)
        event.clearEvents()
    else:
        test.startTime = core.getTime()
        
    pause_trial = test.stimulusInfo[len(test.stimulusInfo)/2]
    pause_time = 0
    for trial in test.stimulusInfo:
        if not test.bot:
            if trial == pause_trial:
                time1 = core.getTime()
                test.presentTextToWindow("Take a break! Press '5' when you're ready to continue.")
                test.waitForKeypress(test.trigger_key)
                test.clearWindow()
                pause_time = core.getTime() - time1
            
        #if botMode = short, don't wait for onset times
        if test.botMode != 'short':
            # wait for onset time
            while core.getTime() < trial['onset'] + test.startTime + pause_time:
                    key_response=event.getKeys(None,True)
                    if len(key_response)==0:
                        continue
                    for key,response_time in key_response:
                        if test.quit_key==key:
                            test.shutDownEarly()
                        elif test.trigger_key==key:
                            test.trigger_times.append(response_time-test.startTime)
                            continue
    
        trial=test.presentTrial(trial)
        test.writeToLog(json.dumps(trial))
        test.alldata.append(trial)
    
    test.writeToLog(json.dumps({'trigger_times':task.trigger_times}))
    test.writeData()
    if bot_on == False:
        test.presentTextToWindow('Thank you. Please wait for the experimenter.')
        test.waitForKeypress(task.quit_key)
    
    # clean up
    test.closeWindow()
    

#************************************
# Send text about task performance
#************************************

    if bot_on == False:   
        username = "thedummyspeaks@gmail.com"
        password = "r*kO84gSzzD4"
        atttext = "9148155478@txt.att.net"
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(username,password)
        message = "Testing done."
        
        msg = """From: %s
        To: %s
        Subject: text-message
        
        %s""" % (username, atttext, message)
        server.sendmail(username, atttext, msg)
        server.quit()
    
#************************************
# Determine payment
#************************************
points,trials = test.getPoints()
performance = (float(points)/trials-.25)/.75 # This seems pretty weird. What's up with this payout?
pay_bonus = round(performance*5)
print('Participant ' + subject_code + ' won ' + str(points) + ' points out of ' + str(trials) + ' trials. Bonus: $' + str(pay_bonus))

#open post-task questionnaire
if bot_on == False:
    webbrowser.open_new('https://stanforduniversity.qualtrics.com/SE/?SID=SV_9KzEWE7l4xuORIF')






