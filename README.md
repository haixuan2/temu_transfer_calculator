# Temu Transfer Calculator

A web application to calculate the latest possible shipment time for different channels and transport types.

## Project Structure

```
Temu Transfer Calculator/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── logic.py
│   └── templates/
│       └── index.html
│
├── run.py
├── requirements.txt
└── README.md
```

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   python run.py
   ```
3. Open your browser and go to `http://127.0.0.1:5000/`

## Description
- **app/logic.py**: Business logic for shipment time calculation.
- **app/routes.py**: Web routes and view logic.
- **app/__init__.py**: App factory and blueprint registration.
- **app/templates/**: HTML templates.
- **run.py**: Entry point to run the app.

---

Feel free to extend this project with more features or tests! 