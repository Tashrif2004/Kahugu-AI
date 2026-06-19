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
| **Voice** | Whisper (OpenAI free tier) | Mozilla STT |
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

## 🚀 Quick Start

### 1. Start Central Agent
```python
from agents.central_agent import CentralAgent

caugu = CentralAgent()
caugu.initialize()
caugu.start()
```

### 2. Enable Specific Agents
```python
caugu.enable_agent('fitness')
caugu.enable_agent('social_media')
caugu.enable_agent('creative')
```

### 3. Send Commands
```python
response = caugu.process_command(
    user_id="user_123",
    command="Show me my workout stats for today",
    context="fitness"
)
```

## 📁 Project Structure

```
CAUGU/
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

# Social Media (optional - for when you get APIs)
TWITTER_API_KEY=
INSTAGRAM_ACCESS_TOKEN=
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
- Discord support
- Email notifications

### 📱 Social Media Agent
- Scheduled posts
- **Approval workflow** (you approve before posting)
- Instagram/Twitter integration
- Caption generation
- Image attachment

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
- Video generation (future)
- Style transfer

### 🗺️ Information Agent
- OpenStreetMap integration
- Location services
- Route planning
- Weather data
- Web search

## 🔐 Approval Workflow Example

```python
# Social media post request
post_request = {
    'platform': 'twitter',
    'content': 'Check out my latest workout!',
    'image': 'workout_photo.jpg'
}

# Get approval
approval = caugu.request_approval(post_request)

if approval:
    caugu.post_to_social_media(post_request)
    print("✅ Posted!")
else:
    print("❌ Rejected by user")
```

## 📈 Tracking & Analytics

CAUGU automatically tracks:
- 📍 Your location & movements
- 🏃 Workouts & fitness metrics
- 💬 Conversations & interactions
- 📝 Generated content
- 🔔 All notifications

View your dashboard:
```bash
python -m http.server 8000 --directory ./dashboard
```

Then visit: `http://localhost:8000`

## 🎓 Example Usage

```python
from caugu import CAUGU

# Initialize
caugu = CAUGU()

# Get fitness advice
advice = caugu.ask("Give me workout advice based on my activity today")

# Generate content
image = caugu.create_image("A futuristic AI assistant dashboard")

# Post with approval
caugu.post_on_social_media(
    platform="twitter",
    content="Amazing workout today! 💪",
    needs_approval=True
)

# Check location
location = caugu.get_current_location()
nearby = caugu.find_gyms_nearby(location, radius=5)

# Music generation
song = caugu.generate_music(
    genre="electronic",
    mood="energetic",
    duration=30
)
```

## 🚨 Privacy & Security

- ✅ **Local processing** - No data sent to external servers
- ✅ **Encryption** - All sensitive data encrypted
- ✅ **User control** - Approval required for public posts
- ✅ **Data privacy** - GDPR compliant
- ✅ **Open source** - Fully auditable code

## 📚 Documentation

- [Setup Guide](docs/SETUP.md)
- [API Reference](docs/API.md)
- [Agent Development](docs/AGENTS.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📄 License

MIT License - See [LICENSE](LICENSE)

## 🆘 Support

- 📧 Email: support@caugu.ai
- 💬 Telegram: [@caugu_support](https://t.me/caugu_support)
- 🐛 Issues: [GitHub Issues](https://github.com/Tashrif2004/Kahugu-AI/issues)

---

**Made with ❤️ by Tashrif2004**

*CAUGU - Your Personal AI Assistant* 🚀
