# Introduction
DocBox is an innovative cloud-based document storage web application designed to securely store, manage, and retrieve documents with ease. Utilizing cutting-edge technologies such as Flask for the backend and AWS S3 for cloud storage, DocBox offers a robust and scalable solution for personal and business document management needs.

DocBox leverages the power of cloud technology to provide a seamless document storage solution. By utilizing AWS S3 for storage, DocBox ensures that your documents are stored in a highly secure and scalable environment. The integration of Flask as the backend framework ensures that the application is lightweight and responsive, while the use of Bootstrap and ApexCharts.js enhances the user experience with a modern, intuitive interface and insightful data visualizations.

With DocBox, you can upload, store, and retrieve your documents effortlessly, ensuring that your important files are always accessible and secure, no matter where you are.

## Importance of File Storage
In today's digital age, the secure and efficient management of documents is crucial. Traditional storage methods often fall short in terms of accessibility, scalability, and security. Cloud storage addresses these issues by providing a centralized, easily accessible, and secure platform for storing documents.

## Technologies Used
- Flask: A lightweight and flexible web framework for Python, enabling rapid development and easy maintenance of web applications.
- AWS S3: A highly scalable and secure cloud storage service, ensuring reliable storage and access to your documents from anywhere.
- AWS EC2: A versatile cloud computing service that provides resizable compute capacity, ensuring the application can handle varying loads efficiently.
- HTML, CSS, JavaScript: Standard web technologies for creating an interactive and responsive user interface.
- Bootstrap: A popular front-end framework for building responsive and mobile-first web pages.
- ApexCharts.js: A powerful library for creating interactive and visually appealing charts, enhancing data visualization within the application.

## Getting Started
### Prerequisites
- Python 3.x
- Flask
- AWS account with S3 and EC2 access

### Installation
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

## Configuration
- Create a `.env` file in the project root directory and provide values for the following variables:
```
APP_SECRET_KEY = ""
SERIALIZER_KEY = ""
DB_URL = ""
SMTP_HOST = ""
SMTP_PORT = ""
SMTP_MAIL = ""
SMTP_PWD = ""
USE_SSL = ""
```

- Create a .flaskenv file and provide values for the following variables.
```
FLASK_APP = 
FLASK_DEBUG=
```

- Run the application:
```
$ flask run
```
Once the application is running, you can access the web interface to manage your documents.

## Usage
- Login:
Log in with the ccredentials on `seed_user.json` file.

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