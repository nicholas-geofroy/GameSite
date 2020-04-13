'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var UserList = function (_React$Component) {
  _inherits(UserList, _React$Component);

  function UserList(props) {
    _classCallCheck(this, UserList);

    var _this = _possibleConstructorReturn(this, (UserList.__proto__ || Object.getPrototypeOf(UserList)).call(this, props));

    _this.state = {
      users: []
    };
    _this.userUpdate = _this.userUpdate.bind(_this);
    return _this;
  }

  _createClass(UserList, [{
    key: 'componentDidMount',
    value: function componentDidMount() {
      console.log("userlist mounted");
      socket.on('user_updates', this.userUpdate);
    }
  }, {
    key: 'componentWillUnmount',
    value: function componentWillUnmount() {
      socket.off('user_updates', this.newMessage);
    }
  }, {
    key: 'userUpdate',
    value: function userUpdate(users) {
      console.log(users);
      this.setState({
        users: users
      });
    }
  }, {
    key: 'render',
    value: function render() {
      var userItems = this.state.users.map(function (user) {
        return React.createElement(User, { key: user.id, name: user.username });
      });

      return React.createElement(
        'div',
        { id: 'userList' },
        React.createElement(
          'h3',
          null,
          ' Players '
        ),
        userItems
      );
    }
  }]);

  return UserList;
}(React.Component);

var User = function (_React$Component2) {
  _inherits(User, _React$Component2);

  function User() {
    _classCallCheck(this, User);

    return _possibleConstructorReturn(this, (User.__proto__ || Object.getPrototypeOf(User)).apply(this, arguments));
  }

  _createClass(User, [{
    key: 'render',
    value: function render() {
      return React.createElement(
        'p',
        null,
        ' ',
        this.props.name,
        ' '
      );
    }
  }]);

  return User;
}(React.Component);