import React from 'react';
import './index.css';
import './App.css';
import { Header, Main } from "../Layouts";
import { BrowserRouter as Router } from 'react-router-dom';

const App: React.FunctionComponent = () => {
  return (
    <div className="App">
      <Router>
        <Header />
        <Main /> 
      </Router>
    </div >
  );
}

export default App;
