# When Bert met Markov: Mirrors Reflect Differently

This is a digital media archaeological exploration of AI-generated text, combining two distinct text generation techniques, both of which predate the ChatGPT moment and neither of which are state of the art. Markov Chains and the BERT language model are here combined to create a series of stylistically varied sections that explore the materiality of two different kinds of language models through their mutual probabilistic modeling of a series of datasets – and of one another. The project is divided into four parts, each shaped by a different dataset: everyday conversations, cinematic dialogue, therapeutic interactions, and a recursive corpus of the book’s own outputs. These datasets inform the tone and content of each section. See details below regarding the source of each of the first three datasets. The fourth (recursive) dataset consists of all the outputs from the *BERTifier* (see below) generated during the first three sections of the book.

The text-generation process unfolds in two stages. First, a Markov Chain algorithm constructs an initial sentence by analyzing the chosen dataset and probabilistically predicting word sequences based on observed patterns. This rudimentary output serves as the foundation. The second stage employs a function called the *BERTifier,* which uses BERT, a pre-trained deep learning language model, to refine the sentence. The *BERTifier* iterates through each word in the sequence, masking and replacing it with the word that BERT predicts to be most contextually appropriate. This iterative process repeats until the sentence stabilizes, meaning no further changes are predicted by BERT. The *BERTifier's* functionality is exemplified in the appendix.

**Datasets and models used:**
- DailyDialog Dataset: https://huggingface.co/datasets/li2017dailydialog/daily_dialog
- Cornell Movie Dialogs Corpus: https://www.cs.cornell.edu/~cristian/Chameleons_in_imagined_conversations.html
- ELIZA Script (edited for the purposes of this book): https://github.com/codeanticode/eliza
- BERT base model (cased): https://huggingface.co/google-bert/bert-base-cased
- ChatGPT (gpt-4o-2024-08-06 and o1-preview-2024-09-12), used for code development and for writing the text above.


## Section 1: Quotidian

**Markov**:
You should appear frugal and prudent.

**Bert**:
It would be frugal and prudent.

## Section 2: Epic

**Markov**:
You blew it!

**Bert**:
I knew it!

## Section 3: Therapeutic

**Markov**:
Can you think machines have to do with your problems?

**Bert**:
Do you think they want to stay with their families?

## Section 4: Recursive

**MARKOV**:
I knew it!

**BERTIFIER**:
I knew it!

## Appendix: Unraveling BERTifier

### Example from Section: Quotidian

**Initial Markov Output:**
You should appear frugal and prudent.

**BERTifier Refinement Steps:**

[It] should appear f ##rug ##al and p ##rud ##ent .

It [would] appear f ##rug ##al and p ##rud ##ent .

It would [be] f ##rug ##al and p ##rud ##ent .

It would be [f] ##rug ##al and p ##rud ##ent .

It would be f [##rug] ##al and p ##rud ##ent .

It would be f ##rug [##al] and p ##rud ##ent .

It would be f ##rug ##al [and] p ##rud ##ent .

It would be f ##rug ##al and [p] ##rud ##ent .

It would be f ##rug ##al and p [##rud] ##ent .

It would be f ##rug ##al and p ##rud [##ent] .

It would be f ##rug ##al and p ##rud ##ent [.]

[It] would be f ##rug ##al and p ##rud ##ent .

It [would] be f ##rug ##al and p ##rud ##ent .

It would [be] f ##rug ##al and p ##rud ##ent .

It would be [f] ##rug ##al and p ##rud ##ent .

It would be f [##rug] ##al and p ##rud ##ent .

It would be f ##rug [##al] and p ##rud ##ent .

It would be f ##rug ##al [and] p ##rud ##ent .

It would be f ##rug ##al and [p] ##rud ##ent .

It would be f ##rug ##al and p [##rud] ##ent .

It would be f ##rug ##al and p ##rud [##ent] .

It would be f ##rug ##al and p ##rud ##ent [.]

**Final Stabilized Output:**
It would be frugal and prudent.

## Appendix: Unraveling BERTifier

### Example from Section: Epic

**Initial Markov Output:**
You blew it!

**BERTifier Refinement Steps:**

[I] blew it !

I [knew] it !

I knew [it] !

I knew it [.]

[I] knew it .

I [knew] it .

I knew [it] .

I knew it [.]

**Final Stabilized Output:**
I knew it.

## Appendix: Unraveling BERTifier

### Example from Section: Therapeutic

**Initial Markov Output:**
Can you think machines have to do with your problems?

**BERTifier Refinement Steps:**

[Do] you think machines have to do with your problems ?

Do [you] think machines have to do with your problems ?

Do you [think] machines have to do with your problems ?

Do you think [they] have to do with your problems ?

Do you think they [have] to do with your problems ?

Do you think they have [to] do with your problems ?

Do you think they have to [deal] with your problems ?

Do you think they have to deal [with] your problems ?

Do you think they have to deal with [their] problems ?

Do you think they have to deal with their [parents] ?

Do you think they have to deal with their parents [?]

[Do] you think they have to deal with their parents ?

Do [you] think they have to deal with their parents ?

Do you [think] they have to deal with their parents ?

Do you think [they] have to deal with their parents ?

Do you think they [have] to deal with their parents ?

Do you think they have [to] deal with their parents ?

Do you think they have to [live] with their parents ?

Do you think they have to live [with] their parents ?

Do you think they have to live with [their] parents ?

Do you think they have to live with their [parents] ?

Do you think they have to live with their parents [?]

[Do] you think they have to live with their parents ?

Do [you] think they have to live with their parents ?

Do you [think] they have to live with their parents ?

Do you think [they] have to live with their parents ?

Do you think they [want] to live with their parents ?

Do you think they want [to] live with their parents ?

Do you think they want to [stay] with their parents ?

Do you think they want to stay [with] their parents ?

Do you think they want to stay with [their] parents ?

Do you think they want to stay with their [families] ?

Do you think they want to stay with their families [?]

[Do] you think they want to stay with their families ?

Do [you] think they want to stay with their families ?

Do you [think] they want to stay with their families ?

Do you think [they] want to stay with their families ?

Do you think they [want] to stay with their families ?

Do you think they want [to] stay with their families ?

Do you think they want to [stay] with their families ?

Do you think they want to stay [with] their families ?

Do you think they want to stay with [their] families ?

Do you think they want to stay with their [families] ?

Do you think they want to stay with their families [?]

**Final Stabilized Output:**
Do you think they want to stay with their families?

## Appendix: Unraveling BERTifier

### Example from Section: Recursive

**Initial Markov Output:**
I knew it!

**BERTifier Refinement Steps:**

[I] knew it !

I [knew] it !

I knew [it] !

I knew it [.]

[I] knew it .

I [knew] it .

I knew [it] .

I knew it [.]

**Final Stabilized Output:**
I knew it.

