import React, { useState } from "react";
import BackgroundImage from "./BackgroundImage";
import SubmitButton from "./SubmitButton";

const Round = ({ backgroundImageSRC, targetImage, targetImageCoordinates }) => {
  const [clickPosition, setClickPosition] = useState({ x: null, y: null });

  const handleBackgroundImageClick = (event) => {
    const rect = event.target.getBoundingClientRect();
    const circleDiameter = 20; // Since the circle's size is 20x20px
    const offsetX = circleDiameter / 2;
    const offsetY = circleDiameter / 2;
    const x = event.clientX - rect.left - offsetX;
    const y = event.clientY - rect.top - offsetY + 80;

    setClickPosition({ x, y });
  };

  // Optionally, define what happens when the submit button is clicked
  const handleSubmitClick = () => {
    console.log(`Submit click at x: ${clickPosition.x}, y: ${clickPosition.y}`);
    console.log(
      `Target Image coordinates at x: ${targetImageCoordinates.x}, y: ${targetImageCoordinates.y}`
    );
    // Here you can add the logic for what should happen on submit, like verifying the click position
  };

  return (
    <div style={roundContainerStyle}>
      <div style={targetImageContainerStyle}>
        <h2>Find this image</h2>
        <img src={targetImage} alt="Target" style={targetImageStyle} />
      </div>
      <div
        style={backgroundImageContainerStyle}
        onClick={handleBackgroundImageClick}
      >
        <BackgroundImage src={backgroundImageSRC} />
        {/* Conditionally render the red circle if coordinates are available */}
        {clickPosition.x !== null && clickPosition.y !== null && (
          <div
            style={{
              ...redCircleStyle,
              left: clickPosition.x + "px",
              top: clickPosition.y + "px",
            }}
          ></div>
        )}
      </div>

      <SubmitButton
        onClick={handleSubmitClick}
        text={"Submit Your Guess"}
        color={"dodgerblue"}
      />
    </div>
  );
};

// Styles
const roundContainerStyle = {
  display: "flex",
  flexDirection: "column", // Changed to column layout to stack items vertically
  alignItems: "center", // Center items horizontally
  width: "100%",
  position: "relative", // To position the red circle absolutely within this container
};

const backgroundImageContainerStyle = {
  position: "relative", // Necessary for absolute positioning of the red circle
  marginBottom: "20px", // Added margin bottom for spacing
};

const targetImageContainerStyle = {
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
  marginBottom: "20px", // Added margin bottom for spacing
};

const targetImageStyle = {
  maxWidth: "100%",
  height: "auto",
};

const redCircleStyle = {
  position: "absolute",
  width: "20px",
  height: "20px",
  borderRadius: "50%",
  backgroundColor: "red",
  // Removed the transform property for direct alignment
};

export default Round;
