# World of Games - The Epic Journey

Welcome to **World of Games: The Epic Journey**!  
This project is a multi-level Python game system built with modularity and DevOps best practices in mind.

## Project Structure

```
.
├── app.py
├── main.py
├── games
│   ├── guess_game.py
│   ├── memory_game.py
│   └── currency_roulette_game.py
├── utils
│   ├── utils.py
│   └── score.py
├── scores.txt
├── main_score.py
├── e2e.py
├── Dockerfile
├── docker-compose.yml
└── Jenkinsfile
```

## Project Levels

### Level 1 - Setup
- `app.py` defines `welcome(name)` and `start_play()` functions.
- `main.py` welcomes the user and lets them select a game and difficulty.

### Level 2 - Game Modules
- **Memory Game**: Memorize a sequence of numbers.
- **Guess Game**: Guess a random number.
- **Currency Roulette**: Guess the ILS value of a random USD amount.

Each game has:
- `generate` functions (numbers/sequence).
- User input functions.
- Comparison functions.
- A `play()` function.

### Level 3 - Score Management
- **Utils**: Contains helpful constants and a `screen_cleaner()` function.
- **Score Manager (`score.py`)**: Manages user scores.
- **Main Score Server (`main_score.py`)**: Runs a Flask app that serves the user's score over HTTP.

### Level 4 - DevOps Integration
- **Dockerfile**: Packages the app.
- **docker-compose.yml**: Builds, runs, and manages the container.
- **Jenkinsfile**: Defines CI/CD pipeline:
  1. Checkout
  2. Build
  3. Run
  4. Test (Selenium with `e2e.py`)
  5. Finalize (Push Docker image to DockerHub)

### E2E Testing
- **e2e.py** uses Selenium to validate the Flask web service by checking if the score is a valid number between 1 and 1000.

## Technologies Used

- Python 3.8
- Flask
- Docker
- Docker Compose
- Jenkins
- Selenium
- GitHub

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/motizaken/wog0105.git
   cd wog0105
   ```

2. Run locally with Python:
   ```bash
   python main.py
   ```

3. Run with Docker:
   ```bash
   docker build -t wog .
   docker run -p 5001:5001 wog
   ```

4. Access the score service at [http://localhost:5001/](http://localhost:5001/).

5. Run E2E Tests:
   ```bash
   python e2e.py
   ```

## Author
- **Moti Zaken**

---

> *This project was created as part of the DevOps Course at DevOps Experts College, under the guidance of Doron Nuni (2024).* 🚀