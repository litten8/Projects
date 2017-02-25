import json, math

def rewrite_json():
    pokedex = json.loads(open('pokedex.json', 'r').read())

    all_types = {
        '岩石': 'Rock',
        '冰': 'Ice',
        '飞行': 'Flying',
        '恶': 'Dark',
        '一般': 'Normal',
        '炎': 'Fire',
        '格斗': 'Fighting',
        '毒': 'Poison',
        '龙': 'Dragon',
        '虫': 'Bug',
        '水': 'Water',
        '电': 'Electric',
        '超能': 'Psychic',
        '草': 'Grass',
        '钢': 'Steel',
        '地上': 'Ground',
        '妖精': 'Fairy',
        '幽灵': 'Ghost'
    }

    new = []
    for p in pokedex:
        moves = set()
        for ms in p['skills'].values():
            for m in ms:
                moves.add(m)

        etypes = []
        for t in p['type']:
            etypes.append(all_types[t])

        new_pokemon = {
            'id': p['id'],
            'name': p['ename'],
            'moves': moves,
            'types': etypes
        }

        new.append(new_pokemon)

    print(json.dumps(new, sort_keys = True, indent = 4))

class Perceptron:
    def __init__(self, type):
        self.type=type
        self.weights={}

    def changeWeight(self, index, amount):
        try:
            self.weights[index]+=amount
        except KeyError:
            self.weights[index]=amount

    def getWeight(self, index):
        try:
            return self.weights[index]
        except KeyError:
            self.weights[index]=0
            return self.weights[index]

    def probability(self, ins):
        outs=[]
        for i in ins:
            outs.append(self.getWeight(i))
        s=sum(outs)
        if s<-10:
            s=-10
        if s>10:
            s=10
        return 1 / (1 + math.exp(-s))

pokedex = json.loads(open('pokedex2.json', 'r').read())
p=Perceptron("Grass")
#rewrite_json()
for k in range(100):
    right=0
    wrong=0
    for i in range(len(pokedex)):
        prob=p.probability(pokedex[i]['moves'])
        if prob >= 0.5:
            guess=1
        else:
            guess=-1

        if p.type in pokedex[i]['types']:
            actual=1
        else:
            actual=-1

        print(pokedex[i]['name'] + ': Guess=' + str(guess) + ' == Actual=' + str(actual))

        for j in range(len(pokedex[i]['moves'])):
            p.changeWeight(pokedex[i]['moves'][j], 0.01*actual)

        if actual==guess:
            right+=1
        if actual!=guess:
            wrong+=1

    print(str(right) +" right and " + str(wrong) + " wrong")
