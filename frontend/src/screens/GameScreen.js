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
    imagesLoaded: false, // New state to track image loading
    difficulty: null,
  };

  minYear = 0;
  maxYear = 2024;

  componentDidMount() {
    const route = window.location.pathname;
    const parts = route.split("/"); // Split the pathname by '/'
    const difficulty = parts[parts.length - 1];

    console.log(difficulty); // Output the difficulty level

    this.setState({ difficulty: difficulty }, () => {
      console.log("Difficulty updated:", this.state.difficulty);
      this.initializeGame(); // Ensure initializeGame is called after difficulty is set
    });
  }

  initializeGame = () => {
    console.log("Game component has been mounted.");
    // Print out the gameID

    console.log("Use difficulty to retrieve a game from Firestore");

    // Here is the difficulty

    console.log(this.state.difficulty);

    // All this data below should be retrieved from firestore. i just put in some mock data

    // Use the difficulty to get the game info from firestore
    const backgroundImage = new Image();
    backgroundImage.src = "https://picsum.photos/1000/500";
    backgroundImage.onload = () => {
      const targetImage = new Image();
      targetImage.src = "https://picsum.photos/500/500";
      targetImage.onload = () => {
        this.setState({
          backgroundImageSRC: backgroundImage.src,
          targetImageSRC: targetImage.src,
          targetImageCoordinates: {
            x: 100,
            y: 200,
          },
          imagesLoaded: true,
        });
      };
    };
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
    let actualYear = 2000;
    let score = this.calculateScoreForYearGuess(this.state.year, actualYear);
    console.log(score);
    this.setState({ onYearGuessPage: false });
  };

  render() {
    const {
      backgroundImageSRC,
      targetImageSRC,
      targetImageCoordinates,
      imagesLoaded,
    } = this.state; // Use backgroundImageSRC from state

    if (!imagesLoaded) {
      return <div>Loading...</div>; // Render a loading indicator until images are loaded
    }

    return (
      <div style={container}>
        {this.state.onYearGuessPage ? (
          <YearGuess
            year={this.state.year}
            onYearChange={this.handleYearChange}
            onSubmitYearGuess={this.submitYearGuess}
            minYear={this.minYear}
            maxYear={this.maxYear}
            backgroundImageSRC={backgroundImageSRC} // Use state value
          />
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
  justifyContent: "center",
  alignItems: "center",
  height: "100vh",
};

export default Game;
