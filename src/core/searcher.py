import json 

def wishes():
    try:
        with open('data/wishes.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            
        print("Searching items...\n")
    
        for item in dados['wishes']:
            print(f"Target: {item['search']}")
            print(f"Stores: {', '.join(item['store'])}")
            print(f"Max Value: R$ {item['max_value']:.2f}")
            print("-" * 30)
            
    except FileNotFoundError:
        print("Wishes dont exist yet. Please add some wishes first.")

    wishes()