'use strict';

class Session extends React.Component {
  constructor(props) {
    super(props);
    this.state = {}
    this.handleGameUpdate = this.handleGameUpdate.bind(this);
    this.makeGuess = this.makeGuess.bind(this);
  }
  componentDidMount() {
    socket.on('game_updates', this.handleGameUpdate);
    socket.emit('game_updates', {
      'type':'request_state'
    });
  }

  handleGameUpdate(message) {
    console.log("Recieved message");
    console.log(message);
    this.setState({
      'teams': message.players,
      'giverId': message.giver,
      'card': message.card,
    })
  }

  requestNextCard() {
    socket.emit('game_updates', {
      'type':'next_card'
    });
  }

  makeGuess(message) {
    socket.emit('game_updates', {
      'type':'guess_word',
      'guess':message
    });
  }

  render() {
    const teams = this.state.teams

    if(!teams || teams.length == 0) {
      return (
        <div id="session">
          <Lobby />
        </div>
      );
    } else {
      const team_elemets = teams.map((players, pos) => {
        return <Team players={players} name={pos + 1} key={pos} id={pos} giverId={this.state.giverId}/>
      })
      return (
        <div id="session">
          <div id="teams">{team_elemets}</div>
          <Card data={this.state.card}/>
          <ChatWindow onSubmitWord={this.makeGuess} />
        </div>
      )
    }
  }
}

const domContainer = document.querySelector('#main');
ReactDOM.render(<Session />, domContainer);
