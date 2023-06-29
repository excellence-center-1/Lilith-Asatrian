import React, { useState } from 'react';

const Game = () => {
  const [letter, setLetter] = useState('');
  const [word, setWord] = useState('');
  const [guessedLetters, setGuessedLetters] = useState([]);

  const handleLetterChange = (e) => {
    setLetter(e.target.value);
  };

  const handleGuessLetter = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('/guess-letter', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ letter }),
      });

      if (response.ok) {
        const data = await response.json();
        setWord(data.word);
        setGuessedLetters(data.guessedLetters);
        setLetter('');
      } else {
        console.log('Error:', response.status);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="container">
      <h1>Pole Chudes</h1>
      <form onSubmit={handleGuessLetter}>
        <input
          type="text"
          value={letter}
          onChange={handleLetterChange}
          placeholder="Enter a letter"
          required
        />
        <button type="submit">Guess</button>
      </form>
      <div>
        <h2>Word: {word}</h2>
        <h2>Guessed Letters</h2>
        {guessedLetters.map((letter, index) => (
          <span key={index}>{letter}</span>
        ))}
      </div>
    </div>
  );
};

export default Game;
