import instaloader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

L = instaloader.Instaloader()

# Login to Instagram (credentials already saved in session file)
username = 'username' # Put your username here
password= "yourpassword" # Enter your password here


try:
    L.load_session_from_file(username)
except FileNotFoundError:
    print("Session file not found. Logging in again.")
    L.login(username, password)
    L.save_session_to_file()

print(f"Logged in as {username}")

analyzer = SentimentIntensityAnalyzer()

# Fetch comments and perform sentiment analysis
def analyze_sentiments(post_url):
    try:
        # Extract the shortcode from the URL (URL format: https://www.instagram.com/p/<shortcode>/)
        shortcode = post_url.split('/')[-2]

        # Loading Post
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        print(f"\nComments for Post: {post_url}")
        print(f"Post Caption: {post.caption}")
        print("\nSentiment Analysis of Comments:")

        # Iterate over all comments
        for comment in post.get_comments():
            comment_text = comment.text
            sentiment_score = analyzer.polarity_scores(comment_text)['compound']
            
            # Determine sentiment
            if sentiment_score >= 0.05:
                sentiment = "Positive"
            elif sentiment_score <= -0.05:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            # Print the comment and its sentiment
            print(f"{comment.owner.username}: {comment_text} (Sentiment: {sentiment})")

    except instaloader.exceptions.InstaloaderException as e:
        print(f"Instaloader error: {str(e)}")
    except Exception as e:
        print(f"Error fetching comments: {str(e)}")


post_url = input("Enter the Instagram post or reel URL: ")
analyze_sentiments(post_url)
