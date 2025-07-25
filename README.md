# Python Web 浏览器

一个基于 Python Flask 框架开发的网页浏览器应用，具有现代化的用户界面和完整的浏览器功能。

## 功能特性

- 🌐 **网页浏览**: 支持访问任何网站
- ⭐ **书签管理**: 添加、删除和管理书签
- 📚 **历史记录**: 自动记录访问历史
- 🎨 **现代化UI**: 美观的渐变界面设计
- 📱 **响应式设计**: 支持桌面和移动设备
- ⚡ **快速导航**: 支持回车键快速访问

## 安装和运行

### 1. 创建虚拟环境（推荐）
```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# Windows:
# venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 运行应用
```bash
python app.py
```

### 3. 访问浏览器
打开浏览器访问: `http://localhost:5060`

## 使用说明

### 基本导航
1. 在地址栏输入网址（如：`google.com`）
2. 点击"🚀 访问"按钮或按回车键
3. 网页将在右侧显示

### 书签功能
- 点击"⭐ 添加书签"按钮添加当前页面到书签
- 在左侧书签列表中点击任意书签快速访问
- 书签数据会自动保存到本地

### 历史记录
- 所有访问的网页都会自动记录到历史记录
- 点击历史记录中的任意条目可快速重新访问
- 可以清空历史记录

## 技术架构

- **后端**: Python Flask
- **前端**: HTML5 + CSS3 + JavaScript
- **数据存储**: JSON 文件
- **网络请求**: requests 库

## 文件结构

```
demo_webos/
├── app.py              # Flask 应用主文件
├── requirements.txt    # Python 依赖
├── templates/         # HTML 模板
│   └── browser.html   # 浏览器界面
├── bookmarks.json     # 书签数据（自动生成）
└── history.json       # 历史记录（自动生成）
```

## 注意事项

- 某些网站可能因为跨域限制无法正常显示
- 建议使用现代浏览器访问以获得最佳体验
- 书签和历史记录数据保存在本地文件中

## 开发说明

这是一个演示项目，展示了如何使用 Python 创建一个功能完整的 Web 浏览器应用。代码结构清晰，易于理解和扩展。
