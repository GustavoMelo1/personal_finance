import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

#function to display wishes
def wishes():
    try:
        with open('data/wishes.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        logging.info("Searching wishes items...")
        
        return dados['wishes']

    except FileNotFoundError:
        logging.warning("Wishes don't exist yet. Please add some wishes first.")
        return []
    except Exception as e:
        logging.error(f"error in wishes: {e}")
        return []

def news():
    try:
        with open('data/financialmarketnews.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            
        logging.info("Searching financial news...")
        
        # Devolve a lista de notícias
        return dados['news']
            
    except FileNotFoundError:
        logging.warning("News don't exist yet. Please add some news first.")
        return []
    except Exception as e:
        logging.error(f"error in news: {e}")
        return []

#executes the functions when the script runs
if __name__ == "__main__":
    wishes()
    news()