import re 

def extract_sentences(text):
    modified_text = re.sub(r"[.!?,]| en | omdat | zodat | want | wanneer | dat ", "|", text)
    
    sentences = modified_text.split("|")
    
    return [sentence.strip() for sentence in sentences if sentence.strip()]

def calculate_ego_score(sentences):
    ego_count = 0  
    
    for sentence in sentences:
        sentence = sentence.lower()
        
        words = sentence.split(' ')
        
        if len(words) >= 2 and (words[0] in ('ik', 'mijn') or words[1] in ('ik', 'mijn')):
            ego_count += 1  
    
    return ego_count  

example_texts = [
   #Test 1 
    """Geachte heer/mevrouw, 
    Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. 
    Ik ben de beste kandidaat voor deze functie omdat ik al jaren ervaring heb in deze branche.""",
    
  #Test 2
    """Het lijkt me geweldig om in uw team te werken. 
    Mijn ervaring met softwareontwikkeling is breed, en ik ben altijd bereid om te leren. 
    Ik denk dat ik veel kan bijdragen aan het succes van uw bedrijf.""",

   #Test 3 
    """Het doel is om het team te verbeteren en samen te werken aan projecten."""
]

for index, text in enumerate(example_texts, start=1):
    sentences = extract_sentences(text)
    score = calculate_ego_score(sentences)

    print(f"Ego score for example text {index}: {score}")
