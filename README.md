# Real-Time Chat Application
This project is a real-time chat application built using HTMX, Django Channels and WebSockets. It allows users to join chat rooms, send messages, and see those messages in real time without refreshing the page.

# Features (So Far)
1. User Authentication: Secure user sign-up, login, and logout functionality.
2. Real-Time Messaging: Instant message exchange between users within the same chat room using Django Channels and WebSockets.
3. Chat Rooms: Users can join different chat rooms to communicate.
4. Private Messaging: One-on-one direct messaging between users.
5. File Sharing: Users will be able to share files (e.g., images, documents) within chat rooms.
6. Notifications: In-app notifications for unread messages and new chat room activity.
7. Message History: Persistent message storage, allowing users to view previous chat histories.

#Features (To be Implemented)
1. Redis for channel layers
2. Deployment on heroku


# Installation
1. Clone this repository: ```git clone https://github.com/direntwi/realtimechat.git```
2. Navigate into the project directory: ```cd realtimechat```
4. Install dependencies: ```pip install -r requirements.txt```
5. Run migrations to set up the database: ```python manage.py migrate```
6. Start the development server: ```python manage.py runserver```

# Requirements
1. Python 3.x
2. Django 3.x or later


   
# Contributing
This project is still under active development, and contributions are welcome! If you'd like to contribute, please fork the repository, create a new branch, and submit a pull request.
