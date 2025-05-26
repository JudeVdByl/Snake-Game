# Snake Game

A lightweight remake of the classic Snake arcade game written in pure Python using the built‑in `turtle` module. Perfect for beginners who want to read clean, well‑commented code and hackers who want a nostalgic time‑killer.

---

## Table of Contents

1. [Features](#features)
2. [Demo](#demo)
3. [Getting Started](#getting-started)
4. [Gameplay](#gameplay)
5. [Project Layout](#project-layout)
6. [Roadmap](#roadmap)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features

* Pure Python only (no third‑party packages)
* Smooth keyboard controls with arrow keys
* Dynamic speed increase as the snake grows
* Scoreboard shows current score and personal best within the session
* Fully modular code base ready for extension (food, snake, scoreboard, main loop)

## Demo <a id="demo"></a>

![Gameplay GIF](https://github.com/user-attachments/assets/251ba1ac-f662-4913-9fc0-b91861cafdfb)



---

## Getting Started

### Prerequisites

* Python **3.8** or newer

### Installation

```bash
# clone the repository
$ git clone https://github.com/yourusername/snake-game.git
$ cd snake-game

# run the game
$ python main.py
```

No other setup required – the standard library ships with everything you need.

---

## Gameplay <a id="gameplay"></a>

| Key         | Action     |
| ----------- | ---------- |
| Up Arrow    | Move up    |
| Down Arrow  | Move down  |
| Left Arrow  | Move left  |
| Right Arrow | Move right |

1. Eat the yellow food squares to grow.
2. Every bite adds 1 point and slightly increases the snake's speed.
3. Colliding with a wall or your own tail ends the game.

---

## Project Layout <a id="project-layout"></a>

```
.
├── main.py        # entry point, sets up screen and game loop
├── snake.py       # Snake class: segments, movement, collision
├── food.py        # Food class: spawns and relocates food
├── scoreboard.py  # Scoreboard class: current score and game‑over banner
└── docs/          # screenshots, GIFs, and future documentation assets
```

---

## Roadmap <a id="roadmap"></a>

* [ ] Persistent high‑score storage in a JSON file
* [ ] Obstacles and levels
* [ ] Sound effects
* [ ] Color themes (light and dark)

Feel free to open an issue to suggest more features.

---

## Contributing <a id="contributing"></a>

Pull requests are warmly welcomed. For major changes, please open an issue first and discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/awesome‑feature`)
3. Commit your changes (`git commit -m "Add awesome feature"`)
4. Push to the branch (`git push origin feature/awesome‑feature`)
5. Open a pull request

---

## License <a id="license"></a>

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---


