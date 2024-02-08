import React, { Component } from "react";
import YearGuess from "../components/GameScreen/YearGuess";
import Round from "../components/GameScreen/Round";

class Game extends Component {
  state = {
    year: 0, // Initial slider value
    onYearGuessPage: true,
    backgroundImageSRC: "", // Moved initialization to state
    targetImageSRC: "",
    targetImageCoordinates: {},
  };

  minYear = 0;
  maxYear = 2024;

  errorText = null;

  componentDidMount() {
    this.initializeGame();
  }

  initializeGame = () => {
    console.log("Game component has been mounted.");
    // Print out the gameID
    console.log("Game ID:", this.props.gameID);

    // Using the Game ID, fetch game information from Firebase and set the state
    // Ex.

    this.setState({
      backgroundImageSRC: "https://picsum.photos/1000/500",
      targetImageSRC: "https://picsum.photos/500/500",
      targetImageCoordinates: {
        x: 100,
        y: 200,
      },
    });
  };

  handleYearChange = (value) => {
    this.setState({ year: value });
  };

  calculateScoreForYearGuess = (yearGuessed, yearActual) => {
    let yearRange = this.maxYear - this.minYear;
    let offBy = Math.abs(yearGuessed - yearActual);
    let score = yearRange - offBy;
    return score;
  };

  submitYearGuess = () => {
    console.log("Selected Year:", this.state.year);

    if (this.state.year == null) {
      this.setState({
        errorText: `Please enter a year in between ${this.minYear} and ${this.maxYear}.`,
      });
      return;
    }
    let actualYear = 2000;
    let score = this.calculateScoreForYearGuess(this.state.year, actualYear);
    console.log(score);

    // If everything is successful
    // If everything is successful, clear the errorText
    this.setState({
      onYearGuessPage: false,
      errorText: null,
    });
  };

  render() {
    const {
      backgroundImageSRC,
      targetImageSRC,
      targetImageCoordinates,
      errorText,
    } = this.state; // Use backgroundImageSRC from state
    return (
      <div>
        {this.state.onYearGuessPage ? (
          <div style={container}>
            <YearGuess
              year={this.state.year}
              onYearChange={this.handleYearChange}
              onSubmitYearGuess={this.submitYearGuess}
              minYear={this.minYear}
              maxYear={this.maxYear}
              backgroundImageSRC={backgroundImageSRC} // Use state value
            />

            <h2 style={errorTextStyle}>{errorText}</h2>
          </div>
        ) : (
          <Round
            backgroundImageSRC={backgroundImageSRC} // Use state value
            targetImage={targetImageSRC}
            targetImageCoordinates={targetImageCoordinates}
          />
        )}
      </div>
    );
  }
}

const container = {
  display: "flex",
  flexDirection: "column",
  justifyContent: "flex-start", // Align items at the top
  alignItems: "center",
  height: "100vh",
};

const errorTextStyle = {
  color: "red",
};

export default Game;
