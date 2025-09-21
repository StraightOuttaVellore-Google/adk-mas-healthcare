# ADK Wellness Bots

A comprehensive AI-powered wellness system built with Google's Agent Development Kit (ADK) that provides specialized mental health support through two distinct agents: General Wellness and Study Stress Management.

## 🌟 Features

### General Wellness Agent
- **Emotional Analysis**: Identifies emotions, focus areas, and mental wellness patterns
- **Personalized Recommendations**: Provides tailored advice, wellness exercises, and resources
- **Safety-First Approach**: Built-in safety review and refinement system
- **Memory Integration**: Remembers previous conversations for continuity

### Study Stress Agent
- **Academic-Focused Analysis**: Specialized in student mental health and study-related challenges
- **Study Strategy Recommendations**: Time management, study techniques, and academic wellness
- **Task Prioritization**: Uses Eisenhower Priority Matrix for effective planning
- **Student-Specific Resources**: Targeted tools and techniques for academic success

## 🏗️ Architecture

The system uses a multi-agent architecture with:

- **Parallel Processing**: Summary and recommendation agents work simultaneously
- **Safety Refinement Loop**: Iterative safety review and improvement
- **Memory Management**: Persistent conversation memory using Mem0
- **Modular Design**: Separate agents for different wellness domains

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Google Cloud Platform account
- Environment variables configured

### Installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:StraightOuttaVellore-Google/adk-wellness-bots.git
   cd adk-wellness-bots
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   export MODEL_NAME="your-model-name"
   export GOOGLE_APPLICATION_CREDENTIALS="path-to-your-credentials.json"
   ```

### Usage

#### General Wellness Agent
```python
from moodboard_wellness_agents.agent import root_agent

# Process a wellness conversation
response = root_agent.run("I've been feeling really anxious lately...")
```

#### Study Stress Agent
```python
from moodboard_study_agents.agent import root_agent

# Process academic stress conversation
response = root_agent.run("I have my final exams next week and I'm having panic attacks...")
```

## 📝 Sample Inputs

### General Wellness Examples

**Anxiety & Stress:**
```
"I've been feeling really anxious lately. Work has been overwhelming with tight deadlines, and I can't seem to sleep properly. I keep worrying about everything and feel like I'm not good enough."
```

**Depression & Low Mood:**
```
"I've been feeling really down for the past few weeks. Nothing seems to bring me joy anymore, and I've been isolating myself from friends and family."
```

**Relationship Issues:**
```
"My partner and I have been fighting constantly lately. We can't seem to communicate without it turning into an argument."
```

### Study Stress Examples

**Exam Anxiety:**
```
"I have my final exams next week and I'm having panic attacks. I've been studying for 8 hours a day but I feel like I don't remember anything."
```

**Academic Perfectionism:**
```
"I'm a straight-A student but I'm completely overwhelmed. I spend 15 hours a day studying because I'm terrified of getting anything less than perfect grades."
```

**Procrastination:**
```
"I have three major assignments due this week but I keep procrastinating. I sit down to study but end up scrolling through social media for hours."
```

## 🔧 Configuration

### Environment Variables

- `MODEL_NAME`: The LLM model to use (e.g., "gemini-1.5-pro")
- `GOOGLE_APPLICATION_CREDENTIALS`: Path to your Google Cloud credentials

### Memory Configuration

The system uses Mem0 for conversation memory. Configure your Mem0 settings as needed for your deployment.

## 🛡️ Safety Features

- **Multi-layer Safety Review**: Automated safety checking and refinement
- **Crisis Detection**: Identifies serious mental health concerns
- **Professional Boundaries**: Avoids medical diagnosis or prescription advice
- **Escalation System**: Routes serious concerns to human review

## 📊 Output Format

### Summary Agent Output
```json
{
    "summary": "detailed summary text",
    "emotions": ["list", "of", "emotions"],
    "focus_areas": ["main", "topics", "discussed"],
    "tags": ["relevant", "mental", "wellness", "tags"]
}
```

### Recommendation Agent Output
```json
{
    "recommendations": [
        {"title": "title", "description": "detailed advice", "category": "category_name"}
    ],
    "wellness_exercises": [
        {"name": "exercise name", "instructions": "step-by-step", "duration": "time needed"}
    ],
    "resources": [
        {"type": "resource type", "title": "title", "description": "how it helps"}
    ],
    "tone": "supportive/encouraging/gentle/motivating"
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Google's Agent Development Kit (ADK)
- Memory management powered by Mem0
- Designed for the Google GenAI Hackathon

## 📞 Support

For support and questions, please open an issue in the GitHub repository.

---

**Note**: This system is designed for general wellness support and should not replace professional mental health care. Always consult with qualified healthcare providers for serious mental health concerns.
