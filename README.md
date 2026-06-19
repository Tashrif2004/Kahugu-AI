# 🤖 CAUGU - Advanced AI Assistant System

**CAUGU** is a powerful, modular AI assistant inspired by JARVIS with multi-agent architecture. Built with open-source tools and free APIs.

## 🎯 Core Features

- 🧠 **Central Agent** - Main orchestrator and decision maker
- 💬 **Communication Agent** - Real-time notifications & alerts
- 📱 **Social Media Agent** - Automated posts with approval workflow
- 🏃 **Fitness Agent** - Tracks workouts, movements, health insights
- 🔬 **Knowledge Agent** - Answers questions, provides advice
- 🎨 **Creative Agent** - Generates images, music, visuals
- 🗺️ **Information Agent** - Maps, location services, web search
- 🎤 **Voice Agent** - Voice recognition & synthesis

## 📋 Architecture

```
┌─────────────────────────────────┐
│     CAUGU Central Agent          │
│  - Task Distribution             │
│  - Agent Coordination            │
│  - Context Management            │
└──────────────┬──────────────────┘
       ┌───────┼─────────┬──────────┐
       │       │         │          │
       ▼       ▼         ▼          ▼
┌────────┐┌────────┐┌────────┐┌────────┐
│Comm.   ││Social  ││Fitness ││Knowledge
│Agent   ││Media   ││Agent   ││ Agent
└────────┘└────────┘└────────┘└────────┘
       │       │         │          │
       └───────┼─────────┼──────────┘
               │         │
       ┌───────┴─────────┴───────┐
       │                         │
       ▼                         ▼
   ┌────────┐              ┌────────┐
   │Creative││              │ Info   │
   │Agent   ││              │ Agent  │
   └────────┘              └────────┘
```

## 🛠️ Tech Stack (Free & Open Source)

| Component | Technology | Alternative |
|-----------|-----------|-------------|
| **LLM** | Mistral/LLaMA 2 | Ollama |
| **Image Gen** | Stable Diffusion | DALL-E mini |
| **Music Gen** | MusicGen | Jukebox |
| **Maps** | OpenStreetMap | Folium |
| **Database** | PostgreSQL | SQLite |
| **Voice** | Whisper | Mozilla STT |
| **Messaging** | Telegram Bot | Discord Bot |
| **Deployment** | Docker | Local/Cloud |

## 📦 Installation

### Prerequisites
```bash
Python 3.10+
Docker (optional)
PostgreSQL (optional, SQLite default)
```

### Setup

```bash
# Clone repository
git clone https://github.com/Tashrif2004/Kahugu-AI.git
cd Kahugu-AI

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download LLM model (first time)
python scripts/download_models.py

# Configure environment
cp .env.example .env
nano .env  # Add your Telegram bot token, etc.

# Run CAUGU
python main.py
```

## 📁 Project Structure

```
Kahugu-AI/
├── agents/
│   ├── central_agent.py       # Main orchestrator
│   ├── communication_agent.py  # Notifications
│   ├── social_media_agent.py   # Social posting
│   ├── fitness_agent.py        # Workout tracking
│   ├── knowledge_agent.py      # QA system
│   ├── creative_agent.py       # Image/music generation
│   └── info_agent.py           # Maps & web search
├── models/
│   ├── llm_handler.py          # LLaMA/Mistral
│   ├── image_gen.py            # Stable Diffusion
│   └── music_gen.py            # MusicGen
├── services/
│   ├── telegram_service.py     # Telegram integration
│   ├── database_service.py     # DB operations
│   ├── tracking_service.py     # GPS/fitness tracking
│   └── map_service.py          # OpenStreetMap
├── utils/
│   ├── config.py               # Configuration
│   ├── logger.py               # Logging
│   └── helpers.py              # Utility functions
├── scripts/
│   ├── download_models.py      # Model downloader
│   ├── setup_db.py             # Database setup
│   └── train_classifier.py     # Model training
├── docker/
│   ├── Dockerfile              # Container setup
│   └── docker-compose.yml      # Multi-container
├── tests/
│   └── test_agents.py          # Unit tests
├── .env.example                # Environment template
├── requirements.txt            # Dependencies
└── main.py                     # Entry point
```

## 🔧 Configuration

Create `.env` file:

```env
# Telegram
TELEGRAM_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id

# Database
DATABASE_URL=sqlite:///caugu.db
# Or PostgreSQL:
# DATABASE_URL=postgresql://user:password@localhost/caugu

# Models
LLM_MODEL=mistral-7b-instruct
IMAGE_MODEL=stable-diffusion-v1.5

# Services
OPENSTREETMAP_API_KEY=free
WEATHER_API_KEY=your_key
YOUTUBE_API_KEY=free_tier

# Fitness Tracking
TRACKING_ENABLED=true
LOCATION_TRACKING=true
```

## 📊 Features Breakdown

### 🧠 Central Agent
- Command parsing & routing
- Multi-agent orchestration
- Context management
- Decision making
- Approval workflows

### 💬 Communication Agent
- Real-time notifications
- Push alerts
- Telegram integration
- Email notifications
- Alert history

### 📱 Social Media Agent
- Scheduled posts
- **Approval workflow** (you approve before posting)
- Caption generation
- Image attachment
- Post history

### 🏃 Fitness Agent
- Step tracking
- Workout logging
- Health metrics
- AI-powered advice
- Goal setting

### 🔬 Knowledge Agent
- Question answering
- Context-aware responses
- Memory/history
- Learning from interactions
- Web search integration

### 🎨 Creative Agent
- Image generation (Stable Diffusion)
- Music composition
- Visual art creation
- Style transfer

### 🗺️ Information Agent
- OpenStreetMap integration
- Location services
- Route planning
- Weather data

## 🚨 Privacy & Security

- ✅ **Local processing** - No data sent to external servers
- ✅ **Encryption** - All sensitive data encrypted
- ✅ **User control** - Approval required for public posts
- ✅ **Data privacy** - GDPR compliant
- ✅ **Open source** - Fully auditable code

---

**Made with ❤️ by Tashrif2004** | *CAUGU - Your Personal AI Assistant* 🚀