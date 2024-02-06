import React, { Component } from "react";
import YearGuess from "../components/GameScreen/YearGuess"; // Import the YearGuess component

class Game extends Component {
  state = {
    year: 0, // Initial slider value
  };

  minYear = 0;
  maxYear = 2024;

  handleYearChange = (value) => {
    this.setState({ year: value });
  };

  calculateScoreForYearGuess = (yearGuessed, yearActual) => {
    // 1. Take the year range

    let yearRange = this.maxYear - this.minYear;

    // 2. Get how much they were off by

    let offBy = Math.abs(yearGuessed - yearActual);
    // 3. Subtract how much they were off by from yearRange

    let score = yearRange - offBy;

    return score;
  };
  submitYearGuess = () => {
    console.log("Selected Year:", this.state.year);

    // Calcuate score for year guess

    let actualYear = 2000;
    let score = this.calculateScoreForYearGuess(this.state.year, actualYear);

    // Waiting for Ryan

    console.log(score);
  };

  render() {
    return (
      <div style={container}>
        <YearGuess
          year={this.state.year}
          onYearChange={this.handleYearChange}
          onSubmitYearGuess={this.submitYearGuess}
          minYear={this.minYear}
          maxYear={this.maxYear}
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
