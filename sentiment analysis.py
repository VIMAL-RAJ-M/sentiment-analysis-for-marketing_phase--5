df['Sentiment'] = df['Text'].apply(analyze_sentiment)
