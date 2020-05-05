`use strict`;

class Card extends React.Component {
  constructor(props){
    super(props);
    this.renderEmpy = this.renderEmpy.bind(this);
    this.renderCard = this.renderCard.bind(this);
  }

  render() {
    if(this.props.data == undefined) {
      return this.renderEmpy()
    } else {
      return this.renderCard(this.props.data)
    }
  }

  renderEmpy() {
    return <div className="card"></div>
  }

  renderCard(card) {
    const bannedWords = card.banned_words.map(word => {
      return <li key={word}>{word}</li>
    });
    return <div className="card">
              <p>{card.target_word}</p>
              <ul className="bannedWords">{bannedWords}</ul>
           </div>
  }
}
