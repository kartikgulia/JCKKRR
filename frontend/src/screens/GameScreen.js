import React, { Component } from "react";
import SubmitButton from "../components/SubmitButton";
import YearSlider from "../components/YearSlider";

class Game extends Component {
  state = {
    year: 0, // Initial slider value
  };

  handleYearChange = (value) => {
    this.setState({ year: value });
  };

  submitYearGuess = () => {};

  render() {
    return (
      <div style={container}>
        <h1>Game Screen</h1>
        <h3>Image</h3>

        <YearSlider min={0} max={2000} onChange={this.handleYearChange} />

        <SubmitButton
          onClick={() => console.log("Selected Year:", this.state.year)}
          text={"Submit Year Guess"}
          color={"dodgerblue"}
        />
      </div>
    );
  }
}

const container = {
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
  alignItems: "center",
  height: "100vh",
};

export default Game;
