from scipy.stats import shapiro

# Data for the other attributes
edited_sentence_length = [22.54, 23.02, 23.64]
unedited_sentence_length = [24.02, 23.91, 23.93]

edited_lexical_diversity = [0.74, 0.75, 0.75]
unedited_lexical_diversity = [0.75, 0.78, 0.74]

edited_sentiment = [0.19, 0.21, 0.20]
unedited_sentiment = [0.17, 0.16, 0.16]

edited_subjectivity = [0.47, 0.47, 0.46]
unedited_subjectivity = [0.46, 0.44, 0.42]

# Calculate differences for each attribute
differences_sentence_length = [e - u for e, u in zip(edited_sentence_length, unedited_sentence_length)]
differences_lexical_diversity = [e - u for e, u in zip(edited_lexical_diversity, unedited_lexical_diversity)]
differences_sentiment = [e - u for e, u in zip(edited_sentiment, unedited_sentiment)]
differences_subjectivity = [e - u for e, u in zip(edited_subjectivity, unedited_subjectivity)]

# Perform Shapiro-Wilk tests for normality on the differences
normality_results = {
    'Total Words': shapiro([e - u for e, u in zip(edited_total_words, unedited_total_words)]),
    'Average Sentence Length': shapiro(differences_sentence_length),
    'Lexical Diversity': shapiro(differences_lexical_diversity),
    'Sentiment': shapiro(differences_sentiment),
    'Subjectivity': shapiro(differences_subjectivity)
}

normality_results

# Perform paired t-tests for each attribute
t_test_results = {
    'Average Sentence Length': ttest_rel(edited_sentence_length, unedited_sentence_length),
    'Lexical Diversity': ttest_rel(edited_lexical_diversity, unedited_lexical_diversity),
    'Sentiment': ttest_rel(edited_sentiment, unedited_sentiment),
    'Subjectivity': ttest_rel(edited_subjectivity, unedited_subjectivity)
}

t_test_results