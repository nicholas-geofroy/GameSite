'use strict';
const gamemodes = {
  TABOO: {
    name: "Taboo",
    value: 1
  },
  HEADBANDS: {
    name: "Headbands",
    value: 2
  }
}

class GameSettings extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      gamemode: gamemodes.TABOO.value
    }
    this.handleGamemodeSelect = this.handleGamemodeSelect.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
  }

  componentWillUnmount() {
  }

  handleGamemodeSelect(event) {
    this.setState({
      gamemode: event.target.value
    })
  }

  handleSubmit(event) {
    console.log("submit settings and start game")
    var message = {
      type: 'start_game',
      gamemode: this.state.gamemode
    }
    socket.emit('game_updates', message)
    event.preventDefault();
  }

  render() {
    const options = Object.keys(gamemodes).map(gamemodeKey => {
      const gamemode = gamemodes[gamemodeKey]
      return <option value={gamemode.value} key={gamemode.name} >{gamemode.name}</option>
    })
    return <form id="gameSettings" onSubmit={this.handleSubmit}>
            <select id="gamemode" form="gameSettings" onChange={this.handleGamemodeSelect}>
              {options}
            </select>
            <input type="submit" value="Start Game" />
          </form>
  }
}
