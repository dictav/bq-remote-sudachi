from flask import Flask, jsonify, request
from sudachipy import Dictionary, SplitMode

app = Flask(__name__)
app.json.ensure_ascii=False
tokenizer = Dictionary().create()

@app.route('/check', methods=['GET'])
def check():
    return "OK"

@app.route('/tokenize', methods=['POST'])
def check_tokenize():
    text = request.json["text"]

    morphemes = tokenizer.tokenize(text)
    tokens = [build_token(i,m) for i,m in enumerate(morphemes)]
    
    return jsonify({"tokens": tokens})

# BigQuery Remote Function endpoint
@app.route('/', methods=['POST'])
def tokenize():
    print("header", dict(request.headers))
    print("body", request.json)

    try:
        replies = []
        calls = request.json['calls']
        for call in calls:
            morphemes = tokenizer.tokenize(call[0])
            tokens = [build_token(i,m) for i,m in enumerate(morphemes)]
            replies.append({"tokens": tokens})

        return jsonify( { "replies" :  replies } )
    except Exception as e:
        return jsonify( { "errorMessage": str(e) } ), 400

def build_token(idx, m):
    pos = m.part_of_speech()
    return {
        "idx": idx,
        "surface": m.surface(),
        "pos_id": m.part_of_speech_id(),
        "pos": pos,
        "_pos": ','.join(pos),
        "_pos0": pos[0],
        "base_form": m.dictionary_form(),
        "normalized": m.normalized_form(),
        "reading": m.reading_form(),
        "dict_id": m.dictionary_id(),
        "synonym_group_ids": m.synonym_group_ids(),
    }

