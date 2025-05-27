# URL Shortener Django

A simple URL shortener web application built with Django.

## Features

- Shorten long URLs
- Redirect to original URLs
- Basic analytics (click count)

## Requirements

- Python 3.8+
- Django 4.x

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/ab01fazl1/url-shortener-django.git
    cd url-shortener-django
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```

5. Visit `http://localhost:8000` in your browser.

##  Example Usage
POST /shorten/
```bash
{
  "original_url": "https://www.example.com"
}
```
Response:

```bash
{
  "id": 1,
  "original_url": "https://www.example.com",
  "short_code": "a1B2c3",
  "created_at": "2025-05-27T12:34:56.789Z"
}
```

## License

MIT License