//App.js basically starts the app on the HomePage (vero confirm this im not 100% sure)
//Every other ____.js file in this folder is the front end code for each page

import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className = "center">
        <HomePage />
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);