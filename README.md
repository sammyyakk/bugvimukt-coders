# Sentiment Analysis on Social Media Comments

This project is designed to perform sentiment analysis on comments from Instagram posts and reels. It helps identify the emotional tone (Positive, Neutral, or Negative) of user-generated content, providing insights into public opinion and engagement on social media platforms.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Algorithm Used](#algorithm-used)
- [Results](#results)
- [Future Scope](#future-scope)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
Social media is a rich source of public opinion. By analyzing comments on posts, this project enables businesses, content creators, and researchers to better understand audience sentiment, track mood trends, and identify potentially harmful content. Sentiment analysis can be used to improve engagement strategies, ensure safer online spaces, and gain insights into public reactions during events or campaigns.

---

## Features
- **Login and Authentication**: Uses Instaloader to log in and fetch comments from Instagram posts and reels.
- **Sentiment Analysis**: Employs VADER Sentiment Analysis to classify comments as Positive, Neutral, or Negative.
- **Emoji and Social Media-Specific Handling**: Effectively analyzes comments with emojis and informal language common on social media.
- **Real-Time Analysis**: Quickly processes and analyzes comments to provide sentiment insights.

---

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-instagram.git
   cd sentiment-analysis-instagram
   ```

2. **Install the required libraries**:
   ```bash
   pip install instaloader vaderSentiment
   ```

3. **Set up Instagram login**:
   - Make sure you have your Instagram credentials handy for authentication.
   - The session will be saved to avoid repeated logins.

---

## Usage

1. **Run the script**:
   ```bash
   python main.py
   ```

2. **Enter the Instagram post or reel URL** when prompted.

3. **View Sentiment Analysis**:
   - The script will output the comments along with their sentiment classification.
   - Sentiments are categorized as Positive, Neutral, or Negative.

---

## Algorithm Used
The project uses the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** algorithm. VADER is a lexicon and rule-based model that analyzes sentiments from text data, especially tailored for social media. It considers word intensity, punctuation, capitalization, and context to classify comments accurately.

---

## Results
The analysis effectively classifies most comments as Positive, Neutral, or Negative. Positive sentiments dominate posts with humor or relatable content. Challenges include interpreting multilingual comments, handling sarcasm, and accurately assessing emoji usage. Nevertheless, the tool provides meaningful insights into social media user emotions.

---

## Future Scope
- **Real-Time Sentiment Analysis**: Implement live sentiment tracking for trending topics.
- **Multilingual Support**: Expand to analyze comments in multiple languages.
- **Emotion Detection**: Identify specific emotions like anger, joy, or sarcasm.
- **Toxicity Filtering**: Automatically flag harmful or inappropriate comments.
- **AI Assistant Integration**: Enhance virtual assistants with emotion-aware interactions.

---

## Contributing
We welcome contributions from the community! Feel free to fork the project and submit pull requests for improvements or new features.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

**Thank you for exploring our Sentiment Analysis project!** If you have any questions or feedback, feel free to reach out.

---