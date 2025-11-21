import nltk

from db.database import Database
from analysis import analyze_sentiment

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except nltk.downloader.DownloadError:
    print("Baixando vader_lexicon do NLTK...")
    nltk.download('vader_lexicon')

database = Database('db/post_analysis.db')

def populate_database_with_samples():
    sample_posts = [
        "I love the new Python update, it's fantastic!",
        "The food was nothing special.",
        "I absolutely hate waiting in line, it's terrible.",
        "The project deadline is next Tuesday.",
        "Amazing service! Will definitely come back.",
        "The weather is bad today, I am sad.",
        "Just a normal comment about something boring.",
        "Worst experience ever. Extremely disappointed.",
        "Python is boring.",
        "Python is izi.",
        "chablaw pew pew.",
        "Samuel work in Full Stack Club.",
        "Victor is a Freelancer.",
        "Ivan is the best player of Brazil."
        "Lucas is a excellent father."
        "Fantastic, cocacolastic."
    ]
    
    print("\n--- Povoando o banco de dados 'post_analysis.db' ---")

    for post_text in sample_posts:
        category, compound_score = analyze_sentiment(post_text)
        
        is_active = True
        if category == 'Negative':
            is_active = False
        database.insert_post(post=post_text, category=category, active=is_active, score=compound_score)
    
    print("--- Povoamento concluído. ---")

def display_all_posts():
    print("\n--- Conteúdo do Banco de Dados ---")
    posts = database.read_posts()
    for post in posts:
        print(f"ID: {post.id} | Post: '{post.post[:25]}...' | Categoria: {post.category} | Ativo: {post.active} | Score: {post.score:.2f}")
    print("----------------------------------")

if __name__ == '__main__':
    populate_database_with_samples()
    # display_all_posts()