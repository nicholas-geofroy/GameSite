`use strict`;

class Team extends React.Component {
  constructor(props){
    super(props);
  }

  render() {
    const players = this.props.players
    const giver_id = this.props.giverId
    console.log("players: ")
    console.log(players)
    const player_elements = players.map(player => {
      console.log(player);
      return <Player key={player.id} name={player.name}
                     giver={player.id == giver_id} />
    })
    return (
      <div className="team">
        <h3>Team {this.props.id}</h3>
        <div id="players">{player_elements}</div>
      </div>
    )
  }
}
