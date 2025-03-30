from fetch_news import fetch_latest_headlines
from user_profiles import get_all_users
from recommender import recommend_articles

def main():
    users = get_all_users()

    print("Select a user:")
    for idx, user in enumerate(users):
        print(f"{idx + 1}. {user['name']} ({user['interests']})")
    choice = int(input("Enter user number: ")) - 1
    selected_user = users[choice]

    print(f"\nFetching latest tech news for {selected_user['name']}...\n")
    articles = fetch_latest_headlines()

    recommendations = recommend_articles(articles, selected_user['interests'])

    print(f"\nTop article recommendations for {selected_user['name']}\n")
    print(recommendations.to_string(index=False))

if __name__ == "__main__":
    main()
