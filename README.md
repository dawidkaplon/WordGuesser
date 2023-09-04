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

## Getting Started

These instructions will help you set up and run the project on your local machine.

#### Prerequisites

- Windows OS
- Python installed
- Docker (if you plan to use Docker)

#### Installation

1. Create a virtual environment & activate it:

```sh
python -m venv venv
venv\Scripts\activate
```
   
2. Install project dependencies from requirements.txt:
```sh
pip install -r requirements.txt
```

3. Run the local server:
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
