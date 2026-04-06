# Token
Tokens and tokenizer concept

## Token definition
Tokens are the smallest unit of data that an LLM would process. 

## Tokenizer definition
It is the component that converts the raw text into tokens before a model(transformer) can process it.
It has a vocabulary (lookup table) that has id for each text and those and id mapped and given as response tokens.

## Need for tokens:

- If we use token for each character, the sequence grows very long and the model might loose the words meaning.
- If we use token for each word, millions of words are there and some words might go missing.
- So, the tokeniser is trained with words and if it is not present in the vocabulary, it then split into halves/characters.

## Tokenisation Algorithm

 - Gemini uses **SentencePie with BPE** (Byte Pair Encoding) algorithm to generate tokens.
 - **Find the most common pair of characters → merge them into one token → repeat**
