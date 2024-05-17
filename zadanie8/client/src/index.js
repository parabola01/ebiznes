import React from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import App from './App';
import { BrowserRouter as Router } from 'react-router-dom';

// Znajdź element root w DOM
const container = document.getElementById('root');

// Utwórz root za pomocą createRoot
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <Router>
      <App />
    </Router>
  </React.StrictMode>
);
