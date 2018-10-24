import React, { Component } from 'react';
import logo from './logo.svg';
import FPM from './FPM.png';
import Malaria from './Malaria.png';
import SickleCell from './SickleCell.png';
import HIV from './HIV.png';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Redefining Blood Tests.
          </p>
          <p>
            Quanto brings reliable, cheap and fast blood testing to consumers. 
          </p>
          <p>
            Our Technology
          </p>
          
          {/* Adding Images here and describing them */}

          <p>
            Blood Cell Count. 
          </p>
          <img src={FPM} className="Our-Technology" alt="FPM" />
          
          <p>
            Malaria Detection. 
          </p>
          <img src={Malaria} className="Our-Technology" alt="Malaria" />
          
          <p>
            SickleCell Detection. 
          </p>
          <img src={SickleCell} className="Our-Technology" alt="SickleCell" />

          <p>
            HIV Detection.
          </p>
          <img src={HIV} className="Our-Technology" alt="HIV" />
          
        </header>
        <footer className = "App-footer">
        </footer>
      </div>
    );
  }
}

export default App;
