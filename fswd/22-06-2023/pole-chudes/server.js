const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.urlencoded({urlencoded: false}));
app.use(bodyParser.json());

const countRemainingLetters = function(phrase){
  return phrase.replace(/[^a-z]/gi, '').length;
};

const countOccurrences = function (phrase, letter) {
  return phrase.split(letter).length - 1;
}

const puzzles = [
  {phrase: "Hello World", category: "Programming"},
  {phrase: "Gone with the wind", category: "Literature"},
  {phrase: "1984", category: "Literature"}
];

let gameState = {
  puzzle: null,
  guessedLetters: [],
  remainingLetters: 0
}

app.post('/game/guess', (req, res) => {
  const letter = req.body.letter.toLowerCase();
  const phrase = gameState.puzzle.phrase.toLowerCase();

  if (gameState.guessedLetters.includes(letter)) {
    res.json({ message: 'Letter already guessed' });
  } else if (phrase.includes(letter)) {
    gameState.guessedLetters.push(letter);
    gameState.remainingLetters -= countOccurrences(phrase, letter);
    res.json({ message: 'Correct guess', remainingLetters: gameState.remainingLetters });
  } else {
    res.json({ message: 'Incorrect guess' });
  }
});

app.post('/game/solve', (req, res) => {
  const guess = req.body.guess.toLowerCase();
  const phrase = gameState.puzzle.phrase.toLowerCase();

  if (guess === phrase) {
    gameState.remainingLetters = 0;
    res.json({ message: 'Congratulations! Puzzle solved' });
  } else {
    res.json({ message: 'Incorrect solution' });
  }
});

app.get('/game/start', function(req, res) {
  const randomIndex = Math.floor(Math.random() * puzzles.length);
  gameState.puzzle = puzzles[randomIndex];
  gameState.guessedLetters = [];
  gameState.remainingLetters = countRemainingLetters(gameState.puzzle.phrase);
  res.json({message: "GAME STARTED", puzzle: gameState.puzzle});
});

app.listen(3000, function(req, res) {
  console.log("The server started");
})