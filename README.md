# DRF Advanced Playground 🚀

## Overview 🏗️
This is an advanced Django Rest Framework (DRF) project showcasing key API functionalities, including authentication, permissions, and CRUD operations. It's designed for learning and experimenting with DRF's powerful features.

## Features ✨
- ✅ JWT Authentication with `djangorestframework-simplejwt` 🔑
- ✅ Role-based permissions 🔒 (Only authenticated users can create articles, and only owners can edit/delete)
- ✅ Full CRUD operations for managing articles 📝
- ✅ `ViewSets` and `Routers` for cleaner API structure
- ✅ Token-based authentication for secure API interactions 🔐
- ✅ Custom permissions to enhance security and user control 🛡️
- ✅ Pagination: Only 5 articles per page for better performance 📄
- ✅ Filtering: Filter articles by title 🔍
- ✅ Searching: Search articles by title and content 🔎
- ✅ Ordering: Sort articles by title or creation date 📊

## Installation 🛠️
1. Clone the repository:
   ```sh
   git clone https://github.com/mahmoudshaker123/drf-advanced-playground.git
   ```
2. Navigate to the project directory:
   ```sh
   cd drf-advanced-playground
   ```
3. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Apply migrations:
   ```sh
   python manage.py migrate
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```

## Authentication 🔐
This project uses JWT authentication for secure access control.
- Obtain an access token:
  ```sh
  POST /api/token/
  ```
- Refresh the token:
  ```sh
  POST /api/token/refresh/
  ```

## API Endpoints 🌍
- `GET /api/articles/` - List all articles 📜
- `POST /api/articles/` - Create a new article (requires authentication) ✍️
- `GET /api/articles/{id}/` - Retrieve a single article 🔍
- `PUT /api/articles/{id}/` - Update an article (only the owner can edit) 📝
- `DELETE /api/articles/{id}/` - Delete an article (only the owner can remove) ❌
- `GET /api/articles/?search=keyword` - Search articles by title or content 🔎
- `GET /api/articles/?ordering=-created_at` - Sort articles by newest first 📊
- `GET /api/articles/?title=example` - Filter articles by title 🔍

## Testing ✅
Run the tests to ensure everything is working correctly:
```sh
python manage.py test
```

## Contributing 🤝
Want to improve this project? Feel free to fork the repository, submit pull requests, or report issues.

## License 📜
This project is open-source and available under the MIT License.

---
🚀 Happy coding and API development! 😃

