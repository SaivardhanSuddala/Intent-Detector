Intent Detector
Overview

This project is a multi-class text classification system that predicts the intent behind user messages.

It uses TF-IDF + SGDClassifier to classify queries like:

card issues
payment problems
account-related queries
Problem Statement

Customer messages are unstructured and require manual reading.

This system:

automatically detects intent
helps route queries faster
reduces manual effort
Tech Stack
Python
scikit-learn
TF-IDF (feature extraction)
SGDClassifier (ML model)
Dataset
Banking77 dataset (subset used)
Reduced to ~10 meaningful intents for better accuracy
Model Pipeline
Text input
TF-IDF vectorization (unigrams + bigrams)
SGDClassifier (log_loss)
Output predicted intent
