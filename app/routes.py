from flask import render_template, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
from .utils.rag import RAGSystem

# Initialize RAG system
rag_system = RAGSystem()

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/upload', methods=['POST'])
    def upload_document():
        if 'document' not in request.files:
            return jsonify({'error': 'No document provided'}), 400
        
        file = request.files['document']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Process the document and add to RAG system
            try:
                rag_system.add_document(filepath)
                return jsonify({'message': 'Document uploaded and processed successfully'})
            except Exception as e:
                return jsonify({'error': str(e)}), 500
    
    @app.route('/ask', methods=['POST'])
    def ask_question():
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'No question provided'}), 400
        
        try:
            answer = rag_system.get_answer(data['question'])
            return jsonify({'answer': answer})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
