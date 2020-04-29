'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var gamemodes = {
  TABOO: {
    name: "Taboo",
    value: 1
  },
  HEADBANDS: {
    name: "Headbands",
    value: 2
  }
};

var GameSettings = function (_React$Component) {
  _inherits(GameSettings, _React$Component);

  function GameSettings(props) {
    _classCallCheck(this, GameSettings);

    var _this = _possibleConstructorReturn(this, (GameSettings.__proto__ || Object.getPrototypeOf(GameSettings)).call(this, props));

    _this.state = {
      gamemode: gamemodes.TABOO.value
    };
    _this.handleGamemodeSelect = _this.handleGamemodeSelect.bind(_this);
    _this.handleSubmit = _this.handleSubmit.bind(_this);
    return _this;
  }

  _createClass(GameSettings, [{
    key: "componentDidMount",
    value: function componentDidMount() {}
  }, {
    key: "componentWillUnmount",
    value: function componentWillUnmount() {}
  }, {
    key: "handleGamemodeSelect",
    value: function handleGamemodeSelect(event) {
      this.setState({
        gamemode: event.target.value
      });
    }
  }, {
    key: "handleSubmit",
    value: function handleSubmit(event) {
      console.log("submit settings and start game");
      var message = {
        type: 'start_game',
        gamemode: this.state.gamemode
      };
      socket.emit('game_updates', message);
      event.preventDefault();
    }
  }, {
    key: "render",
    value: function render() {
      var options = Object.keys(gamemodes).map(function (gamemodeKey) {
        var gamemode = gamemodes[gamemodeKey];
        return React.createElement(
          "option",
          { value: gamemode.value, key: gamemode.name },
          gamemode.name
        );
      });
      return React.createElement(
        "form",
        { id: "gameSettings", onSubmit: this.handleSubmit },
        React.createElement(
          "select",
          { id: "gamemode", form: "gameSettings", onChange: this.handleGamemodeSelect },
          options
        ),
        React.createElement("input", { type: "submit", value: "Start Game" })
      );
    }
  }]);

  return GameSettings;
}(React.Component);