'use strict';

class Lobby extends React.Component {
  render() {
    return (
      <div id="lobbyContent">
        <UserList />
        <GameSettings />
        <ChatWindow />
      </div>
    );
  }
}
