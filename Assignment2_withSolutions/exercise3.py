from transformers import T5Tokenizer

tokenizer = T5Tokenizer.from_pretrained("t5-small")
test_text = "He has a M.Sc. in Math and a Ph.D. in NLP. A session costs 45.55$ or $50. As of 01/02/06, please email X at someone@brown.edu or visit http://www.stanford.edu (if link does not work try https://www.stanford.edu). #test#test2#nlproc"
print(tokenizer.convert_ids_to_tokens(tokenizer(test_text).input_ids))