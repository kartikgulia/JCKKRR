import PropTypes from "prop-types";

const SubmitButton = ({ color, text, onClick }) => {
  const buttonStyle = {
    backgroundColor: color,
    color: "black", // Add text color for better contrast
    padding: "10px 20px", // Increase padding for a bigger button
    fontSize: "20px", // Increase font size for better readability

    borderRadius: "10px", // Round the corners of the button
    border: "none", // Remove the default border
    cursor: "pointer", // Change cursor to pointer on hover
    outline: "none", // Remove outline to improve aesthetics
    boxShadow: "0 2px 4px rgba(0, 0, 0, 0.2)",
    transition: "background-color 0.3s", // Smooth transition for hover effect
  };

  return (
    <button onClick={onClick} style={buttonStyle} className="btn">
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
