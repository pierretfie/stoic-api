# 🧘 Stoic API

A simple Python Flask API that scrapes and returns Stoic philosophy quotes from [stoic-quotes.com](https://stoic-quotes.com).

> 🌐 **Live Demo:** [https://stoic-api.onrender.com/quote](https://stoic-api.onrender.com/quote)

---

## 🔍 Features

- 💬 Fetches real-time quotes from stoic-quotes.com
- 📦 JSON-formatted response
- 🐍 Built with Flask, BeautifulSoup, and Requests
- 🚀 Deployable via Docker or Render
- 🔐 CORS-enabled (ready for browser apps)

---

## 🚀 Usage

### ✅ Endpoint

```http
GET https://stoic-api.onrender.com/quote
````

### 🔄 Example Response

```json
{
  "quote": "We suffer more in imagination than in reality. - Seneca"
}
```

---

## 🐳 Docker Deployment

### 🔧 Build & Run

```bash
docker build -t stoic-api .
docker run -d -p 8000:8000 --restart always stoic-api
```

Access it at: `http://localhost:8000/quote`

---

## 📁 Docker Compose (Optional)

```yaml
version: "3.9"

services:
  stoic-api:
    build: .
    container_name: stoic-api
    ports:
      - "8000:8000"
    restart: always
```

Run with:

```bash
docker-compose up -d --build
```

---

## 🌐 Deploy to Render (Free)

1. Push this repo to GitHub
2. Create a new **Web Service** on [Render](https://render.com)
3. Set:

   * **Start command**: `python app.py`
   * **Build command**: `pip install flask flask-cors requests beautifulsoup4`
   * Python version: 3.x

> ✅ That’s it — your API is live!

---

## ⚙️ Tech Stack

* Flask
* Requests
* BeautifulSoup4
* Flask-CORS


---

## ✨ Credits

All quotes are scraped from [stoic-quotes.com](https://stoic-quotes.com)
Built by maina peter, powered by 🐍 Flask and 📜 the Stoics.

---
