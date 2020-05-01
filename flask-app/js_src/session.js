'use strict';

class Session extends React.Component {
  constructor(props) {
    super(props);
    this.handleGameUpdate = this.handleGameUpdate.bind(this);
  }
  componentDidMount() {
    socket.on('game_updates', this.handleGameUpdate);
  }

  handleGameUpdate(message) {
    console.log("Recieved message");
    console.log(message);
  }

  render() {
    return (
      <div id="session">
        <Lobby />
      </div>
    );
  }
}

const domContainer = document.querySelector('#main');
ReactDOM.render(<Session />, domContainer);
