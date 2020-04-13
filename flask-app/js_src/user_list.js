'use strict';

class UserList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      users: []
    }
    this.userUpdate = this.userUpdate.bind(this);
  }

  componentDidMount() {
    console.log("userlist mounted")
    socket.on('user_updates', this.userUpdate);
  }

  componentWillUnmount() {
    socket.off('user_updates', this.newMessage)
  }

  userUpdate(users) {
    console.log(users);
    this.setState({
      users: users
    })
  }

  render() {
    const userItems = this.state.users.map(user => {
      return <User key={user.id} name={user.username} />
    });

    return <div id="userList">
    <h3> Players </h3>
    {userItems}
    </div>
  }
}

class User extends React.Component {
  render() {
    return <p> {this.props.name} </p>
  }
}
