'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Session = function (_React$Component) {
  _inherits(Session, _React$Component);

  function Session(props) {
    _classCallCheck(this, Session);

    var _this = _possibleConstructorReturn(this, (Session.__proto__ || Object.getPrototypeOf(Session)).call(this, props));

    _this.handleGameUpdate = _this.handleGameUpdate.bind(_this);
    return _this;
  }

  _createClass(Session, [{
    key: 'componentDidMount',
    value: function componentDidMount() {
      socket.on('game_updates', this.handleGameUpdate);
    }
  }, {
    key: 'handleGameUpdate',
    value: function handleGameUpdate(message) {
      console.log("Recieved message");
      console.log(message);
    }
  }, {
    key: 'render',
    value: function render() {
      return React.createElement(
        'div',
        { id: 'session' },
        React.createElement(Lobby, null)
      );
    }
  }]);

  return Session;
}(React.Component);

var domContainer = document.querySelector('#main');
ReactDOM.render(React.createElement(Session, null), domContainer);