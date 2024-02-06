import React from "react";
import SubmitButton from "../components/SubmitButton";

class Game extends React.Component {
  render() {
    return (
      <div style={container}>
        <h1>Game Screen</h1>
        <h3>Image</h3>
        <h3>Slider</h3>
        <h3>Submit Button</h3>
        <SubmitButton
          onClick={() => console.log("hi")}
          text={"Submit Year Guess"}
          color={"dodgerblue"}
        />
      </div>
    );
  }
}

const container = {
  display: "flex",
  flexDirection: "column", // Stack items vertically
  justifyContent: "center", // Center vertically in the container
  alignItems: "center", // Center horizontally in the container
  height: "100vh",
};

export default Game;
