from datetime import datetime, timedelta
import random
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

#This twitter bot is very similar to the MHRise-Hunt-Chooser (https://github.com/Vhou-Atroph/MHRise-Hunt-Chooser), but is on Twitter (not an application to be downloaded- more likely to be looked at).
#Honestly it's mostly a fun little project to see how clean I can make my code (not very!) and if my raspberry pi can handle both a media server and a funky cool twitter bot. I'd hope it does!
'''
CONTRIBUTORS:
- Vhou-Atroph
'''

def wepAndBud():
    weapons=['a Hammer','a Charge Blade','a Greatsword','a Hunting Horn','a Longsword','a Lance','a Gunlance','an Insect Glaive','a Switch Axe','a Dual Blades','a Sword and Shield','a Bow','a Light Bowgun','a Heavy Bowgun']
    buddies=['no buddy','a palico','a palamute']
    wep=random.choice(weapons)
    bud=random.choice(buddies)
    global hunterChoices
    hunterChoices=[wep,bud]

def hunt():
    huntTypes=['Low Rank','High Rank']
    rank=random.choice(huntTypes)
    print("This hunt will be:",rank)
    if rank=="Low Rank":
        monsterPool=['Aknosom','Almudron','Anjanath','Arzuros','Barioth','Barroth','Basarios','Bishaten','Diablos','Goss Harag','Great Baggi','Great Izuchi','Great Wroggi','Khezu','Kulu-Ya-Ku','Lagombi','Magnamalo','Mizutsune','Nargacuga','Pukei-Pukei','Rathalos','Rathian','Royal Ludroth','Somnacanth','Tetranadon','Tigrex','Tobi-Kadachi','Volvidon','Zinogre']
    else:
        monsterPool=['Aknosom','Almudron','Anjanath','Arzuros','Apex Arzuros','Barioth','Barroth','Basarios','Bazelgeuse','Bishaten','Chameleos','Diablos','Apex Diablos','Goss Harag','Great Baggi','Great Izuchi','Great Wroggi','Jyuratodus','Khezu','Kulu-Ya-Ku','Kushala Daora','Lagombi','Magnamalo','Mizutsune','Apex Mizutsune','Nargacuga','Pukei-Pukei','Rajang','Rakna-Kadaki','Rathalos','Apex Rathalos','Rathian','Apex Rathian','Royal Ludroth','Somnacanth','Teostra','Tetranadon','Thunder Serpent Narwa','Narwa the Allmother','Tigrex','Tobi-Kadachi','Crimson Glow Valstrax','Volvidon','Wind Serpent Ibushi','Zinogre','Apex Zinogre']
    monster=random.choice(monsterPool)
    print("The monster hunted will be:",monster)
    
    hunters=random.randint(1,4)
    print("There will be",hunters,"players on the hunt.")
    if hunters==1:
        wepAndBud()
        p1=hunterChoices
        print("The lone hunter will be using a",p1[0],"and bring",p1[1])
    if hunters==2:
        wepAndBud()
        p1=hunterChoices
        wepAndBud()
        p2=hunterChoices
        print("Player one will be using a",p1[0],"and bring",p1[1],"\nPlayer two will be using a",p2[0],"and bring",p2[1])
    if hunters==3:
        wepAndBud()
        p1=hunterChoices
        wepAndBud()
        p2=hunterChoices
        wepAndBud()
        p3=hunterChoices
        print("Player one will be using a",p1[0],"and bring",p1[1],"\nPlayer two will be using a",p2[0],"and bring",p2[1],"\nPlayer three will be using a",p3[0],"and bring",p3[1])
    if hunters==4:
        wepAndBud()
        p1=hunterChoices
        wepAndBud()
        p2=hunterChoices
        wepAndBud()
        p3=hunterChoices
        wepAndBud()
        p4=hunterChoices
        print("Player one will be using a",p1[0],"and bring",p1[1],"\nPlayer two will be using a",p2[0],"and bring",p2[1],"\nPlayer three will be using a",p3[0],"and bring",p3[1],"\nPlayer four will be using a",p4[0],"and bring",p4[1])
        
    print('----------')
    
    #Tweet writing
    twt1=open("txt/lasthunt1.txt","w",encoding="utf-8") #First tweet
    actions=["causing a disaster!","being a nuisance!","that looked at me wrong.","cyberbullying me!","that I want dead.","that would make a cool pet!","that I want to wear.","out there!","being mean to the Kelbi!"]
    action=random.choice(actions)
    line1="There's a "+rank+" "+monster+" "+action+"\n" #Commas weren't working 🙃
    canDoIts=["can take care of it!","can take care of it.","should be able to handle it!","should be enough!","would suffice.","would be sufficient."]
    canDoIt=random.choice(canDoIts)
    if hunters==1:
        line2="I think a lone hunter "+canDoIt+"\n"
    else:
        line2="I think "+str(hunters)+" hunters "+canDoIt+"\n"
    print(line1)
    print(line2)
    twt1.write(line1+line2)
    twt1.close()
    
    twt2=open("txt/lasthunt2.txt","w",encoding="utf-8") #Second tweet, a reply to the first tweet
    line1="If you want my recommendations on what to bring:\n"
    if hunters==1:
        line2="Hunter 1 should bring "+p1[0]+" and "+p1[1]
    if hunters==2:
        line2="Hunter 1 should bring "+p1[0]+" and "+p1[1]+"\nHunter 2 should bring "+p2[0]+" and "+p2[1]
    if hunters==3:
        line2="Hunter 1 should bring "+p1[0]+" and "+p1[1]+"\nHunter 2 should bring "+p2[0]+" and "+p2[1]+"\nHunter 3 should bring "+p3[0]+" and "+p3[1]
    if hunters==4:
        line2="Hunter 1 should bring "+p1[0]+" and "+p1[1]+"\nHunter 2 should bring "+p2[0]+" and "+p2[1]+"\nHunter 3 should bring "+p3[0]+" and "+p3[1]+"\nHunter 4 should bring "+p4[0]+" and "+p4[1]
    print(line1)
    print(line2)
    twt2.write(line1+line2)
    twt2.close()
    
    '''#Post the tweet
    twt1=open("txt/lasthunt1.txt","r")
    monDeclaration=api.update_status(twt1.read())
    twt1.close()
    twt2=open("txt/lasthunt2.txt","r")
    gearRecs=api.update_status(twt2.read(),in_reply_to_status_id=monDeclaration.id,auto_populate_reply_metadata=True)
    twt2.close()'''
    
hunt()

'''while 1:
    print("Generating a hunt!")
    hunt()

    dt = datetime.now() + timedelta(hours=1)
    dt = dt.replace(minute=30)

    while datetime.now() < dt:
        time.sleep(1)'''