'use strict';

const e = React.createElement;

class Message extends React.Component {
  render() {
    return (<p> {this.props.username} : {this.props.message} </p>);
  }
}

class ChatWindow extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      messages: [],
      newMessage: ''
    }
    this.newMessage = this.newMessage.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
    socket.on('message', this.newMessage)
  }

  componentWillUnmount() {
  }

  handleChange(event) {
    this.setState({newMessage: event.target.value});
  }

  handleSubmit(event) {
    console.log('Send message: ' + this.state.newMessage);
    socket.emit('send_message', this.state.newMessage)
    this.setState({
      newMessage:''
    })
    event.preventDefault();
  }

  newMessage(data) {
    // console.log(("new message: " + data));
    this.setState((state, props) => ({
      messages: state.messages.concat([data])
    }))
  }

  render() {
    const messageItems = this.state.messages.map((data, idx) => (
      <Message username={data.user} message={data.message} key={idx} />
    )
    );
    return (
      <div id="chatbox">
        <div id="messages">
          {messageItems}
        </div>
        <form id="chatForm" onSubmit={this.handleSubmit}>
          <input type="text" id="next_message" value={this.state.newMessage}
            onChange={this.handleChange} />
          <input type="submit" value="Send"/>
        </form>
      </div>
    );
  }
}

const domContainer = document.querySelector('#chat_window');
ReactDOM.render(e(ChatWindow), domContainer);
