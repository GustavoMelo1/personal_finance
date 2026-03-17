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

def news():
    try:
        with open('data/financialmarketnews.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            
        print("Searching news...\n")
    
        for item in dados['news']:
            print(f"words_for_search: {', '.join(item['words_for_search'])}")
            print(f"news_sites: {', '.join(item['news_sites'])}")
            print("-" * 30)
            
    except FileNotFoundError:
        print("News dont exist yet. Please add some news first.")

    news()