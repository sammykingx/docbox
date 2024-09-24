# Introduction
The Cloud Document Storage Platform(Docbox) is a scalable, secure, and user-friendly web application designed for storing, sharing, and managing company-sensitive files in the cloud. Built with Django, the platform offers robust features for user authentication, user management, file encryption, collaboration, and billing, making it suitable for enterprise-level use and potential SaaS offerings.

With DocBox, you can upload, store, and retrieve your documents effortlessly, ensuring that your important files are always accessible and secure, no matter where you are.
## Table of Contents
- [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Importance of File Storage](#importance-of-file-storage)
  - [Technologies Used](#technologies-used)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Contributing](#contributing)
- [License](#license)


## Importance of File Storage
In today's digital age, the secure and efficient management of documents is crucial. Traditional storage methods often fall short in terms of accessibility, scalability, and security. Cloud storage addresses these issues by providing a centralized, easily accessible, and secure platform for storing documents.

## Technologies Used
- **Django**: A high-level Python web framework
- **AWS S3**: A highly scalable and secure cloud storage service, ensuring reliable storage and access to your documents from anywhere.
- **AWS EC2**: A versatile cloud computing service that provides resizable compute capacity, ensuring the application can handle varying loads efficiently.
- **HTML, CSS, JavaScript**: Standard web technologies for creating an interactive and responsive user interface.
- **Bootstrap**: A popular front-end framework for building responsive and mobile-first web pages.
- **Docker**: Containerization for consistent environments across development, testing, and production.
- **Gunicorn**: Python WSGI HTTP Server for running Django applications in production.
- **Nginx**: Web server and reverse proxy used for serving the application.
- **Celery**: Distributed task queue for handling asynchronous tasks.
- **Redis**: In-memory data structure store used as a message broker for Celery.

## Getting Started
### Prerequisites
- Python 3.10+
- Django 5.1.x
- AWS account with S3 and EC2 access

### Installation
- If your're using MYSQL in your environment, then install this packages on your system
```bash
sudo apt install -y python3-dev default-libmysqlclient-dev build-essential pkg-config libmysqlclient-dev
```
- Clone the repository:
```
git clone https://github.com/sammykingx/docbox.git
```

- Change directory to `docbox` or open folder with vscode

- Create Virtual environment:
```
# for windows
$ python -m venv venv

# for mac or debian based linux distro
$ python3 -m venv venv
```

- Activate virtual envitonment
```
# for windows
$ venv\Scripts\activate

# for mac or debian based distros
$ source venv/bin/activate
```

- Install Project dependencies
```
$ pip install -r requirements.txt
```
- If you're Using MySQL as your Database, then install mysqclient in your virtual environment
```zsh
pip install mysqlclient
```


## Configuration
- Create a `.env` file in the project root directory and provide values for the following variables:
```
will be updated
```

## Usage
- Start the developement server
```
python manage.py runserver
```

- Access the application via `http://127.0.0.1:8000/`

- Login:
Log in with your user accounts

- Upload Documents:
Use the upload feature to store documents in the cloud.

- View Documents:
Fetch and view your saved documents from the cloud.

## Contributing
- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Commit your changes (git commit -m 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Open a pull request.

# License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.