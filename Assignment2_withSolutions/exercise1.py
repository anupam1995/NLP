BRACKETS = ["(", ")", "[", "]", "{", "}"]
EOS_SYMBOLS = [".", "!", "?", ":"]
SEPARATORS = [",", "/"]
ABBREVATIONS = ["Ph.D.", "Dr.", "M.Sc."]

def tokenize(text):

    tokens = text.split(" ")
    # abbreviations = set()
    ind = 0
    while ind < len(tokens):
        current_token = tokens[ind]
        # id abbrevations:
        if "." in current_token and current_token in ABBREVATIONS:
            pass
        elif current_token[-1] in EOS_SYMBOLS + BRACKETS + SEPARATORS:
            tokens.insert(ind, current_token[:-1])
            ind += 1
            tokens[ind] = current_token[-1]
            # ind += 1
        elif current_token[0] in BRACKETS:
            tokens.insert(ind, current_token[0])
            ind += 1
            tokens[ind] = current_token[1:]
        elif "http:" in current_token or "https:" in current_token or "www." in current_token:
            pass
        elif "@" in current_token:
            pass
        elif any([char in SEPARATORS for char in current_token]):
            date_char_format = [
                [str(n) for n in range(4)],
                [str(n) for n in range(10)],
                ["/"],
                [str(n) for n in range(2)],
                [str(n) for n in range(10)],
                ["/"],
                [str(n) for n in range(10)],
                [str(n) for n in range(10)],
            ]
            is_date = len(current_token) == len(date_char_format)
            if is_date:
                for char, date_chars in zip(current_token, date_char_format):
                    is_date = char in date_chars
                    if not is_date:
                        break
            if not is_date:
                new_token = ""
                for char in current_token:
                    if char in SEPARATORS:
                        tokens.insert(ind, new_token)
                        ind += 1
                        tokens.insert(ind, char)
                        ind += 1
                        new_token = ""
                    else:
                        new_token += char
                tokens[ind] = new_token
        elif "#" in current_token:
            new_tokens = ["#" + new_token for new_token in current_token.split("#")[1:]]
            if len(new_tokens) > 1:
                for new_token in new_tokens[:-1]:
                    tokens.insert(ind, new_token)
                    ind += 1
                tokens[ind] = new_tokens[-1]
        ind += 1
    return tokens


test_text = "He has a M.Sc. in Math and she has a Ph.D. in NLP. A session costs 45.55$ or $50.00. As of 01/02/06, please email X/Y at someone@brown.edu or visit http://www.stanford.edu and if link does not work try https://www.stanford.edu instead. #test#test2#nlproc"
print(tokenize(test_text))
