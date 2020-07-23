import React from 'react';
import './index.css';
import './App.css';
import { Header } from "../shared/Header";
import { Main } from "../shared/Main";
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
