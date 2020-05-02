`use strict`;

class Player extends React.Component {
  constructor(props){
    super(props);
  }

  render() {
    const color = this.props.giver ? "green" : "black"
    return (
      <div className="player">
        <p style={{color: color}}>{this.props.name}</p>
      </div>
    )
  }
}
