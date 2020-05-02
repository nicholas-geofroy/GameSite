'use strict';

class Session extends React.Component {
  constructor(props) {
    super(props);
    this.state = {}
    this.handleGameUpdate = this.handleGameUpdate.bind(this);
  }
  componentDidMount() {
    socket.on('game_updates', this.handleGameUpdate);
  }

  handleGameUpdate(message) {
    console.log("Recieved message");
    console.log(message);
    this.setState({
      'teams':message.players,
      'giverId':message.giver
    })

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
        </div>
      )
    }
  }
}

const domContainer = document.querySelector('#main');
ReactDOM.render(<Session />, domContainer);
