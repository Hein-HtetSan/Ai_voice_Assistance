## Ai voice assistance (Python)
### Libaray and Packages
- pyttsx3   **`pip install pyttsx3`**
- datetime
- speech_recognition **`pip install SpeechRecognition`**
- wikipedia **`pip install wikipedia`**
- smtplib **`pip install smtplib`**
- webbroswer **`pip install webbroswer`**
- os
- pyautogui **`pip install pyautogui`**
- psutil **`pip install psutil`**
- pyjokes **`pip install pyjokes`**
___

### Usage and packages
**pyttsx3** module   **[voice]**
Initialize the pytssx3
>`engine = pyttsx3.init()`<br>
>`engine.say(something)`<br>
>`engine.runAndWait()`<br>

**setting voice rate and speed**
>`voices = engine.getProperty('voices')`
>`engine.setProperty('voices', voices[0].id)`
>`newVoiceRate = 190`
>`engine.setProperty('rate', newVoiceRate)`

**datetime** module
>`time = datetime.datetime.now().strftime("%I:%M:%S")`
>`year = datetime.datetime.now().year`
>`month = datetime.datetime.now().month`
>`day = datetime.datetime.now().day`

**speech_recognition** module **[Microphone]**
>`r = sr.Recognizer()`
>`with sr.Microphone() as source:`
>`r.pause_threshold = 1`
>`audio = r.listen(source)`
>`try:`

>>`query = r.recognize_google(audio) #you need internet connection` 
 
>`except Exception as e:`
 
>>`print(e)`
>`return query #we need to return if inside the function`

**smtplib** module **[Send Mail]**
>`smtp_server = "smpt.gmail.com"`
>`port = 587    #port name as 587` 
>`sender_email = "xyz@gmail.com"`
>`sender_password = 12345`
>`context = ssl.create_default_context()`

>`try:`

>>`server = smtplib.SMTP(smtp_server, port)`
>>`server.ehlo()`
>>`server.starttls(context=context)`
>>`server.ehlo()`
>>`server.login(sender_email, sender_password)`
>>`server.sendmail(sender_email, receiver_email, message)`

>`except Exception as e:`

>>`print(e)`

>`finally:`

>>`server.quit()`

**pyautogui** module **[Screenshot]**
>`img = pyautogui.screenshot()`
>`img.save(your path)`

**psutil** module **[CPU and Battery]**
**CPU**
>`usage = str(psutil.cpu_percent())`
>`print(usage) `

**Battery**
>`battery = psutil.sensors_battery()`
>`print(battery.percent)`

**pyjokes** module **[telling jokes]**
>`pyjokes.get_joke()`

**webbroswer** module **[Web broswer]**
>`webbroswer as `**`wb`**
>`chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"`
>`wb.register('chrome', None, wb.BackgroundBroswer(chromepath))`
>`wb.get('chrome').open_new_tab( link )`

**os** module **[OS]**
- **Logout**
>`os.system("shutdown -l)`
- **Restart**
>`os.system("shutdown /r /t 1")`
- **Shutdown**
>`os.system("shutdown /s /t 1")`
- **Play Song**
>`song_dir = "D:\Music" or [path]`
>`songs = os.listdir(song_dir)`
>`os.startfile(os.path.join(song_dir,songs[0])`

**wikipedia** module **[Search on Wikipedia ]**
>`query = query.replace("wikipedia", "")`
 *[query is from speak() if you say something and return that into query]*
>`res = wikipedia.summary(query)`
>`print(res)`
___
### Functions
- speak()
- time()
- date()
- greeting()
- takeCommand()
- sendEmail()
- screen_shot()
- cpu() and battery()
- jokes()
- playSong()
- wikipedia()
- webBroswer()
- logout(), restart() and shutdown()
___


> **Just for Practice and Notes**
> 
<b> If you like it, ***like and follow*** me </b> :)