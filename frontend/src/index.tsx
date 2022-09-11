import React from 'react';
import { render } from "react-dom";
import ReactDOM from "react-dom/client";
import { 
  BrowserRouter,
  Routes,
  Route, 
} from "react-router-dom";
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Expenses from "./routes/expenses";
import InfoTable from "./routes/infoTable";

const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="expenses" element={<Expenses />} />
        <Route path="infotable" element={<InfoTable />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();


