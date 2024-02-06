import React, { Component } from "react";
import SubmitButton from "../components/SubmitButton";
import YearSlider from "../components/YearSlider";
import BackgroundImage from "../components/BackgroundImage";

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
        <h1>Guess what year this image is from?</h1>
        <BackgroundImage src={"https://picsum.photos/500/500"} />

        <YearSlider min={0} max={2024} onChange={this.handleYearChange} />

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
