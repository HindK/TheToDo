import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Game extends React.Component {
  constructor( props ) {
    super( props );
    this.state = {
      value: 0,
    }
  }

  componentDidMount() {
    fetch( "http://localhost:8000/testApi")
    .then( res => res.json() )
    .then( res => alert( res ) );
  }

  render() {
    const value = this.state.value;
    return (
      <div className="game">
          <p> This is a paragraph with value: {value} </p>
      </div>
    );
  }
}

// ========================================

ReactDOM.render(
  <Game />,
  document.getElementById('root')
);
