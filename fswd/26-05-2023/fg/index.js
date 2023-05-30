class Card {
  constructor(imageUrl) {
    this.imageUrl = imageUrl;
    this.isFlipped = false;
    this.isMatched = false;
  }

  flip() {
    this.isFlipped = !this.isFlipped;
  }

  match() {
    this.isMatched = true;
  }
}

class Game {
  constructor(cards) {
    this.cards = cards;
    this.selectedCards = [];
    this.matches = [];
    this.moves = 0;
    this.gameBoard.addEventListener('click', this.handleCardClick.bind(this));
    this.render();
  }
  handleCardClick(event) {
    const cardElement = event.target; //returns html element that triggered click event
    const cardIndex = parseInt(cardElement.dataset.index); //from cardELement extracts index data attribute

    //checks whether the element is card
    if(isNaN(cardIndex)) {
      return;
    }

    const card = this.cards[cardIndex]; //returns card object based on its index
    if(card.isFlipped || card.isMatched) {
      return;
    }
    card.flip();
    this.selectedCards.push(card);

    if(this.selectedCards.length === 2) {
      this.moves++;
      if(this.selectedCards[0].imageUrl === this.selectedCards[1].imageUrl) {
        this.selectedCards[0].match();
        this.selectedCards[1].match();
        this.selectedCards = [];
        this.matches +=2;
      }

      if(this.matches === this.cards.length) {
        setTimeout(() => {
          alert(`Congratulations, you won the game in ${this.moves} moves.`)
        },1000);
      }
      else {
        setTimeout(() => {
          this.selectedCards[0].flip();
          this.selectedCards[1].flip();
          this.selectedCards = [];
          this.render();
        }, 1000);
      }
    }
    this.render();
  }

  render() {
    this.gameBoard.innerHTML = '';
    this.cards.foreach((card, index) => {
      const cardElement = document.createElement('div');
      cardElement.className = 'card';
      cardElement.dataset.index = index;

      const cardFront = document.createElement('div');
      cardFront.className = 'card-front';
      cardElement.appendChild(cardFront);

      const cardBack = document.createElement('div');
      cardBack.className = 'card-back';
      cardBack.style.backgroundImage = `url(${url.imageUrl})`;
      cardElement.appendChild(cardBack);

      if(card.isMatched) {
        cardElement.classList.add('matched')
      }
      this.gameBoard.appendChild(cardElement);
    });
  }
};

const cards = [
  new Card('img/aquaman.jpg'),
  new Card('img/aquaman.jpg'),
  new Card('img/batman.jpg'),
  new Card('img/batman.jpg'),
  new Card('img/thor.jpg'),
  new Card('img/thor.jpg'),
  new Card('img/captain-america.jpg'),
  new Card('img/captain-america.jpg'),
  new Card('img/flash.jpg'),
  new Card('img/flash.jpg'),
  new Card('img/superman.jpg'),
  new Card('img/superman.jpg'),
];

const game = new Game(cards);
game.render();

