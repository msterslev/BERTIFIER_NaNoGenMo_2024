import random
import re
import torch
from transformers import BertTokenizer, BertForMaskedLM
from collections import defaultdict

# Check if CUDA is available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

intro_text = """This is a digital media archaeological exploration of AI-generated text, combining two distinct text generation techniques, both of which predate the ChatGPT moment and neither of which are state of the art. Markov Chains and the BERT language model are here combined to create a series of stylistically varied sections that explore the materiality of two different kinds of language models through their mutual probabilistic modeling of a series of datasets – and of one another. The project is divided into four parts, each shaped by a different dataset: everyday conversations, cinematic dialogue, therapeutic interactions, and a recursive corpus of the book’s own outputs. These datasets inform the tone and content of each section. See details below regarding the source of each of the first three datasets. The fourth (recursive) dataset consists of all the outputs from the *BERTifier* (see below) generated during the first three sections of the book.

The text-generation process unfolds in two stages. First, a Markov Chain algorithm constructs an initial sentence by analyzing the chosen dataset and probabilistically predicting word sequences based on observed patterns. This rudimentary output serves as the foundation. The second stage employs a function called the *BERTifier,* which uses BERT, a pre-trained deep learning language model, to refine the sentence. The *BERTifier* iterates through each word in the sequence, masking and replacing it with the word that BERT predicts to be most contextually appropriate. This iterative process repeats until the sentence stabilizes, meaning no further changes are predicted by BERT. The *BERTifier's* functionality is exemplified in the appendix.

**Datasets and models used:**
- DailyDialog Dataset: https://huggingface.co/datasets/li2017dailydialog/daily_dialog
- Cornell Movie Dialogs Corpus: https://www.cs.cornell.edu/~cristian/Chameleons_in_imagined_conversations.html
- ELIZA Script (edited for the purposes of this book): https://github.com/codeanticode/eliza
- BERT base model (cased): https://huggingface.co/google-bert/bert-base-cased
- ChatGPT (gpt-4o-2024-08-06 and o1-preview-2024-09-12), used for code development and for writing the text above.
"""

target_length = 5000
corpus_sources = {
    'daily_dialog_corpus.txt': './daily_dialog_corpus.txt',
    'movie_dialogs_corpus.txt': './movie_dialogs_corpus.txt',
    'eliza_corpus.txt': './eliza_corpus.txt'
}
n_gram_size = 2
book_title = 'When Bert met Markov'
book_subtitle = 'Mirrors Reflect Differently'
section_names = ["Quotidian", "Epic", "Therapeutic", "Recursive"]
file_title = book_title.replace(" ", "_")

# Initialize BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
model = BertForMaskedLM.from_pretrained('bert-base-cased').to(device)
model.eval()

# Updated MarkovChain class
class MarkovChain:
    def __init__(self, n=2):
        self.n = n
        self.initial_corpus = []
        self.expanded_corpus = []
        self.model = defaultdict(list)
        self.start_words = []

    def add_initial_corpus(self, text):
        self.initial_corpus.append(text)
        self._add_to_model(text)

    def _add_to_model(self, text):
        # Split text into sentences using sentence-ending punctuation
        sentences = re.split(r'(?<=[.!?])\s+', text)
        for sentence in sentences:
            # Updated regex to handle apostrophes and punctuation
            words = re.findall(r"\w+(?:'\w+)*|[^\w\s]", sentence)
            if len(words) >= self.n:
                self.start_words.append(tuple(words[:self.n]))
                for i in range(len(words) - self.n):
                    key = tuple(words[i:i+self.n])
                    next_word = words[i+self.n]
                    self.model[key].append(next_word)
                # Handle the last n-gram
                key = tuple(words[-self.n:])
                self.model[key].append('')
            elif words:  # For sentences shorter than n
                self.start_words.append(tuple(words))
                self.model[tuple(words)] += ['']

    def generate_sentence(self, max_words=500):
        key = random.choice(self.start_words)
        result = list(key)
        while True:
            next_words = self.model.get(key, [])
            if not next_words:
                break
            next_word = random.choice(next_words)
            if next_word == '':
                break
            result.append(next_word)
            # Check if the last word is a sentence-ending punctuation mark
            if next_word in ('.', '!', '?'):
                break
            if len(result) >= max_words:
                break  # Stop if maximum word limit is reached
            key = tuple(result[-self.n:])
        # Adjust token joining to handle punctuation without extra spaces
        sentence = ''
        for word in result:
            if word in ('.', '!', '?', ',', ';', ':'):
                sentence = sentence.rstrip() + word + ' '
            else:
                sentence += word + ' '
        return sentence.strip()

# Updated bertify_long_text function with processing for small texts
def bertify_long_text(text):
    max_sequence_length = 512  # Max sequence length for BERT
    min_chunk_length = 80      # Minimum chunk length
    min_mask_length = 20       # Minimum mask length

    # Tokenize the entire text
    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)
    total_tokens = len(token_ids)

    # If the text is short, process it in one chunk
    if total_tokens + 2 <= max_sequence_length:
        print("\nProcessing entire text as a single chunk.")
        chunk_token_ids = token_ids
        mask_indices = list(range(len(chunk_token_ids)))  # Mask all tokens
        processed_chunk_token_ids = bertify_chunk(chunk_token_ids, mask_indices)
        output_text = tokenizer.decode(processed_chunk_token_ids, skip_special_tokens=True)
        return output_text
    else:
        # Determine dynamic chunk sizes based on total_tokens
        num_chunks = max(1, total_tokens // 200)
        max_chunk_length = min(max_sequence_length - 2, (total_tokens // num_chunks) + 2)  # +2 for [CLS] and [SEP]
        max_chunk_length = max(min_chunk_length, max_chunk_length)  # Ensure at least min_chunk_length

        # Adjust mask_length to be appropriate
        mask_length = max(min_mask_length, max_chunk_length // 3)
        mask_length = min(mask_length, max_chunk_length - 2)  # Ensure mask_length does not exceed max_chunk_length - 2

        # Now compute context_size
        context_size = max(0, (max_chunk_length - mask_length) // 2)

        processed_token_ids = [None] * total_tokens

        position = 0
        chunk_counter = 1
        while position < total_tokens:
            mask_start = position
            mask_end = min(mask_start + mask_length, total_tokens)

            context_size_before = min(context_size, mask_start)
            context_size_after = min(context_size, total_tokens - mask_end)

            chunk_start = mask_start - context_size_before
            chunk_end = mask_end + context_size_after

            chunk_token_ids = token_ids[chunk_start:chunk_end]
            chunk_length = len(chunk_token_ids)

            # Indices of masked tokens in chunk
            mask_indices_in_chunk = list(range(context_size_before, context_size_before + (mask_end - mask_start)))

            # Adjust mask indices for special tokens
            adjusted_mask_indices = [idx + 1 for idx in mask_indices_in_chunk]  # +1 for [CLS]

            print(f"\nProcessing chunk {chunk_counter}: Tokens {chunk_start} to {chunk_end} of {total_tokens}")
            chunk_counter += 1

            # Process the chunk
            processed_chunk_token_ids = bertify_chunk(chunk_token_ids, adjusted_mask_indices)

            # Update the processed_token_ids list with the new token IDs
            for i, idx in enumerate(range(chunk_start, chunk_end)):
                processed_token_id = processed_chunk_token_ids[i]
                # Only update if not already processed
                if processed_token_ids[idx] is None:
                    processed_token_ids[idx] = processed_token_id

            position += mask_length

        # Replace any None values with the original token IDs
        for i, token_id in enumerate(processed_token_ids):
            if token_id is None:
                processed_token_ids[i] = token_ids[i]

        # Convert token IDs to string using tokenizer.decode
        output_text = tokenizer.decode(processed_token_ids, skip_special_tokens=True)
        return output_text

def bertify_chunk(chunk_token_ids, mask_indices):
    # Add special tokens
    input_ids = [tokenizer.cls_token_id] + chunk_token_ids + [tokenizer.sep_token_id]
    attention_mask = [1] * len(input_ids)

    # Convert to tensors and move to the device
    input_ids = torch.tensor(input_ids).to(device)
    attention_mask = torch.tensor(attention_mask).to(device)

    token_ids = input_ids.clone()

    prev_iterations = []
    iteration = 1

    while True:
        print(f"\nBERTIFY iteration {iteration}:")
        prev_token_ids = token_ids.clone()

        for i in mask_indices:
            # Mask the current token
            masked_input_ids = token_ids.clone()
            masked_input_ids[i] = tokenizer.mask_token_id

            with torch.no_grad():
                outputs = model(
                    masked_input_ids.unsqueeze(0),
                    attention_mask=attention_mask.unsqueeze(0)
                )
                predictions = outputs.logits

            predicted_index = torch.argmax(predictions[0, i]).item()

            token_ids[i] = predicted_index  # Update token_ids with the predicted token ID

        # Print the tokens after this iteration
        tokens_str = tokenizer.decode(token_ids[1:-1].cpu(), skip_special_tokens=True)
        print(f"Tokens after iteration {iteration}: {tokens_str}")

        # Check for convergence or loop
        if torch.equal(token_ids, prev_token_ids):
            print("Convergence achieved.")
            break
        if any(torch.equal(token_ids, prev) for prev in prev_iterations):
            print("Loop detected. Stopping iterations.")
            break
        # Keep only the last three iterations to detect loops
        prev_iterations.append(prev_token_ids)
        if len(prev_iterations) > 3:
            prev_iterations.pop(0)
        iteration += 1

    # Remove special tokens and move back to CPU
    output_token_ids = token_ids[1:-1].cpu()
    return output_token_ids

# Updated bertify_chunk function with detailed step-by-step tracking
def bertify_chunk_with_details(chunk_token_ids, mask_indices):
    input_ids = [tokenizer.cls_token_id] + chunk_token_ids + [tokenizer.sep_token_id]
    attention_mask = [1] * len(input_ids)

    # Convert to tensors and move to the device
    input_ids = torch.tensor(input_ids).to(device)
    attention_mask = torch.tensor(attention_mask).to(device)

    token_ids = input_ids.clone()
    prev_iterations = []
    detailed_steps = []

    while True:
        prev_token_ids = token_ids.clone()

        for idx in mask_indices:
            i = idx + 1  # Adjust index for [CLS] token

            # Mask the current token
            masked_input_ids = token_ids.clone()
            masked_input_ids[i] = tokenizer.mask_token_id

            with torch.no_grad():
                outputs = model(
                    masked_input_ids.unsqueeze(0),
                    attention_mask=attention_mask.unsqueeze(0)
                )
                predictions = outputs.logits

            predicted_index = torch.argmax(predictions[0, i]).item()
            token_ids[i] = predicted_index  # Update token_ids with the predicted token ID

            # Track the current state of the sentence with the current token highlighted
            tokens = tokenizer.convert_ids_to_tokens(token_ids[1:-1])
            tokens_display = tokens.copy()
            tokens_display[idx] = f"[{tokens_display[idx]}]"  # Highlight current token
            detailed_steps.append(" ".join(tokens_display))

        # Check for convergence or loop
        if torch.equal(token_ids, prev_token_ids):
            break
        if any(torch.equal(token_ids, prev) for prev in prev_iterations):
            break
        # Keep only the last three iterations to detect loops
        prev_iterations.append(prev_token_ids)
        if len(prev_iterations) > 3:
            prev_iterations.pop(0)

    output_token_ids = token_ids[1:-1].cpu()
    return output_token_ids, detailed_steps

# Function to generate appendix examples
def generate_bertifier_examples(markov_output, section_name):
    chunk_token_ids = tokenizer.convert_tokens_to_ids(tokenizer.tokenize(markov_output))
    mask_indices = list(range(len(chunk_token_ids)))  # Mask all tokens
    processed_chunk_token_ids, detailed_steps = bertify_chunk_with_details(chunk_token_ids, mask_indices)
    
    final_output = tokenizer.decode(processed_chunk_token_ids, skip_special_tokens=True)
    
    appendix_text = f"## Appendix: Unraveling BERTifier\n\n"
    appendix_text += f"### Example from Section: {section_name}\n\n"
    appendix_text += f"**Initial Markov Output:**\n{markov_output}\n\n"
    appendix_text += "**BERTifier Refinement Steps:**\n\n"
    for step in detailed_steps:
        appendix_text += f"{step}\n\n"
    appendix_text += f"**Final Stabilized Output:**\n{final_output}\n\n"
    return appendix_text

# Initialize Markov chains for the three predefined corpora
markov_chains = {}
for corpus_name, corpus_file in corpus_sources.items():
    markov_chain = MarkovChain(n=n_gram_size)
    # Read the corpus from a text file
    with open(corpus_file, 'r', encoding='utf-8') as f:
        corpus_text = f.read()
    # Add the corpus to the Markov chain
    markov_chain.add_initial_corpus(corpus_text)
    markov_chains[corpus_name] = markov_chain

# Initialize lists to accumulate BERT outputs and first Markov outputs
bert_outputs = []
first_markov_outputs = []

# Calculate the length of each section
section_length = target_length // 4

# Open Markdown file for writing
with open(file_title + ".md", "w", encoding='utf-8') as f:
    f.write(f"# {book_title}: {book_subtitle}\n\n")
    f.write(f"{intro_text}\n\n")

    total_words = 0
    dialogue_counter = 1

    # Process each of the first three sections
    for idx, (corpus_name, markov_chain) in enumerate(markov_chains.items(), start=1):
        section_name = section_names[idx - 1]  # Get the corresponding section name
        print(f"\n=== Section {idx}: {section_name} ===")
        f.write(f"## Section {idx}: {section_name}\n\n")
        section_words = 0
        first_markov_output = None  # Initialize to store the first Markov output

        while section_words < section_length:
            print(f"\n--- Generating dialogue {dialogue_counter} ---")
            num_sentences = random.randint(1, 5)
            markov_outputs = []
            for _ in range(num_sentences):
                markov_output = markov_chain.generate_sentence()
                markov_outputs.append(markov_output)
                section_words += len(markov_output.split())
                # Break if section words exceed limit
                if section_words >= section_length:
                    break
            combined_markov_output = ' '.join(markov_outputs)
            if first_markov_output is None:
                first_markov_output = combined_markov_output  # Store the first Markov output
            print(f"Markov Output:\n{combined_markov_output}\n")
            f.write(f"**Markov**:\n{combined_markov_output}\n\n")
            bertified_output = bertify_long_text(combined_markov_output)
            print(f"BERTIFIED Output:\n{bertified_output}\n")
            f.write(f"**Bert**:\n{bertified_output}\n\n")
            total_words += len(bertified_output.split())
            dialogue_counter += 1

            # Add this line to accumulate BERT outputs
            bert_outputs.append(bertified_output)
        # Append the first Markov output for this section
        first_markov_outputs.append(first_markov_output)

    # Create the fourth Markov chain from the accumulated BERT outputs
    print(f"\n=== Section 4: {section_names[3]} ===")
    f.write(f"## Section 4: {section_names[3]}\n\n")
    bert_corpus_text = ' '.join(bert_outputs)
    bert_markov_chain = MarkovChain(n=n_gram_size)
    bert_markov_chain.add_initial_corpus(bert_corpus_text)

    section_words = 0
    first_markov_output = None  # Initialize to store the first Markov output

    while section_words < section_length:
        print(f"\n--- Generating dialogue {dialogue_counter} ---")
        num_sentences = random.randint(1, 5)
        markov_outputs = []
        for _ in range(num_sentences):
            markov_output = bert_markov_chain.generate_sentence()
            markov_outputs.append(markov_output)
            section_words += len(markov_output.split())
            # Break if section words exceed limit
            if section_words >= section_length:
                break
        combined_markov_output = ' '.join(markov_outputs)
        if first_markov_output is None:
            first_markov_output = combined_markov_output  # Store the first Markov output
        print(f"Markov Output:\n{combined_markov_output}\n")
        f.write(f"**MARKOV**:\n{combined_markov_output}\n\n")
        bertified_output = bertify_long_text(combined_markov_output)
        print(f"BERTIFIED Output:\n{bertified_output}\n")
        f.write(f"**BERTIFIER**:\n{bertified_output}\n\n")
        total_words += len(bertified_output.split())
        dialogue_counter += 1

        # Add this line to accumulate BERT outputs
        bert_outputs.append(bertified_output)
    # Append the first Markov output for the fourth section
    first_markov_outputs.append(first_markov_output)

print("Dialogue generation complete!")

# Generate appendix examples using the stored first Markov outputs
with open(file_title + ".md", "a", encoding='utf-8') as f:
    for idx, section_name in enumerate(section_names, start=1):
        if idx <= len(first_markov_outputs):
            markov_output = first_markov_outputs[idx - 1] if first_markov_outputs[idx - 1] else "No Markov output available for this section."
            appendix_example = generate_bertifier_examples(markov_output, section_name)
            f.write(appendix_example)

print("Appendix generation complete!")
