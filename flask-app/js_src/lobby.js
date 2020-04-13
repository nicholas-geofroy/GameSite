'use strict';

class Lobby extends React.Component {
  render() {
    return (
      <div id="lobbyContent">
        <UserList />
        <form>
          <input type="submit" value="Start Game" />
        </form>
        <ChatWindow />
      </div>
    );
  }
}

const domContainer = document.querySelector('#main');
ReactDOM.render(<Lobby />, domContainer);
