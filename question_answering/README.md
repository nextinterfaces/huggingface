# Question Answering Example

A simple demonstration of question answering using Hugging Face's transformers. The script shows how to:
- Load a pre-trained question answering model (DistilBERT)
- Extract answers from a given context
- Get precise responses to specific questions

## Quick Start

```bash
python3 ask_q.py
```

## How it Works

1. Uses the `distilbert-base-cased-distilled-squad` model (trained on SQuAD dataset)
2. Takes a context paragraph and a question as input
3. Extracts the relevant answer from the context
4. Returns the exact text span that answers the question

## Example Output

For the context:
```
"Hugging Face is a company that develops tools for natural language processing."
```

And the question:
```
"What does Hugging Face do?"
```

It returns:
```
develops tools for natural language processing
```

The model identifies and extracts the specific part of the context that directly answers the question. 