# ⛏️ 2D Voxel Engine (Python - Pygame)

**Created:** October 2023  
**Language:** Python (Pygame)  
**Developer:** Ibtasaam Amjad

---

## 📦 Project Overview

This is a 2D voxel engine built in Python using Pygame — inspired by *Minecraft*'s iconic block-based systems.  
The project focuses on core interaction: placing and removing blocks from a pre-defined map grid.  
No world generation. No complex physics.  
Just the fundamentals — clean, responsive block manipulation within a limited sandbox.

Textures are primarily inspired by (and in many cases directly derived from) *Minecraft* assets to preserve the familiar aesthetic and give the engine a classic feel.

---

## ✨ Features

- 🧱 **Grid-Based Block System**
  - Fixed 25x20 tile map (1000x800 resolution)
  - Each tile is interactable using mouse controls

- 🧰 **Placing & Removing Blocks**
  - Left-click to remove blocks  
  - Right-click to place currently selected block

- 🎨 **Block Selection Menu**
  - Press `M` or `Esc` to open the selection grid  
  - Choose from 25+ different block types

- 🔄 **Directional Blocks**
  - Stair-type blocks support flipping (left/right) based on placement logic

- 🖼️ **Texture Support**
  - Over 25 custom blocks including:
    - Grass, Dirt, Stone, Planks, Logs
    - Cobblestone, Copper, Tuff, Amethyst
    - Stone/Deep Slate Bricks and Stairs
    - End Stone, Netherack, Flowers, etc.

- 🖱️ **Mouse Interaction**
  - Responsive block editing via mouse position and click detection

- 🎮 **60 FPS Stable Game Loop**
  - Smooth rendering and real-time updates using `pygame.Clock`

---

## ▶️ How to Run

1. **Install Pygame:**
   ```bash
   pip install pygame
   ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/Voxel-Engine
   cd Voxel-Engine
   ```

3. **Ensure the following directory structure:**
   ```
   /data/images/
   ├── stone.png
   ├── dirt.png
   ├── grass.png
   └── ... (all other required textures)
   ```

4. **Run the project:**
   ```bash
   python main.py
   ```

---

## 🧱 Controls

- **Left-click** — Remove block  
- **Right-click** — Place block  
- **M / Esc** — Open block selection menu

---

## 🎨 Assets & Credits

- Block textures are visually inspired by *Minecraft* (Mojang Studios)
- This project is non-commercial and educational in nature

---

## 📂 File Structure

- `main.py` — Core engine loop  
- `/data/images/` — All block and UI textures  
- `generate_voxels()` — Grid setup function  
- `generate_voxel_state()` — Initial block layer logic  
- `menu_buttons()` — UI logic for selecting blocks

---

## 🧠 Concepts Implemented

- Tilemap rendering and interaction
- Sprite-free grid logic using `pygame.Rect`
- Mouse collision for editing map data
- Conditional block placement and flipping
- Menu system overlay and state toggling

---

This is a lightweight but expandable voxel engine — a foundation for future systems such as saving/loading, procedural generation, player movement, or even crafting logic.

---

**Created By:** Ibtasaam Amjad  
**Language:** Python | Pygame  
**Created:** September 2023
