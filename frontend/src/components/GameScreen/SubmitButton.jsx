import React, { useState } from "react";
import PropTypes from "prop-types";

const SubmitButton = ({ color, text, onClick }) => {
  const [isPressed, setIsPressed] = useState(false);

  const buttonStyle = {
    backgroundColor: isPressed ? "darkgray" : color,
    color: "black",
    padding: "10px 20px",
    fontSize: "20px",
    borderRadius: "10px",
    border: "none",
    cursor: "pointer",
    outline: "none",
    boxShadow: isPressed
      ? "inset 0 2px 4px rgba(0, 0, 0, 0.2)"
      : "0 2px 4px rgba(0, 0, 0, 0.2)",
    transition: "background-color 0.3s, box-shadow 0.2s",
  };

  const handleMouseDown = () => {
    setIsPressed(true);
  };

  const handleMouseUp = () => {
    setIsPressed(false);
  };

  // Enhance the onClick to also reset the isPressed state
  const enhancedOnClick = (e) => {
    setIsPressed(false);
    onClick(e);
  };

  return (
    <button
      onMouseDown={handleMouseDown}
      onMouseUp={handleMouseUp}
      onMouseLeave={handleMouseUp}
      onClick={enhancedOnClick}
      style={buttonStyle}
      className="btn"
    >
      {text}
    </button>
  );
};

SubmitButton.defaultProps = {
  color: "steelblue",
};

SubmitButton.propTypes = {
  text: PropTypes.string.isRequired,
  color: PropTypes.string,
  onClick: PropTypes.func.isRequired,
};

export default SubmitButton;
