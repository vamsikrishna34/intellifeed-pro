import logging
from fetch_news import fetch_latest_headlines
from user_profiles import get_all_users
from recommender import recommend_articles

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Application started.")
    users = get_all_users()

    print("Select a user:")
    for idx, user in enumerate(users):
        print(f"{idx + 1}. {user['name']} (Interests: {', '.join(user['interests'])})")

    selected_user = None
    while True:
        try:
            choice_str = input(f"Enter user number (1-{len(users)}): ")
            choice = int(choice_str) - 1
            if 0 <= choice < len(users):
                selected_user = users[choice]
                logging.info(f"User selected: {selected_user['name']}")
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(users)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError: # Should not happen with the check above, but as a safeguard
            print(f"Error selecting user. Please enter a number between 1 and {len(users)}.")

    logging.info(f"Fetching latest headlines for user {selected_user['name']} with interests: {', '.join(selected_user['interests'])}")
    print(f"\nFetching latest tech news for {selected_user['name']} (Interests: {', '.join(selected_user['interests'])}) ...\n")
    
    try:
        articles = fetch_latest_headlines()
        if not articles: # fetch_latest_headlines returns [] on error
            logging.error("Failed to fetch news. Articles list is empty.")
            print("Failed to fetch news. Please check your internet connection or API key, or there might be no news available for the selected criteria.")
            return # Exit main gracefully
        logging.info(f"Successfully fetched {len(articles)} articles.")
    except Exception as e:
        logging.error(f"An unexpected error occurred while fetching news: {e}", exc_info=True)
        print(f"An unexpected error occurred while fetching news: {e}")
        return # Exit main gracefully

    user_interest_str = ", ".join(selected_user['interests'])
    logging.info(f"Generating recommendations for user {selected_user['name']} based on interests: {user_interest_str}")
    try:
        recommendations = recommend_articles(articles, user_interest_str)
        if recommendations.empty: # recommend_articles returns an empty DataFrame on error/no results
            logging.warning("Could not generate recommendations. Recommendation engine returned no results or encountered an issue.")
            print("Could not generate recommendations at this time. This might be due to an issue with the recommendation engine or no relevant articles found.")
        else:
            logging.info(f"Successfully generated {len(recommendations)} recommendations.")
            print(f"\nTop article recommendations for {selected_user['name']}\n")
            print(recommendations.to_string(index=False))
    except Exception as e:
        logging.error(f"An unexpected error occurred while generating recommendations: {e}", exc_info=True)
        # Still proceed to show no recommendations message if desired, or just state the error.
        print("Could not generate recommendations due to an unexpected error.")
    
    logging.info("Application finished.")

if __name__ == "__main__":
    main()
