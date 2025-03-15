# Optimise Backend Service

A backend service to demonstrate API response time optimization, with and without performance techniques applied. This project uses [JSONPlaceholder](https://jsonplaceholder.typicode.com/) as a dummy API.

## 🚀 Setting Up

### 1. Clone the Repository
```sh
git clone -b develop https://github.com/gdkimaiyo/optimise-be.git
cd optimise-be
```

### 2. Create a .env File
```sh
touch .env
```
Add respective environment variables as shared.

### 3. Set Up a Virtual Environment
#### For macOS/Linux:
```sh
python -m venv virtual
source virtual/bin/activate
```
#### For Windows:
```sh
python -m venv virtual
virtual\Scripts\activate
```
To deactivate the virtual environment, run:
```sh
deactivate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Server
```sh
python manage.py runserver
```

## 🔥 Important Notes
- If you install additional dependencies, update `requirements.txt` for other developers:
  ```sh
  pip freeze > requirements.txt
  ```
- Check installed packages with:
  ```sh
  pip freeze
  ```

## 📚 Learn More
- [Django Documentation](https://docs.djangoproject.com/en/5.1/)
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

