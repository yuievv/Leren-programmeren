import time, math, random

# Speler statistieken
player_attack = 1
player_defense = 0
player_health = 3
has_key = False

# === [Herbruikbare gevechtsfunctie] === #
def combat(enemy_name, enemy_attack, enemy_defense, enemy_health):
    global player_health
    
    print(f'Je loopt tegen een {enemy_name} aan.')
    
    # Bepaal de schade die de vijand doet
    enemy_hit_damage = (enemy_attack - player_defense)
    
    if enemy_hit_damage <= 0:
        print(f'Jij hebt een te goede verdediging voor de {enemy_name}, hij kan je geen schade doen.')
        return player_health
    else:
        # Bereken hoe vaak de vijand moet slaan om de speler te verslaan
        enemy_attack_amount = math.ceil(player_health / enemy_hit_damage)
        
        # Bepaal de schade die de speler doet
        player_hit_damage = (player_attack - enemy_defense)
        # Bereken hoe vaak de speler moet slaan om de vijand te verslaan
        player_attack_amount = math.ceil(enemy_health / player_hit_damage)

        if player_attack_amount < enemy_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de {enemy_name}.')
            # Bereken de nieuwe health van de speler
            player_health = player_health - (player_attack_amount * enemy_hit_damage)
            print(f'Je health is nu {player_health}.')
            return player_health
        else:
            print(f'Helaas is de {enemy_name} te sterk voor je.')
            print('Game over.')
            exit()

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 2] === #
print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')

# Genereer een willekeurige som
num1 = random.randint(10, 25)
num2 = random.randint(-5, 75)
operator = random.choice(['+', '-', '*'])

# Bereken het juiste antwoord
if operator == '+':
    correct_answer = num1 + num2
elif operator == '-':
    correct_answer = num1 - num2
else:  # operator == '*'
    correct_answer = num1 * num2

print(f'Daarboven zie je een som staan {num1}{operator}{num2}=?')
antwoord = int(input('Wat toets je in?'))

if antwoord == correct_answer:
    print('Het standbeeld laat de sleutel vallen en je pakt het op')
    has_key = True
else:
    print('Er gebeurt niets....')

print('Je ziet achter het standbeeld twee deuren.')
print('Aan de linkerkant zie je een donkere deur (kamer 6).')
print('Recht vooruit zie je een deur naar een lange hal (kamer 3).')
keuze = input('Welke kamer kies je? (typ 6 of 3): ')
print('')
time.sleep(1)

# === [Keuze vertakking] === #

# === [KAMER 6] === #
if keuze == '6':
    print('Je duwt de deur open en stapt een nieuwe, muffe kamer binnen.')
    # De zombie in kamer 6
    combat("zombie", 1, 0, 2)
    print('Achter de zombie zie je een deur en je gaat erdoorheen.')
    print('')
    time.sleep(1)

# === [KAMER 3] === #
# Deze kamer wordt dus bereikt via keuze '3' OF na afloop van kamer '6'
print('Je stapt de lange kamer binnen.')
print('Deze kamer heeft twee ingangen en is langwerpig.')
# Kies willekeurig tussen een schild of een zwaard
item = random.choice(['schild', 'zwaard'])

if item == 'schild':
    player_defense += 1
elif item == 'zwaard':
    player_attack += 2

print(f'In deze kamer staat een tafel met daarop een {item}.')
print(f'Je pakt het {item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [kamer 4] === #
print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
# Nieuwe, sterkere vijand (attack: 2, defense: 0, health: 3)
combat("vijand", 2, 0, 3)
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een vijand tegenkomen.')
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

if has_key:
    print('Je gebruikt de sleutel om de schatkist te openen.')
    print('Gefeliciteerd! Je hebt de dungeon verslagen en de schat bemachtigd!')
else:
    print('Je probeert de schatkist te openen, maar je hebt geen sleutel.')
    print('De schatkist blijft op slot. Je verliest het spel.')
    print('Game over.')