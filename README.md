# WordGuesser

🚨 **Note:** This guide assumes a Windows OS.

## Description

#### The Classic Wordle Challenge 
In ***WordGuesser***, you'll be presented with a secret word that you need to guess correctly within a limited number of attempts. 
Each time you guess a letter, you'll receive feedback on whether the letter is in the word and if it's in the correct position. 
Use this feedback to strategically deduce the hidden word.

#### Web Scraper Feature
One of the standout features of ***WordGuesser*** is its built-in web scraper. The web scraper roams various websites, collecting a treasure trove of words and their definitions. 
It enriches the game by providing you with not just a list of words but also their meanings. This feature not only enhances your gameplay but also offers a valuable learning experience.

#### Multi-language
The game allows the User to instantly change the language between Polish and English. Words are also drawn in the Player's chosen language.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Windows OS
- Python installed
- Docker (if you plan to use Docker)<br><br>

### Installation

***1. Create a virtual environment & activate it:***

```sh
python -m venv venv
venv\Scripts\activate
```
   
***2. Install project dependencies from requirements.txt:***
```sh
pip install -r requirements.txt
```

***3. Set the Secret Key***<br><br>
In order to run the local server, You have to set new Secret Key in ***settings.py*** file.

- **Access the Python Interactive Shell:**
   ```sh
   python manage.py shell
   ```
- **Import the get_random_secret_key function:**
   ```sh
   from django.core.management.utils import get_random_secret_key
   ```
- **Generate the Secret Key in the Terminal using the get_random_secret_key() function:**
   ```sh
   >>> get_random_secret_key()
   'qw^9ej(l4vq%d_06xig$vw+b(-@#00@8l7jlv77=sq5r_sf3nu'
   ```
- **Copy and Paste the Key into your SECRET_KEY variable in the settings.py:**
   ```sh
   SECRET_KEY = 'qw^9ej(l4vq%d_06xig$vw+b(-@#00@8l7jlv77=sq5r_sf3nu'
   ```

***4. Exit the shell using exit() and then make necessary migrations:***
```sh
python manage.py makemigrations
python manage.py migrate
```

***5. Run the local server:***
```sh
python manage.py runserver
```
Now You should be able to get some response using localhost:8000

## Running tests

Run unit tests with:
```sh
python manage.py test
```

## Docker operations

1. Build the image locally with the following command:
```sh
docker build -t wordguesser .
```

2. Run the Docker container:
```sh
docker run -p 8000:8000 wordguesser
```

## Game sneak peek:
- **Quality can be poor due to GIF compression**
- **For better view please check the screenshots below**
  <p></p>
  <br>
- ***Main gameplay***
   <p></p>
![WebsitePreview](https://github.com/dawidkaplon/django-WordGuesser/blob/main/mysite/static/readme_preview/gameplay-gif.gif)
   <br>
   <br>
- ***Start of the game***
  <p></p>
![WebsitePreview2](https://github.com/dawidkaplon/django-WordGuesser/blob/main/mysite/static/readme_preview/game-start.png)
   <br>
   <br>
- ***The mid-game***
   <p></p>
![WebsitePreview3](https://github.com/dawidkaplon/django-WordGuesser/blob/main/mysite/static/readme_preview/mid-game.png)
   <br>
   <br>
- ***Index page (English language)***
   <p></p>
![WebsitePreview4](https://github.com/dawidkaplon/django-WordGuesser/blob/main/mysite/static/readme_preview/index-en.png)
   <br>
   <br>
- ***Index page (Polish language)***
   <p></p>
![WebsitePreview5](https://github.com/dawidkaplon/django-WordGuesser/blob/main/mysite/static/readme_preview/index-pl.png)
   <br>
   <br>
- ***Navbar extended***
   <p></p>
![WebsitePreview6](https://github.com/dawidkaplon/django-WordGuesser/blob/main/mysite/static/readme_preview/navbar.png)
   <br>
   <br>
- ***Single User's statistics***
   <p></p>
![WebsitePreview7](https://github.com/dawidkaplon/django-WordGuesser/blob/main/mysite/static/readme_preview/user-stats.png)
   <br>
   <br>
- ***Single User's drawn words***
   <p></p>
![WebsitePreview8](https://github.com/dawidkaplon/django-WordGuesser/blob/main/mysite/static/readme_preview/user-words-list.png)
   <br>
   <br>
- ***Last words drawn by users (both authenticated and not authenticated). User's email data is restricted to superuser only***
  <p></p>
![WebsitePreview9](https://github.com/dawidkaplon/django-WordGuesser/blob/main/mysite/static/readme_preview/other-users-words.png)
   <br>
   <br>
- ***Win page***
   <p></p>
![WebsitePreview10](https://github.com/dawidkaplon/django-WordGuesser/blob/main/mysite/static/readme_preview/win-page.png)


