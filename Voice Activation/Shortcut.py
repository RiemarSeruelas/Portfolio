import speech_recognition as sr
import subprocess
import AppOpener
import time


recognizer = sr.Recognizer()

def voice_listener():
    with sr.Microphone() as source:
        print("Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Voice assistant running... Say 'Open' to activate.")

        while True:
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                text = recognizer.recognize_google(audio)
                print("You said:", text)

                text_lower = text.lower()

                if "open" in text_lower:

                    if "impact" in text_lower:
                        AppOpener.open("Genshin Impact")

                    elif "roblox" in text_lower:
                        AppOpener.open("Roblox Player")

                    elif "and" in text_lower:
                        AppOpener.open("GRYPHLINK")

                    elif "chaos" in text_lower:
                        AppOpener.open("Chaos Zero Nightmare")

                    elif "minecraft" in text_lower:
                        AppOpener.open("Minecraft Launcher")

                    elif "steam" in text_lower:
                        AppOpener.open("Steam")

                    elif "nowhere" in text_lower:
                        AppOpener.open("LDPlayer")
                        
                    elif "spotify" in text_lower:
                        AppOpener.open("Spotify")       
                    
                    elif "discord" in text_lower:
                        AppOpener.open("Discord")
                        
                    elif "wallpaper" in text_lower:
                        AppOpener.open("Wallpaper Engine")  
                    
                    elif "canva" in text_lower:
                        subprocess.Popen([                
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        "--profile-directory=Profile 4",
                        "https://www.canva.com"
                  ])
                        
                    elif "messenger one" in text_lower or "messenger 1" in text_lower:
                        subprocess.Popen([                
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        "--profile-directory=Profile 1",
                        "https://www.messenger.com" 
                  ])
                        
                    elif "messenger two" in text_lower or "messenger 2" in text_lower:
                        subprocess.Popen([                
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        "--profile-directory=Profile 2",
                        "https://www.messenger.com" 
                  ])
                        
                    elif "messenger three" in text_lower or "messenger 3" in text_lower:
                        subprocess.Popen([                
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        "--profile-directory=Profile 3",
                        "https://www.messenger.com" 
                  ])    
                        
                    elif "mail one" in text_lower or "mail 1" in text_lower:
                        subprocess.Popen([                
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        "--profile-directory=Profile 1",
                        "https://gmail.google.com"
                ])
                        
                    elif "mail two" in text_lower or "mail 2" in text_lower:
                        subprocess.Popen([                
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        "--profile-directory=Profile 2",
                        "https://gmail.google.com"
                ])
                        
                    elif "mail three" in text_lower or "mail 3" in text_lower:
                        subprocess.Popen([                
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        "--profile-directory=Profile 3",
                        "https://gmail.google.com"
                ])
                        
                    elif "x" in text_lower:
                        subprocess.Popen([                
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        "--profile-directory=Profile 1",
                        "x.com"
                ])
                    
                    elif "youtube one" in text_lower or "youtube 1" in text_lower:
                        subprocess.Popen([                
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        "--profile-directory=Profile 1",
                        "https://www.youtube.com"
                ])
                        
                    elif "youtube two" in text_lower or "youtube 2" in text_lower or "youtube to" in text_lower:
                        subprocess.Popen([                
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        "--profile-directory=Profile 2",
                        "https://www.youtube.com"
                ])
                        
                    elif "youtube three" in text_lower or "youtube 3" in text_lower:
                        subprocess.Popen([                
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        "--profile-directory=Profile 3",
                        "https://www.youtube.com"
                ])
                        
                    elif "insta 1" in text_lower or "insta one" in text_lower:
                        subprocess.Popen([                
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        "--profile-directory=Profile 1",
                        "https://www.instagram.com"
                ])
                        
                    elif "insta 2" in text_lower or "insta two" in text_lower:
                        subprocess.Popen([                
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        "--profile-directory=Profile 5",
                        "https://www.instagram.com" 
                ])
                        
                    else:
                        print("App not recognized.")

                    print("Waiting for wake word again...")
                    time.sleep(3)

            except sr.WaitTimeoutError:
                continue

            except sr.UnknownValueError:
                continue

            except sr.RequestError as e:
                print("Speech recognition error:", e)

if __name__ == "__main__":
    voice_listener()