# IST105-Assignment5 — Interactive Treasure Hunt (Django + AWS)

**Author:** Ryo Suzuki  
**Course:** IST105 — Introduction to Programming

A small Django web app where users submit a **number** and **text**.  
The backend returns:
- **Number Puzzle:** even/odd; if even → square root, if odd → cube  
- **Text Puzzle:** text → binary, and vowel count  
- **Treasure Hunt:** simulate guessing a random number (1–100); win if found in ≤5 tries  

## Tech
- Python / Django
- AWS **Launch Template + Auto Scaling Group + Application Load Balancer**