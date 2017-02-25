import random
import string
rnumerals={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"XI"}

class AlienRace:
    def __init__(self, name, size, bodyShape, features, abilities, personalityTraits, originPlanet):
        self.name=name
        self.size=size
        self.bodyShape=bodyShape
        self.features=features
        self.abilities=abilities
        self.personalityTraits=personalityTraits
        self.originPlanet=originPlanet
        self.government=None
    def description(self):
        if len(self.features)>0:
            featurestr=self.features[0]
            for i in range(1,len(self.features)):
                featurestr+=", and "+self.features[i]
        else:
            featurestr="look mostly ordinary"

        if len(self.abilities)>0:
            abilitystr=self.abilities[0]
            for i in range(1,len(self.abilities)):
                abilitystr+=", and "+self.abilities[i]
        else:
            abilitystr="do most normal things and not much else"

        if len(self.personalityTraits)>0:
            personalitystr=self.personalityTraits[0]
            for i in range(1,len(self.personalityTraits)):
                personalitystr+=", and "+self.personalityTraits[i]
        else:
            personalitystr="act mostly ordinary"

        print(self.name + "s come from " + self.originPlanet.name + ".")
        print("They are are a " + self.bodyShape + " being. They are " + self.size + ". They " + featurestr + ".")
        print("They can " + abilitystr + ".")
        print("They " + personalitystr + ".")
        if self.government is None:
            print("They are part of no government.")
        else:
            print("They are part of " + self.government.name + ".")
    def setGov(self,gov):
        if self.government is not None:
            for i in range(len(self.government.races)):
                if self.government.races[i]==self:
                    self.government.races.pop(i)
                    break
        self.government=gov
        if not self in self.government.races:
            self.government.races.append(self)

class Government:
    def __init__(self, name, territory, government, originPlanet, originRace):
        self.name=name
        self.population=0
        self.territory=territory
        self.races=[]
        self.government=government
        self.originPlanet=originPlanet
        self.originPlanet.system.setGov(self)
        self.originRace=originRace
        self.originRace.setGov(self)
        self.relations={}
    def updatePop(self):
        syspops=[]
        for i in range(len(self.territory)):
            ppops=[]
            for j in  range(len(self.territory[i].mclassplanets)):
                ppops.append(sum(self.territory[i].mclassplanets[j].speciespops.values()))
            syspops.append(sum(ppops))
        self.population=sum(syspops)
    def description(self):
        racestr=self.races[0].name+"s"
        for i in range(1,len(self.races)):
            racestr+=", and "+self.races[i].name+"s"
        print(self.name + " was founded by " + self.originRace.name + "s on " + self.originPlanet.name + ".")
        self.updatePop()

        relationstr=""
        for i in self.relations:
            relationstr+="They are " + self.relations[i] + " with " + i.name + ". "
        if relationstr=="They are":
            relationstr="They have not discovered any"

        print("Their population of " + str(self.population) + " spread across " + str(len(self.territory)) + " systems consists mostly of " + racestr + ".")
        print("They are a " + self.government + ".")
        print(relationstr)
    def discoverGov(self, gov):
        if not gov in self.relations:
            self.relations[gov]="Neutral"

class System:
    def __init__(self, name, planets, mclassplanets):
        self.name=name
        self.planets=planets
        self.mclassplanets=mclassplanets
        for i in range(len(mclassplanets)):
            mclassplanets[i].setSystem(self)
        self.government=None
    def setGov(self,gov):
        if self.government is not None:
            for i in range(len(self.government.territory)):
                if self.government.territory[i]==self:
                    self.government.territory.pop(i)
                    break
        self.government=gov
        if not self in self.government.territory:
            self.government.territory.append(self)

class MClassPlanet:
    def __init__(self, name, speciespops):
        self.name=name
        self.speciespops=speciespops
        self.system=None
    def setSystem(self, system):
        if self.system is not None:
            for i in range(len(self.system.mclassplanets)):
                if self.system.mclassplanets[i]==self:
                    self.system.mclassplanets.pop(i)
                    break
        self.system=system
        if not self in self.system.mclassplanets:
            self.system.mclassplanets.append(self)

class ImportantPerson:
    def __init__(self, name, race, birthplace, experiences, government):
        self.name=name
        self.race=race
        self.birthplace=birthplace
        self.experiences=experiences
        self.government=government





sizes=["microscopic","tiny","small","average size","big","giant"]
sizedict={"microscopic":0.001,"tiny":0.1,"small":0.5,"average size":1,"big":10,"giant":1000}
bodyShapes=["humanoid", "ball shaped", "blob shaped", "energy", "quadruped"]
universalFeatures=["are androgynous","have spikes", "have attenae", "have shiny skin","are damp", "have no hair", "have light human-like skin","have dark human-like skin", "have brown skin", "have blue skin", "have blond hair", "have brown hair", "have black hair","have white hair", "have a tail"]
humanoidFeatures=["have spiky ears", "have a bumpy forehead", "have no ears","can grow a beard"]
ballFeatures=["are perfectly spherical", "have an oval shape", "have an egg shape"]
blobFeatures=["are very moldable","have bodies made mostly of liquid"]
energyFeatures=["can have physical form", "are unable to interact with the physical world"]
quadrupedFeatures=["have spiky ears", "have a bumpy forehead", "have no ears","have no head"]
abilities=["read minds", "read emotions", "mind meld", "eminate energy", "drain oxygen very quickly from around them", "shapeshift","breathe without oxygen","breed very fast","fly","turn invisible","see through walls"]
personalityTraits=["are extremely curious", "are very warlike", "always suppress their emotions", "have extremely high value in honor", "are very greedy","are extremely honest","hate all other races", "are extremely kind"]
speciesNames=["Human","Martian","Vulcan","Klingon","Romulan","Reman","Cardassian","Andorian","Betazoid","Bajoran","Risian","Ferengi","Trill","Borg","Q"]
govTypes=["Democracy","Monarchy","Tyranny","Oligarchy","Aristocracy","Communism","Anarchy"]





planets=[]
systems=[]
for i in range(random.randint(150,500)):
    nname="".join([random.choice(string.ascii_uppercase) for i in range(5)])+str(i)
    totalplanets=random.randint(2,9)
    nofmclassps=random.randint(0,totalplanets)
    mclassps=[]
    for j in range(nofmclassps):
        newPlanet=MClassPlanet(nname+" "+rnumerals[j+1],{})
        planets.append(newPlanet)
        mclassps.append(newPlanet)
    newSystem=System(nname,totalplanets,mclassps)
    systems.append(newSystem)

races=[]
for i in range(random.randint(4,10)):
    shape=random.choice(bodyShapes)
    possibleFeatures=[]
    possibleFeatures.extend(universalFeatures)
    if shape=="humanoid":
        possibleFeatures.extend(humanoidFeatures)
    elif shape=="ball shaped":
        possibleFeatures.extend(ballFeatures)
    elif shape=="blob shaped":
        possibleFeatures.extend(blobFeatures)
    elif shape=="energy":
        possibleFeatures=[]
        possibleFeatures.extend(energyFeatures)
    elif shape=="quadruped":
        possibleFeatures.extend(quadrupedFeatures)
    features=[]
    for j in range(random.randint(0,5)):
        newFeature=random.choice(possibleFeatures)
        canadd=True
        for i in range(len(features)):
            if "hair" in features[i] and newFeature=="have no hair":
                canadd=False
                break
            if "hair" in newFeature and features[i]=="have no hair":
                canadd=False
                break
            if "ears" in features[i] and newFeature=="have no ears":
                canadd=False
                break
            if "ears" in newFeature and features[i]=="have no ears":
                canadd=False
                break
            if "head" in features[i] and newFeature=="have no head":
                canadd=False
                break
            if "head" in newFeature and features[i]=="have no head":
                canadd=False
                break
            if "can have physical form" == features[i] and newFeature=="are unable to interact with the physical world":
                canadd=False
                break
            if "can have physical form" == newFeature and features[i]=="are unable to interact with the physical world":
                canadd=False
                break
        if not newFeature in features and canadd:
            features.append(newFeature)
    racePersonalityTraits=[]
    for j in range(random.randint(0,5)):
        newPersonalityTrait=random.choice(personalityTraits)
        if not newPersonalityTrait in racePersonalityTraits:
            racePersonalityTraits.append(newPersonalityTrait)
    raceAbilities=[]
    for j in range(random.randint(0,5)):
        newAbility=random.choice(abilities)
        if not newAbility in raceAbilities:
            raceAbilities.append(newAbility)
    nnamei=random.randint(0,len(speciesNames)-1)
    nname=speciesNames[nnamei]
    speciesNames.pop(nnamei)
    newPlanet=random.choice(planets)
    nsize=random.choice(sizes)
    newPlanet.speciespops[nname]=int(random.randint(5000000000,10000000000)*(1/sizedict[nsize]))
    newRace=AlienRace(nname,nsize,shape,features,raceAbilities,racePersonalityTraits,newPlanet)
    races.append(newRace)

govs=[]
for i in range(random.randint(int(len(races)/5),len(races)-1)):
    oRace=random.choice(races)
    while oRace.government is not None:
        oRace=random.choice(races)
    govNames=[oRace.name+" Federation", oRace.name+" Empire", oRace.name+" Star Empire", oRace.name+" Union", oRace.name+" Alliance", oRace.name+" Ruling Council", oRace.name+" Coalition", oRace.name+" Collective", oRace.name+" Continuum"]
    oPlanet=random.choice(planets)
    newGov=Government(random.choice(govNames),[oPlanet.system],random.choice(govTypes),oPlanet,oRace)
    for j in range(len(govs)):
        govs[j].discoverGov(newGov)
        newGov.discoverGov(govs[j])
    govs.append(newGov)
    oRace.originPlanet.system.setGov(newGov)
    for i in range(random.randint(1,5)):
        gRace=random.choice(races)
        if gRace.government is None:
            gRace.setGov(newGov)
            gRace.originPlanet.system.setGov(newGov)

for i in range(len(govs)):
    for j in range(random.randint(50,150)):
        newSystem=random.choice(systems)
        if newSystem.government is None:
            newSystem.setGov=govs[i]
            govs[i].territory.append(newSystem)

for i in range(len(planets)):
    if planets[i].system.government is None:
        rrace=random.choice(races)
        planets[i].speciespops[rrace.name]=int(random.randint(500000000,1000000000)*(1/sizedict[rrace.size]))
    else:
        for j in range(len(planets[i].system.government.races)):
            planets[i].speciespops[planets[i].system.government.races[j].name]=int(random.randint(200000000,600000000)*(1/sizedict[planets[i].system.government.races[j].size]))




print()
for i in range(len(races)):
    races[i].description()
    print()
for i in range(len(govs)):
    govs[i].description()
    print()
