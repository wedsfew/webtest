from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
from urllib.parse import urlparse, urljoin
import re
from datetime import datetime
import json
import os

app = Flask(__name__)

# 存储书签和历史记录
bookmarks = []
history = []

# 确保数据文件存在
def load_data():
    global bookmarks, history
    try:
        if os.path.exists('bookmarks.json'):
            with open('bookmarks.json', 'r', encoding='utf-8') as f:
                bookmarks = json.load(f)
        if os.path.exists('history.json'):
            with open('history.json', 'r', encoding='utf-8') as f:
                history = json.load(f)
    except:
        pass

def save_data():
    with open('bookmarks.json', 'w', encoding='utf-8') as f:
        json.dump(bookmarks, f, ensure_ascii=False, indent=2)
    with open('history.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

# 加载数据
load_data()

@app.route('/')
def index():
    return render_template('browser.html', bookmarks=bookmarks, history=history)

@app.route('/navigate', methods=['POST'])
def navigate():
    url = request.form.get('url', '').strip()
    
    if not url:
        return jsonify({'error': '请输入有效的URL'})
    
    # 添加协议前缀
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        # 获取网页内容
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        # 添加到历史记录
        history_entry = {
            'url': url,
            'title': extract_title(response.text),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        history.insert(0, history_entry)
        
        # 限制历史记录数量
        if len(history) > 50:
            history.pop()
        
        save_data()
        
        return jsonify({
            'success': True,
            'url': url,
            'content': response.text,
            'status_code': response.status_code
        })
        
    except Exception as e:
        return jsonify({'error': f'无法访问该网站: {str(e)}'})

@app.route('/add_bookmark', methods=['POST'])
def add_bookmark():
    url = request.form.get('url', '').strip()
    title = request.form.get('title', '').strip()
    
    if not url:
        return jsonify({'error': '请输入有效的URL'})
    
    # 检查是否已存在
    for bookmark in bookmarks:
        if bookmark['url'] == url:
            return jsonify({'error': '该书签已存在'})
    
    bookmark = {
        'url': url,
        'title': title or url,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    bookmarks.append(bookmark)
    save_data()
    
    return jsonify({'success': True, 'message': '书签添加成功'})

@app.route('/remove_bookmark', methods=['POST'])
def remove_bookmark():
    url = request.form.get('url', '')
    
    for i, bookmark in enumerate(bookmarks):
        if bookmark['url'] == url:
            del bookmarks[i]
            save_data()
            return jsonify({'success': True, 'message': '书签删除成功'})
    
    return jsonify({'error': '书签不存在'})

@app.route('/clear_history', methods=['POST'])
def clear_history():
    global history
    history.clear()
    save_data()
    return jsonify({'success': True, 'message': '历史记录已清空'})

def extract_title(html_content):
    """从HTML内容中提取标题"""
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    if title_match:
        return title_match.group(1)
    return '无标题'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5060) 