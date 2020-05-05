var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

"use strict";

var Card = function (_React$Component) {
  _inherits(Card, _React$Component);

  function Card(props) {
    _classCallCheck(this, Card);

    var _this = _possibleConstructorReturn(this, (Card.__proto__ || Object.getPrototypeOf(Card)).call(this, props));

    _this.renderEmpy = _this.renderEmpy.bind(_this);
    _this.renderCard = _this.renderCard.bind(_this);
    return _this;
  }

  _createClass(Card, [{
    key: "render",
    value: function render() {
      if (this.props.data == undefined) {
        return this.renderEmpy();
      } else {
        return this.renderCard(this.props.data);
      }
    }
  }, {
    key: "renderEmpy",
    value: function renderEmpy() {
      return React.createElement("div", { className: "card" });
    }
  }, {
    key: "renderCard",
    value: function renderCard(card) {
      var bannedWords = card.banned_words.map(function (word) {
        return React.createElement(
          "li",
          { key: word },
          word
        );
      });
      return React.createElement(
        "div",
        { className: "card" },
        React.createElement(
          "p",
          null,
          card.target_word
        ),
        React.createElement(
          "ul",
          { className: "bannedWords" },
          bannedWords
        )
      );
    }
  }]);

  return Card;
}(React.Component);