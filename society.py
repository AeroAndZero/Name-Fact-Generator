# Made By     ***    *****  *****  *****
#            *   *   *      *   *  *   *
#            *****   ***    *****  *   *
#            *   *   *      *  *   *   *
#            *   *   *****  *   *  *****

# Important Libraries
from PIL import Image, ImageDraw, ImageFont
import random

# input before execution
while True:
    name = input("Enter A Name : ")
    gender_input = input("Enter Your Gender (F for female, M for male) : ")
    if gender_input == "f" or gender_input == "F":
        heshe = "She"
        hisher = "Her"
        guygirl = "girl"
        himher = "her"
        girlguy = "guy"
        break
    elif gender_input == "m" or gender_input == "M":
        heshe = "He"
        hisher = "His"
        guygirl = "guy"
        himher = "him"
        girlguy = "girl"
        break
    else:
        print("Incorrect Gender Entered.")

# Lies
lines = [
    heshe + " is fun and playful, but has a serious side.",
    "A smart, talented and humorous "+guygirl+", who likes\nto take charge.",
    "A "+guygirl+" with a big heart.",
    "Very rare though, "+heshe +
    " is usually a very sweet\nperson and is protective when it comes to "+hisher+"\nfriends.",
    "A perfect blend of brains and strength.",
    "Someone who has many dreams and desires.",
    str(name) + "is a great listener and you can always\ntrust " +
    himher+" with anything.",
    str(name) + ", a fun energetic "+guygirl +
    ", this "+guygirl+" just\noozes charisma.",
    "A nice "+guygirl+",who respect the feelings of " +
    girlguy+"s,\ngood looking personality,charming,smart.",
    "Many ppl find "+str(name)+" rude and arrogant but\n" +
    heshe+" is the best and thus has many enemies.",
    "An attractive, charming "+guygirl+",full of joy.",
    heshe+" is a great person who will be the best friend\nyou ever had once you crack " +
    hisher+" hard outer\nshell.",
    "Romantic and charming.",
    "One of the sweetest "+guygirl+"s you will come across\nalthough\nkeep "+himher +
    " in your life when "+heshe+" comes across\nyou. You might regret leaving "+himher+".",
    str(name) + "is a very unique and interesting person.",
    str(name) + " is an amazing friend and " +
    heshe+" will always\nbe there for you.",
    str(name) + "'s have elegance, charm and good taste,\nare naturally kind, very gentle, and lovers of\nbeauty.",
    heshe+" notices when your down and always brings\nyou back up.",
    heshe + " is a kind and caring person.",
    str(name)+" is overall funny, kind, a savage,\nintelligent and just overall an amazing person.",
    hisher + " beauty over powers all the other "+guygirl+"s and\nnot only is " +
    heshe+" smoking hot but "+hisher+" style is so\ncool.",
    "Not a fan of romantic commitments but deeply\ncommitted to " +
    hisher+" fail out and friends.",
    str(name)+" is extremely smart, loving and\nknowledgeable person.",
    "The epitome of cool. Often used to denote\nsomeone whose very understanfing.",
    "Everyone likes "+himher+".",
    heshe+" has big dreams, and "+heshe+" can make them\ncome true.",
    "You want to be like this "+guygirl+", "+heshe +
    "'s just too good\nto be true. A true legend.",
    "keep "+himher+" in your life when "+heshe +
    " comes across\nyou. You might regret leaving "+himher+".",
    str(name) + " is a healer of hearts.",
    "The Kind of person who is one in million",
    str(name) + " is smart,funny and beautiful.",
    heshe+"'s smart beautiful kind and caring.",
    "Time files with a "+str(name)+", as they are simply\nmesmerizing.",
    str(name)+" has an amazing personality. Also\nfunny and fun to be around.",
    heshe+" is very funny, smart, and good at event the\nnew things "+heshe+" tries.",
    str(name)+" thinks "+heshe+"'s unattractive but every " +
    girlguy+"\n"+heshe+" walks past just stops and stares.",
    "Strong opinions but has an open mind.",
    "Usually loves hugs and respects people a lot.",
    heshe+"'s adorable, "+heshe+"'s hot, "+heshe +
    "'s everything a "+girlguy+"\ncraves for.",
    "A good looking "+guygirl+" with a perfect smile.",
    "Cuddly like a teddy bear but strong like\na soldier.",
    heshe+" is loveable, caring, but also tough and\nprotective.",
    girlguy+"s really dig a "+guygirl+" like "+himher +
    " cuz "+heshe+"'s got most\nof the skills..",
    "Will make you laugh a lot.",
    "This person is always well dressed and very\nloved.",
    heshe+" is a perfectionist.",
    "The most beautiful eyes in the whole wide\nworld. They Look like stars and if you look too\ndeep you'll get lost in them.",
    "Diplomatic and urbane.",
    "Always genuine and will try and help out if\nyou're in need.",
    str(name)+"'s Run the world, and always get what they\ndesire.",
    "A beautiful "+guygirl+" who makes people laugh\nall the time.",
    str(name)+"'s funny as hell.",
    "Quite with the ones "+heshe +
    " is unfamiliar with, and\necstatic with those "+heshe+" prizes.",
    str(name)+" is an amazing person.",
    str(name)+" is a very smart and caring person.",
    "When they need to talk and gives great advice to\nany and everyone.",
    str(name) + " is a very smart, sweet, good looking\nand extremely intelligent "+guygirl+".",
    "Easygoing and sociable.",
    heshe+" can talk to basically anything or anyone for\nhours.",
    "One of the most wonderful person you will ever\nmeet in your life.",
    "Will do anything for friends.",
    heshe+" is dutiful and will never put "+hisher +
    " own thoughts\nand feelings before "+hisher+" loved ones.",
    "Wise enough to overcome every situation.",
    heshe+" makes you smile with all your heart and you\nlove " +
    himher+" and never want to loose "+himher+".",
    "Very passionate and romantic and emotional\ntoo!",
    "If u r "+hisher+" "+girlguy +
    " he'll take care of u like a little\ndiamond of "+hisher+".",
    str(name) + " has a kind heart, and is family oriented.",
    "Will insist that "+heshe+" is a piece of hard candy, but\nif you dig deep enough " +
    heshe+"'s got a soft chewy\ncenter.",
    heshe+" is likesd by everyone and also has a great\ntaste in fashion.",
    "A very awesome person who is well rounded\nand good at everything.",
    str(name)+" can't be wholly defined in few words\nbecause "+heshe +
    "'s so close to perfection that any\nwords for " +
    hisher+" just won't be good enough.",
    "Helps everyone, great friend, crazy about many\nthings.",
    str(name)+" is a "+guygirl+" you will want to hold close\nforever.",
    "Loves to party and have fun, and can always\nmake you smile.",
    hisher+" smile is infectious and "+heshe +
    " laughs all the\ntime which everyone loves about "+himher+".",
    str(name)+" is completely down to earth and sweet\nand kind. " +
    heshe+" is the best friend anybody could\never wish for!",
    str(name)+" might come off as indifferent and\nimpatient occasionally but it's only because\nthey are working for greater good which takes a\nlot of effort.",
    "Cute and caring. One of the nicest people you'll\nmeet.",
    "Stunning long legs, hazel eyes, perfect smile,\ndimples, freckles, and every " +
    girlguy+" dream.",
    "Everything "+heshe+" does is so sexy and appealing,\nwhen you see "+himher+"..",
    heshe+" thinks only about only the lucky " +
    girlguy+" "+heshe+" loves and\nno one else.",
    "Someone you can talk to and trust.",
    str(name)+" is funny and "+heshe+" will make you laugh in\nthe hardest times beacuase " +
    heshe+" loves to see\npeople smile.",
    "The most perfect "+guygirl+" in the universe.",
    heshe+" is a strong hearted charming person.",
    heshe+" is good looking, polite, and just all round\nplain awesome.",
    heshe+" holds "+hisher+" emotions and true feelings back\n" +
    heshe+"'s very protective of what "+heshe+" cares for.",
    "Everyone likes "+himher+".",
    "Destined to become a person who does not\nhave an average job.",
    "One of the most unique "+guygirl+" you'll every meet.",
    str(name)+"'s are extremely caring, affable, and they\nare very sensititve but tend to hide it.",
    heshe+"'s the kind of "+guygirl+"who's so loveable that\neveryone likes her.",
    "Black hair, brown eyes, falls in love hard and\nfast but won't admit it.",
    "You are really lucky if you have a " +
    str(name)+" in your\nlife especially if you are dating her.",
    str(name)+" is and achiever and the best person you turn\nto when you need a shoulder to cry on.",
    str(name)+" is the definition of compassion.",
    "The best person ever. "+heshe+" is one of a kind.",
    heshe+"'s beautiful, lovely body and lovely\npersonality.",
    "A "+str(name)+" is worthy of being a friend for quite\na long time.",
    heshe+" doesn't know how valuable "+heshe +
    " really is so\nmake "+himher+" realise "+hisher+" worth.",
    heshe+" is unique in every way starting from "+hisher +
    "\nname to "+hisher+" looks and personality.",
    "Always will have your back no matter who you\nare unless you get on " +
    hisher+" bad; once you on "+hisher+"\nbad side there's no coming back.",
    heshe+" is loyal to people and won't back stab you.",
    "Really beautiful, has an amazing body.",
    "The ruler of real goon nation and one of a kind.",
    "Never less than awesome.",
    str(name)+"'s are the model type, loved by "+girlguy +
    ", and\nhated by some "+guygirl+"s who are jealous.",
    str(name)+" can do whatever "+heshe+" puts "+hisher+" mind to and\n"+heshe +
    " is not quitter, "+heshe+" does not give up easily\non anything or anyone.",
    heshe+" loves music.",
    str(name)+" is a very smart and caring person.",
    heshe+" has a rocken model body that makes other\n" +
    guygirl+" jealous, but "+heshe+" is very modest.",
    "They are logical, understanding, and see\nthrough any trick or gig you try to pull on them.",
    "The person who radiates happiness.",
    str(name)+" is a "+guygirl +
    " who is not really insecure and is\nquite protective sometimes.",
    "They have trouble expressing their\nemotions in real life, but it takes the right person\nto see through this barrier and into their true\nhearts.",
    str(name)+" has beautiful hairs.",
    heshe+" is really funny and sarcastic but really\nsweet and kindhearted at the same time.",
    "If you ever come across a "+str(name)+" never let "+himher +
    "\ngo because "+heshe+"'ll be the best thing that you've\never had.",
    str(name)+" have a lot of talent in the arts and\nperformance arts and have quite a lot of sports\npotential that they may/may not put to use.",
    "Someone who loves and cares for everyone.",
    "Modest, but also speak "+hisher+" mind in a way that\nothers can't.",
    "Sometimes you need to have patience with "+himher+"\nbecause " +
    heshe+" has anger issues but "+heshe+"'ll get\nover it very fast.",
    heshe+"'s beautiful, talented and intelligent af You\ncan not ignore a " +
    str(name)+", If you do, you have\nforgotten it till you die.",
    "Smart and out to prove the world wrong.",
    "It's like a drug! Your heart races and you can't\nget enough of " +
    str(name)+"'s gorgeousness.",
    "If you ever find "+himher +
    " just hold on tight and never\nlet go cause "+heshe+" is a gem.",
    str(name)+"s are the best !",
    str(name)+"'s are absolutely stunning, gorgeous, and\nallurging.",
    heshe+" cares about "+hisher+" family and "+hisher +
    " friends and\nis a person who is trustworthy.",
    heshe+" is not only unique but one of a kind.",
    str(name)+" is too perfect to describe.",
    str(name)+" likes to keep "+hisher+" circle tight and small,"+heshe +
    "\n is picky about who "+heshe+" trusts, and isn't fond of\nlarge circles.",
    girlguy+" really wish to have a man who is protective\nenough and secure enough.",
    heshe+"'ll leave you coming back for more; wanted\nby many.",
    "Their eyes, eyebrows, and overall facial\nstructure are striking.",
    "Idealistic and peaceable.",
    "Cute and Horny",
    "Useless"

]

# Setting Up Image
image = Image.new('RGB', (1000, 1000), (255, 255, 255))
lines_font = ImageFont.truetype('Please write me a song.ttf', size=38)
name_font = ImageFont.truetype('theboldfont.ttf', size=72)
watermark_font = ImageFont.truetype('arial.ttf', size=24)

history = []
# Printing on image
y0, dy = 220, 40
for i in range(6):
    y0 += 10
    text = random.choice(lines)
    try:
        history.index(text)
        continue
    except:
        history.append(text)
        for j, line in enumerate(text.split('\n')):
            y0 += dy
            ImageDraw.Draw(image).text(
                (70, y0), line, fill='rgb(255, 54, 51)', font=lines_font)

ImageDraw.Draw(image).rectangle(
    [50, 150, 1000-50, y0+70], fill=None, outline=(0, 0, 0), width=5)
ImageDraw.Draw(image).text((70, 180), str(name),
                           fill='rgb(0,0,0)', font=name_font)
ImageDraw.Draw(image).text((1000-400, 1000-30),
                           'Python Script Made By @aero.n.zero', fill='rgb(97, 0, 166)', font=watermark_font)

# Showing Output
image.save(str(name)+'.png')
image.show()
