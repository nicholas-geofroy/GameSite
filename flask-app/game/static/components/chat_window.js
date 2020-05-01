'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var e = React.createElement;

var Message = function (_React$Component) {
  _inherits(Message, _React$Component);

  function Message() {
    _classCallCheck(this, Message);

    return _possibleConstructorReturn(this, (Message.__proto__ || Object.getPrototypeOf(Message)).apply(this, arguments));
  }

  _createClass(Message, [{
    key: 'render',
    value: function render() {
      return React.createElement(
        'p',
        null,
        ' ',
        this.props.username,
        ' : ',
        this.props.message,
        ' '
      );
    }
  }]);

  return Message;
}(React.Component);

var ChatWindow = function (_React$Component2) {
  _inherits(ChatWindow, _React$Component2);

  function ChatWindow(props) {
    _classCallCheck(this, ChatWindow);

    var _this2 = _possibleConstructorReturn(this, (ChatWindow.__proto__ || Object.getPrototypeOf(ChatWindow)).call(this, props));

    _this2.state = {
      messages: [],
      newMessage: ''
    };
    _this2.newMessage = _this2.newMessage.bind(_this2);
    _this2.handleChange = _this2.handleChange.bind(_this2);
    _this2.handleSubmit = _this2.handleSubmit.bind(_this2);
    return _this2;
  }

  _createClass(ChatWindow, [{
    key: 'componentDidMount',
    value: function componentDidMount() {
      socket.on('message', this.newMessage);
    }
  }, {
    key: 'componentWillUnmount',
    value: function componentWillUnmount() {
      socket.off('message', this.newMessage);
    }
  }, {
    key: 'handleChange',
    value: function handleChange(event) {
      this.setState({ newMessage: event.target.value });
    }
  }, {
    key: 'handleSubmit',
    value: function handleSubmit(event) {
      event.preventDefault();
      console.log('Send message: ' + this.state.newMessage);
      if (this.props.onSubmitWord != undefined) this.props.onSubmitWord(this.state.newMessage);
      socket.emit('send_message', this.state.newMessage);
      this.setState({
        newMessage: ''
      });
    }
  }, {
    key: 'newMessage',
    value: function newMessage(data) {
      // console.log(("new message: " + data));
      this.setState(function (state, props) {
        return {
          messages: state.messages.concat([data])
        };
      });
    }
  }, {
    key: 'render',
    value: function render() {
      var messageItems = this.state.messages.map(function (data, idx) {
        return React.createElement(Message, { username: data.user, message: data.message, key: idx });
      });
      return React.createElement(
        'div',
        { id: 'chatbox' },
        React.createElement(
          'h3',
          null,
          ' Chat '
        ),
        React.createElement(
          'div',
          { id: 'messages' },
          messageItems
        ),
        React.createElement(
          'form',
          { id: 'chatForm', onSubmit: this.handleSubmit },
          React.createElement('input', { type: 'text', id: 'next_message', value: this.state.newMessage,
            onChange: this.handleChange }),
          React.createElement('input', { type: 'submit', value: 'Send' })
        )
      );
    }
  }]);

  return ChatWindow;
}(React.Component);