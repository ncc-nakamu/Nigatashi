"""from flask import Flask, render_template, request, jsonify, abort
import MeCab
import os

app = Flask(__name__)

def segment_text(text):
    try:
        print(f"Segmenting text: {text}")  # デバッグ用ログを追加
        
        # mecabrcのパスを環境変数で指定する
        mecab_rc_path = os.environ.get('MECABRC', 'C:\\Program Files\\MeCab\\etc\\mecabrc')
        mecab = MeCab.Tagger(f'-Owakati -r {mecab_rc_path}')
        
        parsed_text = mecab.parse(text)
        
        if parsed_text is None:
            print(f"MeCab failed to parse text: {text}")
            return None
        
        words = parsed_text.split()
        output_text = ' '.join(words)
        print(f"Segmented text: {output_text}")  # デバッグ用ログを追加
        return output_text
    except Exception as e:
        print(f"Error in segmenting text: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        if 'texts' not in data:
            abort(400, description="Missing 'texts' in request data")
        
        texts = data['texts']  # textsは複数のテキストのリスト
        if not isinstance(texts, list):
            abort(400, description="'texts' should be a list of strings")
        
        segmented_texts = [segment_text(text) for text in texts]
        return jsonify({'segmented_texts': segmented_texts})
    except Exception as e:
        print(f"Error in processing request: {e}")
        abort(500, description="Internal server error")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # PORT 環境変数からポートを取得
    app.run(host='0.0.0.0', port=port, debug=True)"""
from flask import Flask, render_template, request, jsonify
import MeCab
import os
 
app = Flask(__name__)
 
def segment_text(text):
    mecab = MeCab.Tagger('-Owakati')
    parsed_text = mecab.parse(text)
    words = parsed_text.split()
    output_text = ' '.join(words)
    return output_text
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    texts = data['texts']  # textsは複数のテキストのリスト
    segmented_texts = [segment_text(text) for text in texts]
    return jsonify({'segmented_texts': segmented_texts})
 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # 環境変数からポートを取得
    app.run(host='0.0.0.0', port=port, debug=True)


