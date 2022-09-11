import React from 'react';
import './App.css';
import {
  BrowserRouter as Router,
  Route,
  Link,
  useNavigate,
} from "react-router-dom";
import { Importer, ImporterField } from "react-csv-importer";
import axios from "axios";

// theme CSS for React CSV Importer
import "react-csv-importer/dist/index.css";

// basic styling and font for sandbox window
import "./index.css";


export default function App() {
  let nav = useNavigate();
  return (
    <div>
      <h1>React CSV Importer sandbox</h1>

      <Importer
        chunkSize={10000} // optional, internal parsing chunk size in bytes
        assumeNoHeaders={false} // optional, keeps "data has headers" checkbox off by default
        restartable={false} // optional, lets user choose to upload another file when import is complete
        onStart={({ file, preview, fields, columnFields }) => {
          // optional, invoked when user has mapped columns and started import
          console.log("starting import of file", file, "with fields", fields);
        }}
        processChunk={async (rows, { startIndex }) => {
          // required, receives a list of parsed objects based on defined fields and user column mapping;
          // may be called several times if file is large
          // (if this callback returns a promise, the widget will wait for it before parsing more data)
          // console.log("received batch of rows", rows);
          console.log(rows.length)
          console.log(startIndex)
          for(let i =0; i < rows.length; i++) {
            let item = {'customer':rows[i].name, 'address': rows[i].address, 'zipCode': rows[i].date, 'phoneNumber': rows[i].phoneNumber, 'client': "JB"}
            if(i < 2) {
              // console.log(rows[i])
              // console.log(item)

              axios
                .post("/api/didTheyMove/", item)
            }
            
              // .then((res) => this.refreshList());
          }
          

          // mock timeout to simulate processing
          await new Promise((resolve) => setTimeout(resolve, 500));
        }}
        onComplete={({ file, preview, fields, columnFields }) => {
          // optional, invoked right after import is done (but user did not dismiss/reset the widget yet)
          console.log("finished import of file", file, "with fields", fields);

        }}
        onClose={() => {
          // optional, invoked when import is done and user clicked "Finish"
          // (if this is not specified, the widget lets the user upload another file)
          nav("/infoTable")
          console.log("importer dismissed");
        }}
      >
        <ImporterField name="name" label="Name" />
        <ImporterField name="address" label="Address" />
        <ImporterField name="date" label="Date of Installation" />
        <ImporterField name="phoneNumber" label="Phone Number"  />
        {/* // CSV options passed directly to PapaParse if specified:
        // delimiter={...}
        // newline={...}
        // quoteChar={...}
        // escapeChar={...}
        // comments={...}
        // skipEmptyLines={...}
        // delimitersToGuess={...}
        // chunkSize={...} // defaults to 10000
        // encoding={...} // defaults to utf-8, see FileReader API */}
      </Importer>
      
  </div>
  );
}