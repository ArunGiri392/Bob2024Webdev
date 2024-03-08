import React from 'react';
import ReactDOM from 'react-dom';
import './styles/app.css'; // Adjust the path to 'app.css' if needed
import App from './components/App'; // Adjust the path to 'App' component if needed

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// Note: Ensure that reportWebVitals function is defined or remove the import statement if not needed

// reportWebVitals(); // Comment out or remove this line if 'reportWebVitals' is not defined or not used
