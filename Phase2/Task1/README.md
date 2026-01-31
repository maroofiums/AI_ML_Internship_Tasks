

# Task 1 – News Topic Classifier Using BERT

## Objective

The goal of this task was to fine-tune a pre-trained transformer model (BERT) to classify news headlines into topic categories. This is part of **Phase 2 of the internship project**, focused on practical NLP applications and end-to-end model deployment.

## Problem Statement

News headlines are often short and lack context, making topic classification a challenging NLP problem. The task required:

* Handling a large text dataset (AG News) with four categories: World, Sports, Business, Science & Technology.
* Preprocessing raw text data (title + description).
* Building a classifier that can generalize well across different news topics.
* Deploying the trained model for live interaction.

## Approach & Solution

1. **Data Collection and Preprocessing**

   * Dataset used: [AG News](https://huggingface.co/datasets/ag_news).
   * Combined `title` and `description` to form a single text input.
   * Labels were adjusted to start from 0.
   * Split dataset into training (90%), validation (10%), and test sets.

2. **Model Selection**

   * Pre-trained `bert-base-uncased` model from Hugging Face Transformers.
   * Added a classification head for 4 output classes.

3. **Training**

   * Optimizer: AdamW with learning rate 5e-5.
   * Batch size: 16, Epochs: 2.
   * Trained on GPU if available.

4. **Evaluation**

   * Metrics: Accuracy and Weighted F1-score.
   * Achieved test accuracy of ~93.7% and weighted F1-score of ~93.7%, indicating balanced performance across all classes.

5. **Deployment**

   * Deployed using Gradio for interactive inference.
   * Users can input a headline and get the predicted category in real-time.

6. **Saving Artifacts**

   * Fine-tuned model and tokenizer saved for future inference.
   * Label mapping stored in JSON for consistency in predictions.

## Challenges

* Handling a large dataset efficiently within GPU memory constraints.
* Tokenization and batching to fit BERT’s maximum sequence length.
* Ensuring the model generalizes well despite short and noisy headlines.

## Skills Gained

* Practical NLP using Transformer models (BERT).
* Transfer learning and fine-tuning for text classification.
* Evaluation and interpretation of classification metrics.
* Lightweight deployment using Gradio for live model interaction.

## Kaggle Notebook

The complete code and workflow are available on Kaggle:
[News Topic Classifier Using BERT](https://www.kaggle.com/code/maroofiums/news-topic-classifier-using-bert/)
