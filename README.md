# BERTIFIER adaptation for NaNoGenMo 2024

**By Malthe Stavning Erlsev**

This is a digital media archaeological exploration of AI-generated text, combining two distinct text generation techniques, both of which predate the ChatGPT moment and neither of which are state of the art. Markov Chains and the BERT language model are here combined to create a series of stylistically varied sections that explore the materiality of two different kinds of language models through their mutual probabilistic modeling of a series of datasets – and of one another. The project is divided into four parts, each shaped by a different dataset: everyday conversations, cinematic dialogue, therapeutic interactions, and a recursive corpus of the book’s own outputs. These datasets inform the tone and content of each section. See details below regarding the source of each of the first three datasets. The fourth (recursive) dataset consists of all the outputs from the *BERTifier* (see below) generated during the first three sections of the book.

The text-generation process unfolds in two stages. First, a Markov Chain algorithm constructs an initial sentence by analyzing the chosen dataset and probabilistically predicting word sequences based on observed patterns. This rudimentary output serves as the foundation. The second stage employs a function called the *BERTifier,* which uses BERT, a pre-trained deep learning language model, to refine the sentence. The *BERTifier* iterates through each word in the sequence, masking and replacing it with the word that BERT predicts to be most contextually appropriate. This iterative process repeats until the sentence stabilizes, meaning no further changes are predicted by BERT. The *BERTifier's* functionality is exemplified in the appendix.

**Datasets and models used:**

- DailyDialog Dataset: https://huggingface.co/datasets/li2017dailydialog/daily\_dialog

- Cornell Movie Dialogs Corpus: https://www.cs.cornell.edu/~cristian/Chameleons\_in\_imagined\_conversations.html

- ELIZA Script (edited for the purposes of this book): https://github.com/codeanticode/eliza

- BERT base model (cased): https://huggingface.co/google-bert/bert-base-cased

- ChatGPT (gpt-4o-2024-08-06 and o1-preview-2024-09-12), used for code development and for writing the text above.

*This project is part of a larger research project, BERTIFIER, which focuses on practice-based ways to perform digital media archaeoloy of langujage models, particularly BERT.*

Licensed under Apache 2.0, see LICENSE file.