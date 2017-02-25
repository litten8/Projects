import random
def choice(choices):
    print("Choose one:" + ", ".join(choices))
    c=input()
    whatdo(c)

def randchoice(choices):
    whatdo(random.choice(choices))

def whatdo(c):
    global finalsentence
    if c[0]=='"':
        finalsentence+=c[1:-1]+" "
    else:
        check(c)

def check(g):
    if type(g)==str:
        s=g.split("+")
        for i in range(len(s)):
            exec("check("+s[i]+")")
    else:
        randchoice(g)


I=("P+Punc")
P=("vS","dS","vS","dS","P+C+P")
vS=("SV+O","vS+Av","SoV","vS+Pl")
Pl="Pr+Oa"
C=('"or"','"and"','"because"','"; therefore,"','"; however,"','"; furthermore,"','"; meanwhile,"','", but"','"if"','"while"','"when"')
Pr=('"on"','"in"','"with"')
SV=("Op+Vp","spPro+Vp","S+V","S+bV+Vp","Op+bV+Vp")
bV=('"can"','"can\'t"','"will"','"won\'t"','"should"','"shouldn\'t"','"would"','"wouldn\'t"')
SoV=("Op+oVp","S+oV","S+bV+oVp")
dS=("S+Sd+O","Op+Sp+O","they+Sp+O","iPro+Si+O")
they=['"they"']
iPro=['"I"']
Sd=['"is"']
Sp=['"are"']
Si=['"am"']
Op=("Detp+Np","pPro","Np")
S=("Detc+Nc","Deta+Na","Pro","sPro")
O=("Detc+Nc","Deta+Na","Pro","oPro")
Oa=("O","Op")
V=('"swats"','"chews"','"bites"','"smashes"',"Av+V")
Vp=('"swat"','"chew"','"bite"','"smash"',"Av+Vp")
oV=('"sleeps"','"sings"','"dances"',"Av+oV","says+quote+I+quote")
oVp=('"sleep"','"sing"','"dance"',"Av+oVp","say+quote+I+quote")
says=['"says"']
say=['"say"']
quote=['"\""']
Pro=('"Rudy"','"Bernie"','"Tholen"','"Yuko"')
oPro=('"them"','"him"','"her"','"me"')
sPro=('"he"','"she"')
spPro=('"they"','"I"')
pPro=['"you"']
Deta=('"the"','"an"','"every"')
Detc=('"the"','"a"','"every"')
Detp=['"the"','"all"','"the group of"','"a group of"']
Det=("Deta","Detc")
SP=['"group of"']
Na=('"aardvark"','"anteater"',"Aa+N")
Nc=('"cat"','"dog"','"bone"','"mouse"','"house"','"person"','"teenager"',"Ac+N","SP+Np")
Np=('"cats"','"dogs"','"bones"','"mice"','"aardvarks"','"anteaters"','"houses"','"people"',"A+Np")
N=("Na","Nc")
Punc=('"."','"!"','"?"')
Ac=('"big"','"brown"','"rude"','"cute"')
Aa=('"orange"','"ugly"','"annoying"','"adorable"')
A=("Ac","Aa")
Av=('"happily"','"badly"','"sadly"','"angrily"','"badly"','"annoyingly"')
'''
I="P+Punc"
P=("S+al+A","Vo+S+yUxya+O","Vs+S","P+yixyU+P")
al=('"al"')
yUxya=('"yUxya"')
yixyU=('"yixyU"')
mi=('"mi"','"mi"')
S=("N","N+name","name")
O=("N","N+name","name")
name=('"lila"','"hUli"','"sukul"','"malkul"')
N=('"liSaukal"','"kUri"','"SUuxkapi"','"suUl"','"kulUlk"','"hUkxkUlk"','"laulsu"','"sula"','"kyUkxkSau"')
Vo=("A+Vo",'"malUl"','"susu"','"uxkakxkyU"','"laulsu"','"malUl"','"kyUkxkSau"')
Vs=("A+Vs",'"Saul"','"susu"','"SUkul"','"SUuUl"','"laulsu"','"suSau"','"malUl"')
A=('"liwa"','"uliSU"',"O+mi",'"Ulkxksu"','"Ulul"','"hUkxkUlk"','"kyUkxkSau"')
Punc=('"."','"!"')

I="P+Punc"
P=["oddn+odds","evenn+evens"]
oddn=["n+oddn",'"1"','"3"','"5"','"7"','"9"']
evenn=["n+evenn",'"0"','"2"','"4"','"6"','"8"']
n=["oddn","evenn"]
odds=('" is odd"')
evens=('" is even"')
Punc=('"."','"."')

I="U+L+M+L+D"
L=('"\n"')
space=('" "')
U=["H","Hat+L+H"]
Hat=['" ?"','" !"','" ^"','" *"','" zzz"']
H=['" o"','" O"','" ."','" *"','" @"','" #"']
M="A+B+A"
A=['"\\"','"/"','"-"','" "','"="','"<"','">"','")"','"("','"o"','"!"']
B=['"|"','"*"','"0"','"!"','"#"']
D="Leg+space+Leg"
Leg=['"/"','"\\"','"("','")"','"!"','"."','"o"','"O"','" "']

I="P+n+P+Punc"
n=['"and"']
P=["GC+GCE","BR+BREGP+GP","E","BR+BREGC+GC","RC+RCE"]
MC=['"Picard"','"Riker"','"LaForge"','"Data"','"Doctor Crusher"','"Wesley"','"O\'Brian"','"Spot"','"Worf"','"a crewmember"','"Yar"','"Troi"','"Alexander"','"Keiko"','"Barclay"']
RC=['"Lwaxanna"','"Spock"','"Worf\'s parents"','"Gowron"','"an ambassador"','"an admiral"']
GC=["RC","MC"]
RCE=['"visits the enterprise"','"demands the ship changes course"']
BC=['"Lore"','"Q"','"Sela"']
GCE=['"is badly injured"','"starts behaving strangely"','"is believed to have died"','"is killed by evil alien space goop"','"goes on a diplomatic mission"']
BR=['"Cardassians"','"Romulans"','"a newly discovered alien race"','"Borg"','"a rogue Ferengi ship"']
BREGP=['"attack"']
GP=['"the Enterprise"', '"a nearby Federation outpost"']
E=['"Troi loses her powers"','"Romulans are found in Federation space"']
BREGC=['"kidnap"','"mind control"','"torture"']
Punc=['"."']
'''

finalsentence=""
check(I)
print(finalsentence+" ")
